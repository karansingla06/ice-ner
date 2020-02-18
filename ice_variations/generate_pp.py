import json
import falcon
import os
import sys


from generate_paraphrases import *

class Resource(object):

	def on_post(self,req,resp):
		body = req.stream.read()
		text = json.loads(body.decode('utf-8'))
		resp.body= json.dumps({'message':text['text']})
		resp.status = falcon.HTTP_200

	def on_get(self, req, resp):
		doc = {"message":"hello"}
		resp.body = json.dumps(doc)
		resp.status = falcon.HTTP_200



class GenerateVariationsResource(object):
	def on_post(self, req, resp):
#		doc = req.context['doc'] or {}
	#	try:
			body = req.stream.read()
			doc = json.loads(body.decode('utf-8'))
			resp.body = json.dumps(generate_variations(doc['text']))
			resp.status = falcon.HTTP_200

	#	except Exception as ex:
	#		print "exception raised"
	#		resp.set_header('X-Powered-By', 'USTGlobal ICE')
	#		resp.status = falcon.HTTP_500

