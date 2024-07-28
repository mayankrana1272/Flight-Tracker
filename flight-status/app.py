from flask import Flask
from flask_restful import Api
from resources.flight import FlightResource

app = Flask(__name__)
api = Api(app)

api.add_resource(FlightResource, '/flights/<string:flight_id>')

if __name__ == '__main__':
    app.run(debug=True)
