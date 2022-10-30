from pymongo import MongoClient


client = MongoClient('mongodb://localhost:27017')

db = client['flask-full-stack']
users_auth = db['users']


def insert_user(user):
    try:
        user_id = users_auth.db.insert_one(user).inserted_id
        return user_id
    except:
        return {
            'success': False,
            'message': 'Failed inserting user to database'
        }
