import hashlib
import os
import getpass
import sys

# NOT DONE:
# - grabpass function
# - Delete user function

## Check file 
def check(file, string):
    with open(file, 'r') as read:
        for line in read:
            if string in line:
                return True
    return False

def checklogin(file, string):
    global lf
    with open(file, 'r') as read:
        for (lf, line) in enumerate(read):
            if string in line:
                return True
    return False

## Get password from user input - use in later function
def mpass(prompt='Password: '):
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

## Read pass
def grabpass(password):
    global pass_to_check
    writef = open("user_database.txt", "r")
    cl = lf + 1
    ltr = [cl]
    for position, line in enumerate(writef):
        if position in ltr:
            pass_to_check = line    
    
## Add user (Sign up)
# IMPORTANT: must have the password input from mpass() function
# username = input("Username: ")
# password = mpass()
# password is encrypted with sha256, i.e. can't be decrypted
def add_user(username, password):
    while True:
        newuser = username
        if check('user_database.txt', newuser):
            print("User already exists!")
        else:
            break
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

## Get user from db
def read_db():
    ## IMPORTANT - Check if user_db is empty or not
    if os.path.getsize("user_database.txt") == 0:
        #print("Database is empty!\n")
        pass
    else:
        with open("user_database.txt", "rb") as handle:
            user_db = pickle.loads(handle)
            for i in user_db:
                for k in user_db[i]:
                    username = next(iter(user_db[i]))
        # return username

## Log in
# IMPORTANT: must have the password input from mpass() function
# username = input("Username: ")
# password = mpass()
def log_in(username, password):
    if os.path.getsize("user_database.txt") == 0:
        #print("Database is empty!\n")
        pass
    else:
        while True:
            userinput = username
            with open("user_database.txt", "rb") as handle:
                user_db = pickle.loads(handle)
                if checklogin(userinput in user_db.value()):
                    print("Welcome " + username + "!\n")
                    break
                else:
                    print("Invalid username.")
        while True:
            h = hashlib.pbkdf2_hmac('sha256', password.encode("utf-8"), b'*@#d2', 182)
            passinput = h.hex()
            grabpass()
            ptct = pass_to_check.replace("Password: ", '')
            ptcr = pass_to_check.rstrip("\n")
            if passinput == ptcr:
                currentuser = userinput
                clear()
                print("Successfully logged in as " + currentuser + "!\n")
                usrtitle = ("title Secure Login System (logged in as " + currentuser + ")")
                os.system(usrtitle)
                break
            else:
                print("Invalid Password.")

def delete_user():
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