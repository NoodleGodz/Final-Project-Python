import hashlib
import os
import getpass
import sys
import getch

def input_username():
    pass

def input_passwd(prompt='Password: '):
    """
    This function to get a password from the user and display a masked value at the prompt. It made to be used with the later function like encrypting the user input password.
    
    Parameter:
        (user input password)
        
    Return:
        masked password at the prompt (e.g.: 123456 -> ******)
    """
    if sys.stdin is not sys.__stdin__:
        pwd = getpass.getpass(prompt)
        return pwd
    else:
        pwd = ""
        sys.stdout.write(prompt)
        sys.stdout.flush()
        while True:
            key = ord(getch())
            if key == 13:
                sys.stdout.write('\n')
                return pwd
                break
            if key == 8:
                if len(pwd) > 0:
                    sys.stdout.write('\b' + ' ' + '\b')
                    sys.stdout.flush()
                    pwd = pwd[:-1]
            else:
                char = chr(key)
                sys.stdout.write('*')
                sys.stdout.flush()
                pwd = pwd + char
        return pwd

## Check user name exist
def check_if_exist(username):
    """
    This function to check if the username exist in the object database or not.
    
    Parameter: 
        username
    
    Return:
        True: username exist
        False: username not exist
    """
    read_data = []
    with open("Object_Folder/user_database.obj", "rb") as handle:
        user_db = pickle.loads(handle)
        pickle.loads(handle)
        for i in range(len(user_db)):
            read_data.append(next(iter(user_db[i])))
        if username in read_data:
            return True
        else:
            return False

## Check password exist
def check_passwd_from_db(username):
    """
    This function to get the password from the database, for using it for double check later.
    
    Parameter:
        username
        
    Return:
        user password with the following username
    """
    with open("user_database.txt", "rb") as handle:
        user_db = pickle.loads(handle)
        for i in range(len(user_db)):
            val = user_db[i].values()
            user, passwd = next(val), next(val)
            if username = user:
                password = passwd
                break
        return password
        
## Register (Sign up)
def register(username, password):
    """
    This function to sign up then save to pickle files.
    
    Parameter:
        username
        password
        
    Return:
        Save username and password to object file
    """
    while True:
        if not check_if_exist(username):
            # Continue with the input
            break
        else:
            # username exist!
            return False
            
    h = hashlib.pbkdf2_hmac('sha256', password.encode("utf-8"), b'*@#d2', 182)
    newpass = h.hex() 
    
    # Add item to list of dictionary
    users = { 
        "user_name": newuser,
        "passwd": newpass
    }
    user_list = []
    user_list.append(users)
    
    # Write file to database
    with open("Object_Folder/user_database.obj", "w+b") as handle:
        user_db = pickle.loads(handle)
        user_db.extend(user_list)
        pickle.dumps(user_db, handle, protocol=pickle.HIGHEST_PROTOCOL)

def check_empty_user_db():
    """
    This function to check if the user database is empty or not
    
    Return:
        True if empty
        False if not empty
    """
    if os.path.getsize("user_database.txt") == 0:
        return True
    return False
    
## Log in
def log_in(username, password):
    """
    This function to check the log in from user.
    
    Paramter:
        username
        password
    
    Return:
        True: successfullry login
        False: invalid login
    """
    if check_empty_user_db():
        break
    else:
        while True:
            userinput = username
            with open("user_database.txt", "rb") as handle:
                if check_exist("user_database.txt", userinput):
                    break
                else:
                    continue
        while True:
            h = hashlib.pbkdf2_hmac('sha256', password.encode("utf-8"), b'*@#d2', 182)
            passinput = h.hex()
            passcheck = check_passwd_from_db(userinput)
            if passinput == passcheck:
                return True
            else:
                return False