@echo off

for /L %%i in (950, 1, 8010) do (
    echo %%i
    rem timeout 1
    python gather_issues.py single %%i
    ping 127.0.0.1 -n 2 > nul
)
