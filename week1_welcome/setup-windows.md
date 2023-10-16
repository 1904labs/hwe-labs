# Windows Setup Instructions

## Install Python

1. Navigate to the [V3.10.11 downloads page](https://www.python.org/downloads/release/python-31011/) and download "Windows installer (64-bit)" for 3.10.11
<br/>OR<br/>directly [download the file through this link](https://www.python.org/ftp/python/3.10.11/python-3.10.11-amd64.exe)
2. Run the executable and complete the Python installation process. Make sure "Add python.exe to PATH" is selected as an install option.
3. After completion, there is one extra step you may need to take to make sure Python is working. By default, Windows will attempt to install Python from the Windows store instead of executing your program when `python` is executed from the command line. To fix this:
1. Type `Manage app execution aliases` in the Windows search bar
2. Make sure the 2 Python options are disabled:
* "App Installer/python.exe"
* "App Installer/python3.exe"

4. To test your Python installation, open a command prompt and type "python --version". You should be greeted with a Python command line prompt matching the version you just installed.
```
c:\Users\you>python --version
3.10.11
```
Q: What if it doesnt work?
A: If you have other versions of Python installed you may see a different version of Python reported.

Attempt these remedies and return to step 4 above:
   - Uninstall other versions of Python
   - Remove conflicting PATH entries (dont forget to restart your command prompt before outputting the Python version again)

## Install Java 1.8

1. Navigate to the adoptium.net downloads page using [this link which will preconfigure the download filters](https://adoptium.net/temurin/releases/?os=windows&arch=x64&package=jdk&version=8). After navigating to the page you should see these settings selected:
    - Operating System = Windows
    - Architecture = x64
    - Package Type = JDK
    - Version = 8 - LTS

2. Download and execute the .msi Eclipse Temurin Installer with the following options set:
    - Add to PATH
    - Set JAVA_HOME variable

3. To test your Java installation, open a new command/DOS prompt (do not re-use an existing one), and type `java -version`. You should receive a message indicating an OpenJDK instance of Java 1.8 is installed.
    ```
    C:\Users\you>java -version
    openjdk version "1.8.0_382"
    OpenJDK Runtime Environment (Temurin)(build 1.8.0_382-b05)
    OpenJDK 64-Bit Server VM (Temurin)(build 25.382-b05, mixed mode)
    ```


## Git Bash
1. Navigate to the [Git-scm website Windows download page](https://git-scm.com/download/win)
2. Download the "64-bit Git for Windows Setup" installer and execute it.


## Execute Configure-Environment.ps1 Script

Using Git Bash you installed above, clone the main branch of this reposiory.

    cd <folder>
    git clone https://github.com/1904labs/hwe-labs.git
    
Next we will run a Powershell script from the command prompt which performs the following:
   - Download WinUtils: the Windows binaries for Hadoop
   - Setup environment variables using a Powershell script
   - Create a Python virtual environment
   - Install Python dependencies

   Please execute these steps from a command prompt to run the Powershell script.  Note: this script will take several minutes - pyspark is a large download with a lot of dependencies:
   1. Change directory to this folder: `cd <folder>/hwe-labs/week1_welcome`
   2. Execute the script: `powershell.exe -ExecutionPolicy Bypass -File Configure-Environment.ps1`

## Modify Powershell execution policy

Under the Default Powershell execution policy, your programs will execute successfully but the output will be hard to read. To make the output easier:
1. Open Powershell as an Adminstrator
2. Execute the following command: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned`

## Visual Studio Code

   1. Navigate to the [VS Code download page](https://code.visualstudio.com/download)
   2. Click on the Windows 10/11 download to download the .exe and run it.

## Configure VS Code to use your virtual environment

Open VS Code, Select `File\Open Folder`, navigate to your `hwe-labs` repo directory, click once on `hwe-labs` to highlight it (don't double click to enter it!), then click the `Select Folder` button.

On the left side explorer panel, double click on `week1_welcome\spark_installation_test.py`.

If you don't have the Python Extension installed, please do so by clicking on the 'Extensions' icon and install the extension from Microsoft.

In the bottom right corner, next to the word `Python`, it should say something like `3.10.11 64-bit`. Change the interpreter to the one located in your virtual environment by doing the following:

* Click on the text box with `3.10.11 64-bit` (or possibly a different version if prior Python versions have been installed)
* Click on the text box saying `+ Enter Interpreter Path`
* Click on the text box saying `Find...`
* Browse your file system to find `C:\Users\YOU\.hwe_venv\Scripts`
* Click once to highlight (but don't double click!) `python.exe` (it should have an icon of a DOS prompt)
    * Example: my path is `C:\Users\nick\.hwe_venv\Scripts\python.exe`
* Click `Select Interpreter` to choose that executable

## Test your environment

Click the triangle/play near the top right corner of your editor to execute the script. If everything is successful, you should see a congratulatory message.

Note: It is common to see lines that look like the ones below at the end of your output. You will see them often throughout the course, but they can be ignored and do not indicate any problems with your code.

```
SUCCESS: The process with PID 10068 (child process of PID 19344) has been terminated.
SUCCESS: The process with PID 19344 (child process of PID 9988) has been terminated.
SUCCESS: The process with PID 9988 (child process of PID 12832) has been terminated.
```
## Troubleshooting Winutils

On Windows, you may encounter [errors](https://stackoverflow.com/questions/45947375/why-does-starting-a-streaming-query-lead-to-exitcodeexception-exitcode-1073741) like `Error writing stream metadata StreamMetadata` or other issues writing files (usually to temp directories). 

First, validate that winutils is working correctly by navigating to the winutils bin directory and executing:

```
winutils.exe ls
```

If you get no output and the return code is non-zero, then you're probably missing [Visual Studio 2010 (VC++ 10.0) SP1](https://learn.microsoft.com/en-US/cpp/windows/latest-supported-vc-redist?view=msvc-170#visual-studio-2010-vc-100-sp1-no-longer-supported). Download and install it and check again. here. [Direct link to download page](https://www.microsoft.com/en-us/download/details.aspx?id=26999).

Why? The winutils binaries are compiled using the Visual Studio 2010 Redistributable and need it to run.
