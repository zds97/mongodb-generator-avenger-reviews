import datetime, httplib, sys
import pymongo
import uuid, json, random
from loremipsum import get_paragraph
from random import randint

settings = {
    'host': '<mongodb host name goes here>',
    'database': '<database name>',
    'username': '<user>',
    'password': '<password>'
}

avenger = ""
avengers = ["Black Widow", "Jarvis", "Iron Man", "Thor", "Hulk", 
        "Captain America", "Hulk", "Nick Fury", "Pepper Potts", "Hawkeye",
        "Luke Cage", "Falcon", "Scarlet Witch"]

try:
    conn = pymongo.MongoClient("mongodb://{username}:{password}@{host}/{database}".format(**settings))
except Exception as ex:
    print "Error:", ex
    exit('Failed to connect, terminating.')


db = conn.random_data


while True:
    if len(sys.argv) > 1:
        avenger = sys.argv[1]
    else:
        avenger = random.choice(avengers)


    doc = {
        'timestamp': datetime.datetime.utcnow(),
        'review_id': str(uuid.uuid1()),
        'user_id': str(uuid.uuid1()),
        'product_name': avenger,
        'comment': get_paragraph(),
        'cost': randint(1, 10),
        'value': randint(1, 10),
        'product_quality': randint(1, 10),
        'up_votes': randint(1, 2000),
        'down_votes': randint(1, 1000),
    }

    mongo_collection = 'product_reviews'
    
    print("{: <25}  {: >20}".format(mongo_collection, db[mongo_collection].insert(doc)))
