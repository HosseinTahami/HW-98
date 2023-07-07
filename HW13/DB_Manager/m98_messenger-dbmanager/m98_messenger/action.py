from menu.models import generate_menu_from_dict
from menu.utils import get_input
from core.models import User, Message
from data_manager import DBManager
from core.models import User
import datetime
from main import user_inf

db_config = {'dbname':'Farzad3','host':'127.0.0.1','port':'5432',
            'password':'8890333','user':'Farzad3'}
def create_message():
    message_txt = input('Enter message: ')
    from_user = user_inf
    to_user = int(input('Enter user id you want to send to:(id) '))
    subject = input('Enter Subject: ')
    time = datetime.datetime.now()
    message = Message(message_txt,from_user._id,
                      to_user,time, subject)
    m = DBManager({'db_config':db_config})
    m.create(m)

def inbox():
    manager = DBManager({'db_config':db_config})
    result = manager.read_all(user_inf._id, Message)
    for item in result:
        if item[3] == user_inf._id:
            print(item[1])

def sent_box():
    manager = DBManager({'db_config':db_config})
    result = manager.read_all(user_inf._id, Message)
    for item in result:
        if item[2] == user_inf._id:
            print(item[1])