# Mac Setup Instructions

Note: It is possible you already have other/more recent versions of Python and Java already on your computer (Java 1.8 came out in 2014!). However, it is very important to have exactly these versions: lots of data engineering projects were built off of Java 1.8, and you will encounter lots of errors (some obvious, some tricky) if your versions of Java, Python, and AWS libraries are not correctly in sync!

> NOTE: these instructions are written for the OS-default `zsh` shell - if you've replaced it with another, it's assumed you're knowledgeable enough to make the necessary adjustments. Reach out if there are any issues.

## Installing Homebrew

Homebrew is a package manager for macOS that we'll be using to streamline setting up our dev environment.

In a new terminal window, run:

```zsh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

You will be asked for your password and then will need to press `Enter` when prompted to continue the installation. This may take a while, especially if you haven't previously installed tools such as Xcode.

Once it's complete, run these two commands to make Homebrew accessible in future shell sessions:

```bash
echo 'eval $(/opt/homebrew/bin/brew shellenv)' >> ~/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"
```

## Enable `homebrew/cask-versions` tap

We'll need to access cask-versions in order to install specific versions of Python and Java:

```zsh
brew tap homebrew/cask-versions
```

## Installing prerequisites (M-series Macs only)

If you are on an Intel Mac, skip this step.

If you are on an M-series Mac (with an M1/M2 chip or any of their variants), you will need to install Rosetta 2 for Java 8 to work on your computer:
```zsh
sudo softwareupdate --install-rosetta
```

You'll need to provide your password and enter `A` to accept the terms and conditions.

## Installing packages

We need to install Java, Python (macOS ships with Python preinstalled, but it's probably not the version we need, so we need to explicitly grab Python 3.10), Visual Studio Code (our IDE), and a virtual environment manager. We'll use Homebrew to make that easy:

```zsh
brew install python@3.10 temurin8 visual-studio-code virtualenvwrapper 
```

Once the necessary software is installed, we'll need to add a step to our shell's rc file in order to easily manage our virtual environment:

```bash
echo "source virtualenvwrapper.sh" >> ~/.zshrc
source ~/.zshrc
```

## Git Bash

`cd` to the directory where you'd like to keep your code for the course (the default home directory is fine) and clone the HwE Labs repo:

```zsh
git clone https://github.com/1904labs/hwe-labs.git
```

Next, move into the repo's root directory:

```zsh
cd hwe-labs
```

## Setting up a virtual environment

Finally, create the virtual environment we'll use for the course (from within the `hwe-labs` root directory):

```zsh
mkvirtualenv -a . -r resources/requirements.txt -p python3.10 hwe
```

Once this step is complete, your `hwe` virtual environment will be set up and activated.

## Verifying package versions

#### Java
To get the version of the active Java installation, run `java -version`. You should receive a message indicating an OpenJDK instance of Java 1.8 is in use, looking something like this:

```zsh
openjdk version "1.8.0_382"
OpenJDK Runtime Environment (Temurin)(build 1.8.0_382-b05)
OpenJDK 64-Bit Server VM (Temurin)(build 25.382-b05, mixed mode)
```

#### Python
To get the version of the active Python installation, run `python --version` or `python3 --version` (both should be symlinked to the virtual environment's Python executable). You should receive a message indicating version 3.10.12 of Python is in use:

```zsh
Python 3.10.12
```

If you see another version for either package or get an error message, make sure that your `hwe` virtual environment is activated and try again:

```zsh
workon hwe
```

## Configure VS Code

In the bar on the far left side of the VS Code window, you should see an Explorer icon that looks like this: 

![Alt text](<resources/explore.png>)

Click it to open the Explorer pane, then click the blue `Open Folder` button.

![Alt text](<resources/open_folder.png>)

Navigate to the directory where you cloned the HwE Labs repo, click on the `hwe-labs` folder to highlight it, then click the `Open` button.

> Note: if you get a popup about trusting the authors of the files in the opened folder, click `Yes, I trust the authors`.

### Install the Python extension
In the bar on the far left of the VS Code window, you should see an Extensions icon that looks like this:

![Alt text](<resources/extensions.png>)

Click it to open the Extensions pane. At the top of the list of extensions available to install, you should see the Python extension:

![Alt text](<resources/python.png>)

Click install.

### Use your virtual environment's interpreter

Go back to the Explorer panel and click on the `week1_welcome` folder, then on `spark_installation_test.py`.

In the bottom right corner, next to the word `Python`, it should say something like `3.11.4 64-bit`:

![Alt text](<resources/python_version.png>)

Change the interpreter to the one located in your virtual environment by doing the following:

* Click on `3.11.4 64-bit` (or whatever version you see in the taskbar)
* A "Select Interpreter" box will appear at the top of the window, and an option should be listed that looks something like `Python 3.10.12 ('hwe')`:
  ![Alt text](<resources/interpreters.png>)
* Click the `hwe` virtual environment option indicated.

## Test your environment

Click the triangle/play button near the top right corner of your editor to run the script:

![Alt text](<resources/run.png>)

If everything is successful, you should see a congratulatory message. This may take a little while.