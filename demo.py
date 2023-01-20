# from src.components.data_ingestion import DataIngestion
# from src.entity.config_entity import DataIngestionConfig
# from src.components.data_validation import DataValidation
# from src.entity.config_entity import DataValidationConfig
# from src.configuration.mongodb import MongoDBOperation

# de = DataValidation(data_validation_config=DataValidationConfig(), mongo_op=MongoDBOperation())
# data__artifacts = de.initiate_data_ingestion()

# #de = DataIngestion(data_ingestion_config=DataIngestionConfig(), mongo_op=MongoDBOperation())

# #data_ingestion_artifacts = de.initiate_data_ingestion()


# # from src.pipline.train_pipeline import TrainPipeline

from src.pipline.train_pipeline import TrainPipeline

if __name__ == '__main__':
    
    TrainPipeline().run_pipeline()