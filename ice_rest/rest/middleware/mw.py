import json
import logging
from cgi import FieldStorage

import falcon

from ice_rest.decorators.base import middleware
from ice_commons.utility.encoding import json_encode

logger = logging.getLogger(__name__)


def parse(req, ):
    if 'multipart/form-data' not in (req.content_type or ''):
        return

    env = req.env
    env.setdefault('QUERY_STRING', '')

    # TODO: Add error handling, when the request is not formatted
    # correctly or does not contain the desired field...

    # TODO: Consider overriding make_file, so that you can
    # stream directly to the destination rather than
    # buffering using TemporaryFile (see http://goo.gl/Yo8h3P)
    form = FieldStorage(fp=req.stream, environ=env)
    for key in form:
        field = form[key]
        if not getattr(field, 'filename', False):
            field = form.getvalue(key)
        # TODO: put files in req.files instead when #493 get merged.
        req._params[key] = field


@middleware()
class RequireJSON(object):
    def process_request(self, req, resp):
        if not req.client_accepts_json:
            raise falcon.HTTPNotAcceptable(
                'This API only supports responses encoded as JSON.',
                href='rest://docs.examples.com/api/json')

        if req.method in ('POST', 'PUT'):
            if not ('application/json' not in req.content_type or 'multipart/form-data' not in req.content_type):
                raise falcon.HTTPUnsupportedMediaType(
                    'This API only supports requests encoded as JSON or multipart/form-data.',
                    href='rest://docs.examples.com/api/json')


@middleware()
class RequestBodyTranslator(object):
    def process_request(self, req, resp):
        """
        # req.stream corresponds to the WSGI wsgi.input environ variable,
        # and allows you to read bytes from the request body.
        #
        # See also: PEP 3333

        :param req:
        :param resp:
        :return:
        """

        if req.content_length in (None, 0):
            # Nothing to do
            return

        try:
            if 'application/json' in req.content_type:
                body = req.stream.read()
                if not body:
                    raise falcon.HTTPBadRequest('Empty request body', 'A valid JSON document is required.')
                req.context['doc'] = json.loads(body.decode('utf-8'))
            elif 'multipart/form-data' in (req.content_type or ''):
                parse(req)
            else:
                raise falcon.HTTPUnsupportedMediaType(
                    'This API only supports requests encoded as JSON or multipart/form-data.')
        except (ValueError, UnicodeDecodeError):
            raise falcon.HTTPError(falcon.HTTP_753,
                                   'Malformed JSON',
                                   'Could not decode the request body. The '
                                   'JSON was incorrect or not encoded as '
                                   'UTF-8.')

    def process_response(self, req, resp, resource, xyz=None):
        """
        :param req:
        :param resp:
        :param resource:
        :return:
        """
        callback = req.get_param('callback') or None
        response = resp.data
        if not isinstance(response, str):
            response = json_encode(response)
        if callback is not None:
            response = req.get_param('callback') + '(' + response + ')'
        resp.data = bytes(response, 'utf-8')
