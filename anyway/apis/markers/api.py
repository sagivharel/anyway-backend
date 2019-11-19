from flask_restplus import Namespace, Resource, fields

markers_api = Namespace('markers', description='Markers related operations')

marker = markers_api.model('Marker', {
    'id': fields.String(required=True, description='The marker identifier'),
    'name': fields.String(required=True, description='The marker name'),
})

MARKERS = [
    {'id': 'test', 'name': 'Test name'},
]


@markers_api.route('/')
class MarkersList(Resource):

    @markers_api.doc('list_markers')
    @markers_api.marshal_list_with(marker)
    def get(self):
        # List all markers
        return MARKERS


@markers_api.route('/<id>')
@markers_api.param('id', 'The marker identifier')
@markers_api.response(404, 'Marker not found')
class Marker(Resource):

    @markers_api.doc('get_marker')
    @markers_api.marshal_with(marker)
    def get(self, id):
        # Fetch a marker given its identifier
        for marker in MARKERS:
            if marker['id'] == id:
                return marker
        markers_api.abort(404)
