import stat_module
import datetime
import pickle 
import pandas as pd


class Stat_List:
    def __init__(self,Today) -> None:
        self.List_Of_Day=[]
        self.Start_Point=Today
        self.End_Point=Today

    def Running_Time(self):
        return (self.End_Point-self.Start_Point).days    

    def New_day(self,Today,Day):
        self.End_Point=Today
        self.List_Of_Day.append(Day)

    def LoadTemp(self):
        self.List_Of_Day=stat_module.load_pickle_obj_to_day_list()
        self.Start_Point=datetime.date(2022,3,1)
        self.End_Point=datetime.date(2022,3,31)

    def Ploting_Usage_Of_All_Clients(self):
        return stat_module.cal_sum_of_day(self.List_Of_Day)    

    def Ploting_Usage_Of_Specific_Client(self,id):
        usage_of_client=[]
        date=[]
        for i in range(len(self.List_Of_Day)):
            for k in range(len(self.List_Of_Day[i])):
                if self.List_Of_Day[i][k]['Id']==id:
                    usage_of_client.append(self.List_Of_Day[i][k]['Energy Usage'])
                    date.append(self.List_Of_Day[i][k]['Date'])        
        return usage_of_client,date   

    def Export_Elec_Usage_To_Excel(self):
        stat_module.each_day_usage_to_excel(stat_module.each_day_usage_to_dataframe(self.List_Of_Day)) 

    def Price_In_This_Time_Interval(self):
        df=stat_module.each_day_usage_to_dataframe(self.List_Of_Day)
        try : 
            id_list=df[-1]['Id'].tolist()
        except:
            id_list=[]   

        price_list=[]
        for i in id_list:
            usage_of_client,date=self.Ploting_Usage_Of_Specific_Client(i)

            price_list.append({'Id':i,'Energy Usage':sum(usage_of_client),'Time interval (days)':len(date),'Price':stat_module.electric_bill(sum(usage_of_client))})
        return price_list   

    def Price_List_To_Excel(self,price_list:list):
        path="Excel_file/Price_"+self.Start_Point.strftime("From_%b_%d_%Y")+self.End_Point.strftime("_To_%b_%d_%Y")+".xlsx"
        writer = pd.ExcelWriter(path,engine = 'openpyxl',datetime_format=str)
        Data=pd.DataFrame(price_list)
        Data.to_excel(writer, sheet_name = 'Price')
        #writer.save()
        writer.close()   

    def Save_History(self):
        filename="Stat_History/"+self.Start_Point.strftime("From_%b_%d_%Y")+self.End_Point.strftime("_To_%b_%d_%Y")+".obj"
        file_sl = open(filename, 'wb')
        pickle.dump(self,file_sl)
        file_sl.close()

    def Flush(self):
        price_list=self.Price_In_This_Time_Interval()  
        self.Price_List_To_Excel(price_list)
        self.Save_History()
        self.List_Of_Day=[]
        self.Start_Point=self.End_Point

    def Save_SL(self):
        file_sl = open('Object_Folder/Stat_L.obj', 'wb')
        pickle.dump(self,file_sl)
        file_sl.close()    

    def Load_Previous_Version(self,path):
        """
        WARNING: IN THE PANEL WHEN USE FOR THIS FUNCTION, DO NOT Save_Data() WHEN CLOSING, That will overwrite the Current Database
        SHould use filechooser here 

        This function is for load the Stat_History/*.obj (View only)
        """    
        file_cl = open(path, 'rb')
        self = pickle.load(file_cl)    
        file_cl.close()


         
