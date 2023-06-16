import uuid
from users import *
from contacts import *
import pickle
import os

users_dict = {}

if os.path.getsize("users.pickle") > 0:
    with open("users.pickle", "rb") as pf :
        users_dict = pickle.load(pf)
class User :
    
    
    def __init__(self,
                 username:str,
                 password:str,
                 ):
        
        self.username = username
        self.password = password
        self.user_id = uuid.uuid1()
        
        
    @classmethod
    def creat_user(cls, username, password):
        new_user = cls(username, password)
        return new_user
    
    
    @staticmethod
    def repeat_username(username):
        if users_dict.get(username) is None :
            return True
        return False
        
        
    @staticmethod
    def authenticate_user(username,password):
        print("username:", username,"password", password)
        users_dict = User.loading()
        if not(User.repeat_username(username)) and (users_dict[username]["password"] == password) :
            return True
        return False
    
    
    @staticmethod
    def delet_user(del_user):
        users_dict = User.loading()
        users_dict.pop(del_user)
        users_dict = User.dumping(users_dict)
    
    
    def modify_user(option, old_username : str, new_username : str, old_password : str, new_password : str, user_id):
        users_dict = User.loading()
        if User.repeat_username is not None :
            if option == 1:
                new_user = User.creat_user(new_username,old_password)  
                new_user_dict = {
                    
                    "username" : new_user.username,
                    "password" : new_user.password,
                    "user_id" : user_id
                }
                
                users_dict.update({new_username : new_user_dict})
                User.dumping(users_dict)
                User.delet_user(old_username)
                
            if option == 2:
                users_dict[old_username]["password"] = new_password
                User.dumping(users_dict)

            if option == 3:
                User.delet_user(old_username)
            
    
    @staticmethod
    def loading():
        if os.path.getsize("users.pickle") > 0:
            with open("users.pickle", "rb") as pf :
                users_dict = pickle.load(pf)
                return users_dict
        users_dict = {}
        return users_dict

        
    @staticmethod
    def dumping(users_dict):
        with open("users.pickle", "wb") as pf :
            pickle.dump(users_dict,pf)

    
    