from adult_income.pipeline.training_pipeline import start_training_pipeline
from adult_income.pipeline.batch_prediction import start_batch_prediction
from adult_income.exception import IncomeException
import os,sys

file_path="/config/workspace/sample_adult.csv"
if __name__=="__main__":
     try:
          start_training_pipeline()
          # output_file = start_batch_prediction(input_file_path=file_path)
          # print(output_file)
     except Exception as e:
          IncomeException(e, sys)