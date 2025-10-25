import os
import tempfile

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(scope="function")
def driver():
    browser = "chrome"

    if browser == "firefox":
        options = FirefoxOptions()
        # options.add_argument("-headless")
        profile_dir = tempfile.mkdtemp()
        options.profile = profile_dir
        service = FirefoxService(executable_path=GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=options)
    elif browser == "chrome":
        options = ChromeOptions()
        options.add_argument("--incognito")
        # options.add_argument("--headless") # Ejecuta Chrome sin UI
        # options.add_argument("--no-sandbox") # Desactiva el sandboxing de chrome
        # options.add_argument("--disable-dev-shm-usage") # Desactiva el uso compartido de memoria en dispositivos con poca memoria
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)

    # driver.maximize_window()
    yield driver
    driver.quit()
