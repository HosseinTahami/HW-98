from data_manager import BaseModel
from dataclasses import dataclass
import datetime

@dataclass
class User(BaseModel):
    TABLE_NAME = 'users'
    COLUMNS = {
        'name':('name','VARCHAR(20)','NOT NULL'),   #      CREATE TABLE users (username VARCHAR(20) UNIQUE,
        'username':('username','VARCHAR(20)','UNIQUE'),  #          name VARCHAR(20) NOT NULL,
        'password':('password','VARCHAR(100)','NOT NULL'),  #      password varchar(100) NOT NULL)
    }

    name: str
    username: str
    password: str


@dataclass
class Message(BaseModel):
    TABLE_NAME = 'Messages'
    COLUMNS = {
        'message': ('message', 'VARCHAR(500)', 'NOT NULL'),
        'from_user':('from_user', 'BIGINT', 'NOT NULL'),
        'to_user':('to_user', 'BIGINT', 'NOT NULL'),
        'time':('time', 'TIMESTAMP', 'NOT NULL'),
        'subject':('subject', 'VARCHAR(50)', 'NULL')
    }

    message: str
    from_user: BaseModel
    to_user: BaseModel
    time: datetime
    subject: str
