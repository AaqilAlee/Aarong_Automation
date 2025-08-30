from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup
service = Service(r"F:\drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.aarong.com/bgd")  # Aarong site
driver.maximize_window()

wait = WebDriverWait(driver, 10)

# Wait until menu is visible (use a stable locator, not li[10])

close_btn = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div/main/div/div/div/div/div/div/button'))
)
close_btn.click()


popup_banner = wait.until(EC.presence_of_element_located(
    (By.XPATH, '//*[@id="headlessui-dialog-:r2a:"]/div/div[2]/div/div[2]')
))
popup_banner.click()

search_product = wait.until(EC.presence_of_element_located(
    (By.XPATH, '/html/body/div/header[2]/div/div/div/div[1]/div[2]/div[1]/input')
))
search_product.send_keys("Gold" + Keys.RETURN)


print("✅ Hover and submenu click successful!")
time.sleep(10)
driver.quit()
