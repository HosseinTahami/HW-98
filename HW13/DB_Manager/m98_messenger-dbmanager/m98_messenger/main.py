from data_manager import DBManager
from core.models import User
from menu.models import generate_menu_from_dict
from menu.utils import get_input
from core.models import User, Message
import datetime
from action import create_message, inbox, sent_box

db_config = {'dbname':'Farzad3','host':'127.0.0.1','port':'5432',
            'password':'8890333','user':'Farzad3'}
manager = DBManager({'db_config':db_config})

user_inf = list()

main_menu_dict = {
    'name':'Messenger',
    'children':[
        {
            'name':'Create message',
            'action': create_message,
        },
        {
            'name':'Inbox',
            'action': inbox,
        },
        {
            'name':'Outbox',
            'action': sent_box,
        },
]}

root_menu = generate_menu_from_dict(main_menu_dict, parent=None)

def main():
    global user_inf
    username = get_input("Username: ")
    password = get_input("Password: ")
    try:
        manager = DBManager({'db_config':db_config})
        user = manager.login(username, password, User)
        
    except AssertionError:
        print("Manager user is not set")
        exit()

    if user:
        print("Welcome manager...\n")
        user_inf.append(user)
        root_menu()
    else:
        print("invalid username or password")

main()
