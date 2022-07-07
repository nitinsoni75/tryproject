from django.test import TestCase

# Create your tests here.

def verifyInput(username,password):

    error = []


    if len(username) < 6:

        error.append('username should be at least be 6 character long')


    elif len(password) < 8 :

        error.append('password should be at least be 8 character long') 
    else:

        print("ok")
    
    return error





