from ice_commons.core.resolution.utils.handleDatesTime import DateUtils


def test_parse_date():
    obj = DateUtils()
    text = 'Block my calender for 4 pm day after tomorrow and book a ticket by 3.45 pm on next christmas, coming new ' \
           'year and on all holidays '
    assert obj.parse_date(text) == [
        dict(timestamp='2019-04-14 00:00:00+05.50', words='day after tomorrow', unit='day', position=[6, 9]),
        dict(timestamp='2019-12-25 00:00:00+05.50', words='next christmas', unit='festival', position=[17, 19]),
        dict(timestamp='2020-01-01 00:00:00+05.50', words='coming new year', unit='festival', position=[20, 23]),
        dict(timestamp='2019-04-12 16:00:00', words='4 pm day', unit='date', position=[4, 7])]


def test_parse_date_weekdays():
    obj = DateUtils()
    text = 'I will be leave on the coming wednesday and thursday and was working from home on last monday'
    assert obj.parse_date(text) == [
        dict(timestamp='2019-04-17 00:00:00+05.50', words='coming wednesday', unit='day', position=[6, 8]),
        dict(timestamp='2019-04-18 00:00:00+05.50', words='thursday', unit='day', position=[9, 10]),
        dict(timestamp='2019-04-08 00:00:00+05.50', words='last monday', unit='day', position=[16, 18])]


def test_parse_date_past():
    obj = DateUtils()
    text = 'I was leave on day before yestrerday and on last christmas'
    assert obj.parse_date(text) == [
        dict(timestamp='2019-04-11 00:00:00+05.50', words='before day', unit='day', position=[5, 5]),
        dict(timestamp='2018-12-25 00:00:00+05.50', words='last christmas', unit='festival', position=[9, 11])]


def test_parse_date_duration():
    obj = DateUtils()
    text = 'I was leave from last week monday to this week saturday and will be working from now to next sunday'
    assert obj.parse_date(text) == [
        dict(timestamp='2019-04-05 00:00:00+05.50', words='last week', unit='week', position=[4, 6]),
        dict(timestamp='2019-04-08 00:00:00+05.50', words='monday', unit='day', position=[6, 7]),
        dict(timestamp='2019-04-12 00:00:00+05.50', words='this week', unit='week', position=[8, 10]),
        dict(timestamp='2019-04-06 00:00:00+05.50', words='saturday', unit='day', position=[10, 11]),
        dict(timestamp='2019-04-14 00:00:00+05.50', words='next sunday', unit='day', position=[18, 20])]


def test_parse_date_christmas():
    obj = DateUtils()
    text = 'The christmas celebration is on 23rd Decemberand thanksgiving cermony will be on 28th of this month'
    assert obj.parse_date(text) == [
        dict(timestamp='2019-12-25 00:00:00+05.50', words='christmas', unit='festival', position=[1, 2]),
        dict(timestamp='2019-11-22 00:00:00+05.50', words='thanksgiving', unit='festival', position=[7, 8]),
        dict(timestamp='2019-04-12 00:00:00+05.50', words='this month', unit='month', position=[14, 16])]


def test_previous_thankgiving():
    obj = DateUtils()
    text = 'day before yesterday was my birthday'
    assert obj.parse_date(text) == [{'timestamp': '2019-04-10 00:00:00+05.50', 'words': 'day before yesterday', 'unit': 'day', 'position': [0, 3]}]

