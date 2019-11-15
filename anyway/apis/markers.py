from flask_restplus import Namespace, Resource, fields

api = Namespace('markers', description='Markers related operations')

marker = api.model('Marker', {
    'id': fields.String(required=True, description='The marker identifier'),
    'name': fields.String(required=True, description='The marker name'),
})

MARKERS = [
    {'id': 'test', 'name': 'Test name'},
]


@api.route('/')
class MarkersList(Resource):

    @api.doc('list_markers')
    @api.marshal_list_with(marker)
    def get(self):
        # List all markers
        return MARKERS


@api.route('/<id>')
@api.param('id', 'The marker identifier')
@api.response(404, 'Marker not found')
class Marker(Resource):

    @api.doc('get_marker')
    @api.marshal_with(marker)
    def get(self, id):
        # Fetch a marker given its identifier
        for marker in MARKERS:
            if marker['id'] == id:
                return marker
        api.abort(404)
