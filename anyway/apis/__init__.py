from flask_restplus import Api

from .markers import api as markers_api
from .rsa import ns_rsa as rsa_api

api = Api(
    title='Anyway',
    version='1.0',
    description='Anyway API'
)

api.add_namespace(markers_api, path='/markers')
api.add_namespace(rsa_api, path='/rsa')
