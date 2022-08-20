from buffmeapi.firestore import db


def insert_user(user):
    users_collection = db.collection('users')
    if users_collection.document(user['platform_user_id']).get():
        # TODO: Update user
        print('User already exists')
    else:
        users_collection.set(user)
