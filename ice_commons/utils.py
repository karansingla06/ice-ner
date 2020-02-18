import base64
import datetime
import hashlib

import random
import numpy as np
import pandas as pd
import os
import time

MODEL_TYPE_IR = "ir"
MODEL_TYPE_NER = "ner"
FILE_EXTENSION = "dat"


def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()

        print('%r (%r, %r) %2.2f sec' % \
              (method.__name__, args, kw, te - ts))
        return result

    return timed


def remove_trailing_chars(words, trailing_chars=None):
    """

    :param words:
    :param trailing_chars:
    :return:
    """
    if not trailing_chars:
        return words
    return [
        word[:-len(trailing_chars)]
        if word.endswith(trailing_chars) else word
        for word in list(words)
        ]


def contains(base, sub_list):
    """
    Checks if an array is a subset of another
    :param base:
    :param sub_list:
    :return:
    """
    return set(base) & set(sub_list) == set(sub_list)


def dict_contains(dct, keys):
    """
    :param dct:
    :param keys:
    :return:
    """
    assert isinstance(dct, dict), "dict_contains: dct should be of type dict "
    assert type(keys) in [int, str, list], "dict_contains: keys should be of type list or string "
    if not type(keys) == list:
        keys = [keys]

    return contains(list(dct.keys()), keys)


def token():
    """

    :return:
    """
    hlib = hashlib.sha256(str(random.getrandbits(256))).digest()
    rand = random.choice(['rA', 'aZ', 'gQ', 'hH', 'hG', 'aR', 'DD'])
    return base64.b64encode(hlib, rand).rstrip('==')


def pandas_column_merge(df, columns):
    """

    :param df:
    :param columns:
    :return:
    """

    def concat(*args):
        strings = [str(arg) for arg in args if not pd.isnull(arg)]
        return ' '.join(strings) if strings else np.nan

    np_concat = np.vectorize(concat)
    data = [df[col] for col in columns]
    return pd.Series(np_concat(*data))


def has_same_type(lst, exp_type):
    """

    :param lst:
    :param exp_type:
    :return:
    """
    return all(isinstance(n, exp_type) for n in lst)


def now():
    """
    Returns the current date time. useful for created_at for db operations
    :return:
    """
    return datetime.datetime.utcnow()


def make_dir(path):
    """

    :param path:
    :return:
    """
    if not os.path.exists(path):
        os.makedirs(path)


def make_dirs(paths, extension=None):
    """

    :param locations:
    :param extension:
    :return:
    """
    final_paths = remove_trailing_chars(paths, extension)
    for path in final_paths:
        if not os.path.exists(path):
            os.makedirs(path)


def remove_dir(path):
    import shutil

    def del_rw(action, name, exc):
        os.chmod(name, os.stat.S_IWRITE)
        os.remove(name)

    if os.path.isfile(path):
        os.remove(path)
    else:
        shutil.rmtree(path, onerror=del_rw)


def remove_duplicates(l, keys=None):
    if keys is not None:
        return [
            dict(t) for t in set([tuple(
                [(k, d[k]) for k in keys]
            ) for d in l])
            ]
    return [dict(t) for t in set([tuple(d.items()) for d in l])]


def intersect(a, b):
    return list(set(a) & set(b))


def get_model_name(serviceid, model_type, engine=None):
    if engine=="":
        engine=None
    model_name = serviceid if engine is None else "%s-%s" % (serviceid, engine)
    return "%s-%s" % (model_name, model_type)

def get_file_name(serviceid, model_type, engine=None, extension=None):
   return "%s.%s" % (get_model_name(serviceid, model_type, engine),extension)
