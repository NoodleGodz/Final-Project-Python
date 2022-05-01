import datetime
import pickle 
import pandas as pd

def load_pickle_obj_to_day_list():    
    pickl_month = open("Temp_Obj/Stat_E_U.obj","rb")
    list_of_day = pickle.load(pickl_month)
    return list_of_day   #length equal to number of days in month

def load_pickle_obj_to_client_list():
    pickl_month = open("Temp_Obj/CLTesting.obj","rb")
    objs = pickle.load(pickl_month)
    list_of_client = objs.ListOfDict()
    return list_of_client
def each_day_usage_to_dataframe(list_of_day):
    Data = []
    for i in range( len(list_of_day)): 
        df=pd.DataFrame(list_of_day[i])
        Data.append(df)
    return Data      
def each_day_usage_to_excel(Data): # nead to have openpyxl moduel
    path = "Excel_file/Each_day_usage.xlsx"
    writer = pd.ExcelWriter(path, engine = 'openpyxl')
    for i in range(len(Data)):
        Data[i].to_excel(writer, sheet_name = 'day '+str(i+1)+' usage')
    writer.save()
    writer.close()    
    return    
          
def client_in4_to_Datframe(list_of_client):
    df = pd.DataFrame(list_of_client)
    return df
def client_in4_to_excel(Data):
    path = "Excel_file/Client_infor.xlsx"
    writer = pd.ExcelWriter(path, engine = 'openpyxl')
    Data.to_excel(writer, sheet_name = 'Client infor')
    writer.save()
    writer.close()    
    return       
def cal_sum_of_day(list_of_day):
    sum_of_day = []
    date = []
    for i in range(len(list_of_day)):         # for each day
        sum = 0
        for k in range(len(list_of_day[i])):  # for each user
            sum += list_of_day[i][k]['Energy_Usage']
            date.append(list_of_day[i][k]['Date'])
        sum_of_day.append(sum)  
    date = list(set(date))       
    return sum_of_day,date
def cal_sum_of_client(list_of_client):
    pass