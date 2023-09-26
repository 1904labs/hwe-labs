# ChromeOS Setup Instructions

*** CURRENTLY THIS ASSUMES YOUR CHROMEBOOK IS AMD64, NOT ARM ***

## Enable Linux Develoment Environment

Go to Settings -> Advanced -> <> Devlopers -> Linux development environment

Enable Linux with 10G or so of disk space.  Allow it to download and install.

Open a command line prompt. (Terminal -> Penguin)

## Execute Configure-Linux.sh Script

Using Git, clone the main branch of this reposiory.

    cd <folder>
    git clone https://github.com/1904labs/hwe-labs.git
    
Next we will run a shell script from the command prompt which performs the following:
   - Download and install Java 1.8
   - Create a Python virtual environment
   - Install Python dependencies

   Please execute these steps from a command prompt to run the Powershell script.  Note: this script will take several minutes - pyspark is a large download with a lot of dependencies:
   1. Change directory to this folder: `cd <folder>/hwe-labs/week1_welcome`
   2. Execute the script: `bash Configure-Linux.sh`
   3. Edit your ~/.bashrc file and add the following:
```
# Set JAVA_HOME
export JAVA_HOME=/usr/lib/jvm/openlogic-openjdk-8-hotspot-amd64
```
  4. `source ~/.bashrc`
  5. Execute the script again: `bash Configure-Linux.sh`
  6. You should see a message that all checks have passed.

## Install Java 1.8

To test your Java installation, type `java -version`. You should receive a message indicating an OpenJDK instance of Java 1.8 is installed.
```
    C:\Users\you>java -version
    openjdk version "1.8.0_382"
    OpenJDK Runtime Environment (Temurin)(build 1.8.0_382-b05)
    OpenJDK 64-Bit Server VM (Temurin)(build 25.382-b05, mixed mode)
```
If it does not, please re-run the configuration script again, and double check your JAVA_HOME variable.

## Visual Studio Code

Follow the instruction here: https://code.visualstudio.com/blogs/2020/12/03/chromebook-get-started

## Configure VS Code to use your virtual environment

Open VS Code, Select `File\Open Folder`, navigate to your `hwe-labs` repo directory, click once on `hwe-labs` to highlight it (don't double click to enter it!), then click the `Select Folder` button.

On the left side explorer panel, double click on `week1_welcome\spark_installation_test.py`.

If you don't have the Python Extension installed, please do so by clicking on the 'Extensions' icon and install the extension from Microsoft.

In the bottom right corner, next to the word `Python`, it should say something like `3.10.11 64-bit`. Change the interpreter to the one located in your virtual environment by doing the following:

* Click on the text box with `3.10.13 64-bit` (or possibly a different version if prior Python versions have been installed)
* Click on the text box saying `+ Enter Interpreter Path`
* Click on the text box saying `Find...`
* Browse your file system to find `~/miniconda3/envs/hwe/bin`
* Click once to highlight (but don't double click!) `python.exe`
* Click `Select Interpreter` to choose that executable

## Test your environment

Click the triangle/play near the top right corner of your editor to execute the script. If everything is successful, you should see a congratulatory message.

Note: It is common to see lines that look like the ones below at the end of your output. You will see them often throughout the course, but they can be ignored and do not indicate any problems with your code.

```
SUCCESS: The process with PID 10068 (child process of PID 19344) has been terminated.
SUCCESS: The process with PID 19344 (child process of PID 9988) has been terminated.
SUCCESS: The process with PID 9988 (child process of PID 12832) has been terminated.
```
