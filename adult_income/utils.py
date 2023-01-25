import pandas as pd
from adult_income.logger import logging
from adult_income.exception import IncomeException
from adult_income.config import session
import os,sys

def get_collection_as_dataframe(keyspaceName:str,tableName:str)->pd.DataFrame:
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
        row = session.execute(f"select * from {keyspaceName}.{tableName}")
        df=pd.DataFrame([i for i in row])
        return df
    except Exception as e:
        raise IncomeException(e, sys)