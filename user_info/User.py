import hashlib
import os
import getpass
import sys

## NOTE: NOT done:
# - Delete user function

## Get username
def input_username():
    pass

## Get password from user input - use in later function
def input_passwd(prompt='Password: '):
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
    #inputusername
    with open("user_database.txt", "rb") as handle:
        pickle.loads(handle)
        if check_if_exist_username('user_database.txt', username):
            #print("User already exists!")
            pass
        else:
            break

## Check user name exist
def check_if_exist_username(file, string):
    read_username = []
    with open(file, 'rb') as read:
        user_db = pickle.loads(read)
        for i in user_db:
            read_username.append(next(iter(user_db[i])))
        if string in read_username:
            return True
        return False

## Check password exist - NOT done
def check_passwd(username):
    with open("user_database.txt", "rb") as handle:
        user_db = pickle.loads(handle)
        for i in user_db:
            val = user_db[i].values()
            user, passwd = next(val), next(val)
            if username = user:
                password = passwd
                break
        return password
        
## Add user (Sign up)
# IMPORTANT: must have the password input from input_passwd() function
# username = input("Username: ")
# password = input_passwd()
def register(username, password):
    check_if_exist(username)
    h = hashlib.pbkdf2_hmac('sha256', password.encode("utf-8"), b'*@#d2', 182)
    newpass = h.hex() 
    # Add item to list
    users = { 
        "user_name": newuser,
        "passwd": newpass
    }
    user_list = []
    user_list.add(users)
    # open(file, mode=""), for a is writing to the db
    with open("user_database.txt", "a") as handle:
        pickle.dumps(user_list, handle, protocol=pickle.HIGHEST_PROTOCOL)
    # remember to have a successfully message!

## Read user from db
def read_user():
    ## IMPORTANT - Check if user_db is empty or not
    read_username = []
    if os.path.getsize("user_database.txt") == 0:
        #print("Database is empty!\n")
        pass
    else:
        with open("user_database.txt", "rb") as handle:
            user_db = pickle.loads(handle)
            for i in user_db:
                read_username.append(next(iter(user_db[i])))
        return username

## Log in
# IMPORTANT: must have the password input from input_passwd() function
# username = input("Username: ")
# password = input_passwd()
def log_in(username, password):
    if os.path.getsize("user_database.txt") == 0:
        #print("Database is empty!\n")
        pass
    else:
        while True:
            userinput = username
            with open("user_database.txt", "rb") as handle:
                if check_if_exist_username("user_database.txt", userinput):
                    #print("Welcome " + userinput + "!\n")
                    break
                else:
                    #print("Invalid username.")
                    break
        while True:
            h = hashlib.pbkdf2_hmac('sha256', password.encode("utf-8"), b'*@#d2', 182)
            passinput = h.hex()
            passcheck = check_passwd(userinput)
            if passinput == passcheck:
                #Succesfully log in
                break
            else:
                #print("Invalid Password.")
                pass
            
def delete_user(username):
    pass

## Wipe all db
# For this part, it is better to integrated it with the gui
# idk why I want to delete all data, lol!
def wipe_db():
    if os.path.getsize("user_database.txt") == 0:
        #print("Database is already empty!\n")
        pass
    else:
        while True:
            a = input("Are you sure you want to wipe the user database [y/n]? ")
            if a == "y":
                datab = open("user_database.txt", "w")
                datab.write("")
                datab.close()
                clear()
                print("Database wiped!\n")
                break
            elif a == "n":
                clear()
                print("Database will not be wiped!\n")
                break
            else:
                print("Invalid selection.")