from asyncio.windows_events import NULL
from django.test import TestCase

# Create your tests here.
from random import *
def generate_password():
    lst = []
    a = 'abcdefghijklmnopqrstuvwxyz1234567890@#$'
    for i in a:
        lst.append(i)
    passwordlist = []
    for i in range(8):
        passwordlist.append(choice(lst))
    password = ''
    for i in passwordlist:
        password+= i
    return(password)
print(type(generate_password()))