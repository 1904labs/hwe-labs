<#
.SYNOPSIS
Downloads the 'winutils' repo needed to run Hadoop on Windows, as well as configures the HADOOP_HOME environment 
variable.

.DESCRIPTION
This function checks if the winutils folder exists and if it does not, clones the winutils repository from GitHub.
It then determines the absolute path to the highest versioned subfolder within the winutils folder and sets the
HADOOP_HOME environment variable to this path. If the HADOOP_HOME environment variable does not exist, it is created.
Next, it checks for the presence of a local .gitignore file and if it does not exist, creates it. Finally, it checks
the contents of the .gitignore file and adds 'winutils' to it if it is not already present, and then runs 'git add'
on the .gitignore file.

.PARAMETER None

.EXAMPLE
Assuming you trust this script, you will need to run the script via an ELEVATED command line
and possibly bypass the default Powershell execution policy.  Here are the command line steps below:
cd <same-directory-as-this-script>
powershell.exe -ExecutionPolicy Bypass -File Configure-Hadoop.ps1

#>

$currentPrincipal = New-Object Security.Principal.WindowsPrincipal([Security.Principal.WindowsIdentity]::GetCurrent())
if (-Not ($currentPrincipal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator))) {
    Write-Host "== This script needs to run under admin level to set environment variables, exiting..."
    return
}

# If we don't find the 'winutils' directory, assume it hasnt been setup yet and proceed.
$winutilsPath = "$env:USERPROFILE\.winutils"
if (Test-Path $winutilsPath) {
    # otherwise we are done
    Write-Host "== Winutils folder already exists, exiting..."
    return
}

Write-Host "== Cloning winutils repository to $winutilsPath..."
git clone https://github.com/cdarlint/winutils $winutilsPath

## find the highest versioned hadoop install in winutils
$hadoopHome = "$winutilsPath\hadoop-3.2.0"
if (-Not (Test-Path $hadoopHome)) {
    # otherwise we are done
    Write-Host "== hadoop-3.2.0 sub folder didnt exist at '$hadoopHome', exiting..."
    return
}
                

[Environment]::SetEnvironmentVariable("HADOOP_HOME", $hadoopHome, [EnvironmentVariableTarget]::Machine)
Write-Host "== Set HADOOP_HOME variable to '$hadoopHome'"

$javaHome = "C:\Program Files\Java\jre1.8.0_361"
if (-Not (Test-Path $javaHome)) {
    # otherwise we are done
    Write-Host "== Java install didnt exist at '$javaHome', exiting..."
    return
}
[Environment]::SetEnvironmentVariable("JAVA_HOME", $javaHome, [EnvironmentVariableTarget]::Machine)
Write-Host "== Set JAVA_HOME variable to '$javaHome'"

$pysparkPython = "$env:USERPROFILE\AppData\Local\Programs\Python\Python310\python.exe"
if (-Not (Test-Path $pysparkPython)) {
    # otherwise we are done
    Write-Host "== PYSPARK_PYTHON install didnt exist at '$pysparkPython', exiting..."
    return
}
[Environment]::SetEnvironmentVariable("PYSPARK_PYTHON", $pysparkPython, [EnvironmentVariableTarget]::Machine)
Write-Host "== Set PYSPARK_PYTHON variable to '$pysparkPython'"

# SPARK_HOME	C:\Users\YOU\hwe\Lib\site-packages\pyspark
# PYSPARK_PYTHON	C:\Users\YOU\AppData\Local\Programs\Python\Python310\python.exe

#
## Now that we added another git repo in our existing repo, we want to make sure
## our existing repo doesnt try to claim these files.  We do this by telling
## our existing repo to ignore the new winutils folder.
#$gitIgnorePath = "$PSScriptRoot\.gitignore"
#if (-not (Test-Path $gitIgnorePath)) {
#    Write-Host "Creating .gitignore file..."
#    New-Item $gitIgnorePath -ItemType File
#}
#
#$gitIgnoreVal = 'winutils/'
#$gitIgnoreContent = Get-Content $gitIgnorePath -Raw
#if (-not ($gitIgnoreContent -match $gitIgnoreVal)) {
#    Write-Host "Adding 'winutils' to .gitignore..."
#    Add-Content $gitIgnorePath $gitIgnoreVal
#    git add $gitIgnorePath
#}
#
#Write-Host "Don't forget to restart IntelliJ so the added/updated environment variable value is loaded in the IDE."
#
#