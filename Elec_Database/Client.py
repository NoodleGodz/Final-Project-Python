import pickle
import random
import datetime
class Client:
    """
    THis function contain all infomation of 1 clients with unique Id
        Display variable (can be change at GUI):
            Contract_ID
            Owner_Name
            Address
            Info
            Open(State)
            Energy_Mode : Radio_Button from 0-5

        Main function:
            UpdateInput(): Update the User-editable variable when click edit button

            Get_Plot(): Return this clients 
                + a list of Engery_Usage in that time inverval and an equal len list of Date in that time inverval

            Print_Info_File() : Export this clients infomation into 'id'.txt file in Clients_Info

            Set_Open: Open/Closing the Contract (Dong dien :v)

        GUI guide:
        +All display infomation in the main panel 
        +All main function in the setting panel   

    """
    def __init__(self,Today:datetime.date) -> None:
        self.Base_Energy_Usage=30
        self.Random_Usage_Factor=0
        self.Start_date=Today
        self.Today=Today
        self.Energy_Usage=0
        self.Energy_mode=0
        self.Open=True
    def Set_id(self,id):
        self.Contract_ID=id
    def Set_name(self,name):
        self.Owner_Name=name
    def Set_address(self,address):
        self.Address=address    
    def Set_info(self,info):
        self.Info=info 
    def Set_Energy_Mode(self,EM):
        self.Energy_mode=int(EM)
    def Set_Open(self,b:bool):
        """
        This function is for the state of the Contract
            true=This clients still use Electricity 
            false=This clients stop use
        """
        self.Open=b    
    def Get_Plot(self):
        """
        This function return the All E_Usage of this client into 2 array of value and date

        For ploting graph

        return:
            + a list of Energy Usage of this client in Stat_List
            + a list of Date with same length
        
        """
        file_cl = open('Object_Folder/Client_L.obj', 'rb')
        Stat_L = pickle.load(file_cl)   
        file_cl.close()  
        usage_of_client,date  = Stat_L.Ploting_Usage_Of_Specific_Client(self.Contract_ID)
        return usage_of_client,date
    
    def UpdateInput(self,id,name,address,info,EM):
        """
        This function set all User-editable Variable
        Work as Saving after user finish edit

        """
        self.Set_id(id)    
        self.Set_name(name)  
        self.Set_address(address)
        self.Set_info(info)
        self.Set_Energy_Mode(EM)   
    def New_day(self,Today:datetime.date):
        """
        This function simulate a day pass
        
        Return:
            Energy_Usage of this client in Yesterday
        """
        self.Today=Today
        self.Energy_Usage=round(self.Base_Energy_Usage*(self.Energy_mode/5)*self.Random_Usage_Factor*int(self.Open))
        self.Random_Usage_Factor=random.uniform(0.10,2.5)                  
    def __str__(self) -> str:
        buffer='-------------Client-------------------\n'
        buffer=buffer +"ID : "+ self.Contract_ID +'\n'
        buffer=buffer +"Name : "+ self.Owner_Name +'\n'
        buffer=buffer +"Address : "+ self.Address +'\n'
        buffer=buffer +"Info : "+ self.Info +'\n'
        buffer=buffer +'-------------Contract-------------------\n'
        Minh=""
        if self.Open : Minh="Open" 
        else: Minh="Close"
        buffer=buffer +"State : "+ Minh +'\n'
        buffer=buffer +"Energy Mode : "+ str(self.Energy_mode) +'\n'
        buffer=buffer +"Start Date (mm/dd/yy): "+ self.Start_date.strftime("%x") +'\n'
        buffer=buffer +"Length : "+ str((self.Today - self.Start_date).days) + " days" +'\n'
        return buffer

    def Print_Info_File(self):
        """
        This function export Client info into .txt file in Clients_Info folder
        """
        filename="Clients_Info/"+str(self.Contract_ID)+".txt"
        f = open(filename,'w')
        f.write(str(self))
        f.close()
        return filename

    def Contract_Info(self):
        buffer=""
        Minh=""
        if self.Open : Minh="Open" 
        else: Minh="Close"
        buffer=buffer +"**State :** "+ Minh +'\n\n'
        buffer=buffer +"**Energy Mode :** "+ str(self.Energy_mode) +'\n\n'
        buffer=buffer +"**Start Date (mm/dd/yy):** "+ self.Start_date.strftime("%x") +'\n\n'
        buffer=buffer +"**Length :** "+ str((self.Today - self.Start_date).days) + " days" +'\n\n'
        return buffer

    def ToDict(self):
        """
        Client represention as Dictionary
        """
        return {"Contract_ID":self.Contract_ID,"Owner_Name":self.Owner_Name,"Address":self.Address,"Info":self.Info,"Energy_Mode":self.Energy_mode,"Open":self.Open,"Start_Date":self.Start_date,}    
