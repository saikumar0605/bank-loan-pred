import sys
import os
import logging
from pandas import DataFrame
from sklearn.model_selection import train_test_split
from typing import Tuple

logger = logging.getLogger(__name__)

class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig, mongo_op: MongoDBOperation):
        self.data_ingestion_config = data_ingestion_config
        self.mongo_op = mongo_op

    def get_data_from_mongo(self) -> DataFrame:
        try:
            logger.info("Getting data from mongo using data_ingestion class")
            data = self.mongo_op.read_from_mongo(self.data_ingestion_config.mongo_db_name,
                                                 self.data_ingestion_config.mongo_collection_name)
            return data
        except Exception as e:
            logger.error("Error while getting data from mongo")
            raise 