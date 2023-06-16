import re

global email_pattern, password_pattern
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
password_pattern = "^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$"


def email_validation(email):
    return re.fullmatch(email_pattern, email) 

def password_validation(password):
    return re.fullmatch(password_pattern, password)

def phone_validation(phone):
    pass
