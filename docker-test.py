from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

chrome = webdriver.Remote(
    command_executor='http://localhost:4444/wd/hub',
    desired_capabilities=DesiredCapabilities.CHROME)

chrome.get('https://dev04.quantuvis.net/#/login')
print(chrome.title)  # Get Quantuvis title

chrome.quit()