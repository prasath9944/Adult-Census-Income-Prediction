import pandas as pd
from adult_income.logger import logging
from adult_income.exception import IncomeException
from adult_income.config import mongo_client
import os,sys
import yaml
import numpy as np
import dill


def get_collection_as_dataframe(database_name:str,collection_name:str)->pd.DataFrame:
    """
    Description: This function return collection as dataframe
    =========================================================
    Params:
    database_name: database name
    collection_name: collection name
    =========================================================
    return Pandas dataframe of a collection
    """
    try:
        logging.info(f"Reading data from database: {database_name} and collection: {collection_name}")
        df = pd.DataFrame(list(mongo_client[database_name][collection_name].find()))
        logging.info(f"Found columns: {df.columns}")
        if "_id" in df.columns:
            logging.info(f"Dropping column: _id ")
            df = df.drop("_id",axis=1)
        logging.info(f"Row and columns in df: {df.shape}")
        return df
    except Exception as e:
        raise IncomeException(e, sys)



def write_yaml_file(file_path,data:dict):
    try:
        file_dir = os.path.dirname(file_path)
        os.makedirs(file_dir,exist_ok=True)
        with open(file_path,"w") as file_writer:
            yaml.dump(data,file_writer)
    except Exception as e:
        raise IncomeException(e, sys)

def convert_columns_float(df:pd.DataFrame,exclude_columns:list)->pd.DataFrame:
    try:
        logging.info(f"Convarting the Features to float type")
        for column in df.columns:
            if column not in exclude_columns:
                df[column]=df[column].astype('float')
        return df
    except Exception as e:
        raise IncomeException(e, sys)

def encode_categorical_tonumerical(df:pd.DataFrame,exclude_columns:list)->pd.DataFrame:
    try:
        if exclude_columns!=[]:
            df=df.drop(exclude_columns,axis=1)
        data=pd.get_dummies(df,drop_first=True)
        return data
    except Exception as e:
        raise IncomeException(e, sys)

def fetching_numerical_features(df:pd.DataFrame)->pd.DataFrame:
    try:
        numerical_columns=[i for i in df.columns if df[i].dtype!='O']
        return df[numerical_columns]
    except Exception as e:
        raise IncomeException(e, sys)