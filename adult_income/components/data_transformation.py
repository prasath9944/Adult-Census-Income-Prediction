from adult_income.entity import artifact_entity,config_entity
from adult_income.exception import IncomeException
from adult_income.logger import logging
from typing import Optional
import os,sys 
from sklearn.pipeline import Pipeline
import pandas as pd
from adult_income import utils
import numpy as np
from sklearn.preprocessing import LabelEncoder
from imblearn.combine import SMOTETomek
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import RobustScaler
from adult_income.config import TARGET_COLUMN



class DataTransformation:


    def __init__(self,data_transformation_config:config_entity.DataTransformationConfig,
                    data_ingestion_artifact:artifact_entity.DataIngestionArtifact):
        try:
            logging.info(f"{'>>'*20} Data Transformation {'<<'*20}")
            self.data_transformation_config=data_transformation_config
            self.data_ingestion_artifact=data_ingestion_artifact
        except Exception as e:
            raise IncomeException(e, sys)


    @classmethod
    def get_data_transformer_object(cls)->Pipeline:
        try:
            logging.info(f"Simple Imputer with median strategy")
            simple_imputer = SimpleImputer(strategy='constant', fill_value=0)
            robust_scaler =  RobustScaler()
            pipeline = Pipeline(steps=[
                    ('Imputer',simple_imputer),
                    ('RobustScaler',robust_scaler)
                ])
            logging.info(f"Pipeline consists of Imputer and robust scalar: {pipeline}")
            return pipeline
        except Exception as e:
            raise IncomeException(e, sys)


    def initiate_data_transformation(self,) -> artifact_entity.DataTransformationArtifact:
        try:
            logging.info("reading training and testing file")
            #reading training and testing file
            train_df = pd.read_csv(self.data_ingestion_artifact.train_file_path)
            test_df = pd.read_csv(self.data_ingestion_artifact.test_file_path)
            
            logging.info(f"selecting input feature for train and test dataframe")
            #selecting input feature for train and test dataframe
            input_feature_train_df=train_df.drop(TARGET_COLUMN,axis=1)
            input_feature_test_df=test_df.drop(TARGET_COLUMN,axis=1)

            logging.info("Onehot Encoding the Categorical Features")

            logging.info(f"selecting target feature for train and test dataframe")
            #selecting target feature for train and test dataframe
            logging.info("selecting target feature for train and test dataframe")
            target_feature_train_df = train_df[TARGET_COLUMN]
            target_feature_test_df = test_df[TARGET_COLUMN]

            label_encoder = LabelEncoder()
            label_encoder.fit(target_feature_train_df)

            #transformation on target columns
            logging.info(f"transformation on target columns")

            target_feature_train_arr=np.array(target_feature_train_df)
            target_feature_test_arr=np.array(target_feature_test_df)
            logging.info(f"Transformation object")
            transformation_pipleine = DataTransformation.get_data_transformer_object()
            transformation_pipleine.fit(input_feature_train_df)

            #transforming input features
            logging.info("transforming input features")
            input_feature_train_arr = transformation_pipleine.transform(input_feature_train_df)
            logging.info(f"Transoformed the input_train_arr")
            input_feature_test_arr = transformation_pipleine.transform(input_feature_test_df)
            logging.info(f"Transoformed the input_test_arr")

            logging.info(f"target_feature_train_arr shape: {target_feature_train_arr.shape}")
            logging.info(f"target_feature_test_arr shape: {target_feature_test_arr.shape}")
            logging.info(f"Transformed the input_train_arr and input_test_arr")

            
            logging.info(f"Before resampling in training set Input: {input_feature_train_arr.shape} Target:{target_feature_train_arr.shape}")
            smt = SMOTETomek(sampling_strategy="minority")
            input_feature_train_arr, target_feature_train_arr = smt.fit_resample(input_feature_train_arr, target_feature_train_arr)
            logging.info(f"After resampling in training set Input: {input_feature_train_arr.shape} Target:{target_feature_train_arr.shape}")
            
            logging.info(f"Before resampling in testing set Input: {input_feature_test_arr.shape} Target:{target_feature_test_arr.shape}")
            input_feature_test_arr, target_feature_test_arr = smt.fit_resample(input_feature_test_arr, target_feature_test_arr)
            logging.info(f"After resampling in testing set Input: {input_feature_test_arr.shape} Target:{target_feature_test_arr.shape}")

            #target encoder
            logging.info(f"target encoder")
            train_arr = np.c_[input_feature_train_arr, target_feature_train_arr ]
            test_arr = np.c_[input_feature_test_arr, target_feature_test_arr]


            #save numpy array
            logging.info(f"save transformed train array")
            utils.save_numpy_array_data(file_path=self.data_transformation_config.transformed_train_path,
                                        array=train_arr)

            logging.info(f"saving the transformed test array")
            utils.save_numpy_array_data(file_path=self.data_transformation_config.transformed_test_path,
                                        array=test_arr)

            logging.info(f"saving the transformer object")
            utils.save_object(file_path=self.data_transformation_config.transform_object_path,
             obj=transformation_pipleine)

            logging.info(f"saving the target encoder object")
            utils.save_object(file_path=self.data_transformation_config.target_encoder_path,
             obj=label_encoder)


            logging.info(f"Data Transformation artifact")
            data_transformation_artifact = artifact_entity.DataTransformationArtifact(
                transform_object_path=self.data_transformation_config.transform_object_path,
                transformed_train_path = self.data_transformation_config.transformed_train_path,
                transformed_test_path = self.data_transformation_config.transformed_test_path,
                target_encoder_path = self.data_transformation_config.target_encoder_path

            )

            logging.info(f"Data transformation object {data_transformation_artifact}")
            return data_transformation_artifact
        except Exception as e:
            raise IncomeException(e, sys)


