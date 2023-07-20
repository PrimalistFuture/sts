"""Seed file to make sample data for playtimes db."""

from model import Playtime, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it

# Add pets
run1 = Playtime(
    character='IRONCLAD',
    playtime=3002,
    floor_reached=51
)
run2 = Playtime(
    character='The_SILENT',
    playtime=1565,
    floor_reached=35
)
run3 = Playtime(
    character='IRONCLAD',
    playtime=2998,
    floor_reached=51
)
run4 = Playtime(
    character='DEFECT',
    playtime=3002,
    floor_reached=51
)

# Add new objects to session, so they'll persist
db.session.add(run1)
db.session.add(run2)
db.session.add(run3)
db.session.add(run4)

# Commit--otherwise, this never gets saved!
db.session.commit()