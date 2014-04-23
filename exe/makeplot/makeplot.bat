@echo off

::portable r path
set R=%CD%\..\portable-r\App\R-Portable\bin\R.exe

::"start" suppresses the CMD window
start %R% R CMD BATCH makeplot.r