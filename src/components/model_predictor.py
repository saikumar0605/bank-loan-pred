import logging
import sys
from typing import Dict
from pandas import DataFrame
import pandas as pd
from src.constant import *
from src.configuration.s3_operations import S3Operation
from src.exception import CustomException

logger = logging.getLogger(__name__)

class bankData:
    def __init__(self, Gender, Married, Depender, Education, Self_Employed, Applicantincome, Coapplicantincome, LoanAmount, Loan_Amount_Term, Credit_History, Property_Area, Loan_Status):
        self.Gender = Gender
        self.Married = Married
        self.Depender = Depender
        self.Education = Education
        self.Self_Employed = Self_Employed
        self.Applicantincome = Applicantincome
        self.Coapplicantincome = Coapplicantincome
        self.LoanAmount = LoanAmount
        self.Loan_Amount_Term = Loan_Amount_Term
        self.Credit_History = Credit_History
        self.Property_Area = Property_Area
        self.Loan_Status = Loan_Status


    def get_data(self) -> Dict:
        logger.info("Entered get_data method of SensorData class")
        try:
            input_data = {
                "Gender": [self.Gender],
                "Married": [self.Married],
                "Depender": [self.Depender],
                "Education": [self.Education],
                "Self_Employed": [self.Self_Employed],
                "Applicantincome": [self.Applicantincome],
                "Coapplicantincome": [self.Coapplicantincome],
                "LoanAmount": [self.LoanAmount],
                "Loan_Amount_Term": [self.Loan_Amount_Term],
                "Credit_History": [self.Credit_History],
                "Property_Area": [self.Property_Area],
                "Loan_Status": [self.Loan_Status],
                }
            return input_data
        
        except Exception as e:
            raise CustomException(e, sys)


    def get_bankdata_input_data_frame(self) -> DataFrame:
        logger.info(
            "Entered get_bankdata_input_data_frame method of bankdata class"
        )
        try:
            bankdata_input_dict = self.get_data()
            logger.info("Got bank data as dict")
            logger.info(
                "Exited get_bankdata_input_data_frame method of bankdata class"
            )
            return pd.DataFrame(bankdata_input_dict)

        except Exception as e:
            raise CustomException(e, sys) from e


class LoanstatusPredictor:
    def __init__(self):
        self.s3 = S3Operation()
        self.bucket_name = BUCKET_NAME


    def predict(self, X) -> None:
        logger.info("Entered predict method of LoanstatusPredictor class")
        try:
            best_model = self.s3.load_model(MODEL_FILE_NAME, self.bucket_name)
            logger.info("Loaded best model from s3 bucket")
            result = best_model.predict(X)
            logger.info("Exited predict method of LoanstatusPredictor class")
            return result

        except Exception as e:
            raise CustomException(e, sys) from e