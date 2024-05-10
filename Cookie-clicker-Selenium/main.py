from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.ID, "cookie")
five_sec = time.time() + 5
five_min = time.time() + 60*5
store = driver.find_elements(By.CSS_SELECTOR, value="#store div")
items_id = [item.get_attribute("id") for item in store]
