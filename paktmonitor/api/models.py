from paktmonitor import login_manager
import pymongo
import hashlib

class User:
    database = pymongo.MongoClient()['paktmonitor']['users']
    def __init__(self, username, session_id, password):
        self.username = username
        self.session_uuid = session_id
        self.password = password

    @staticmethod
    def get_user(uuid):
        user = User.database.find_one({"uuid": uuid})
        if not user:
            return False
        return user

    @staticmethod
    def login_user(username, password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        user = User.database.find_one({"username": username})
        if user['password'] == hashed_password:
            return user
        else:
            return None

    @staticmethod
    def create_user(username, password):
        if not User.database.find_one({"username": username}):
            User.database.insert_one(
                {
                    "username": username,
                    "password": hashlib.sha256(password.encode()).hexdigest()
                }
            )
    @staticmethod
    @login_manager.user_loader
    def user_loader(uuid):
        user = User.database.find_one({"uuid": uuid})
        if user:
            return user
        else:
            return None