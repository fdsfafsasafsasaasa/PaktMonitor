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
        user = pymongo.find_one({"uuid": uuid})
        if not user:
            return False
        return user

    @staticmethod
    def login_user(username, password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        user = pymongo.find_one({"username": username})
        if user['password'] == hashed_password:
            return True
        else:
            return False

    @staticmethod
    def create_user(username, password):
        if not pymongo.find_one({"username": username}):
            pymongo.insert_one(
                {
                    "username": username,
                    "password": hashlib.sha256(password.encode()).hexdigest()
                }
            )