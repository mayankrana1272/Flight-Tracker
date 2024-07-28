from flask_restful import Resource
from models import flights

class FlightResource(Resource):
    def get(self, flight_id):
        flight = flights.get(flight_id)
        if flight:
            return flight, 200
        return {'message': 'Flight not found'}, 404
