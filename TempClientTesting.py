
from Elec_Database import Client as Cle
from Elec_Database import Clients_List as Cle_L
import datetime
import pickle
Today=datetime.date(2002,11,23)

def New_day(A):
    A+=datetime.timedelta(1)
    print(Cl.New_day(A))
    return A

c=Cle.Client(Today)


c.UpdateInput("HDD-PTVHP2J","Le Thien An","101 Bo Y Te Group, Tho Lao, Hai Ba Trung, Ha Noi","dinhhuong_truong@hotmail.com",5)
c.New_day(Today)
print(c)
c.Print_Info_File()

Cl=Cle_L.Clients_List(Today)
Cl.CreateNewClient("HDD-PTVHP2J","Le Thien An","101 Bo Y Te Group, Tho Lao, Hai Ba Trung, Ha Noi","dinhhuong_truong@hotmail.com",5)
Cl.CreateNewClient("HDD-YF4OO6F","Thi Minh Toan","T5 Hoang Hoa Tham, Ward 13, Hai Ba Trung, Ha Noi","quangminh.dang@gmail.com",5)
Cl.CreateNewClient("HDD-FGY86KQ","Pham Thanh Hau","11 Mau Than Street, Rach Gia Township, Hai Ba Trung, Ha Noi","haiphong.nguyen5@yahoo.com",5)
Cl.CreateNewClient("HDD-OMEXR1C","Tieu Quang Thong","182/2/6 Nguyen Huu Canh St., Hai Ba Trung, Ha Noi","minhquang_phung39@gmail.com",4)
print(Cl.ListOfDict())

file_cl = open('Temp_Obj/CLTesting.obj', 'wb')
pickle.dump(Cl,file_cl)
file_cl.close()





for i in range(5):
    Today=New_day(Today)

Cl.List[1]['Client_Object'].Print_Info_File()

file_cm = open('Temp_Obj/CLTesting.obj', 'rb')
b = pickle.load(file_cm)  
print(b.ListOfDict())

print(Today)