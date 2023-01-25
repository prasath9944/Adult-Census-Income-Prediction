import pandas as pd
import json
from dataclasses import dataclass
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import os
@dataclass
class EnvironmentVariable:
    clientId:str = os.getenv("CASSANDRA_CLIENTID")
    secret_key:str=os.getenv("CASSANDRA_SECRET_KEY")
    secure_bundle:str=os.getenv("CASSANDRA_SECURE_BUNDLE")


env_var = EnvironmentVariable()

cloud_config= {    
         'secure_connect_bundle': env_var.secure_bundle
}
auth_provider = PlainTextAuthProvider(env_var.clientId, env_var.secret_key)
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()


