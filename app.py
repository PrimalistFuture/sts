import os

from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension

from model import db, connect_db, Playtime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", 'postgresql:///sts_test')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

def add_run_data(obj):
    """Add some data from a .run to a table"""

    character = obj['character_chosen']
    playtime = obj['playtime']
    floor_reached = obj['floor_reached']

    run = Playtime(
        character=character,
        playtime=playtime,
        floor_reached=floor_reached
    )

    db.session.add(run)
    db.session.commit()

    return run