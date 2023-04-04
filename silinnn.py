from selenium import webdriver
from telegram import Update
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
import time

options = webdriver.ChromeOptions()

options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(
    service= Service('C:\\Program Files (x86)\\chromedriver.exe'), 
    options=options,
)

try:
    driver.get('https://imkon.uz/weather')
    time.sleep(10)
    site_html = driver.page_source
    soup = BeautifulSoup(site_html, 'html.parser')
    currencies = soup.find(class_ = "text-xs text-white-600 mb-1")
    print(currencies.text.strip())
    print(soup.find(class_ = "font-medium text-15 color-white mt-4").text)
    print(soup.find(
        class_ = "today-degree__amount text-[80px] md:text-[96px] text-white py-9 relative").text.strip())
except Exception as ex:
    print(ex)
finally:    
    driver.close()
    driver.quit()
    pass










