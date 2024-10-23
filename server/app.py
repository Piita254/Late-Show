from flask import request
from flask_restful import Resource
from config import app, db, api
from models import Episode, Appearance, Guest

# Route to get all episodes
class EpisodeListResource(Resource):
    def get(self):
        episodes = Episode.query.all()
        episodes_list = [episode.to_dict() for episode in episodes]
        return episodes_list, 200  # No need for jsonify, Flask-RESTful handles it

# Resource for fetching a single episode by ID
class EpisodeResource(Resource):
    def get(self, id):
        episode = Episode.query.filter(Episode.id == id).first()

        if episode is None:
            return {"error": "Episode not found"}, 404

        episode_data = {
            "id": episode.id,
            "date": episode.date,
            "number": episode.number,
            "appearances": [
                {
                    "id": appearance.id,
                    "episode_id": appearance.episode_id,
                    "guest_id": appearance.guest_id,
                    "guest": {
                        "id": appearance.guest.id,
                        "name": appearance.guest.name,
                        "occupation": appearance.guest.occupation
                    },
                    "rating": appearance.rating
                }
                for appearance in episode.appearance
            ]
        }

        return episode_data, 200

# Resource for fetching all guests
class GuestListResource(Resource):
    def get(self):
        guests = Guest.query.all()
        guests_list = [
            {
                'id': guest.id,
                'name': guest.name,
                'occupation': guest.occupation
            }
            for guest in guests
        ]
        return guests_list, 200

# Resource for creating a new appearance
class AppearanceResource(Resource):
    def post(self):
        data = request.get_json()

        rating = data.get('rating')
        episode_id = data.get('episode_id')
        guest_id = data.get('guest_id')

        # Validate inputs
        if rating is None or not (1 <= rating <= 5):
            return {"errors": ["Rating must be between 1 and 5"]}, 400

        if not episode_id or not guest_id:
            return {"errors": ["Both episode_id and guest_id are required"]}, 400

        episode = Episode.query.get(episode_id)
        guest = Guest.query.get(guest_id)

        if not episode or not guest:
            return {"errors": ["Episode or Guest not found"]}, 404

        new_appearance = Appearance(
            rating=rating,
            episode_id=episode_id,
            guest_id=guest_id
        )

        db.session.add(new_appearance)
        db.session.commit()

        # Format the response data
        response_data = {
            "id": new_appearance.id,
            "rating": new_appearance.rating,
            "guest_id": new_appearance.guest_id,
            "episode_id": new_appearance.episode_id,
            "episode": {
                "id": episode.id,
                "date": episode.date,
                "number": episode.number
            },
            "guest": {
                "id": guest.id,
                "name": guest.name,
                "occupation": guest.occupation
            }
        }
        return response_data, 201

# Adding resources to API
api.add_resource(EpisodeListResource, '/episodes')
api.add_resource(EpisodeResource, '/episodes/<int:id>')
api.add_resource(GuestListResource, '/guests')
api.add_resource(AppearanceResource, '/appearances')

if __name__ == '__main__':
    app.run(port=5555, debug=True)
