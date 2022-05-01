import random
import datetime
class Client:
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
        self.Energy_mode=EM
    def Set_Open(self,b:bool):
        self.Open=b    
    def UpdateInput(self,id,name,address,info,EM):
        self.Set_id(id)    
        self.Set_name(name)  
        self.Set_address(address)
        self.Set_info(info)
        self.Set_Energy_Mode(EM)   
    def New_day(self,Today:datetime.date):
        self.Today=Today
        self.Energy_Usage=round(self.Base_Energy_Usage*(self.Energy_mode/5)*self.Random_Usage_Factor)
        self.Random_Usage_Factor=random.uniform(0.10,2.5)                  
    def __str__(self) -> str:
        buffer='-------------Client-------------------\n'
        buffer=buffer +"ID : "+ self.Contract_ID +'\n'
        buffer=buffer +"Name : "+ self.Owner_Name +'\n'
        buffer=buffer +"Address : "+ self.Address +'\n'
        buffer=buffer +"Info : "+ self.Info +'\n'
        buffer=buffer +'-------------Contract-------------------\n'
        buffer=buffer +"State : "+ str(self.Open) +'\n'
        buffer=buffer +"Energy Mode : "+ str(self.Energy_mode) +'\n'
        buffer=buffer +"Start Date (mm/dd/yy): "+ self.Start_date.strftime("%x") +'\n'
        buffer=buffer +"Length : "+ str((self.Today - self.Start_date).days) + " days" +'\n'
        return buffer

    def Print_Info_File(self):
        filename="Clients_Info/"+str(self.Contract_ID)+".txt"
        f = open(filename,'w')
        f.write(str(self))
        f.close()

    def ToDict(self):
        return {"Contract_ID":self.Contract_ID,"Owner_Name":self.Owner_Name,"Address":self.Address,"Info":self.Info,"Energy_Mode":self.Energy_mode,"Open":self.Open,"Start_Date":self.Start_date,}    
