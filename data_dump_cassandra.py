import pandas as pd
import json
import csv
import os
from adult_income.config import session

# cloud_config= {
#          'secure_connect_bundle': 'secure-connect-adult-census-income.zip'
# }
# auth_provider = PlainTextAuthProvider('YZWGgDNGqgigHftDxrKugMRZ', 'boChdpRPzaig.mkfk+5+Pg7m2kDTpv-,AjBX.W016s6+SDDLT-xh632tlIJ_RUNZv+EiW94JPs2fnsif6TylLkqxemCtnHZrfDeFmiem77TbLq+LymIYeX.ay_wTKBJq')
# cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
# session = cluster.connect()

DATA_FILE_PATH="sample_adult.csv"
KEYSPACE_NAME="adult"
TABLE_NAME="income"




if __name__=="__main__":
    row = session.execute(f"CREATE TABLE IF NOT EXISTS {KEYSPACE_NAME}.{TABLE_NAME} (age int PRIMARY KEY,workclass text,fnlwgt int,education text,education_num int,marital_status text,occupation text,relationship text,race text,sex text,capital_gain int,capital_loss int,hours_per_week int,country text,salary text);")

    with open(DATA_FILE_PATH,'r') as data:
        next(data)
        data_csv= csv.reader(data,delimiter=',')
        #csv reader object
        print(data_csv)
        all_value= []
        for i in data_csv:
            session.execute(f"insert into {KEYSPACE_NAME}.{TABLE_NAME} (age,workclass,fnlwgt,education,education_num,marital_status,occupation,relationship,race,sex,capital_gain,capital_loss,hours_per_week,country,salary) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",[int(i[0]),i[1],int(i[2]),i[3],int(i[4]),i[5],i[6],i[7],i[8],i[9],int(i[10]),int(i[11]),int(i[12]),i[13],i[14]])
    print('Finished')

