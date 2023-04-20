from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()), options=options)
url = 'https://www.poshantracker.in/'
driver.get(url)

elements = driver.find_elements(By.NAME, 'home_faq_sect')
for title in elements:
    heading = title.find_element(By.NAME, 'tab-content').text
    print(heading)

#tab-content
