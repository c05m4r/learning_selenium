import os
from pathlib import Path

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from helpers.ddt import DDTHelper
from pages.saucedemo.login.login_page import LoginPage

DATA_PATH = "data/saucedemo/data.json"
ddt = DDTHelper(DATA_PATH)
data = ddt.get_json_data_by_testid("login")

# @pytest.mark.login
@pytest.mark.skip
@pytest.mark.saucedemo
@pytest.mark.parametrize("case", data)
def test_login(case, driver):
    base_url = case["base_url"]
    username = case["username"]
    password = case["password"]
    dashboard_title = case["dashboard_title"]
    tc_status = case["tc_status"]

    if isinstance(tc_status, str) and tc_status.lower() == "skip":
        pytest.skip("skipped")

    driver.get(base_url)

    login_page = LoginPage(driver)
    login_page.login(username, password)

    assert driver.title == dashboard_title
