import datetime
import pickle 
import pandas as pd

def load_pickle_obj_to_day_list():
    '''
    this function is to load pickle binary file contain information of each day
    into list of dictionary
        Return: 
            list of list of dictionary
    '''    
    pickl_month = open("Temp_Obj/Stat_E_U.obj","rb")
    list_of_day = pickle.load(pickl_month)
    return list_of_day   #length equal to number of days in month    

def load_pickle_obj_to_client_list():
    '''
    This function is to load pickle binary file conrtain information of client into list 
    dictionary
        returm : 
            list of dictionary
    '''
    pickl_month = open("Temp_Obj/CLTesting.obj","rb")
    objs = pickle.load(pickl_month)
    list_of_client = objs.ListOfDict()
    return list_of_client
def each_day_usage_to_dataframe(list_of_day):
    '''
    this function transform list of dictionary to dataframe(pandas) which for extracting 
    information or export to excel file,csv file
    Parameter: 
        list_of_day: list of list of dictionary
    Return:
        array of dateframe for each day    
    '''
    Data = []
    for i in range( len(list_of_day)): 
        df=pd.DataFrame(list_of_day[i])
        Data.append(df)
    return Data      
def each_day_usage_to_excel(Data): # nead to have openpyxl moduel
    '''
    this function is to export dataframe to excel file
    Requirement : 
        openpyxl module
    Parameter:
        Data: array of dataframe
    Return:
        void
            
    '''
    path = "Excel_file/Each_day_usage.xlsx"
    writer = pd.ExcelWriter(path, engine = 'openpyxl')
    for i in range(len(Data)):
        Data[i].to_excel(writer, sheet_name = 'day '+str(i+1)+' usage')
    writer.save()
    writer.close()    
    return    
          
def client_in4_to_Datframe(list_of_client):
    '''
    this function transform list of client into dataframe which later used for 
    extracting information or export to excel file,csv file
    Parameter:
        list_of_client: list of dictionary
    Returns:
        dataframe of clients            
    '''
    df = pd.DataFrame(list_of_client)
    return df
def client_in4_to_excel(Data):
    '''
    this function is for exporting client information to excel file
    Parameter:
        Data: dataframe of client
    Return:
        void    
    '''
    path = "Excel_file/Client_infor.xlsx"
    writer = pd.ExcelWriter(path, engine = 'openpyxl')
    Data.to_excel(writer, sheet_name = 'Client infor')
    writer.save()
    writer.close()    
    return       
def cal_sum_of_day(list_of_day):
    '''
    this function allow to calculate sum of usage of each day and return two list
    contain sum of a day and the day in correct index  
    Paramter:
        list_of_day: list of list of dictionary
    Return:
        list of sum of usage of each day and list of day    
    '''
    sum_of_day = []
    date = []
    for i in range(len(list_of_day)):         # for each day
        sum = 0
        for k in range(len(list_of_day[i])):  # for each user
            sum += list_of_day[i][k]['Energy Usage']
            date.append(list_of_day[i][k]['Date'])
        sum_of_day.append(sum)  
    date = sorted(list(set(date)))       
    return sum_of_day,date
def cal_sum_of_client(list_of_client):
    pass
    