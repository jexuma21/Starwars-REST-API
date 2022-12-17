from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Characters(db.Model):
    __tablename__ = 'characters'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<Character %r>' % self.name
        
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
        }

class Planets(db.Model):
    __tablename__ = 'planets'
    planet_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<Planet %r>' % self.name
        
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
        }       

class Vehicles(db.Model):
    __tablename__ = 'vehicles'
    vehicle_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<Vehicle %r>' % self.name
        
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
        }       

class Favorites(db.Model):
    __tablename__ = 'favorites'
    date_added = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True, nullable=False)
    favorite_characters = db.Column(db.Integer, db.ForeignKey('characters.name'))
    favorite_planets = db.Column(db.Integer, db.ForeignKey('planets.name'))
    favorite_vehicles = db.Column(db.Integer, db.ForeignKey('vehicles.name'))


    def __repr__(self):
        return '<Favorite %r>' % self.name
        
    def serialize(self):
        return {
            "date_added": self.date_added,
            "user_id": self.user_id,
            "favorite_characters": self.favorite_characters,
            "favorite_planets": self.favorite_characters,
            "favorite_vehicles": self.favorite_characters
        }       