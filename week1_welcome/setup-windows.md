# Windows Setup Instructions

Note: It is possible you already have other/more recent versions of Python and Java already on your computer (Java 1.8 came out in 2014!). However, it is very important to have exactly these versions: lots of data engineering projects were built off of Java 1.8, and you will encounter lots of errors (some obvious, some tricky) if your versions of Java, Python, and AWS libraries are not corrreclty in sync!

## Installing Python

Navigate to https://www.python.org/downloads/windows and find the "Windows installer (64-bit)" for 3.10.11.

![Alt text](install-python-windows-1.png)

Download the 64 bit Microsoft installer. Run the executable to start the Python installation process.


After completion, there is one extra step you may need to take to make sure Python is working. By default, Windows will attempt to install Python from the Windows store instead of executing your program when `python` is executed from the command line. To fix this:

1. Type `Manage app execution aliases` in the Windows search bar
2. Make sure the 2 Python options are disabled:
    * "App Installer/python.exe"
    * "App Installer/python3.exe"

After this is complete, open a command prompt and type "python". You should be greeted with a Python command line prompt matching the version you just installed.

## Install Java 1.8
Navigate to https://adoptium.net/download/:

Filter on:
* Operating System = Windows
* Architecture = x64
* Package Type = JDK
* Version = 8 - LTS

Download the and execute Zulu Microsoft Installer (msi).

Make sure the options about updating your PATH and setting JAVA_HOME are set.

After installation is complete, open a brand new command prompt (do not re-use an existing DOS prompt), and type `java -version`. You should receive a message indicating an OpenJDK instance of Java 1.8 (Zulu) is installed.

## Git Bash

## WinUtils

Clone the `winutils` repo:
`git clone https://github.com/cdarlint/winutils`

## Visual Studio Code

## Modify Powershell execution policy
Under the Default Powershell execution policy, your programs will execute successfully but the output will be hard to read. To make the output easier:
1. Open Powershell as an Adminstrator
2. Execute the following command: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned`


## Set up environment variables:
To edit Windows environment variables, type `env` in the Windows search bar, and click either `New` or `Edit` in the top/`User Variables` section.

Note: Any time you change an environment variable, you should close/re-open any DOS prompt or VS Code window to pick up the new changes.

### Create or replace these variables

|Variable Name |Value                                                          |
|--------------|---------------------------------------------------------------|
|SPARK_HOME    |C:\Users\YOU\hwe\Lib\site-packages\pyspark                     |
|PYSPARK_PYTHON|C:\Users\YOU\AppData\Local\Programs\Python\Python310\python.exe|
|HADOOP_HOME   |C:\Users\YOU\winutils\hadoop-3.2.0                             |
|JAVA_HOME     |C:\Program Files\Zulu\zulu-8                                   |

### Append these entries to your Path
Find the `Path` environment variable, click `Edit`, and click `New` to add 2 entries:

|New Path Entries                                            |
|------------------------------------------------------------|
|C:\Users\YOU\AppData\Local\Programs\Python\Python310        |
|C:\Users\YOU\AppData\Local\Programs\Python\Python310\Scripts|

## Setting up a virtual environment

All commands below should be executed from a DOS command prompt:

```
cd C:\Users\YOU
pip install virtualenv
python -m virtualenv hwe
hwe\Scripts\activate
cd hwe-labs
pip install -r resources/requirements.txt
```

Note: The last step will take several minutes - pyspark is a large download with a lot of dependencies.

## Configure VS Code to use your virtual environment

Open VS Code, Select `File\Open Folder`, navigate to your `C:\Users\YOU` directory, click once on `hwe-labs` to highlight it (don't double click to enter it!), then click the `Select Folder` button.

On the left side explorer panel, double click on `week1\spark_installation_test.py`.

In the bottom right corner, next to the word `Python`, it should say something like `3.10.11 64-bit`. Change the interpreter to the one located in your virtual environment by doing the following:

* Click on the text box with `3.10.11 64-bit`
* Click on the text box saying `+ Enter Interpreter Path`
* Click on the text box saying `Find...`
* Browse your file system to find `C:\Users\YOU\hwe\Scripts`
* Click once to highlight (but don't double click!) `python` (it should have an icon of a DOS prompt)
* Click `Select Interpreter` to choose that executable

## Test your environment

Click the triangle/play near the top right corner of your editor to execute the script. If everything is sucessful, you should see a congratulatory message.

Note: It is common to see lines that look like the ones below at the end of your output. You will see them often throughout the course, but they can be ignored and do not indicate any problems with your code.

```
SUCCESS: The process with PID 10068 (child process of PID 19344) has been terminated.
SUCCESS: The process with PID 19344 (child process of PID 9988) has been terminated.
SUCCESS: The process with PID 9988 (child process of PID 12832) has been terminated.
```
