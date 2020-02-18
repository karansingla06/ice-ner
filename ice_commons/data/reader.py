import logging

import numpy as np
import pandas as pd

from ice_commons.data.source.mongo import Mongo


class MongoReader(object):
    """
        Connects to a Mongodb database and returns a pandas dataframe for the given config

        :param config:
            config = {
                "uri": "mongodb://localhost:27017",
                "database": "sample_database",
                "collection": "sample_collection",
                "db_filter": ({"field1": "value"}, {"field2": 1, "field3": 1}) Use mongodb find filter queries
            }
        :return pandas.DataFrame:
    """

    def __init__(self, config, shuffle_rows=True, logger=None):
        """

        :param config:
        :param shuffle_rows:
        :return:
        """
        self.config = config
        self.shuffle_rows = shuffle_rows
        self.logger = logger or logging.getLogger(__name__)

    def fit(self, *_):
        return self

    def transform(self, config=None):
        """

        :param config:
        :return:
        """
        new_config = self.config.update(config) if config else self.config
        return self._to_pandas(new_config)

    def _to_pandas(self, config, columns=None):
        """

        :param config:
        :param columns:
        :return:
        """
        uri = "mongodb://localhost:27017"
        if "uri" in config:
            uri = config["uri"]

        if uri is not None:
            db = Mongo(
                uri=uri,
                default_db=config["database"],
                default_collection=config["collection"]
            )

            # Apply any database filter
            db_filter = {}
            if "db_filter" in config:
                db_filter = config["db_filter"]

            # select top n rows specified by limit
            if 'limit' in config:
                data = list(db.find(db_filter).limit(int(config['limit'])))
            else:
                data = list(db.find(db_filter))

            df = pd.DataFrame(data, columns=columns)

            # Shuffle row
            if self.shuffle_rows:
                df = df.iloc[np.random.permutation(len(df))]

            df = df.replace(np.nan, '', regex=True)
            return df

        return pd.DataFrame()


class CSVReader(object):
    """
        Scikit Transformation to read a csv file into a pandas DataFrame.
        Uses pandas.read_csv internally

        :param filepath_or_buffer: Refer pandas read_csv filepath_or_buffer
        :param shuffle_rows: shuffles the rows of the dataframe
        :return pandas DataFrame for the given CSV

    """

    def __init__(self, filepath_or_buffer, shuffle_rows=True, logger=None, **kwargs):
        """

        :param filepath_or_buffer:
        :param shuffle_rows:
        :param logger:
        :param kwargs:
        """
        self.logger = logger or logging.getLogger(__name__)
        self.filepath_or_buffer = filepath_or_buffer
        self.shuffle_rows = shuffle_rows
        self.kwargs = kwargs

    def fit(self, *_):
        return self

    def transform(self):
        """

        :return:
        """
        if self.filepath_or_buffer:
            return self._fetch()
        else:
            raise AttributeError("Argument missing input file")

    def _fetch(self):
        """
        :return:
        """
        df = None
        try:
            df = pd.read_csv(
                self.filepath_or_buffer,
                error_bad_lines=True,
                encoding='latin_1',
                **self.kwargs
            )
            if not df.empty and self.shuffle_rows:
                df = df.iloc[np.random.permutation(len(df))]
        except Exception as re:
            self.logger.exception(re, exc_info=True)
        return df


class ExcelReader(object):
    """
        Scikit Transformation to read an excel file into a pandas DataFrame.
        Uses pandas.read_excel internally

        :param filepath_or_buffer: Refer pandas read_csv filepath_or_buffer
        :param shuffle_rows: shuffles the rows of the dataframe
        :return pandas DataFrame for the given CSV

    """

    def __init__(self, name, shuffle_rows=True, logger=None, **kwargs):
        """
        :param name:
        :param shuffle_rows:
        :param logger:
        :param kwargs:
        """
        self.logger = logger or logging.getLogger(__name__)
        self.name = name
        self.shuffle_rows = shuffle_rows
        self.kwargs = kwargs

    def fit(self, *_):
        return self

    def transform(self):
        """

        :return:
        """
        if self.name:
            return self._fetch()
        else:
            self.logger.exception("Argument missing input file")
            raise RuntimeError("Argument missing input file")

    def _fetch(self):
        """

        :return:
        """
        df = pd.read_excel(self.name, **self.kwargs)
        if self.shuffle_rows:
            df = df.iloc[np.random.permutation(len(df))]
        return df
