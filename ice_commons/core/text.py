"""
This module implements several scikit-learn compatible transformers, see
scikit-learn documentation for the convension fit/transform convensions.
"""
import logging
import unicodedata
from html.parser import HTMLParser

import numpy as np
import pandas as pd
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from unidecode import unidecode

from ice_commons.core.interfaces import StatelessTransform
from ice_commons.utils import contains, pandas_column_merge

logger = logging.getLogger(__name__)

cachedNLTKStopWords = stopwords.words("english")


class Concatenate(StatelessTransform):
    """

    """

    def transform(self, X, columns=None):
        """

        :param df:
        :param columns:
        :return:
        """
        logger.info("Performing Concatenate Transformation")

        if not isinstance(X, pd.DataFrame):
            X = pd.DataFrame(X)

        if not columns:
            columns = X.columns.values

        assert contains(X.columns.values, columns), "Invalid columns provided for concatenation"
        results = self._concatenate(X, columns)
        return results.as_matrix()

    @staticmethod
    def _concatenate(df, columns):
        """

        :param df:
        :param columns:
        :return:
        """
        return pandas_column_merge(df, columns)


class UnicodeDecoder(StatelessTransform):
    """

    """

    @staticmethod
    def _decode(text):
        """

        :param text:
        :return:
        """
#        if type(text) == str:
 #           text = bytes(text, "utf-8")

        return unidecode(text)

    def transform(self, X):
        """
        `X` is expected to be a list of `str` instances.
        """
        decode = np.vectorize(self._decode)
        return decode(X)


class CleanText(StatelessTransform):
    """

    """

    def _clean(self, text):
        try:
            return "".join(ch for ch in text if unicodedata.category(ch)[0] != "C")
        except TypeError:
            return ""
        except AttributeError:
            return " "

    def transform(self, X):
        """
        `X` is expected to be a list of `str` instances.
        """
        logger.info("Performing CleanText Transformation")
        clean = np.vectorize(self._clean)
        return clean(X)


class HTMLTagRemover(StatelessTransform):
    """

    """

    def _tag_remover(self, html):
        """

        :param html:
        :return:
        """

        class MLStripper(HTMLParser):
            def __init__(self):
                super().__init__()
                self.reset()
                self.fed = []

            def handle_data(self, d):
                self.fed.append(d)

            def get_data(self):
                return ''.join(self.fed)

        s = MLStripper()
        s.feed(html)
        return s.get_data()

    def transform(self, X):
        """
        `X` is expected to be a list of `str` instances.
        """
        logger.info("Performing HTMLTagRemover Transformation")
        tag_remover = np.vectorize(self._tag_remover)
        return tag_remover(X)


class StopWord(StatelessTransform):
    """
    """

    def __init__(self, sw=cachedNLTKStopWords):
        self.stopwords = sw

    def transform(self, X):
        """

        :param X:
        :return:
        """
        logger.info("Performing StopWord Transformation")
        sanitize = np.vectorize(self.sanitize)
        return sanitize(X)

    def sanitize(self, text):
        """Sanitize using intersection and list.remove()"""
        # Downsides:
        #   - Looping over list while removing from it?
        #     http://stackoverflow.com/questions/1207406/remove-items-from-a-list-while-iterating-in-python

        stop_words = set(self.stopwords)
        words = text.lower().split()
        for sw in stop_words.intersection(words):
            while sw in words:
                words.remove(sw)

        return " ".join(words)


class Lemma(StatelessTransform):
    def __init__(self, lemmatizer=WordNetLemmatizer()):
        self.lemmatizer = lemmatizer

    def transform(self, X):
        """
        `X` is expected to be a list of `str` instances.
        """
        logger.info("Performing Lemma Transformation")
        lemma = np.vectorize(self._lemma)
        return lemma(X)

    def _lemma(self, text):
        words = [self.lemmatizer.lemmatize(w) for w in text.split()]
        return " ".join(words)
