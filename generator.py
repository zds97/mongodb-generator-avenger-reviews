import datetime, httplib, sys
import pymongo
import os
import uuid, json, random
from loremipsum import get_paragraph
from random import randint

settings = {
    'host': str(os.environ.get('HOSTCONNECT')),
    'database': str(os.environ.get('DATABASE')),
    'username': str(os.environ.get('USERNAME')),
    'password': str(os.environ.get('PASSWORD'))
}

avenger = ""
avengers = ["Nexus 6", "Nexus 5x", "Nexux 6p", "iPhone 5", "iPhone 6", 
        "iPhone 7", "Pixel", "Windows Phone", "Galaxy s5", "Galaxy s6",
        "Galaxy s7", "HTC 10", "LG G5"]

try:
    print "Connecting to {}/{}".format(settings['host'], settings['database'])
    conn = pymongo.MongoClient("mongodb://{username}:{password}@{host}/{database}".format(**settings))
except Exception as ex:
    print "Error:", ex
    exit('Failed to connect, terminating.')

try:
    db = conn[settings['database']]
except Exception as ex:
    exit('Error {}'.format(ex))

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
