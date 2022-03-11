from selenium import webdriver
import time

chrome_driver_path = r"C:\Users\kosht\OneDrive\Desktop\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(by="id", value="cookie")
upgrades_id = ["buyTime machine", "buyPortal", "buyAlchemy lab", "buyShipment", "buyMine", "buyFactory", "buyGrandma",
               "buyCursor"]

iterations = 1
total_timeout = time.time() + (60 * 5)

while time.time() <= total_timeout:
    for _ in range(iterations):
        cookie.click()

    for upgrade_id in upgrades_id:
        try:
            driver.find_element_by_id(upgrade_id).click()
        except:
            continue

    iterations += 10

cps = driver.find_element_by_id("cps").text
print(cps)

driver.quit()



