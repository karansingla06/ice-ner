from ice_commons.core.resolution.date_er import DateResolutionNER
from ice_commons.core.resolution.utils.handleDatesTime import DateUtils


def test_date_resolver_validator():
    text = 'Block my calender on 7th fEb  at 4 pm and We are planning to celebrate coming Christmas in my aunts house'
    date_er_obj = DateResolutionNER()
    actual_response = date_er_obj.resolve(text)
    expected_response = [dict(start=15, resolvedTo={'second': '00', 'baseEntity': 'coming Christmas', 'hour': '12',
                                                    'year': '2019', 'timestamp': '2019-12-25 00:00:00+05.50',
                                                    'day': '25', 'minute': '00', 'month': 'December'},
                              tag='TIMESTAMP', end=17, entity='coming Christmas')]
    assert expected_response == actual_response, "Response failed"


def test_input_without_date():
    text = 'There is an apple in the box.'
    date_er_obj = DateResolutionNER()
    actual_response = date_er_obj.resolve(text)
    expected_response = []
    assert expected_response == actual_response, "Response failed"


def test_none_input():
    text = None
    date_er_obj = DateResolutionNER()
    actual_response = date_er_obj.resolve(text)
    expected_response = []
    assert expected_response == actual_response, "Response failed"


def test_null_input():
    text = ''
    date_er_obj = DateResolutionNER()
    actual_response = date_er_obj.resolve(text)
    expected_response = []
    assert expected_response == actual_response, "Response failed"


def test_time_without_date():
    text = 'Block my calender for 4 pm and book a meeting room by 3.45 pm'
    date_er_obj = DateResolutionNER()
    actual_response = date_er_obj.resolve(text)
    expected_response = [dict(start=4, resolvedTo=dict(second='00', baseEntity='4 pm', hour=' 4', year='2019',
                                                       timestamp='2019-04-12 16:00:00', day='12', minute='00',
                                                       month='April'), tag='TIMESTAMP', end=6, entity='4 pm'),
                         dict(start=12,
                              resolvedTo=dict(second='00', baseEntity='3.45 pm', hour=' 3', year='2019',
                                              timestamp='2019-04-12 15:00:00', day='12', minute='00', month='April'), tag='TIMESTAMP', end=6, entity='3.45 pm')]

    assert expected_response == actual_response, "Response failed"


def test_date_resolver(mocker):
    date_er_obj = DateResolutionNER()
    obj = mocker.patch('ice_commons.core.resolution.date_er.DateUtils', return_value=DateUtils())
    obj.return_value.parse_date={'timestamp': '2019-03-06 16:00:00'}
    actual_response = date_er_obj.resolve('Block my calender for 4 pm and book a meeting room by 3.45 pm')
    assert actual_response == []