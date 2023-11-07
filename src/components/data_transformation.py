import sys
from dataclasses import dataclass

import numpy as np 
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler

from src.exception import CustomException
from src.logger import logging
import os
from src.utils import save_object
#save_object for saving pkl file

@dataclass
class DataTransformationConfig:
    """path,src needs for data transformation"""
    #preprocessor_obj_file_path=os.path.join('artifacts',"preprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()

    def get_data_transformer_object(self):
        '''
        This function is responsible for data transformation
        ie create pkl file for preprocessor pipeline data transformation
        '''
        try:
            numerical_columns = ["Total_Stops", "Price", 'Day', 'Month', 'Arrival_Hour', 'Arrival_Mins', 'Dep_Hours','Dep_Mins', 'Duration_Mins']
            categorical_columns = ["Airline", "Source", "Destination"]

            num_pipeline = Pipeline(steps=[
                ("imputer", SimpleImputer(strategy="mean")),
                ("scaler", StandardScaler())])

            cat_pipeline = Pipeline(steps=[
                ("imputer", SimpleImputer(strategy="most_frequent")),
                ("one_hot_encoder", OneHotEncoder()),
                ("scaler", StandardScaler())])

            logging.info(f"Categorical columns: {categorical_columns}")
            logging.info(f"Numerical columns: {numerical_columns}")

            preprocessor = ColumnTransformer(
                [("num_pipeline", num_pipeline,numerical_columns),
                 ("cat_pipelines", cat_pipeline,categorical_columns)])

            return preprocessor
        
        except Exception as e:
            raise CustomException(e,sys)
        
    def initiate_data_transformation(self,train_path,test_path):
        """From Data Ingestion"""
        try:
            """all column transformation ie return preprocessor from above"""
            preprocessing_obj = self.get_data_transformer_object()

            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info("Read train and test data completed")
            logging.info("Obtaining preprocessing object")


            target_column_name= "Price"
            input_feature_train_df = train_df.drop(columns=[target_column_name],axis=1)
            target_feature_train_df = train_df[target_column_name]

            input_feature_test_df=test_df.drop(columns=[target_column_name],axis=1)
            target_feature_test_df=test_df[target_column_name]

            logging.info(f"Applying preprocessing object on training dataframe and testing dataframe.")

            input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df)

            train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_df)]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            logging.info(f"Saved preprocessing object.")

            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path, #'artifacts'/"proprocessor.pkl"
                obj=preprocessing_obj

            ) #utils --> take the preprocessor steps and make a pkl file in utils

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path, #pkl file
            )

        except Exception as e:
            raise CustomException(e,sys)
