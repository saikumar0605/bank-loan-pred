import sys
from src.configuration.s3_operations import S3Operation
from src.entity.artifacts_entity import DataTransformationArtifacts, ModelPusherArtifacts, ModelTrainerArtifacts
from src.entity.config_entity import ModelPusherConfig
from src.exception import CustomException
import logging

logger = logging.getLogger(__name__)

class ModelPusher:
    def __init__(self, model_pusher_config: ModelPusherConfig, model_trainer_artifacts: ModelTrainerArtifacts, 
                    data_transformation_artifacts: DataTransformationArtifacts,
                    s3: S3Operation):

        self.model_pusher_config = model_pusher_config
        self.model_trainer_artifacts = model_trainer_artifacts
        self.data_transformation_artifacts = data_transformation_artifacts
        self.s3 = s3


    def initiate_model_pusher(self) -> ModelPusherArtifacts:
        logger.info("Entered initiate_model_pusher method of ModelTrainer class")
        try:
            logger.info("Uploading artifacts folder to s3 bucket")
            
            self.s3.upload_file(
                self.model_trainer_artifacts.trained_model_file_path,
                self.model_pusher_config.S3_MODEL_KEY_PATH,
                self.model_pusher_config.BUCKET_NAME,
                remove=False,
            )
            logger.info("Uploaded artifacts folder to s3 bucket")
            logger.info("Exited initiate_model_pusher method of ModelTrainer class")

            model_pusher_artifact = ModelPusherArtifacts(bucket_name=self.model_pusher_config.BUCKET_NAME, 
                                                            s3_model_path=self.model_pusher_config.S3_MODEL_KEY_PATH)

            return model_pusher_artifact

        except Exception as e:
            raise CustomException(e, sys) from e