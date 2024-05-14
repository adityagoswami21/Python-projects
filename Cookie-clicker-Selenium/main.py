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
store = driver.find_elements(By.CSS_SELECTOR, value="#store div")[:-1]
items_id = [item.get_attribute("id") for item in store]
print(items_id)
while True:
    cookie.click()
    if time.time() > five_sec:
        score = driver.find_element(By.ID, value="money").text
        if "," in score:
            score = score.replace(",", "")
        int_score = int(score)
        # print(int_score)

        cost_of_upgrades = []
        for upgrade in driver.find_elements(By.CSS_SELECTOR, value="#store div b")[:-1]:
            upgrade_text = upgrade.text
            upgrade_price = int(upgrade_text.split("-")[1].strip().replace(",", ""))
            # print(upgrade_price)
            cost_of_upgrades.append(upgrade_price)
        # print(cost_of_upgrades)

        cookie_upgrades = {}
        for n in range(len(cost_of_upgrades)):
            cookie_upgrades[cost_of_upgrades[n]] = items_id[n]

        affordable_upgrade = []
        for cost, iD in cookie_upgrades.items():
            if int_score > cost:
                affordable_upgrade.append(cost)
        # print(affordable_upgrade)

        highest_upgrade = max(affordable_upgrade)
        # print(f"highest_upgrade: {highest_upgrade}")
        highest_id = items_id[cost_of_upgrades.index(highest_upgrade)]
        print(f"highest_id: {highest_id}")

