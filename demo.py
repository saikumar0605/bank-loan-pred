from src.components.data_ingestion import DataIngestion
from src.entity.config_entity import DataIngestionConfig
from src.configuration.mongodb import MongoDBOperation



de = DataIngestion(data_ingestion_config=DataIngestionConfig(), mongo_op=MongoDBOperation())

data_ingestion_artifacts = de.initiate_data_ingestion()


# from src.pipline.train_pipeline import TrainPipeline


# if __name__ == '__main__':
    
#     TrainPipeline().run_pipeline()