import pytest
import time
import allure
from base.BaseTest import BaseTest
from pages.LoginPage import LoginPage

@allure.epic("UTC Web Application")
@allure.feature("Login Feature")
class LoginE2ETest(BaseTest):
