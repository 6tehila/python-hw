import re

def isvalid_email(user_email ):
    email = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9-.]+$')
    if email.match(user_email):
        return True
    return False

user_email = input("enter your email")

if(isvalid_email(user_email)):
    print("The Email is valid")
else:
    print("The Email is not valid")
