import time
from dataclasses import dataclass
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

# Set up the webdriver
service = Service("./chromedriver.exe")
options = ChromeOptions()
browser = Chrome(service=service, options=options)

# options.headless = True

# Go to the website
browser.get("http://localhost:5555/iss-sim.spacex.com")


class ElementIDs:
    roll = "roll"
    pitch = "pitch"
    yaw = "yaw"


class UnitStrings:
    angle = "°"
    angular_rate = "°/s"


def parse_angle(s: str) -> float:
    return float(s.replace(UnitStrings.angle, ""))


def parse_rate(s: str) -> float:
    return float(s.replace(UnitStrings.angular_rate, ""))


def get_error(webelement: WebElement) -> float:
    value: str = webelement.find_element(By.CSS_SELECTOR, ".error").text
    return parse_angle(value)


def get_rate(webelement: WebElement) -> float:
    value: str = webelement.find_element(By.CSS_SELECTOR, ".rate").text
    return parse_rate(value)


def get_webelement(browser: WebDriver, element_id: str) -> WebElement:
    return browser.find_element(By.ID, element_id)


# Find the roll web element:
roll_id = (By.ID, "roll")
roll_error_selector = (By.ID, "roll")
roll_webelement = browser.find_element(*roll_id)
roll_value = roll_webelement.find_element(By.CSS_SELECTOR, ".error").text


