from ice_commons.core.resolution.number_er import NumberResolutionNER


def test_number_resolver_validator():
    number_er = NumberResolutionNER()
    text = 'There are 26 thousand people in UST and still the company needs two thousand six HUNDRED and forty three ' \
           'more. '
    expected_response = [
        dict(end=4, entity="26 thousand", resolvedTo=dict(baseEntity="26 thousand", digit=26000), start=2,
             tag="NUMBER"),
        dict(end=19, entity="two thousand six HUNDRED and forty three",
             resolvedTo=dict(baseEntity="two thousand six HUNDRED and forty three", digit=2643), start=12, tag="NUMBER")
    ]
    actual_response = number_er.resolve(text)
    print(actual_response)
    assert actual_response == expected_response, "Response failed"