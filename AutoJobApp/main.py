from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
from dotenv import load_dotenv
import time
load_dotenv()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3924223523&distance=25&f_AL=true&geoId=102257491"
           "&keywords=python%20developer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true")
# Clicking Sign in button
driver.find_element(By.XPATH, "/html/body/div[1]/header/nav/div/a[2]").click()

time.sleep(10)
#Email
email_box = driver.find_element(By.XPATH, value="//*[@id='username']")
email_box.send_keys(os.getenv("EMAIL"), Keys.ENTER)
#Password
password_box = driver.find_element(By.XPATH, value="//*[@id='password']")
password_box.send_keys(os.getenv("PASSWORD"), Keys.ENTER)