from flask_restful import Resource
from instance.api import api
from flask import request
from instance.db import db
from application.models import Venue

class Venues(Resource):
    def post(self):
        data = request.get_json()
        print(data)
        name = data['name']
        location = data['location']
        capacity = data['capacity']
        
        if name and location and capacity:
            venue = Venue.query.filter_by(name=name).first()
            if venue:
                return {"message": "Venue already exists."}, 409
            else:
                venue = Venue(name=name, location=location, capacity=capacity)
                db.session.add(venue)
                db.session.commit()
                return {"message": "Venue created successfully."}, 201
        return {"message": "Incorrect Data"}, 400
    
    def get(self):
        print("Get Venue API Called")
        venues = Venue.query.all()
        if not venues:
            return {"message": "No venues found."}, 404
        else:
            data = []
            for venue in venues:
                data.append({"id": venue.id, "name": venue.name, "location": venue.location, "capacity": venue.capacity})
            return data, 200
        
    def put(self):
        print("Update Venue API Called")
        data = request.get_json()
        id = data['id']
        name = data['name'] 
        location = data['location'] 
        capacity = data['capacity'] 
        print(data)
        
        if id and name and location and capacity:
            venue = Venue.query.filter_by(id=id).first()
            if venue:
                venue.name = name
                venue.location = location
                venue.capacity = capacity
                db.session.commit()
                return {"message": "Venue updated successfully."}, 200
            else:
                return {"message": "Invalid Venue ID"}, 404
        else:
            return {"message": "Incorrect Data"}, 400
        
        
    
    
api.add_resource(Venues, '/venues')