import shutil
import sys
from typing import Dict, Tuple, List
import numpy as np
import pandas as pd
from yaml import safe_dump
import yaml
from pandas import DataFrame
from src.constant import *
from src.exception import CustomException
import logging


class MainUtils:

    def read_yaml_file(self, filename: str) -> dict:
        try:
            with open(filename, "rb") as yaml_file:
                return yaml.safe_load(yaml_file)

        except Exception as e:
            raise CustomException(e, sys) from e


    def write_json_to_yaml_file(self, json_file: dict, yaml_file_path: str) -> yaml:
        try:
            data = json_file
            stream = open(yaml_file_path, 'w')
            yaml.dump(data, stream)

        except Exception as e:
            raise CustomException(e, sys) from e


    def read_schema_file_path(self) -> dict:
        try:
            schema_config = self.read_yaml_file(SCHEMA_FILE_PATH)
            return schema_config

        except Exception as e:
            raise CustomException(e, sys) from e


    def read_model_config_file(self) -> dict:
        try:
            model_config = self.read_yaml_file(MODEL_CONFIG_FILE)
            return model_config

        except Exception as e:
            raise CustomException(e, sys) from e

        
    def save_numpy_array_data(self, file_path: str, array: np.array):
        try:
            with open(file_path, 'wb') as file_obj:
                np.save(file_obj, array)

            return file_path

        except Exception as e:
            raise CustomException(e, sys) from e


    def load_numpy_array_data(self, file_path: str) -> np.array:
        try:
            with open(file_path, 'rb') as file_obj:
                return np.load(file_obj)

        except Exception as e:
            raise CustomException(e, sys) from e


    def get_tuned_model(self, model_name: str, train_x: DataFrame, train_y: DataFrame, test_x: DataFrame, test_y: DataFrame) -> Tuple[float, object, str]:
        logging.info("Entered the get_tuned_model method of MainUtils class")
        try:
            model = self.get_base_model(model_name)
            model_best_params = self.get_model_params(model, train_x, train_y)
            model.set_params(**model_best_params)
            model.fit(train_x, train_y)
            preds = model.predict(test_x)
            model_score = self.get_model_score(test_y, preds)
            logging.info("Exited the get_tuned_model method of MainUtils class")
            return model_score, model, model.__class__.__name__

        except Exception as e:
            raise CustomException(e, sys) from e


    @staticmethod
    def get_model_score(test_y: DataFrame, preds: DataFrame) -> float:
        logging.info("Entered the get_model_score method of MainUtils class")
        try:
            model_score = r2_score(test_y, preds)
            logging.info("Model score is {}".format(model_score))
            logging.info("Exited the get_model_score method of MainUtils class")
            return model_score

        except Exception as e:
            raise CustomException(e, sys) from e








    @staticmethod
    def save_object(file_path: str, obj: object) -> None:
        logging.info("Entered the save_object method of MainUtils class")
        try:
            with open(file_path, "wb") as file_obj:
                dill.dump(obj, file_obj)

            logging.info("Exited the save_object method of MainUtils class")

            return file_path

        except Exception as e:
            raise CustomException(e, sys) from e

    @staticmethod
    def get_best_model_with_name_and_score(model_list: list) -> Tuple[object, float]:
        logging.info(
            "Entered the get_best_model_with_name_and_score method of MainUtils class"
        )
        try:
            best_score = max(model_list)[0]
            best_model = max(model_list)[1]
            logging.info(
                "Exited the get_best_model_with_name_and_score method of MainUtils class"
            )
            return best_model, best_score

        except Exception as e:
            raise CustomException(e, sys) from e


    @staticmethod
    def load_object(file_path: str) -> object:
        logging.info("Entered the load_object method of MainUtils class")
        try:
            with open(file_path, "rb") as file_obj:
                obj = dill.load(file_obj)
            logging.info("Exited the load_object method of MainUtils class")
            return obj

        except Exception as e:
            raise CustomException(e, sys) from e


    @staticmethod
    def create_artifacts_zip(file_name: str, folder_name: str) -> None:
        logging.info("Entered the create_artifacts_zip method of MainUtils class")
        try:
            shutil.make_archive(file_name, "zip", folder_name)
            logging.info("Exited the create_artifacts_zip method of MainUtils class")

        except Exception as e:
            raise CustomException(e, sys) from e


    @staticmethod
    def unzip_file(filename: str, folder_name: str) -> None:
        logging.info("Entered the unzip_file method of MainUtils class")
        try:
            shutil.unpack_archive(filename, folder_name)
            logging.info("Exited the unzip_file method of MainUtils class")

        except Exception as e:
            raise CustomException(e, sys) from e


    def update_model_score(self, best_model_score: float) -> None:
        logging.info("Entered the update_model_score method of MainUtils class")
        try:
            model_config = self.read_model_config_file()
            model_config["base_model_score"] = str(best_model_score)
            with open(MODEL_CONFIG_FILE, "w+") as fp:
                safe_dump(model_config, fp, sort_keys=False)
            logging.info("Exited the update_model_score method of MainUtils class")

        except Exception as e:
            raise CustomException(e, sys) from e

    def get_Bank_list(self) -> List:
        logging.info("Entered the get_car_list method of MainUtils class")
        try:
            with open(CONFIG_FILE_PATH) as f:
                data =  yaml.safe_load(f)
            Bankdata = data["Bankdata"]
            logging.info("Exited the get_bank_data method of MainUtils class")
            return Bankdata

        except Exception as e:
            raise CustomException(e, sys) from e