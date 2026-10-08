@echo off
echo Đang chạy test...
pytest
echo.
echo Test chay xong! Dang mo Allure Report...
allure serve allure-results
pause
