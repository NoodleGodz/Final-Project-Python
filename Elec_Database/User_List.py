import Elec_Database.User_module as User_module
import pickle
import os
import getpass
import sys

if os.name == "nt":
    from msvcrt import getch
else:
    from readchar import readchar as getch

is_windows = os.name == "nt"
is_linux = os.name == "posix"

BACKSPACE_WINDOWS = 8
BACKSPACE_LINUX = 127
RETURN_KEY = 13

class User_List:
    """
    This class contains a list of Administrator user
    
    Main function get display on the GUI:
        + log_in(username,password)
        + user_register(username,password)
        + read_userdb()
        + delete_user(username)
    
    GUI guide:
        + Log in and sign up button in the log in panel.
        + A button to display all username in the main panel.
        + A button to delete specific username in the main panel after display all username from above.
        
    Note:
        + Registration password must be used with the specific input_passwd function.
    """
    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password
        
    ## Register (Sign up)
    def register(self, username, password):
        """
        This function to sign up then save to pickle files.  
        Parameter:
            username
            password  
        Return:
            Save username and password to object file
        """
        while True:
            if User_module.check_empty_user_db():
                break
            else:
                if not User_module.check_if_exist(self.username):
                    # Continue with the input
                    break
                else:
                    # username exist!
                    return False
        newuser = self.username
        newpass = User_module.password_encryption(self.password)
        # Add item to list of dictionary
        user_dict = { 
            "user_name": newuser,
            "passwd": newpass
        }
        user_db = User_module.load_pickle("Object_Folder/user_database.obj")
        user_db.append(user_dict)
        User_module.write_pickle("Object_Folder/user_database.obj", user_db)

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
                if key == RETURN_KEY:
                    sys.stdout.write("\n")
                    return pwd
                    break
                if (
                    is_windows
                    and key == BACKSPACE_WINDOWS
                    or is_linux
                    and key == BACKSPACE_LINUX
                ):
                    if len(pwd) > 0:
                        # Erases previous character.
                        sys.stdout.write("\b" + " " + "\b")
                        sys.stdout.flush()
                        pwd = pwd[:-1]
                else:
                    # Masks user input.
                    char = chr(key)
                    sys.stdout.write("*")
                    sys.stdout.flush()
                    pwd = pwd + char
        
    ## Log in
    def user_log_in(self, username, password):
        """
        This function to check the log in from user.
        Paramter:
            username
            password
        Return:
            True: successfullry login
            False: invalid login
        """
        if User_module.check_empty_user_db():
            return
        else:
            while True:
                userinput = self.username
                if User_module.check_if_exist(userinput):
                    break
                else:
                    continue
            while True:
                passinput = User_module.password_encryption(password)
                passcheck = User_module.check_passwd_from_db(userinput)
                if passinput == passcheck:
                    return True
                else:
                    return False

    def read_db(self):
        """
        This function calls the load_user_db function from User_module
        """
        User_module.load_user_db()
                
    def delete_user(self, username):
        """
        This function to delete one user.
        Data is deleted from user database object.
        Return:
            void
        """
        if User_module.check_empty_user_db():
            #Empty database
            return
        else:
            user_db = User_module.load_pickle("Object_Folder/user_database.obj")
            print(user_db)
            if User_module.check_if_exist(username):
                for i in range(len(user_db)):
                    if next(iter(user_db[i].items()))[1] == username:
                        del user_db[i]
                User_module.write_pickle("Object_Folder/user_database.obj", user_db)
            else:
                #no user to delete
                return