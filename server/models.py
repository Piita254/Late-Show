from sqlalchemy.orm import validates
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy_serializer import SerializerMixin

from config import db, bcrypt

class Episode(db.Model, SerializerMixin):
    __tablename__ = 'episodes'

    serialize_rules = ('-appearances.episode',)

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String)
    number = db.Column(db.Integer)

    # Relationship: an episode can have multiple appearances
    appearances = db.relationship('Appearance', back_populates='episode')

    def to_dict(self):
        return {
            "id": self.id,
            "date": self.date,
            "number": self.number
        }

class Guest(db.Model, SerializerMixin):
    __tablename__ = 'guests'

    serialize_rules = ('-appearances.guest',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    occupation = db.Column(db.String)

    # Relationship: a guest can have multiple appearances
    appearances = db.relationship('Appearance', back_populates='guest')

class Appearance(db.Model, SerializerMixin):
    __tablename__ = 'appearances'

    serialize_rules = ('-episode.appearances', '-guest.appearances')

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    episode_id = db.Column(db.Integer, db.ForeignKey('episodes.id'), nullable=False)
    guest_id = db.Column(db.Integer, db.ForeignKey('guests.id'), nullable=False)

    # Relationships
    episode = db.relationship('Episode', back_populates='appearances')
    guest = db.relationship('Guest', back_populates='appearances')

    @validates('rating')
    def validate_rating(self, key, rating):
        if not (1 <= rating <= 5):
            raise ValueError('Rating must be between 1 and 5 (inclusive).')
        return rating
