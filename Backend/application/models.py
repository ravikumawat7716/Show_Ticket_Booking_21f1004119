from instance.db import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    role = db.Column(db.String(80), nullable=False)
    
class Venue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    location = db.Column(db.String(120), nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    
class Show(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.Time, nullable=False)
    venue_id = db.Column(db.Integer, db.ForeignKey('venue.id'), nullable=False)
    venue = db.relationship('Venue', backref=db.backref('shows', lazy=True))
    
class Bookings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('bookings', lazy=True))
    show_id = db.Column(db.Integer, db.ForeignKey('show.id'), nullable=False)
    show = db.relationship('Show', backref=db.backref('bookings', lazy=True))
    tickets = db.Column(db.Integer, nullable=False)
    amount = db.Column(db.Float, nullable=False)
    
class Reviews(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('reviews', lazy=True))
    show_id = db.Column(db.Integer, db.ForeignKey('show.id'), nullable=False)   
    show = db.relationship('Show', backref=db.backref('reviews', lazy=True))
    rating = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(500), nullable=False)
    
    
