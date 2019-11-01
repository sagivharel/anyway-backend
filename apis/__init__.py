from flask_restplus import Api

from .markers import api as markers_api

api = Api(
    title='Anyway',
    version='1.0',
    description='Anyway apis',
    # All API metadatas
)

api.add_namespace(markers_api, path='/markers')
