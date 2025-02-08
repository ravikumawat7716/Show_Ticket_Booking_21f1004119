from instance.api import api
from flask_restful import Resource
from flask import request
from instance.db import db
from application.models import User
from werkzeug.security import check_password_hash , generate_password_hash
from utils.mail import send_email


class Login(Resource):
    def post(self):
        print("Login API called")
        data = request.get_json()
        username = data['username']
        password = data['password']
        if username and password:
            user = User.query.filter_by(username=username).first()
            if user:
                if check_password_hash(user.password, password):
                    role = user.role
                    token = "1234"
                    username = user.username
                    return {"message": "Login successful.", "user_role" : role, "token": token , "username" : username}, 200
                else:
                    return {"message": "Invalid credentials."}, 401
            else:
                return {"message": "User not found."}, 404
        else:
            return {"message": "Invalid data."}, 400
            
            
    
class Registration(Resource):
    def post(self):
        print("Registration API called")
        data = request.get_json()
        username = data['username']
        email = data['email']
        password = data['password']
        password_copy = password
        if username and email and password:
            user = User.query.filter_by(username=username).first()
            if user:
                return {"message": "User already exists."}, 409
            else:
                password = generate_password_hash(password)
                user = User(username=username, email=email, password=password, role='user')
                db.session.add(user)
                db.session.commit()
                print("Database Commit done , now sending the email")
                send_email(email, "Registration successful", f"You have successfully registered on our Show Ticket Booking platform.Your Username is {email} and Password is {password_copy}")
                return {"message": "User created successfully."}, 201
        else:
            return {"message": "Invalid data."}, 400

    
api.add_resource(Login, '/login')
api.add_resource(Registration, '/register')