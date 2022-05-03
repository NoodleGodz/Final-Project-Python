import hashlib
import os
import getpass
import sys
import pickle
from itertools import islice

def load_pickle(filename):
    """
    This function to file from file   
    Parameter:
        filename
    Return:
        list of item from saving files
    """
    objects = []
    with open(filename, "rb") as handle:
        while True:
            try:
                objects.extend(pickle.load(handle))
            except EOFError:
                break
    return objects
                
def write_pickle(filename, object):
    """
    This function to pickle to file
    Parameter:
        filename
    Return:
        void
    """
    with open(filename, "wb") as handle:
        pickle.dump(object, handle)      
                
## Check password exist
def check_passwd_from_db(username):
    """
    This function to get the password from the database, for using it for double check later.
    Parameter:
        username
    Return:
        user password with the following username
    """
    user_db = load_pickle("Object_Folder/user_database.obj")
    for i in range(len(user_db)):
        user, passwd = islice(user_db[i].values(), 2)
        if username == user:
            password = passwd
    return password

def load_user_db():
    """
    This function to get the username from the list of database
    Return:
        List of username
    """
    read_data = []
    user_db = load_pickle("Object_Folder/user_database.obj")
    for i in range(len(user_db)):
        read_data.append(next(iter(user_db[i].items()))[1])
    return read_data

def check_if_exist(username):
    """
    This function to check if the username exist in the object database or not.
    Parameter: 
        username
    Return:
        True: username exist
        False: username not exist
    """
    user_lists = load_user_db()
    if username in user_lists:
        return True
    else:
        return False

def check_empty_user_db():
    """
    This function to check if the user database is empty or not
    Return:
        True if empty
        False if not empty
    """
    if os.path.getsize("Object_Folder/user_database.obj") == 0:
        return True
    else:
        return False
    
def password_encryption(password):
    """
    This function to encrypt the password to SHA256 - nondecrypt password
    Parameter:
        password
    Return:
        Encrypted pass
    """
    h = hashlib.pbkdf2_hmac('sha256', password.encode("utf-8"), b'*@#d2', 182)
    return h.hex()
    