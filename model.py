from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """Connect to database"""

    app.app_context().push()
    db.app = app
    db.init_app(app)

class Playtime(db.Model):
    """Playtime table"""

    __tablename__ = 'playtimes'

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    character = db.Column(
        db.String(20),
        nullable=False,
    )

    playtime = db.Column(
        db.Integer,
        nullable=False
    )

    floor_reached = db.Column(
        db.Integer,
        nullable=False
    )