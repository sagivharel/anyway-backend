from flask_restplus import Api

from .markers import api as markers_api
from .rsa import ns_rsa as rsa_api

api = Api(
    title='Anyway',
    version='1.0',
    description='Anyway apis',
    # All API metadatas
)

api.add_namespace(markers_api, path='/markers')
api.add_namespace(rsa_api, path='/rsa')
