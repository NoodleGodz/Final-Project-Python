from Elec_Database import Client
import datetime

class Clients_List:
    def __init__(self,Today) -> None:
        self.List=[]
        self.Today=Today

    def Cell(self,id,obj):
        return {'id':id,'Client_Object':obj}    

    def CountClients(self):
        return len(self.List)

    def CheckIDexist(self,id):
        return any(d['id'] == id for d in self.List)
               

    def CreateNewClient(self,Contact_ID,Owner_Name,Address,Info,E_Mode):
        a=Client.Client(self.Today)
        a.UpdateInput(Contact_ID,Owner_Name,Address,Info,E_Mode)       
        Check=self.CheckIDexist(Contact_ID)
        if Check:
            print("Error ! ID duplicate")
        else:
            print("OK")
            self.List.append(self.Cell(Contact_ID,a))
        return not Check

    def FindClientsListbyInput(self,text):
        return [d for d in self.List if text in d['id']]

    def GetUsageDay(self):
        return [d['Client_Object'].Energy_Usage for d in self.List]

    def New_day(self,Today):
        for d in self.List:
            d['Client_Object'].New_day(Today)
        self.Today=Today
        return self.GetUsageDay()    

    def ListOfDict(self):
        return [d['Client_Object'].ToDict() for d in self.List]
