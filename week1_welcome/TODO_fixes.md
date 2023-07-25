# Issues I have found running in Windows

## Issue 1: Error message that pops up the first time an executable is run:

This only seems to happen the very first time you run an executable in VS Code. Obnoxious but probably not a show stopper;
```
PS C:\Users\tsago\hwe-labs> & c:/Users/tsago/hwe/Scripts/Activate.ps1
& : File C:\Users\tsago\hwe\Scripts\Activate.ps1 cannot be loaded because running scripts is disabled on 
this system. For more information, see about_Execution_Policies at      
https:/go.microsoft.com/fwlink/?LinkID=135170.
At line:1 char:3
+ & c:/Users/tsago/hwe/Scripts/Activate.ps1
+   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : SecurityError: (:) [], PSSecurityException
    + FullyQualifiedErrorId : UnauthorizedAccess
```

## Issue 2: Ignorable error about not being able to delete a temporary directory

It appears Spark creates a temporary directory during execution it is unable to delete upon cleanup. This is obnoxious because it throws a big ugly stack trace which makes it look like the program failed. There is probably a way to set this directory to something else which will require additional config but prevent this.

```
PS C:\Users\tsago\hwe-labs> 23/07/10 13:37:47 ERROR ShutdownHookManager: Exception while deleting Spark temp dir: C:\Users\tsago\AppData\Local\Temp\spark-bdc8ff46-16c1-49e0-a36c-93cad3fc8e67\pyspark-1bad4816-6e3d-4eb2-9814-56ae374d9e51
java.nio.file.NoSuchFileException: C:\Users\tsago\AppData\Local\Temp\spark-bdc8ff46-16c1-49e0-a36c-93cad3fc8e67\pyspark-1bad4816-6e3d-4eb2-9814-56ae374d9e51
```

## Issue 3: Ugly/unnecessary log lines

These make the output ugly/harder to read, but also don't impact execution.

```
SUCCESS: The process with PID 21332 (child process of PID 20460) has been terminated.
SUCCESS: The process with PID 20460 (child process of PID 8020) has been terminated.
SUCCESS: The process with PID 8020 (child process of PID 12296) has been terminated.
```
