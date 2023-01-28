from adult_income.logger import logging
from adult_income.exception import IncomeException
from adult_income.utils import get_collection_as_dataframe
import sys,os
from adult_income.entity import config_entity,artifact_entity
from adult_income.components.data_ingestion import DataIngestion
from adult_income.components.data_validation import DataValidation
from adult_income.components.data_transformation import DataTransformation
from adult_income.components.model_trainer import ModelTrainer




if __name__=="__main__":
     try:
          training_pipeline_config = config_entity.TrainingPipelineConfig()
          data_ingestion_config  = config_entity.DataIngestionConfig(training_pipeline_config=training_pipeline_config)
          print(data_ingestion_config.to_dict())
          data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
          data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
          print("Data Ingestion Completed")
          

          print("Data Validation Started")
          data_validation_config = config_entity.DataValidationConfig(training_pipeline_config=training_pipeline_config)
          data_validation = DataValidation(data_validation_config=data_validation_config,
                         data_ingestion_artifact=data_ingestion_artifact)

          data_validation_artifact = data_validation.initiate_data_validation()
          print("Data Validation Completed")

          print("Data Transformation Started")
          data_transformation_config=config_entity.DataTransformationConfig(training_pipeline_config=training_pipeline_config)
          data_transformation=DataTransformation(data_transformation_config=data_transformation_config, data_ingestion_artifact=data_ingestion_artifact)
          data_transformation_artifact=data_transformation.initiate_data_transformation()
          print("Data Transformation has been completed")

          print("Model Trainer Started")
          model_trainer_config=config_entity.ModelTrainerConfig(training_pipeline_config=training_pipeline_config)
          model_trainer=ModelTrainer(model_trainer_config=model_trainer_config, data_transformation_artifact=data_transformation_artifact)
          model_trainer_artifact=model_trainer.initiate_model_trainer()
          print("Model Trainer Completed")

     except Exception as e:
          IncomeException(e, sys)