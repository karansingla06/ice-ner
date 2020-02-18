import logging
import json
import falcon
from falcon import HTTPBadRequest
from ice_rest.decorators import route
from ice_commons.utils import dict_contains
from pydash import get
from ice_commons.data.dl.manager import TestRunsManager

logger = logging.getLogger(__name__)




@route('/api/parse/report')
class ReportFetchResource(object):
    @staticmethod
    def _bad_request():
        description = 'Mandatory params missing from the request. ' \
                      'Please check your request params and retry'
        logger.exception(description)
        raise HTTPBadRequest("HTTP Bad Request", description)

    def _validate_model_config(req, resp, resource, params):
        doc = req.context['doc'] or {}
        mandatory_fields = ['serviceid', 'timestamp']
        assert dict_contains(doc, mandatory_fields) is True, ReportFetchResource._bad_request()

    @falcon.before(_validate_model_config)
    def on_post(self, req, resp):
        doc = req.context['doc'] or {}
        serviceid = get(doc, "serviceid", None)
        timestring = get(doc, "timestamp", None)

        try:
            manager = TestRunsManager()
            reports = manager.fetch_all_reports(serviceid)
            results = []
            if 'runs' in reports:
                for i in reports['runs']:
                    i['run_time'] = i['run_time'].strftime('%Y-%m-%d %H:%M:%S')
                    ts = i['run_time']
                    if timestring == ts:
                        results = i
                        break
            resp.data = results

        except Exception as ex:
            logger.exception(ex)
            description = 'Internal Server Error, Please try again later'
            raise falcon.HTTPServiceUnavailable('Service Outage', description, 30)

        resp.set_header('X-Powered-By', 'USTGlobal Verbis')
        resp.status = falcon.HTTP_200



@route('/api/parse/report/ts')
class TimestampFetchResource(object):
    @staticmethod
    def _bad_request():
        description = 'Mandatory params missing from the request. ' \
                      'Please check your request params and retry'
        logger.exception(description)
        raise HTTPBadRequest("HTTP Bad Request", description)

    def _validate_model_config(req, resp, resource, params):
        doc = req.context['doc'] or {}
        mandatory_fields = ['serviceid']
        assert dict_contains(doc, mandatory_fields) is True, TimestampFetchResource._bad_request()

    @falcon.before(_validate_model_config)
    def on_post(self, req, resp):
        doc = req.context['doc'] or {}
        serviceid = get(doc, "serviceid", None)
        try:
            response = {}
            manager = TestRunsManager()
            timestamps_map = manager.fetch_timestamps(serviceid)
            ts_list = []
            all_reports = manager.fetch_all_reports(serviceid)
            if timestamps_map is not None:
                for t in timestamps_map['runs']:
                    ts_list.append(t['run_time'].strftime('%Y-%m-%d %H:%M:%S'))
                response['timestamps']=ts_list
            ts_list.sort(reverse=True)
            if all_reports is not None:
                for report in all_reports['runs']:
                    report['run_time'] = report['run_time'].strftime('%Y-%m-%d %H:%M:%S')
                    if report['run_time']==ts_list[0]:
                        response['report'] = report
                        break
            resp.data = response
        except Exception as ex:
            logger.exception(ex)
            description = 'Internal Server Error, Please try again later'
            raise falcon.HTTPServiceUnavailable('Service Outage', description, 30)

        resp.set_header('X-Powered-By', 'USTGlobal Verbis')
        resp.status = falcon.HTTP_200