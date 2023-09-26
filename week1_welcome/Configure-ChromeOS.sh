#! /bin/bash
#SYNOPSIS
#Automates many parts of the HWE ChromeOS development environment setup.

#DESCRIPTION
#Automates many parts of the HWE ChromeOS development environment setup. The main steps include:
#- Ensuring Java version 1.8.* is installed along with having the JAVA_HOME env variable set
#- Creating a Python virtual environment via Python's pip
#- Download HWE course Python dependencies like Pyspark
#- Configuring additional env variables for Python, Spark, etc

#PARAMETER None

#EXAMPLE
#Assuming you trust this script execute it as below:
# cd <same-directory-as-this-script>
# bash ./Configure-ChromeOS.sh

#
RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color

# Side load Java 8.
install_java() {
   # This is for debian.
   echo "Installing Java 8"
   sudo apt update
   wget https://builds.openlogic.com/downloadJDK/openlogic-openjdk/8u382-b05/openlogic-openjdk-8u382-b05-linux-x64-deb.deb
   sudo dpkg -i ./openlogic-openjdk-8u382-b05-linux-x64-deb.deb
   sudo apt --fix-broken -y install 
   rm ./openlogic-openjdk-8u382-b05-linux-x64-deb.deb
   sudo update-alternatives --set java /usr/lib/jvm/openlogic-openjdk-8-hotspot-amd64/bin/java
   whichJava=$(which java)
   if [ -z $whichJava ]
   then
     echo -e "${RED}Something bad happened and could not install Java 8"
     echo -e "Contact your instructor for troubleshooting.${NC}"
     exit
   fi
}


# Test that we run in the correct location, we will use the requirements.txt file as the test
if [ ! -f "../resources/requirements.txt" ]
then
    echo "== Did not find expected resource file at ..\resources\requirements.txt. " 
    echo -e "${RED}Verify you are executing this script at the correct location, exiting... ${NC}"
    exit
fi

# Install java if it is not in the path.
whichJava=$(which java)
if [ -z $whichJava ]
then
   install_java
fi

# Install java if the version isn't right.
versionJava=$(java -version 2>&1)
echo $versionJava
if [[ $versionJava =~ 1.8. ]];
then
   echo "Correct Java version in the path."
else
   echo "Not the right version of Java, trying to fix."
   install_java
   versionJava=$(java -version)
   echo $versionJava
   if [[ $versionJava =~ 1.8. ]];
   then
      echo -e "${RED} Java 8 doesn't seem to be installed.${NC}"
      exit
   fi
fi

# Check to see if the JAVA_HOME directory is set.
javaHome=$JAVA_HOME
if [ -z $javaHome ]
then
   echo -e "${RED}== JAVA_HOME env variable not set.  Please set it to the Java 8 home."
   echo -e "Should be one of these in /usr/lib/jvm${NC}"
   ls /usr/lib/jvm
   exit
else
   versionJava=$(${JAVA_HOME}/bin/java -version 2>&1)
   if [[ $versionJava =~ 1.8. ]];
   then
      echo "Correct Java version in JAVA_HOME."
   else
      echo -e "${RED}== Incorrect version of Java in JAVA_HOME."
      echo -e "Should be one of these in /usr/lib/jvm${NC}"
      ls /usr/lib/jvm
   fi
fi

# Setup side-loaded Python using Miniconda.
virtualEnv=${HOME}/miniconda3/envs/hwe
if [ ! -d $virtualEnv ];
then
   echo "Virtual environment does not exist.  Creating."
   wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
   bash Miniconda3-latest-Linux-x86_64.sh
   source ~/.bashrc
   conda create --name hwe
   conda activate hwe
   conda install python=3.10
   python -m pip install -r ../resources/requirements.txt
   rm Miniconda3-latest-Linux-x86_64.sh
else
   conda activate hwe
fi

echo -e "${GREEN}==============================================" 
echo -e "== Completed -- all checks passed -- YOU ARE GOOD!${NC}" 
