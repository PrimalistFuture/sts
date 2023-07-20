import json
import os

from model import db, connect_db, Playtime
from app import add_run_data
from json.decoder import JSONDecodeError

# test to see if I could get in a file
# file = "./STS-Runs/TEST/0001.run"
# with open(file, 'r') as read_file:
#     to_python = json.load(read_file)
#     print(to_python)

# script works just fine. Now to adapt it to a function.
# sts_test = os.fsencode('./STS-Runs/TEST')
# sum = 0
# runs = 0

# for b_file in os.listdir(sts_test):
#     file = os.fsdecode(b_file)
#     path = './STS-Runs/TEST/'
#     try:
#         with open(path+file) as read_file:
#             to_python = json.load(read_file)
#             print(f'{file}:', to_python['playtime'])
#             sum = sum + to_python['playtime']
#             runs = runs + 1
#     except JSONDecodeError as e:
#         print(file, e)

# test to see if I could get in a file and add one run to db
def add_file_data_to_db():
    """Quick attempt to make sure I can actually add a single file data to db before doing the full loop"""
    file = "./STS-Runs/TEST/1607742609.run"
    with open(file, 'r') as read_file:
        to_python = json.load(read_file)
        return add_run_data(to_python)


def collect_runs_and_add_to_db():
    """Adds the character, playtime and floor_reached to the db table playtimes"""

    sts_test = os.fsencode('./STS-Runs/TEST')

    for b_file in os.listdir(sts_test):
        file = os.fsdecode(b_file)
        path = './STS-Runs/TEST/'
        try:
            with open(path+file) as read_file:
                to_python = json.load(read_file)
                add_run_data(to_python)
        except JSONDecodeError as e:
            print('Did not add to db:', file, e)