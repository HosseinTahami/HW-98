from users import *
from contacts import *
import pickle
from validators import password_validation



def signup(username, password):
    if not User.repeat_username(username):
        print("This username is already taken !")
    if not password_validation(password):
        print("This passwoed is not safe enough !")

    new_user = User.creat_user(username, password)

    new_user_dict = {

        "username" : new_user.username,
        "password" : new_user.password,
        "user_id" : new_user.user_id
    }

    users_dict.update({new_user.username : new_user_dict})
    #print(users_dict)
    with open("users.pickle", "wb") as pf :
        pickle.dump(users_dict, pf)

    print("Username Created Succesfully !")


def login(username : str, password : str) :
        
        if User.authenticate_user(username, password):
            
            return True
        else:
            return False
        

