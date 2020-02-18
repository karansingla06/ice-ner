import copy
import logging

import numpy as np
from sklearn.linear_model import SGDClassifier
from sklearn.multiclass import OneVsOneClassifier
from sklearn.pipeline import FeatureUnion

from ice_commons.core.class_utils import create_instance, get_function
from ice_commons.utils import dict_contains

logger = logging.getLogger(__name__)


def build_feature_selector(config=None):
    """
    Build a feature selector for the model. Sample config
    "selector": [{
             "class": "ice.prep.base.OneVsOne"
        },
        {
            "class": "sklearn.decomposition.PCA",
            "params": {
                "n_components": 2,
                "random_state": 42
            }

        },
        {
            "class": "feature_selection.SelectFromModel",
            "params": {
                "estimator": {
                    "class": "sklearn.linear_model.LassoCV",
                    "params": {
                    }
                }
            }
        },
        {
            "class": "sklearn.feature_selection.SelectKBest",
            "params": {
                "score_func": "sklearn.feature_selection.chi2",

            }
        }]
    :param config:
    :return:
    """

    def _instantiate(configuration):
        assert dict_contains(configuration, ['class']), \
            "build_feature_selector: missing mandatory class"
        params = copy.copy(configuration["params"]) if 'params' in configuration else {}
        if 'score_func' in params:
            params['score_func'] = get_function(params['score_func'])

        return create_instance(configuration["class"], **params)

    def _get_selector(settings):
        """

        :param settings:
        :return:
        """

        selector_params = settings["params"] if 'params' in settings else {}
        if 'estimator' in selector_params:
            estimator_config = selector_params["estimator"]
            estimator = _instantiate(estimator_config)
            settings["params"] = {
                "estimator": estimator
            }

        clazz = _instantiate(settings)
        return settings['class'], clazz

    if isinstance(config, list):
        selectors = [_get_selector(cfg) for cfg in config]
        return FeatureUnion(selectors)

    elif isinstance(config, dict):
        desc, instance = _get_selector(config)
        return instance


class OneVsOne(object):
    """

        A transformation that essentially implement a form of dimensionality reduction.
        This class uses a fast SGDClassifier configured like a linear SVM to produce
        a vector of decision functions separating target classes in a
        one-versus-rest fashion.
        It's useful to reduce the dimension bag-of-words feature-set into features
        that are richer in information.

    """

    def __init__(self):
        self.classifiers = None

    def fit(self, raw_documents, y):
        """
        `raw_documents` is expected to be an array-like or a sparse matrix.
        `y` is expected to be an array-like containing the classes to learn.
        :param raw_documents:
        :param y:
        :return:
        """
        # self.classifiers = fit_ovo(SGDClassifier(), X, np.array(y), n_jobs=-1)[0]
        ovo = OneVsOneClassifier(SGDClassifier()).fit(raw_documents, np.array(y))
        self.classifiers = ovo.estimators_

        return self

    def fit_transform(self, raw_documents, y):
        """

        :param raw_documents:
        :param y:
        :return:
        """
        self.fit(raw_documents, y)
        return self.transform(raw_documents)

    def transform(self, raw_documents):
        """
        `raw_documents` is expected to be an array-like or a sparse matrix.
        It returns a dense matrix of shape (n_samples, m_features) where
            m_features = (n_classes * (n_classes - 1)) / 2
        :param raw_documents:
        :return:
        """
        xs = [clf.decision_function(raw_documents).reshape(-1, 1) for clf in self.classifiers]
        return np.hstack(xs)
