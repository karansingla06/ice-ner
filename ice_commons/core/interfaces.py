import os
from abc import ABCMeta, abstractmethod

import numpy as np
from imblearn.pipeline import make_pipeline
from sklearn.svm import LinearSVC
from sklearn.tree import DecisionTreeClassifier
#from pystruct.models import MultiClassClf
from sklearn.ensemble import RandomForestClassifier

from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.base import TransformerMixin
from sklearn.model_selection import StratifiedShuffleSplit, cross_val_score
from sklearn.preprocessing import LabelEncoder

from ice_commons.core.class_utils import create_instance
from ice_commons.core.features import build_feature_selector
from ice_commons.core.transformations import build_dataframe_mapper
from ice_commons.utils import dict_contains, token, has_same_type
import collections


class StatelessTransform(TransformerMixin):
    """
    Base class for all transformations that do not depend on training (ie, are
    stateless).
    """

    def fit(self, *_):
        """

        :param _:
        :return:
        """
        return self


_docs = \
    """
    Interface to train different **{}** models from different machine learning libraries, like **sklearn, XGBoost**, ...

    :param estimator: model type
    :type estimator: model instance
    :param extractor: Transformation Pipeline used to extract features from dataset
    :type extractor: DataframeMapper(sklearn-pandas) type or None
    :param selector: Feature selection
    :type extractor: SelectModel from sklearn
    :param sampler: Data Sampler for creating a balanced dataset
    :type extractor: Sampling Algorithms from imbalanced-learn package

    .. note::
        * if `extractor` aren't set (**None**), then all features in the training dataset will be used

        * Datasets should be `pandas.DataFrame`, not `numpy.array`.
        * It works fine with `numpy.array` as well, but in this case all the features will be used.
    """


class Estimator(BaseEstimator):
    def __init__(self, config, serviceid=None, useSelector = True):
        """

        :param config:
        :param serviceid:
        """
        assert isinstance(config, dict), \
            "build_ml_pipeline: invalid configuration"

        self.serviceid = serviceid or token()
        self.config = config
        self.preprocessor = self.__build_preprocessor(useSelector)
        self.learner = None

    def __build_extractor(self):
        """
        Method for building machine learning pre processing configurations
        """
        assert isinstance(self.config, dict), \
            "Estimator: __build_extractor: invalid configuration"
        assert dict_contains(self.config, ['preprocessors']), \
            "Estimator: __build_extractor: missing mandatory preprocessors"

        preprocessor_config = self.config['preprocessors']
        return build_dataframe_mapper(preprocessor_config)

    def __build_selector(self):
        """
        Method for building machine learning feature selections configurations
        """
        assert isinstance(self.config, dict), \
            "Estimator: __build_selector: invalid configuration"
        if dict_contains(self.config, ['selector']):
            selector_config = self.config['selector']
            return build_feature_selector(selector_config)

    def __build_preprocessor(self, useSelector):
        """

        :return:
        """
        extractor = self.__build_extractor()
        if(useSelector):
            selector = self.__build_selector()
            return make_pipeline(extractor, selector)
        else:
            return make_pipeline(extractor)

    @abstractmethod
    def _build_cross_validation(self, y=None):
        pass

    @abstractmethod
    def fit(self, X, y, **fit_params):
        """
        Train a classification model on the data.

        :param pandas.DataFrame X: data of shape [n_samples, n_features]
        :param y: labels of samples, array-like of shape [n_samples]
        :param fit_params: weight of samples,

        :return: self
        """
        pass

    @abstractmethod
    def predict(self, X):
        """
        Predict labels for all samples in the dataset.

        :param pandas.DataFrame X: data of shape [n_samples, n_features]
        :rtype: numpy.array of shape [n_samples] with integer labels
        """
        pass

    @abstractmethod
    def cross_validate(self):
        pass


class IntentRecognizer(Estimator, ClassifierMixin, metaclass=ABCMeta):
    __doc__ = _docs.format('classification') + \
              """
                  * Classes values must be from 0 to n_classes-1!
              """

    def __init__(self, config, serviceid=None, useSelector=True):
        Estimator.__init__(self, config, serviceid, useSelector)
        self.encoder = None
        self.labels = []

    def __encode_label(self, y):
        """
        Encodes labels to integers using LabelEncoder for string labels
        :param y: labels to be encoded
        :return:
        """
        assert not has_same_type(y, float), \
            "Invalid type float for labels"

        if not self.encoder:
            self.encoder = LabelEncoder()
            self.encoder.fit(y)
            self.labels = list(self.encoder.classes_)

        return self.encoder.transform(y)

    def __decode_label(self, y):
        """

        :param y:
        :return:
        """
        if not self.encoder:
            return y
        return self.encoder.inverse_transform(y)

    def _build_cross_validation(self, y=None):
        if dict_contains(self.config, "cross_validation"):
            cv_config = self.config["cross_validation"]
            params = cv_config["params"] if 'params' in cv_config else {}
            if y is not None:
                params["y"] = y
            return create_instance(cv_config['class'], **params)
        return StratifiedShuffleSplit(n_splits=5, test_size=0.33, random_state=42)

    def fit(self, X, y, **fit_params):
        """

        :param X:
        :param y:
        :param fit_params:
        :return:
        """
        y = self.__encode_label(y)
        X = self.preprocessor.fit_transform(X, y, **fit_params)


        X_train_bias = np.hstack([X, np.ones((X.shape[0], 1))])

        #model = MultiClassClf(n_features=X_train_bias.shape[1], n_classes=len(self.labels))
        #self.learner = NSlackSSVM(model, verbose=2, check_constraints=False, max_iter=1000,
        #                          C=0.1, batch_size=100, tol=1e-2)
        #self.learner.fit(X_train_bias, y)

        self.learner = RandomForestClassifier()
        self.learner.fit(X_train_bias, y)

    def predict(self, X):
        """

        :param X:
        :return:
        """
        X = self.preprocessor.transform(X)
        X = np.hstack([X, np.ones((X.shape[0], 1))])
        return self.__decode_label(self.learner.predict(X))

    def predict_proba(self, X):

        """
        Predict probabilities for each class label for samples.

        :param pandas.DataFrame X: data of shape [n_samples, n_features]
        :rtype: numpy.array of shape [n_samples, n_classes] with probabilities
        """

        invert_op = getattr(self.learner, "predict_proba", None)
        if isinstance(invert_op, collections.Callable):

            X = self.preprocessor.transform(X)
            X = np.hstack([X, np.ones((X.shape[0], 1))])
            #return self.learner.predict_proba(X)
            data_proba =  self.learner.predict_proba(X)
            data_proba  = np.round(data_proba,2)
            return data_proba

    def cross_validate(self, X, y, **kwargs):
        y = self.__encode_label(y)
        cv = self._build_cross_validation(y)
        X = self.preprocessor.fit_transform(X, y)
        X_train_bias = np.hstack([X, np.ones((X.shape[0], 1))])
        model = MultiClassClf(n_features=X_train_bias.shape[1], n_classes=len(self.labels))

        #self.learner = NSlackSSVM(model, verbose=2, check_constraints=False, C=0.1, batch_size=100, tol=1e-2)
        #return np.round(cross_val_score(self.learner, X_train_bias, y, cv=cv, **kwargs), 2)

        self.learner = RandomForestClassifier()
        self.learner.fit(X_train_bias, y)
        return np.round(cross_val_score(self.learner, X, y, cv=cv, **kwargs), 2)
