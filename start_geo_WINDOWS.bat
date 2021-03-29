echo "Starting environment geo ..."

@ECHO OFF

@echo ~dp0= %~dp0
 
if exist "%USERPROFILE%"\Anaconda3\Scripts\activate.bat (call "%USERPROFILE%"\anaconda3\Scripts\activate.bat) else (call C:\ProgramData\Anaconda3\Scripts\activate.bat)

call conda activate geo && (
	call cd %~dp0
	call jupyter notebook
	pause
) || (
  echo "Error: Please add Anaconda to the environment variables!"
)