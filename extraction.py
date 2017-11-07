import pandas as pd
import os
from variables import *

def get_files():
    data_files = []
    f = os.listdir('/home/karthik/Documents/project/data_set')
    for files in f:
        if files.endswith(".csv") or files.endswith(".xlsx") or files.endswith(".xls"):
            data_files.append(files)
    return (data_files)

def get_column_names(a_file):
    path = '/home/karthik/Documents/project/data_set/'
    #for files in data_files:
    if a_file.endswith(".csv"):
        #print (path + a_file)
        files_df = pd.read_csv(path + a_file, header=None)
        files_df_column = files_df.head(1).values[0]
        files_df = pd.read_csv(path + a_file)
        print (files_df)
        return files_df, files_df_column
    elif a_file.endswith(".xls") or a_file.endswith(".xlsx"):
        print (2)
        #print (path + a_file)
        files_df = pd.read_excel(path + a_file, header=None)
        files_df_column = files_df.head(1).values[0]
        files_df = pd.read_excel(path + a_file)
        return files_df, files_df_column

def drop_columns_in_files(df, files):
    for afile in files:
        dataframe, res = get_column_names(afile)
        #print (dataframe)
        for i in range(0, len(res)):
            if res[i] not in hospital_column_names and res[i] is not None:
                dataframe = dataframe.drop(res[i], axis=1)
                #print (dataframe)
        #print (dataframe)
        df = df.append(dataframe, ignore_index=True)
    df.to_csv('/home/karthik/Documents/project/data_set/mycommoncsv.csv')
    #print (df)

ret = get_files()
#print (ret)
df = pd.DataFrame(columns=hospital_column_names)
#print (df)
drop_columns_in_files(df, ret)
