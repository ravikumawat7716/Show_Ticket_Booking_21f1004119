from instance.app import app
from instance.api import api
from flask_cors import CORS
from instance.db import db
from application.config import Config
from application.models import User, Venue , Show , Bookings , Reviews
from werkzeug.security import generate_password_hash
from instance.mail import mail


def create_app():
    app.config.from_object(Config)
    CORS(app)
    db.init_app(app)
    api.init_app(app)
    mail.init_app(app)
    initialize_database()
    return app

def initialize_database():
    with app.app_context():
        inspector = db.inspect(db.engine)
        tables = inspector.get_table_names()
        if not tables:
            db.create_all()
            print("Database initialized successfully")
            print("================================")
        if not User.query.filter_by(role='admin').first():
            username = input("Enter username for Admin : ")
            email = input("Enter email for Admin : ")
            password = input("Enter password for Admin : ")
            confirm_password = input("Confirm password for Admin : ")
            if password == confirm_password:
                password = generate_password_hash(password)
                user = User(username=username, email=email, password=password, role='admin')
                db.session.add(user)
                db.session.commit()
                print("Admin created successfully.")
            else:
                print("Passwords do not match. Try again.")
                initialize_database()
        else:
            print("Admin already exists.")
            print("================================")
        