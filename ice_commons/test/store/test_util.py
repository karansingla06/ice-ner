# import sys
# sys.path.append('/home/nivedithahn/ner/verbis/')
import pytest, falcon
from ice_commons.store.util import regex_checker, phrase_checker, validate_regex
import re


def test_phrase_checker_with_null(mocker):
    phrase= phrase_checker('', [])
    assert phrase==[]



def test_phrase_checker_with_data1(mocker):
    phrases = phrase_checker('my fav color is blue and i hate pink', [{
			"phrase" : [
				"blue",
				"yellow",
				"pink"
			],
			"entity" : "colors"
		}])

    assert phrases == [{'end': 5, 'entity': 'blue', 'start': 4, 'tag': 'colors'},{'end': 9, 'entity': 'pink', 'start': 8, 'tag': 'colors'}]


def test_phrase_checker_with_data2(mocker):
    phrases = phrase_checker('my fav color is black and charcoal black ', [{
			"phrase" : [
				"black",
				"sky blue",
				"pink"
			],
			"entity" : "colors"
		}])
    assert phrases == [{'end': 5, 'entity': 'black', 'start': 4, 'tag': 'colors'},{'end': 8, 'entity': 'black', 'start': 7, 'tag': 'colors'}]


def test_regex_checker_with_null(mocker):
    patterns= regex_checker('', [])
    resp= mocker.patch('ice_commons.store.util.remove_duplicates', [])
    assert patterns==resp


def test_regex_checker_with_data1(mocker):
    patterns = regex_checker('my birthdate is 27-06-1995', [
		{
			"entity" : "custom_date",
			"pattern" : "\s\d{4}-\d{2}-\d{2}|\d{2}-\d{2}-\d{4}"
		}
	])
    assert patterns == [{'end': 4, 'entity': '27-06-1995', 'start': 3, 'tag': 'custom_date'}]


def test_regex_checker_with_data2(mocker):
    patterns = regex_checker('my birthdate is 27-06-1995 and my brithers is 28-04-1993' , [
		{
			"entity" : "custom_date",
			"pattern" : "\s\d{4}-\d{2}-\d{2}|\d{2}-\d{2}-\d{4}"
		}
	])
    assert patterns == [{'end': 4, 'entity': '27-06-1995', 'start': 3, 'tag': 'custom_date'}, {'end': 9, 'entity': '28-04-1993', 'start': 8, 'tag': 'custom_date'}]


def test_validate_regex_with_null(mocker):
    pattern = None
    resp = validate_regex(pattern)
    expected = False
    assert expected == resp

def test_validate_regex_with_text(mocker):
    pattern = '[a-z0-9A-Z_.-]+@[da-zA-Z.-]+.[a-zA-Z.]{2,6}'
    resp = validate_regex(pattern)
    assert resp == re.compile(pattern)
