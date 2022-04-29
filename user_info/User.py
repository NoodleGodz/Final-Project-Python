import hashlib
from msvcrt import getch
import os
import getpass
import sys

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

def check(file, string):
    with open(file, 'r') as read:
        for line in read:
            if string in line:
                return True
    return False

def grabpass():
    global ptc
    writef = open("user_database.obj", "r")
    cl = lf + 1
    ltr = [cl]
    for position, line in enumerate(writef):
        if position in ltr:
            ptc = line

def checklogin(file, string):
    global lf
    with open(file, 'r') as read:
        for (lf, line) in enumerate(read):
            if string in line:
                return True
    return False

def clear():
    os.system("cls")

def add_user():
    while True:
        a = input("Username: ")
        h = hashlib.pbkdf2_hmac('sha256', a.encode("utf-8"), b'(*!@#s', 823)
        newuser = h.hex()
        if check('user_database.obj', newuser):
            print("User already exists!")
        else:
            break
    b = mpass()
    h = hashlib.pbkdf2_hmac('sha256', b.encode("utf-8"), b'*@#d2', 182)
    newpass = h.hex()
    users = open("user_database.obj", "a")
    users.write("Username: " + newuser + "\nPassword: " + newpass + "\n\n")
    users.close()
    clear()
    print("The following has been saved to the user database...\n")
    print("Username: " + newuser + "\nPassword: " + newpass + "\n")
    print("Press any key to continue...")
    getch()
    clear()

def read_db():
    if os.path.getsize("user_database.obj") == 0:
        clear()
        print("Database is empty!\n")
    else:
        clear()
        print("User Database:\n")
        reader = open("user_database.obj", "r")
        print(reader.read())
        reader.close()
        print("Press any key to continue...")
        getch()
        clear()

def wipe_db():
    if os.path.getsize("user_database.obj") == 0:
        clear()
        print("Database is already empty!\n")
    else:
        while True:
            a = input("Are you sure you want to wipe the user database [y/n]? ")
            if a == "y":
                datab = open("user_database.obj", "w")
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

def log_in():
    if os.path.getsize("user_database.obj") == 0:
        clear()
        print("Database is empty!\n")
    else:
        while True:
            a = input("Username: ")
            h = hashlib.pbkdf2_hmac('sha256', a.encode("utf-8"), b'(*!@#s', 823)
            userinput = h.hex()
            if checklogin('user_database.obj', userinput):
                print("Welcome " + a + "!\n")
                break
            else:
                print("Invalid username.")
        while True:
            b = mpass()
            h = hashlib.pbkdf2_hmac('sha256', b.encode("utf-8"), b'*@#d2', 182)
            passinput = h.hex()
            grabpass()
            ptct = ptc.replace("Password: ", '')
            ptcr = ptct.rstrip("\n")
            if passinput == ptcr:
                currentuser = a
                clear()
                print("Successfully logged in as " + currentuser + "!\n")
                usrtitle = ("title Secure Login System (logged in as " + currentuser + ")")
                os.system(usrtitle)
                break
            else:
                print("Invalid Password.")
                
def delete_user():
    pass
            
def main():
    pass

if __name__ == '__main__':
    main()