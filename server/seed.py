from models import db, Episode, Guest, Appearance
from datetime import datetime
from app import app,db

def seed_data():
    data = [
        {"year": 1999, "occupation": "actor", "show_date": "1/11/99", "group": "Acting", "guest_list": "Michael J. Fox"},
        {"year": 1999, "occupation": "Comedian", "show_date": "1/12/99", "group": "Comedy", "guest_list": "Sandra Bernhard"},
        {"year": 1999, "occupation": "television actress", "show_date": "1/13/99", "group": "Acting", "guest_list": "Tracey Ullman"},
        {"year": 1999, "occupation": "film actress", "show_date": "1/14/99", "group": "Acting", "guest_list": "Gillian Anderson"},
        {"year": 1999, "occupation": "actor", "show_date": "1/18/99", "group": "Acting", "guest_list": "David Alan Grier"},
        {"year": 1999, "occupation": "actor", "show_date": "1/19/99", "group": "Acting", "guest_list": "William Baldwin"},
        {"year": 1999, "occupation": "Singer-lyricist", "show_date": "1/20/99", "group": "Musician", "guest_list": "Michael Stipe"},
        {"year": 1999, "occupation": "model", "show_date": "1/21/99", "group": "Media", "guest_list": "Carmen Electra"},
        {"year": 1999, "occupation": "actor", "show_date": "1/25/99", "group": "Acting", "guest_list": "Matthew Lillard"},
        {"year": 1999, "occupation": "stand-up comedian", "show_date": "1/26/99", "group": "Comedy", "guest_list": "David Cross"},
        {"year": 1999, "occupation": "actress", "show_date": "1/27/99", "group": "Acting", "guest_list": "Yasmine Bleeth"},
        {"year": 1999, "occupation": "actor", "show_date": "1/28/99", "group": "Acting", "guest_list": "D. L. Hughley"},
        {"year": 1999, "occupation": "television actress", "show_date": "10/18/99", "group": "Acting", "guest_list": "Rebecca Gayheart"},
        {"year": 1999, "occupation": "Comedian", "show_date": "10/19/99", "group": "Comedy", "guest_list": "Steven Wright"},
        {"year": 1999, "occupation": "actress", "show_date": "10/20/99", "group": "Acting", "guest_list": "Amy Brenneman"},
        {"year": 1999, "occupation": "actress", "show_date": "10/21/99", "group": "Acting", "guest_list": "Melissa Gilbert"},
        {"year": 1999, "occupation": "actress", "show_date": "10/25/99", "group": "Acting", "guest_list": "Cathy Moriarty"},
        {"year": 1999, "occupation": "comedian", "show_date": "10/26/99", "group": "Comedy", "guest_list": "Louie Anderson"},
        {"year": 1999, "occupation": "actress", "show_date": "10/27/99", "group": "Acting", "guest_list": "Sarah Michelle Gellar"},
        {"year": 1999, "occupation": "Singer-songwriter", "show_date": "10/28/99", "group": "Musician", "guest_list": "Melanie C"},
        {"year": 1999, "occupation": "actor", "show_date": "10/4/99", "group": "Acting", "guest_list": "Greg Proops"},
        {"year": 1999, "occupation": "television personality", "show_date": "10/5/99", "group": "Media", "guest_list": "Maury Povich"},
        {"year": 1999, "occupation": "actress", "show_date": "10/6/99", "group": "Acting", "guest_list": "Brooke Shields"},
        {"year": 1999, "occupation": "Comic", "show_date": "10/7/99", "group": "Comedy", "guest_list": "Molly Shannon"},
        {"year": 1999, "occupation": "actor", "show_date": "11/1/99", "group": "Acting", "guest_list": "Chris O'Donnell"},
        {"year": 1999, "occupation": "actress", "show_date": "11/15/99", "group": "Acting", "guest_list": "Christina Ricci"},
        {"year": 1999, "occupation": "Singer-songwriter", "show_date": "11/16/99", "group": "Musician", "guest_list": "Tori Amos"},
        {"year": 1999, "occupation": "actress", "show_date": "11/17/99", "group": "Acting", "guest_list": "Yasmine Bleeth"},
        {"year": 1999, "occupation": "comedian", "show_date": "11/18/99", "group": "Comedy", "guest_list": "Bill Maher"},
        {"year": 1999, "occupation": "actress", "show_date": "11/2/99", "group": "Acting", "guest_list": "Jennifer Love Hewitt"},
        {"year": 1999, "occupation": "rock band", "show_date": "11/29/99", "group": "Musician", "guest_list": "Goo Goo Dolls"},
        {"year": 1999, "occupation": "musician", "show_date": "11/3/99", "group": "Musician", "guest_list": "Dave Grohl"},
        {"year": 1999, "occupation": "Film actor", "show_date": "11/30/99", "group": "Acting", "guest_list": "Stephen Rea"},
        {"year": 1999, "occupation": "Model", "show_date": "11/4/99", "group": "Media", "guest_list": "Roshumba Williams"},
        {"year": 1999, "occupation": "television actress", "show_date": "11/8/99", "group": "Acting", "guest_list": "Kellie Martin"},
        {"year": 1999, "occupation": "actress", "show_date": "11/9/99", "group": "Acting", "guest_list": "Kathy Griffin"},
        {"year": 1999, "occupation": "actress", "show_date": "12/1/99", "group": "Acting", "guest_list": "Laura San Giacomo"},
        {"year": 1999, "occupation": "journalist", "show_date": "12/13/99", "group": "Media", "guest_list": "Joan Lunden"},
        {"year": 1999, "occupation": "actress", "show_date": "12/14/99", "group": "Acting", "guest_list": "Shannen Doherty"},
        {"year": 1999, "occupation": "NA", "show_date": "12/15/99", "group": "NA", "guest_list": "Greatest Millennium Special"},
        {"year": 1999, "occupation": "comedian", "show_date": "12/16/99", "group": "Comedy", "guest_list": "George Carlin"},
        {"year": 1999, "occupation": "actor", "show_date": "12/2/99", "group": "Acting", "guest_list": "Michael Boatman"},
        {"year": 1999, "occupation": "actor", "show_date": "12/20/99", "group": "Acting", "guest_list": "David Boreanaz"},
        {"year": 1999, "occupation": "singer-songwriter", "show_date": "12/21/99", "group": "Musician", "guest_list": "Jewel"},
        {"year": 1999, "occupation": "actor", "show_date": "12/6/99", "group": "Acting", "guest_list": "Paul Rudd"},
        {"year": 1999, "occupation": "us senator", "show_date": "12/7/99", "group": "Politician", "guest_list": "Senator Bob Dole"},
        {"year": 1999, "occupation": "us senator", "show_date": "12/8/99", "group": "Politician", "guest_list": "Senator Bob Dole"},
        {"year": 1999, "occupation": "actor", "show_date": "12/9/99", "group": "Acting", "guest_list": "Steve Zahn"}
    ]
    
    for entry in data:
        try:
            show_date = datetime.strptime(entry["show_date"], '%m/%d/%y').strftime('%Y-%m-%d')
        except ValueError:
            print(f"Skipping invalid date format: {entry['show_date']}")
            continue

        episode = Episode(
            date=show_date,
            number=None
        )

        db.session.add(episode)
        db.session.commit()

        guests = entry["guest_list"].split(", ")

        for guest_name in guests:
            guest = Guest.query.filter_by(name=guest_name).first()
            if not guest:
                guest = Guest(
                    name=guest_name,
                    occupation=entry["occupation"]
                )
                db.session.add(guest)
                db.session.commit()

            appearance = Appearance(
                rating=3,
                episode_id=episode.id,
                guest_id=guest.id
            )
            db.session.add(appearance)

    db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        seed_data()
