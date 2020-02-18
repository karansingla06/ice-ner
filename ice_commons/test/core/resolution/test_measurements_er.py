from ice_commons.core.resolution.measurements_er import MeasurementsResolutionNER


def test_resolve_validate_expected_response():
    measurement_er_obj = MeasurementsResolutionNER()
    text = 'The LHC smashes proton beams at 12.9 TeV'
    actual_response = measurement_er_obj.resolve(text)
    expected_response = [
        {'end': 8, 'entity': "12.9 TeV", 'resolvedTo': dict(baseEntity="12.9 TeV", quantity=12.9,
                                                            unit="teraelectronvolt"), 'start': 6, 'tag': "ENERGY"}
    ]
    assert expected_response == actual_response, "Expected Response is wrong"


def test_resolve_input_text_without_unit():
    measurement_er_obj = MeasurementsResolutionNER()
    text = 'I have five balls in my hand'
    actual_response = measurement_er_obj.resolve(text)
    assert actual_response == [], "measurement with unit is expected"


def test_resolve_validate_text_with_no_measurements():
    measurement_er_obj = MeasurementsResolutionNER()
    text = 'I have balls with me'
    actual_response = measurement_er_obj.resolve(text)
    assert actual_response == [], "Measurement expected"


def test_resolve_unicode_text():
    measurement_er_obj = MeasurementsResolutionNER()
    text = 123454
    actual_response = measurement_er_obj.resolve(text)
    assert actual_response == [], "The expected type of text is string or unicode"


def test_resolve_uncertain_input():
    measurement_er_obj = MeasurementsResolutionNER()
    text = 'it is seven and eight km away from agra'
    actual_response = measurement_er_obj.resolve(text)
    assert actual_response == [
        dict(resolvedTo={'baseEntity': 'seven and eight km', 'unit': 'kilometre', 'quantity': 15.0}, tag='LENGTH',
             end=6, start=2,
             entity='seven and eight km')], "The expected text is 'IT IS SEVEN KM AND EIGHT KM AWAY FROM AGRA "


def test_resolve_with_null_text():
    measurement_er_obj = MeasurementsResolutionNER()
    text = ''
    actual_response = measurement_er_obj.resolve(text)
    assert actual_response == [], "The expected type of text is string or unicode"

