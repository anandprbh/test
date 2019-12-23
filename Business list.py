

import pandas as pd

import re

import time

from datetime import datetime







filename = pd.read_csv("C:/Users/anand/Downloads/business_list.csv")

filename.dropna(inplace=True)

filename = filename.reset_index(drop=True)

search_datetime=time.ctime()

location="Cupertino"





def check_if_open(start_day,stop_day,start_time,end_time,extra_day,Current_time_location):

    pat = re.compile("([A-z][a-z]{2})(\s[A-z][a-z]{2}\s\d\d)\s(\d?\d):(\d?\d)")

    m = pat.match(Current_time_location)

    current_day= m.group(1)

    current_time = m.group(3)

    

    

    



def get_regex1(string_A,Current_time_location):

    pattern_A = re.compile("([A-Z][a-z]{2})-([A-Z][a-z]{2}),\s([A-Z][a-z]{2})\s(\d?\d*:*\d?\d\s[ap][m])\s-\s(\d?\d*:*\d?\d\s[ap][m])")

    m = pattern_A.match(string_A)

    start_day = m.group(1)

    stop_day = m.group(2)

    extra_day = m.group(3)

    start_time = m.group(4)

    end_time = m.group(5)

    

    if ":" in start_time:

        start_time = datetime.strptime(start_time, "%I:%M %p")

        start_time= datetime.strftime(start_time, "%H:%M")

        

    else:

        start_time = datetime.strptime(start_time, "%I %p")

        start_time= datetime.strftime(start_time, "%H%M")

    if ":" in end_time:

        end_time = datetime.strptime(end_time, "%I:%M %p")

        end_time= datetime.strftime(end_time, "%H:%M")

        

    else:

        end_time = datetime.strptime(end_time, "%I %p")

        end_time= datetime.strftime(end_time, "%H %M")

    

    

    #end_time = datetime.strptime(end_time, "%I:%M %p")

    #end_time= datetime.strftime(end_time, "%H:%M")

    

    

    print(start_day+"_"+stop_day+"_"+start_time+"_"+end_time)#+"_"+Current_time_location)

    

    #check_if_open(start_day,stop_day,start_time,end_time,extra_day,Current_time_location)

    



def get_regex2(string_B,Current_time_location):

    pattern_B = re.compile("([A-Z][a-z]{2})-([A-Z][a-z]{2})\s(\d?\d*:*\d?\d\s[ap][m])\s-\s(\d?\d*:*\d?\d\s[ap][m])")

    m = pattern_B.match(string_B)

    start_day = m.group(1)

    stop_day = m.group(2)

    start_time = m.group(3)

    end_time = m.group(4)

    

    check_if_open(start_day,stop_day,start_time,end_time,Current_time_location)

    



def get_business_data(business_list,Current_time_location):

    

    

    for index,value in enumerate(business_list["Time"]):

        

        

        if "/" in value:

            value= value.split("/")

            #print(value)

            for index_1 in value:

                if "," in index_1:

                   get_regex1(index_1,Current_time_location)

                #else:

                    #get_regex2(index_1,Current_time_location)

        #else:

            #list_Business

         #   if "," in list_Business['Time'][index]:

          #          get_regex1(list_Business["Time"][index],Current_time_location)

           #     else:

            #        get_regex2(list_Business["Time"][index],Current_time_location)

            

            

        

    #return list_Business       





def getOpenBusinessOutlets(search_datetime,filename,location):

    

    business_list = filename

    Current_time_location = location +" "+search_datetime

    #print("1_"+Current_time_location)

    get_business_data(business_list,Current_time_location)



    

    



getOpenBusinessOutlets(search_datetime,filename,location)
