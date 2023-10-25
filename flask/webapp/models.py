from flask_login import UserMixin
from .bd import get_user
class UserData:
    def __init__(self,username,password,name,email):
        self.username = username
        self.password = password
        self.name = name
        self.email = email

class UserModel(UserMixin):
    def __init__(self, user_data):
        self.id = user_data.username
        self.password = user_data.password
        self.name = user_data.name
        self.email = user_data.email

    @staticmethod
    def query(user_id):
        user_doc = get_user(user_id)
        user_data = UserData(
            username=user_doc['username'],
            password=user_doc['password'],
            name=user_doc['name'],
            email=user_doc['email']
        )

        return UserModel(user_data)