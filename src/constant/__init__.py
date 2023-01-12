import os
from os import environ
from datetime import datetime

from from_root import from_root

TIMESTAMP: str = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")

DB_NAME = 'banking'
COLLECTION_NAME = 'bankdf'
DB_URL = environ["MONGO_DB_URL"]

TARGET_COLUMN = 'Loan_Status'

SCHEMA_FILE_PATH = "config/schema.yaml"
MODEL_CONFIG_FILE = 'config/model.yaml'


TEST_SIZE = 0.2
ARTIFACTS_DIR = os.path.join(from_root(), 'artifacts', TIMESTAMP)
DATA_INGESTION_ARTIFACTS_DIR = 'DataIngestionArtifacts'
DATA_INGESTION_TRAIN_DIR = 'Train'
DATA_INGESTION_TEST_DIR = 'Test'
DATA_INGESTION_TRAIN_FILE_NAME = 'train.csv'
DATA_INGESTION_TEST_FILE_NAME = 'test.csv'