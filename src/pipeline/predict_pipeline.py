import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object
import os


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            model_path=os.path.join("artifacts","model.pkl")
            #preprocessor_path=os.path.join('artifacts','proprocessor.pkl')
            #print("Before Loading")
            model=load_object(file_path=model_path)
            #preprocessor=load_object(file_path=preprocessor_path)
            #print("After Loading")
            #data_scaled=preprocessor.transform(features)
            #preds=model.predict(data_scaled)
            preds = model.predict(features)
            return preds
        
        except Exception as e:
            raise CustomException(e,sys)



class CustomData:
    def __init__(
            self,
            Total_stops: int,
            Journey_day: int,
            Journey_month: int,
            Arrival_hour: int,
            Arrival_min: int,
            Dep_hour: int,
            Dep_min: int,
            Duration_Mins,
            Air_India,
            GoAir,
            IndiGo,
            Jet_Airways,
            Jet_Airways_Business,
            Multiple_carriers,
            Multiple_carriers_Premium_economy,
            SpiceJet,
            Trujet,
            Vistara,
            Vistara_Premium_economy,
            s_Chennai,
            s_Delhi,
            s_Kolkata,
            s_Mumbai,
            d_Cochin,
            d_Delhi,
            d_Hyderabad,
            d_Kolkata,
            d_New_Delhi
    ):

        self.Total_stops = Total_stops
        self.Journey_day = Journey_day
        self.Journey_month = Journey_month
        self.Arrival_hour = Arrival_hour
        self.Arrival_min = Arrival_min
        self.Dep_hour = Dep_hour
        self.Dep_min = Dep_min
        self.Duration_Mins = Duration_Mins
        self.Air_India = Air_India
        self.GoAir = GoAir
        self.IndiGo = IndiGo
        self.Jet_Airways = Jet_Airways
        self.Jet_Airways_Business = Jet_Airways_Business
        self.Multiple_carriers = Multiple_carriers
        self.Multiple_carriers_Premium_economy = Multiple_carriers_Premium_economy
        self.SpiceJet = SpiceJet
        self.Trujet = Trujet
        self.Vistara = Vistara
        self.Vistara_Premium_economy = Vistara_Premium_economy
        self.s_Chennai = s_Chennai
        self.s_Delhi = s_Delhi
        self.s_Kolkata = s_Kolkata
        self.s_Mumbai = s_Mumbai
        self.d_Cochin = d_Cochin
        self.d_Delhi = d_Delhi
        self.d_Hyderabad = d_Hyderabad
        self.d_Kolkata = d_Kolkata
        self.d_New_Delhi = d_New_Delhi

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "Total_Stops": [self.Total_stops],
                "Day": [self.Journey_day],
                "Month": [self.Journey_month],
                "Arrival_Hour": [self.Arrival_hour],
                "Arrival_Mins": [self.Arrival_min],
                "Dep_Hours": [self.Dep_hour],
                "Dep_Mins": [self.Dep_min],
                "Duration_Mins": [self.Duration_Mins],
                "Airline_Air India": [self.Air_India],
                "Airline_GoAir": [self.GoAir],
                "Airline_IndiGo": [self.IndiGo],
                "Airline_Jet Airways": [self.Jet_Airways],
                "Airline_Jet Airways Business": [self.Jet_Airways_Business],
                "Airline_Multiple carriers": [self.Multiple_carriers],
                "Airline_Multiple carriers Premium economy": [self.Multiple_carriers_Premium_economy],
                "Airline_SpiceJet": [self.SpiceJet],
                "Airline_Trujet": [self.Trujet],
                "Airline_Vistara": [self.Vistara],
                "Airline_Vistara Premium economy": [self.Vistara_Premium_economy],
                "Source_Chennai": [self.s_Chennai],
                "Source_Delhi": [self.s_Delhi],
                "Source_Kolkata": [self.s_Kolkata],
                "Source_Mumbai": [self.s_Mumbai],
                "Destination_Cochin": [self.d_Cochin],
                "Destination_Delhi": [self.d_Delhi],
                "Destination_Hyderabad": [self.d_Hyderabad],
                "Destination_Kolkata": [self.d_Kolkata],
                "Destination_New Delhi": [self.d_New_Delhi],
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)

