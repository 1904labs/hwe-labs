import pprint
import json
import boto3
import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import count
from pyspark.sql.types import StructType, StructField, StringType, TimestampType


aws_access_key_id = os.environ.get("AWS_ACCESS_KEY_ID")
aws_secret_access_key = os.environ.get("AWS_SECRET_ACCESS_KEY")
aws_session_token = os.environ.get("AWS_SESSION_TOKEN")


querystring = """
create external table hwe.tim_ints2 ( 
    id int) 
stored as parquet  
location 's3://hwe-tsagona/ints2'
"""


# Initialize Boto3 Glue client
ath = boto3.client('athena', region_name='us-east-1', aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    aws_session_token=aws_session_token)

# OR Initialize Boto3 Glue resource
#glue_resource = boto3.resource('glue', region_name='us-east-1')

# Get the Glue Catalog databases
#databases = glue_client.get_databases()
#pprint.pprint(databases, width=1)
#print(json.dumps(databases, indent=4))

ath.start_query_execution(QueryString=querystring, WorkGroup="hwe",
        ResultConfiguration={'OutputLocation': 's3://hwe-tsagona/queries/'})