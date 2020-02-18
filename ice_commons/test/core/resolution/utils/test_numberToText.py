import pytest

from ice_commons.core.resolution.utils.numberToText import stringToNumHandlingFunc

expected_output = [dict(text='26 thousand', digit=26000.0, start_index=2, end_index=3),
                   dict(text='two thousand six HUNDRED and forty three', digit=2643, start_index=12, end_index=18)]


@pytest.fixture
def text():
    # text = u'There are 26 thousand people in UST and still the company needs two thousand six HUNDRED and forty \
    # three more. '
    text = 'It is one half of the bottle'
    return text


def test_stringToNumHandlingFunc(text):
    actual_output = stringToNumHandlingFunc(text)
    print(actual_output)
    # assert actual_output == expected_output, "Failed to get the expected output"
