to create environment : 
PS C:\Users\zaina\PythonRevision> python -m venv venv
PS C:\Users\zaina\PythonRevision> .\venv\Scripts\Activate

second approach to activate it is : 
PS C:\Users\zaina\PythonRevision> python -m venv venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
PS C:\Users\zaina\PythonRevision> .\venv\Scripts\Activate
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Bypass