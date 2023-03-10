import sys
from src.configuration.mongodb import MongoDBOperation
from src.entity.artifacts_entity import DataIngestionArtifacts,DataTransformationArtifacts,DataValidationArtifacts
from src.entity.config_entity import DataIngestionConfig,DataTransformationConfig,DataValidationConfig
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.data_validation import DataValidation
from src.exception import CustomException
import logging

logger = logging.getLogger(__name__)

class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        self.data_transformation_config = DataTransformationConfig()
        self.data_validation_config = DataValidationConfig()
        self.mongo_op = MongoDBOperation()


    def start_data_ingestion(self) -> DataIngestionArtifacts:
        logger.info("Entered the start_data_ingestion method of TrainPipeline class")
        try:
            logger.info("Getting the data from mongodb")
            data_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config, mongo_op=self.mongo_op)
            data_ingestion_artifacts = data_ingestion.initiate_data_ingestion()
            logger.info("Got the train_set and test_set from mongodb")
            logger.info(
                "Exited the start_data_ingestion method of TrainPipeline class"
            )
            return data_ingestion_artifacts

        except Exception as e:
            raise CustomException(e, sys) from e

    def start_data_validation(self, data_ingestion_artifacts: DataIngestionArtifacts) -> DataValidationArtifacts:
        """
        This method of TrainPipeline class is responsible for starting data validation component 
        """
        logging.info("Entered the start_data_validation method of TrainPipeline class")

        try:
            data_validation = DataValidation(
                data_ingestion_artifacts=data_ingestion_artifacts,
                data_validation_config=self.data_validation_config,
            )

            data_validation_artifact = data_validation.initiate_data_validation()

            logging.info("Performed the data validation operation")

            logging.info(
                "Exited the start_data_validation method of TrainPipeline class"
            )

            return data_validation_artifact

        except Exception as e:
            raise CustomException(e, sys) from e            

    def start_data_transformation(self, data_ingestion_artifacts: DataIngestionArtifacts,
                                  data_validation_artifact: DataValidationArtifacts) -> DataTransformationArtifacts:
        """
        This method of TrainPipeline class is responsible for starting data transformation  
        """
        try:
            data_transformation = DataTransformation(
                data_ingestion_artifacts=data_ingestion_artifacts,
                data_transformation_config=self.data_transformation_config
            )
            data_transformation_artifact = (
                data_transformation.initiate_data_transformation()
            )
            return data_transformation_artifact

        except Exception as e:
            raise CustomException(e,sys) from e

    def run_pipeline(self,) -> None:
        """
        This method of TrainPipeline class is responsible for running complete pipeline
        """
        try:
            data_ingestion_artifacts = self.start_data_ingestion()
            data_validation_artifact = self.start_data_validation(data_ingestion_artifacts=data_ingestion_artifacts)
            data_transformation_artifact = self.start_data_transformation(data_ingestion_artifacts=data_ingestion_artifacts, 
                                                                          data_validation_artifact=data_validation_artifact)
        except Exception as e:
            raise CustomException(e, sys) from e