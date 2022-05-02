
from Elec_Database import Clients_List
from Elec_Database import Stat_List
import datetime
import pickle


class Main_Menu():
    """
    Main class for the database, Contain:
        + Today: Current Date
        + Clients_List: An Instance of a class contains all Client Infomations and generate Energy_Usage
                        -> GUI into Customer_Mange_Panel
        + Stat_List:    An Instance of a class contains all Energy_Usages in a time period, export to excel and calculate price
                        -> GUI into Stat_Panel       
                                 
    Main function:
        + New_day: Simmulate a day pass-> New Energy_Usage add to the Stat list

    GUI:
        + savedata() when closing
    """

    def __init__(self) -> None:
        self.Load_TempData()
        #self.Load_Data()

    def Load_TempData(self):
        """
        This function is for loading old demo data
        Therefore Changes will not be save when close

        When finish testing, use Load_Data() instead
        """
        file_cl = open('Temp_Obj/CLTesting.obj', 'rb')
        self.Client_L = pickle.load(file_cl)   
        file_cl.close() 
        self.Today= self.Client_L.Today+datetime.timedelta(1)
        self.Stat_L=Stat_List.Stat_List(self.Today)
        self.Stat_L.LoadTemp()

    def Load_Data(self):
        file_cl = open('Object_Folder/Client_L.obj', 'rb')
        self.Client_L = pickle.load(file_cl)    
        file_cl.close()
        self.Today= self.Client_L.Today+datetime.timedelta(1)
        file_sl = open('Object_Folder/Stat_L.obj', 'rb')
        self.Stat_L = pickle.load(file_sl)    
        file_sl.close()
        

    def Save_Data(self):
        """
        This function save all current change in gui into .obj file
        Keep persistent info after closing app

        (Remember to change the __init__ to Load_Data() to persistent info)

        """
        file_cl = open('Object_Folder/Client_L.obj', 'wb')
        pickle.dump(self.Client_L,file_cl)
        file_cl.close()
        file_sl = open('Object_Folder/Stat_L.obj', 'wb')
        pickle.dump(self.Stat_L,file_sl)
        file_sl.close()

    def New_day(self):
        """
        

        """
        block=self.Client_L.New_day(self.Today)
        self.Stat_L.New_day(self.Today,block)
        self.Today+=datetime.timedelta(1)


