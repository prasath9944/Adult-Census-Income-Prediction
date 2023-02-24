from adult_income.logger import logging
from adult_income.exception import IncomeException
import sys,os
from adult_income.entity import config_entity
from adult_income.components.data_ingestion import DataIngestion
from adult_income.components.data_validation import DataValidation
from adult_income.components.data_transformation import DataTransformation
from adult_income.components.model_trainer import ModelTrainer
from adult_income.components.model_evaluation import ModelEvaluation
from adult_income.components.model_pusher import ModelPusher


def start_training_pipeline():
    try:
        logging.info("Training Pipeline Started")
        training_pipeline_config = config_entity.TrainingPipelineConfig()

        #data ingestion
        logging.info("Data Ingestion Started")
        data_ingestion_config  = config_entity.DataIngestionConfig(training_pipeline_config=training_pipeline_config)
        print(data_ingestion_config.to_dict())
        data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
        data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
        logging.info("Data Ingestion Ended")
        
        #data validation
        logging.info("Data Validation Started")
        data_validation_config = config_entity.DataValidationConfig(training_pipeline_config=training_pipeline_config)
        data_validation = DataValidation(data_validation_config=data_validation_config,
                        data_ingestion_artifact=data_ingestion_artifact)

        data_validation_artifact = data_validation.initiate_data_validation()
        logging.info("Data Ingestion Ended")

        #data transformation
        logging.info("Data Transformation Started")
        data_transformation_config = config_entity.DataTransformationConfig(training_pipeline_config=training_pipeline_config)
        data_transformation = DataTransformation(data_transformation_config=data_transformation_config, 
        data_ingestion_artifact=data_ingestion_artifact)
        data_transformation_artifact = data_transformation.initiate_data_transformation()
        logging.info("Data Transformation Ended")
        
        #model trainer
        logging.info("Model Trainer Started")
        model_trainer_config = config_entity.ModelTrainerConfig(training_pipeline_config=training_pipeline_config)
        model_trainer = ModelTrainer(model_trainer_config=model_trainer_config, data_transformation_artifact=data_transformation_artifact)
        model_trainer_artifact = model_trainer.initiate_model_trainer()
        logging.info("Model Trainer Ended")

        #model evaluation
        logging.info("Model Evaluation Started")
        model_eval_config = config_entity.ModelEvaluationConfig(training_pipeline_config=training_pipeline_config)
        model_eval  = ModelEvaluation(model_eval_config=model_eval_config,
        data_ingestion_artifact=data_ingestion_artifact,
        data_transformation_artifact=data_transformation_artifact,
        model_trainer_artifact=model_trainer_artifact)
        model_eval_artifact = model_eval.initiate_model_evaluation()
        logging.info("Model Evaluation Ended")

        #model pusher
        logging.info("Model Pusher Started")
        model_pusher_config = config_entity.ModelPusherConfig(training_pipeline_config)
        
        model_pusher = ModelPusher(model_pusher_config=model_pusher_config, 
                data_transformation_artifact=data_transformation_artifact,
                model_trainer_artifact=model_trainer_artifact)

        model_pusher_artifact = model_pusher.initiate_model_pusher()
        logging.info("Model Pusher Ended")
        logging.info("Training Pipeline Ended")
    except Exception as e:
        raise IncomeException(e, sys)
