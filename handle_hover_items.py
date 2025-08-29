from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
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

# ok from here

popup_banner = wait.until(EC.presence_of_element_located(
    (By.XPATH, '//*[@id="headlessui-dialog-:r2a:"]/div/div[2]/div/div[2]')  
))
popup_banner.click()

menu_item = wait.until(EC.presence_of_element_located(
    (By.XPATH, '//*[@id="mega-menu-full"]/ul/li[10]/div/a')
))

# Hover over the menu
actions = ActionChains(driver)
actions.move_to_element(menu_item).perform()
time.sleep(2)

# Now locate a submenu item

submenu_item = wait.until(EC.element_to_be_clickable((
    By.XPATH, "//a[text()='Saree']"
)))
submenu_item.click()

print("✅ Hover and submenu click successful!")
time.sleep(10)
driver.quit()
