import pymongo
import pandas as pd
import json
from dataclasses import dataclass
# Provide the mongodb localhost url to connect python to mongodb.
import os

@dataclass
class EnvironmentVariable:
    mongo_db_url:str = os.getenv("MONGO_DB_URL")






env_var = EnvironmentVariable()
mongo_client = pymongo.MongoClient(env_var.mongo_db_url)
TARGET_COLUMN = "salary"









# @dataclass
# class EnvironmentVariable:
#     clientId:str = os.getenv("CASSANDRA_CLIENTID")
#     secret_key:str=os.getenv("CASSANDRA_SECRET_KEY")
#     secure_bundle:str=os.getenv("CASSANDRA_SECURE_BUNDLE")


# env_var = EnvironmentVariable()

# cloud_config= {    
#          'secure_connect_bundle': env_var.secure_bundle
# }
# auth_provider = PlainTextAuthProvider(env_var.clientId, env_var.secret_key)
# cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
# session = cluster.connect()


