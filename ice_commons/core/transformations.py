#! /usr/bin/python
# -*- coding: UTF-8 -*-

# adapted from: http://code.activestate.com/recipes/223972/

import logging
from sklearn_pandas import DataFrameMapper
from ice_commons.core.class_utils import create_instance

logging.basicConfig(level=logging.INFO)


def instance(cfg, impl_attr="class", logger=None):
    """
    :param cfg:
    :param impl_attr:
    :param logger:
    :return:
    """
    logger = logger or logging.getLogger(__name__)
    assert impl_attr in cfg, 'Mandatory field for identifying implementation missing from config'
    logger.info("building transformations from configs: %s" % cfg)
    params = cfg["params"] if 'params' in cfg else {}
    return create_instance(cfg[impl_attr], **params)


def build_transformations(configs, impl_attr="class", logger=None):
    """
    :param configs:
    :param impl_attr:
    :param logger:
    :return:
    """

    logger = logger or logging.getLogger(__name__)
    assert len(configs) > 0, 'Invalid configuration for build transformations'
    logger.info("building transformations from configs: %s" % configs)
    transformations = [instance(config, impl_attr) for config in configs]
    logger.info("transformations created: %s" % transformations)
    return transformations


def build_transformation_steps(
        configs,
        impl_attr="class",
        columns_tag='columns',
        transformations_tag='transformations',
        logger=None):
    """
    :param configs:
    :param impl_attr:
    :param columns_tag:
    :param transformations_tag:
    :param logger:
    :return:
    """
    logger = logger or logging.getLogger(__name__)
    assert isinstance(configs, list), \
        'build_dataframe_mapper: invalid type for build dataframe mapper configuration'
    assert len(configs) > 0, \
        'build_dataframe_mapper: invalid configuration for build data frame mapper'
    steps = []
    for step in configs:
        logger.info(configs)
        assert columns_tag in step, \
            'build_dataframe_mapper: Mandatory field for columns missing from config'
        assert transformations_tag in step, \
            'build_dataframe_mapper: Mandatory field for transformations missing from config'
        steps.append((
            step[columns_tag],
            build_transformations(step[transformations_tag], impl_attr=impl_attr)
        ))
    return steps


def build_dataframe_mapper(
        configs,
        default=False,
        sparse=False,
        df_out=False,
        columns_tag='columns',
        transformations_tag='transformations',
        impl_attr='class',
        logger=None):
    """
    :param configs:
    :param default:
    :param sparse:
    :param df_out:
    :param columns_tag:
    :param transformations_tag:
    :param impl_attr:
    :param logger:
    :return:
    """
    steps = build_transformation_steps(
        configs=configs,
        impl_attr=impl_attr,
        columns_tag=columns_tag,
        transformations_tag=transformations_tag
    )
    mapper = DataFrameMapper(steps, default=default, sparse=sparse, df_out=df_out)
    return mapper
