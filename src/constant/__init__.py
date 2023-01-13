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

DATA_VALIDATION_ARTIFACT_DIR = 'DataValidationArtifacts'
DATA_DRIFT_FILE_NAME = "DataDriftReport.yaml"

DATA_TRANSFORMATION_ARTIFCATS_DIR = 'DataTransformationArtifacts'
TRANSFORMED_TRAIN_DATA_DIR = 'TransformedTrain'
TRANSFORMED_TEST_DATA_DIR = 'TransformedTest'
TRANSFORMED_TRAIN_DATA_FILE_NAME = 'transformed_train_data.npz'
TRANSFORMED_TEST_DATA_FILE_NAME = 'transformed_test_data.npz'
PREPROCESSOR_OBJECT_FILE_NAME = "loan_status_preprocessor.pkl"

MODEL_TRAINER_ARTIFACTS_DIR = 'ModelTrainerArtifacts'
MODEL_FILE_NAME = 'loan_status_preprocessor.pkl'

BUCKET_NAME = 'car-price-io-files'
S3_MODEL_NAME = 'loan_status_preprocessor.pkl'



MODEL_SAVE_FORMAT = '.pkl'

APP_HOST = '0.0.0.0'
APP_PORT = 8080