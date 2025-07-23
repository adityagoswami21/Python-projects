from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import os
from dotenv import load_dotenv
import time
load_dotenv()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3928440622&f_AL=true&f_E=2&f_WT=2&geoId=102713980&keywords=python%20developer&location=India&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&spellCorrectionEnabled=true")
# Clicking Sign in button
driver.find_element(By.XPATH, "/html/body/div[1]/header/nav/div/a[2]").click()

time.sleep(5)
#Email
email_box = driver.find_element(By.XPATH, value="//*[@id='username']")
email_box.send_keys(os.getenv("EMAIL"), Keys.ENTER)
#Password
password_box = driver.find_element(By.XPATH, value="//*[@id='password']")
password_box.send_keys(os.getenv("PASSWORD"), Keys.ENTER)
first_job = driver.find_element(By.CSS_SELECTOR, value=".jobs-apply-button--top-card button")
first_job.click()
reminder_button = driver.find_element(By.CSS_SELECTOR, value=".jobs-s-apply button")
reminder_button.click()
submit_button = driver.find_element(By.CSS_SELECTOR, value="footer button").click()
# all_jobs_elmnt = driver.find_element(By.TAG_NAME, value="ul .scaffold-layout__list-container")
# for job in all_jobs_elmnt:
#     print(job)

