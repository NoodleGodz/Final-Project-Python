import Elec_Database.stat_module as stat_module
import datetime
import pickle 
import pandas as pd


class Stat_List:
    """
    This class contain a list of Energy Usage of the whole area each day from Start_Point to End_Point
    
    Main function get display on the GUI:
        +Ploting_Usage_Of_Specific_Client(id)
        +Export_Elec_Usage_To_Excel()
        +Ploting_Usage_Of_All_Clients() #for create plot of the whole area
        +Price_List_To_Excel()
        +Flush()

    GUI guide:
        +All display infomation in the main panel 
            At the top have the time interval like: From {self.Start_Point} To {self.End_Point} 
            A plot of Usage of all Clients
        +All main function in the setting panel 
            Flush(): at the bottom of the panel (Nut xuat tien thang nay :v)
            Export_Elec_Usage_To_Excel()
            Price_List_To_Excel()
    
    """
    def __init__(self,Today) -> None:
        self.List_Of_Day=[]
        self.Start_Point=Today
        self.End_Point=Today

    def Running_Time(self):
        return (self.End_Point-self.Start_Point).days    

    def New_day(self,Today,Day):
        """
        This function simulate a day pass
        This add yesterday usage to the list
        """
        self.End_Point=Today
        self.List_Of_Day.append(Day)

    def LoadTemp(self):
        self.List_Of_Day=stat_module.load_pickle_obj_to_day_list()
        self.Start_Point=datetime.date(2022,3,1)
        self.End_Point=datetime.date(2022,3,31)

    def Ploting_Usage_Of_All_Clients(self):
        '''
        this function allow to calculate sum of usage of each day and return two list
        contain sum of a day and the day in correct index  

        Return:
            list of sum of usage of each day and list of day    
        '''       
        return stat_module.cal_sum_of_day(self.List_Of_Day)    

    def Ploting_Usage_Of_Specific_Client(self,id):
        
        '''
        this function allow to calculate sum of usage of each day and return two list
        contain sum of a day and the day in correct index of a specific Client 

        Parameter:
            Id of that Client

        Return:
            list of sum of usage of each day and list of day of that Client 
  
        '''          
        
        usage_of_client=[]
        date=[]
        for i in range(len(self.List_Of_Day)):
            for k in range(len(self.List_Of_Day[i])):
                if self.List_Of_Day[i][k]['Id']==id:
                    usage_of_client.append(self.List_Of_Day[i][k]['Energy Usage'])
                    date.append(self.List_Of_Day[i][k]['Date'])        
        return usage_of_client,date   

    def Export_Elec_Usage_To_Excel(self):
        '''
        this function is to export all clients stat to excel file
        
        Requirement : 
            openpyxl module

        '''
        stat_module.each_day_usage_to_excel(stat_module.each_day_usage_to_dataframe(self.List_Of_Day)) 
        return "Excel_file/Each_day_usage.xlsx"

    def Price_In_This_Time_Interval(self):
        """
        this function calculate total amount of power they used during [Start_point,End_point] and return usage, time and price
        in correct index

        Return :list of Dict of
            + Client Id
            + Energy Usage in this time interval
            + Time interval 
            + Price need to pay
        """
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

    def Price_List_To_Excel(self):
        """
        This function export Price_List of this interval to Excel file
        The Excel file is in Excel_file folder and have the name of the interval
        """
        price_list=self.Price_In_This_Time_Interval()  
        path="Excel_file/Price_"+self.Start_Point.strftime("From_%b_%d_%Y")+self.End_Point.strftime("_To_%b_%d_%Y")+".xlsx"
        writer = pd.ExcelWriter(path,engine = 'openpyxl',datetime_format=str)
        Data=pd.DataFrame(price_list)
        Data.to_excel(writer, sheet_name = 'Price')
        #writer.save()
        writer.close()  
        return path 

    def Save_History(self):
        """
        This function save a version of this exact Stat_Stat
        The old version is in Stat_History folder and have the name of the interval
        """
        filename="Stat_History/"+self.Start_Point.strftime("From_%b_%d_%Y")+self.End_Point.strftime("_To_%b_%d_%Y")+".obj"
        file_sl = open(filename, 'wb')
        pickle.dump(self,file_sl)
        file_sl.close()

    def Flush(self):
        """
        WARNING: Dangerous Function
        This function save the current Stat_List, export Price.xlsx and Reset the Stat_L in new Time Interval
        """
        self.Price_List_To_Excel()
        self.Save_History()
        self.List_Of_Day=[]
        self.Start_Point=self.End_Point

    def Save_SL(self):
        file_sl = open('Object_Folder/Stat_L.obj', 'wb')
        pickle.dump(self,file_sl)
        file_sl.close()    

    def Load_SL(self):
        file_sl = open('Object_Folder/Stat_L.obj', 'rb')
        Minh = pickle.load(file_sl)
        self.List_Of_Day=Minh.List_Of_Day
        self.Start_Point=Minh.Start_Point
        self.End_Point=Minh.End_Point  
        file_sl.close()    

    def Load_Previous_Version(self,path):
        """
        WARNING: IN THE PANEL WHEN USE FOR THIS FUNCTION, DO NOT Save_Data() WHEN CLOSING, That will overwrite the Current Database
        SHould use filechooser here 

        This function is for load the Stat_History/*.obj (View only)
        """    
        file_cl = open(path, 'rb')
        Minh = pickle.load(file_cl)
        self.List_Of_Day=Minh.List_Of_Day
        self.Start_Point=Minh.Start_Point
        self.End_Point=Minh.End_Point   
        file_cl.close()


         
