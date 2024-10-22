from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin


metadata = MetaData()

db = SQLAlchemy(metadata=metadata) 

class Episode(db.Model, SerializerMixin):
    __tablename__ = 'episodes'

    serializer_rules = ('-appearances.episode',)

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String)
    number = db.Column(db.Integer)

    appearances = db.relationship('Appearance', back_populates='episode')

class Guest(db.Model, SerializerMixin):
    __tablename__ = 'guests'

    serializer_rules = ('-appearances.guest',)

    id = db.Column(db.Integer, primary_key=True)  
    name = db.Column(db.String)  
    occupation = db.Column(db.String)  

    appearances = db.relationship('Appearance', back_populates='guest')

class Appearance(db.Model, SerializerMixin):
    __tablename__ = 'appearances'

    serializer_rules = ('-episode.appearances -guest.appearances')

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer)
    episode_id = db.Column(db.Integer, db.ForeignKey('episodes.id',ondelete='CASCADE'))
    guest_id = db.Column(db.Integer, db.ForeignKey('guests.id',ondelete='CASCADE')) 

    episode = db.relationship('Episode', back_populates='appearances')  
    guest = db.relationship('Guest', back_populates='appearances')  
