# Getting the Superset server up and running
Note: Directions are sourced from https://superset.apache.org/docs/installation/installing-superset-from-scratch/  but I found multiple things I needed to change to get this working.

Create an EC2 instance of Ubuntu 20.04 with at least 8GB RAM and 40GB hard drive (I used t2.large)

```

# Prepare the OS
sudo apt update
sudo apt-get install -y build-essential libssl-dev libffi-dev python3-dev python3-pip libsasl2-dev libldap2-dev default-libmysqlclient-dev
sudo apt install -y python3.8-venv
# Set up a virtual environment
python3 -m venv superset
. superset/bin/activate
# pip install dependencies, including ones superset has the wrong version of and are missing on their end...
pip install wheel #Not present but should be
pip install apache-superset
pip install sqlparse=='0.4.3' #Superset comes with an incorrect version 0.4.4 which does not work
pip install marshmallow-enum #Not present but should be
# Setup a superset_config.py file
echo "SECRET_KEY=<redacted>" > /home/ubuntu/superset_config.py
echo "export PYTHONPATH=/home/ubuntu" >> /home/ubuntu/.profile
# Initialize the database
superset db upgrade
# More Superset config
export FLASK_APP=superset
# Create an admin user in your metadata database (use `admin` as username to be able to load the examples)
superset fab create-admin
# Load some data to play with
superset load_examples
# Create default roles and permissions
superset init
# To start a development web server on port 8088, use -p to bind to another port
# Superset will only be available locally without the --host 0.0.0.0 flag
superset run -p 8088 --with-threads --reload --debugger --host 0.0.0.0
Connecting the server to Athena
Install an Athena Python driver


pip install pyathena[pandas]==2.25.2 # Must be >=2, < 3
Create an IAM User


#Create a user in IAM with AthenaFullAccess
#This user must have permanent credentials:
#Temporary will not suffice for the Superset connection to Athena
Create the connection
Settings > Database Connections > Other > (Click “Database” button) > “Supported Databases” > Other



SQLAlchemy URI = awsathena+rest://AWS_ACCESS_KEY_ID:AWS_SECRET_ACCESS_KEY@athena.us-east-1.amazonaws.com/hwe?s3_staging_dir=s3://hwe-tsagona/superset_staging&work_group=hwe

```
Then you are ready to start creating data sets.