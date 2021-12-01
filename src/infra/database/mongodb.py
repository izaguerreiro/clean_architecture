import os
import logging

from pymongo import ASCENDING
from pymongo import MongoClient


logger = logging.getLogger(__name__)

MONGODB_CLIENT = MongoClient(os.getenv("MONGO_URI"))


def get_database_instance():
    """Return a collection addresses from database viacep."""
    try:
        db = MONGODB_CLIENT.get_database("viacep")
        database = db.get_collection("addresses")
        db.domain.addresses.create_index([("cep", ASCENDING)], unique=True)
        MONGODB_CLIENT.server_info()

        return database
    except Exception as e:
        logger.error(f"Error connect database: {e}")
        exit()