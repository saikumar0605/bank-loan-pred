from src.components.data_ingestion import DataIngestion
from src.entity.config_entity import DataIngestionConfig
from database.mongodb import MongoDBOperation



de = DataIngestion(data_ingestion_config=DataIngestionConfig(), mongo_op=MongoDBOperation())

data = de.get_data_from_mongo()

print(data)