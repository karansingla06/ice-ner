
import falcon

from generate_pp import Resource, GenerateVariationsResource

api= application = falcon.API()

gen = Resource()
api.add_route('/paraphrases',gen)

gen_pp = GenerateVariationsResource()
api.add_route('/generate_variations',gen_pp)

