from adult_income.exception import IncomeException
from adult_income.utils import get_collection_as_dataframe


if __name__=="__main__":
     try:
          adult_ls=get_collection_as_dataframe(keyspaceName='adult',tableName='censusincome')
          print(f"The Shape of the Dataaframe is {adult_ls.shape}")
          print(adult_ls.head(1))
     except Exception as e:
          print(e)


