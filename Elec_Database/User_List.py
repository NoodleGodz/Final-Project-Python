import Elec_Database.User_module as User_module
import pickle

class User:
    """
    This class contains a list of Administrator user
    
    Main function get display on the GUI:
        + log_in(username,password)
        + register(username,password)
        + read_userdb()
        + delete_user(username)
    
    GUI guide:
        + Log in and sign up button in the log in panel.
        + A button to display all username in the main panel.
        + A button to delete specific username in the main panel after display all username from above.
        
    Note:
        + Registration password must be used with the specific function from User_module.
    """
    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password
        
    def register(self, username, password):
        User_module.register(self.username, self.password)
        return
    
    def log_in(self, username, password):
        User_module.log_in(self.username, self.password)

    def read_userdb(self):
        """
        This function to list all user.
        
        Return:
            list of username
        """
        if User_module.check_empty_user_db():
            #Empty database
            break
        else:
            read_db = []
            with open("Object_Folder/user_database.obj", "rb") as handle:
                user_db = pickle.loads(handle)
                for i in range(len(user_db)):
                    read_db.append(next(iter(user_db[i])))
            return read_db
    
    def delete_user(self, username):
        """
        This function to delete one user.
        Data is deleted from user database object
        
        Return:
            void
        """
        if User_module.check_empty_user_db():
            #Empty database
            break
        else:
            with open("Object_Folder/user_database.obj", "w+b") as handle:
                user_db = pickle.loads(handle)
                if check_if_exist(username):
                    for i in range(len(user_db)):
                        if user_db[i]['user_name'] = username:
                            del user_db[i]
                    pickle.dumps(user_db, handle, protocol=pickle.HIGHEST_PROTOCOL)