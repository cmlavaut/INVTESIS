from flask_login import UserMixin
from .database import get_user

class UserData:
    def __init__(self,username,password,name,email, id_plantacion):
        self.username = username
        self.password = password
        self.name = name
        self.email = email
        self.id_plantacion = id_plantacion

class UserModel(UserMixin):
    def __init__(self, user_data):
        self.id = user_data.username
        self.password = user_data.password
        self.name = user_data.name
        self.email = user_data.email
        self.id_plantacion = user_data.id_plantacion



    @staticmethod
    def query(user_id):
        user_doc = get_user(user_id)
        user_data = UserData(
            username=user_doc['username'],
            password=user_doc['password'],
            name=user_doc['name'],
            email=user_doc['email'],
            id_plantacion = user_doc['id_plantacion']
        )

        return UserModel(user_data)