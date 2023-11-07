import numpy as np
import pandas as pd
import os
import sys
from src.exception import CustomException
from src.logger import logging

class Preprocessing:
    def __init__(self):
        pass

    def cleaning_data(self):
        logging.info("Entered the data ingestion method or component")
        try:
            df = pd.read_csv('notebook\data\data.csv',parse_dates=['Date_of_Journey'])
            logging.info('Read the dataset as dataframe')

            df['Day'] = df['Date_of_Journey'].dt.day
            df['Month'] = df['Date_of_Journey'].dt.month
            df['Year'] = df['Date_of_Journey'].dt.year

            df['Arrival_Time'] = df['Arrival_Time'].apply(lambda x: x.split(" ")[0])
            df['Arrival_Hour'] = df['Arrival_Time'].apply(lambda x: x.split(":")[0])
            df['Arrival_Mins'] = df['Arrival_Time'].apply(lambda x: x.split(":")[1])
            df['Arrival_Hour'] = df['Arrival_Hour'].astype(int)
            df['Arrival_Mins'] = df['Arrival_Mins'].astype(int)

            df['Dep_Hours'] = df['Dep_Time'].apply(lambda x: x.split(":")[0])
            df['Dep_Mins'] = df['Dep_Time'].apply(lambda x: x.split(":")[1])
            df['Dep_Hours'] = df['Dep_Hours'].astype(int)
            df['Dep_Mins'] = df['Dep_Mins'].astype(int)

            stops = {'non-stop': 0, '2 stops': 2, '1 stop': 1, '3 stops': 3, '4 stops': 4, 'nan': 1}
            df['Total_Stops'] = df['Total_Stops'].map(stops)

            df['Duration'].replace(['5m', '50m'], inplace=True)
            df['Duration_Hours'] = df['Duration'].str.split(" ").str[0].str.split('h').str[0].astype(int)
            df['Duration_Mins'] = df['Duration'].str.split(" ").str[1]
            df['Duration_Mins'].replace([np.nan, '0'], inplace=True)
            df['Duration_Mins'] = df['Duration_Hours'] * 60 + df['Duration_Mins'].str.split(" ").str[0].str.split('m').str[0].astype(int)

            df.fillna(0, inplace=True)

            df.drop(['Date_of_Journey'], axis=1, inplace=True)
            df.drop('Arrival_Time', axis=1, inplace=True)
            df.drop('Dep_Time', axis=1, inplace=True)
            df.drop(['Route'], inplace=True, axis=1)
            df.drop(['Additional_Info'], axis=1, inplace=True)
            df.drop(['Duration', 'Duration_Hours'], inplace=True, axis=1)
            df.drop(['Year'], inplace=True, axis=1)

            ohe_cols = ['Airline', 'Source', 'Destination']
            pd.get_dummies(df, columns=ohe_cols, drop_first=True).to_csv('notebook\data\Flight.csv',index=False)
            logging.info("Data Pre Processing Done!")

        except Exception as e:
            raise CustomException(e,sys)

