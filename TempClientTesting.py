
from Elec_Database import Client as Cle
from Elec_Database import Clients_List as Cle_L
#from Elec_Database import Stats_List as Ca
import datetime
import pickle
import pandas as pd

ListEU=[]
Today=datetime.date(2022,3,1)

def New_day(A):
    bl=Cl.New_day(A)
    print(A)
    ListEU.append(bl)
    print(pd.DataFrame(bl))
    print()
    A+=datetime.timedelta(1)
    return A

c=Cle.Client(Today)

"""
c.UpdateInput("HDD-PTVHP2J","Le Thien An","101 Bo Y Te Group, Tho Lao, Hai Ba Trung, Ha Noi","dinhhuong_truong@hotmail.com",5)
c.New_day(Today)
print(c)
c.Print_Info_File()
"""
Cl=Cle_L.Clients_List(Today)
Cl.CreateNewClient("HDD-PTVHP2J","Le Thien An","101 Bo Y Te Group, Tho Lao, Hai Ba Trung, Ha Noi","dinhhuong_truong@hotmail.com",5)
Cl.CreateNewClient("HDD-YF4OO6F","Thi Minh Toan","T5 Hoang Hoa Tham, Ward 13, Hai Ba Trung, Ha Noi","quangminh.dang@gmail.com",5)
Cl.CreateNewClient("HDD-FGY86KQ","Pham Thanh Hau","11 Mau Than Street, Rach Gia Township, Hai Ba Trung, Ha Noi","haiphong.nguyen5@yahoo.com",5)
Cl.CreateNewClient("HDD-OMEXR1C","Tieu Quang Thong","182/2/6 Nguyen Huu Canh St., Hai Ba Trung, Ha Noi","minhquang_phung39@gmail.com",4)
Today=New_day(Today)
Today=New_day(Today)
Today=New_day(Today)

Cl.CreateNewClient("HDD-2MS1Z7Y","Bui Thanh Long","315C Nam Ky Khoi Nghia St., Ward 7, Dist. 3, Ha Noi","duycan.trinh@hotmail.com",5)
Cl.CreateNewClient("HDD-ET2T10D","Thach Gia Phong","1C Trang Tien, Trang Tien Ward, Hai Ba Trung, Ha Noi","lamkhe_le@yahoo.com",5)
Cl.CreateNewClient("HDD-Y60ZK3P","Duu Thanh Cong","22 Truong Dinh, Dist.1, Ha Noi","thuydu1@hotmail.com",5)
"""
print(Cl.ListOfDict())
"""
for i in range(28):
    Today=New_day(Today)
"""
Cl.List[5]['Client_Object'].Print_Info_File()

file_cm = open('Temp_Obj/CLTesting.obj', 'rb')
b = pickle.load(file_cm)  
print(b.ListOfDict())
"""
print(Today)

file_cl = open('Temp_Obj/CLTesting.obj', 'wb')
pickle.dump(Cl,file_cl)
file_cl.close()

file_cl = open('Temp_Obj/Stat_E_U.obj', 'wb')
pickle.dump(ListEU,file_cl)
file_cl.close()