# Hours with Experts - Week 1 

A very simple Spark program to make sure your environment on your laptop is set up for Spark.

## Installing Python

Note: If your computer has already has Python set up and you have used it before, you can skip this step!

### Windows
Navigate to https://www.python.org/downloads/windows and click on the most recent maintenance release. This will be the first one listed that has the option of "Windows installer (64-bit)" (at time of writing, this was 3.11.4)

![Alt text](install-python-windows-1.png)

Click the link in the screenshot to download the 64 bit installer. Run the executable to start the Python installation process.

After completion, there are a few extra steps we need to take to make sure Python is working. 

1. "Manage app execution aliases"
2. Add Python and pip to PATH
C:\Users\tsago\AppData\Local\Programs\Python\Python311
C:\Users\tsago\AppData\Local\Programs\Python\Python311\Scripts

After both steps are complete, open a command prompt and type "python". You should be greeted with a Python command line prompt matching the version you just installed.

## Installing virtualenv

`pip install virtualenv`

## Create a virtual environment

`python -m virtualenv hwe`


## Activate the virtual environment

`hwe\Scripts\activate`

## Install the dependencies
`cd hwe-labs\week1`
`pip install -r requirements.txt`

Note: pyspark is a large download with a lot of dependencies - this will take several minutes.

## Set SPARK_HOME
SPARK_HOME=C:\Users\tsago\hwe\Lib\site-packages\pyspark

## Install Java 1.8 in a path without spaces and set JAVA_HOME appropriately

## Create an env variable for PYSPARK_PYTHON
PYSPARK_PYTHON=C:\Users\tsago\AppData\Local\Programs\Python\Python311\python.exe

## Configure VS Code to use your virtual environment
Click in the bottom right corner , click "Enter Interpreter Path", then browse to:

`C:\Users\you\hwe\Scripts\python.exe`

## Running a simple pyspark program
Clicking the run button in VS Code should work