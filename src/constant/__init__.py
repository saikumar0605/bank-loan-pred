import os
from os import environ
from datetime import datetime

from from_root import from_root

TIMESTAMP: str = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")

DB_NAME = 'banking'
COLLECTION_NAME = 'bankdf'
DB_URL = environ["MONGO_DB_URL"]