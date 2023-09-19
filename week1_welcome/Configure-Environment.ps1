<#
.SYNOPSIS
Automates many parts of the HWE Windows development environment setup.

.DESCRIPTION
Automates many parts of the HWE Windows development environment setup. The main steps include:
- Cloning Hadoop binaries for Windows and setting up HADOOP_HOME env variable
- Ensuring Java version 1.8.* is installed along with having the JAVA_HOME env variable set
- Creating a Python virtual environment via Python's pip
- Download HWE course Python dependencies like Pyspark
- Configuring additional env variables for Python, Spark, etc

.PARAMETER None

.EXAMPLE
Assuming you trust this script, you will need to execute it by bypassing the default Powershell execution policy.  Here are the command line steps below:
cd <same-directory-as-this-script>
powershell.exe -ExecutionPolicy Bypass -File Configure-Environment.ps1

#>


# Test that we run in the correct location, we will use the requirements.txt file as the test
if (-Not (Test-Path ..\resources\requirements.txt))
{
    Write-Host "== Did not find expected resource file at ..\resources\requirements.txt. " + "Verify you are executing this script at the correct location, exiting..." -ForegroundColor Red
    return
}

# If we don't find the 'winutils' directory, it hasnt been setup yet
$winutilsPath = "$env:USERPROFILE\.winutils"
if (Test-Path $winutilsPath) {
    # already there
    Write-Host "== Winutils folder already exists, continuing..." -ForegroundColor Green
} else {
    # not there, so go get it
    Write-Host "== Cloning winutils repository to $winutilsPath..."
    git clone https://github.com/cdarlint/winutils $winutilsPath
    Write-Host "== Cloning winutils completed" -ForegroundColor Green
}

# check the hadoop version you are using is where its expected
$hadoopHome = "$winutilsPath\hadoop-3.2.0"
if (-Not (Test-Path $hadoopHome)) {
    # otherwise we are done
    Write-Host "== hadoop-3.2.0 sub folder didnt exist at '$hadoopHome', exiting..."
    return
}
[Environment]::SetEnvironmentVariable("HADOOP_HOME", $hadoopHome, [EnvironmentVariableTarget]::User)
Write-Host "== Set HADOOP_HOME env variable to '$hadoopHome'" -ForegroundColor Green

$javaHome = $env:JAVA_HOME
if (($null -eq $javaHome) -or ($javaHome -eq ""))
{
    Write-Host "== JAVA_HOME env variable not set. Attempt running installer " + `
            "with 'Set JAVA_HOME variable' option set, exiting..." -ForegroundColor Red
    return
} elseif (-Not (Test-Path $javaHome)) {
    Write-Host "== Java install didnt exist at env variable JAVA_HOME = '$javaHome', exiting..." -ForegroundColor Red
    return
} else {
    Write-Host "== Found JAVA_HOME env variable set to '$javaHome'" -ForegroundColor Green

    # look for the expected Java version
    $javaVersion = java.exe -version 2>&1 | %{ "$_" }
    $javaVersion -join "`r`n" | Out-String
    if (-Not ([bool]($javaVersion -match "`"1.8.")))
    {
        Write-Host "== Java version doesnt report '1.8.*', exiting..." -ForegroundColor Red
        return
    }
    else {
        Write-Host "== Java version reports '1.8.*'" -ForegroundColor Green
    }
}

$virtualEnv = "$env:USERPROFILE\.hwe_venv" 
if (Test-Path $virtualEnv)
{
    . $virtualEnv\Scripts\activate.ps1
    Write-Host "== Found Python virtual environment at '$virtualEnv', activated" -ForegroundColor Green
} else {
    Write-Host "== Creating Python virtual environment..."
    python.exe -m pip install --upgrade pip
    python -m pip install virtualenv
    python -m virtualenv $virtualEnv
    . $virtualEnv\Scripts\activate.ps1
    Write-Host "== Created and activated Python virtual environment at '$virtualEnv'" -ForegroundColor Green
}

Write-Host "== Installing Python dependencies (NOTE: this could take a while)..."
python -m pip install -r ..\resources\requirements.txt

$pysparkPython = "$env:USERPROFILE\AppData\Local\Programs\Python\Python310\python.exe"
if (-Not (Test-Path $pysparkPython)) {
    # otherwise we are done
    Write-Host "== PYSPARK_PYTHON install didnt exist at '$pysparkPython', exiting..." -ForegroundColor Red
    return
}
[Environment]::SetEnvironmentVariable("PYSPARK_PYTHON", $pysparkPython, [EnvironmentVariableTarget]::User)
Write-Host "== Set PYSPARK_PYTHON env variable to '$pysparkPython'" -ForegroundColor Green

$sparkHome = "$virtualEnv\Lib\site-packages\pyspark"
if (-Not (Test-Path $sparkHome)) {
    # otherwise we are done
    Write-Host "== SPARK_HOME install didnt exist at '$sparkHome', exiting..." -ForegroundColor Red
    return
}
[Environment]::SetEnvironmentVariable("SPARK_HOME", $sparkHome, [EnvironmentVariableTarget]::User)
Write-Host "== Set SPARK_HOME env variable to '$sparkHome'" -ForegroundColor Green

# check and add missing items to PATH variable
$pathItems = @("$env:USERPROFILE\AppData\Local\Programs\Python\Python310", `
                "$env:USERPROFILE\AppData\Local\Programs\Python\Python310\Scripts", `
                "$hadoopHome\bin")
foreach ($pathItem in $pathItems) {
    if (-Not (Test-Path $pathItem))
    {
        Write-Host "== PATH item didnt exist at '$pathItem', exiting..." -ForegroundColor Red
        return
    }

    if (-Not ($env:PATH -contains $pathItem))
    {
        $env:Path += ';$pathItem'
        Write-Host "== Added '$pathItem' to PATH env variable" -ForegroundColor Green
    } else {
        Write-Host "== Found '$pathItem' in PATH env variable" -ForegroundColor Green
    }

}

Write-Host "==============================================" -ForegroundColor Green
Write-Host "== Completed -- all checks passed -- YOU GOOD!" -ForegroundColor Green
