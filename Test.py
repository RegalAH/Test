from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime, timedelta
import time, os, glob, pandas as pd

# Input Comscore Login
username = 'aaharper'
password = '789Rh345'

# Choose Data Dumping Location
download_dir = os.getcwd()

# Set Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')  # Add this line
chrome_options.add_argument('--no-sandbox')  # Add this line
chrome_options.add_argument('--disable-dev-shm-usage')  # Add this line

prefs = {
    "download.default_directory": download_dir,
    "download.prompt_for_download": False,
    "directory_upgrade": True,
    "safebrowsing.enabled": True
}
chrome_options.add_experimental_option("prefs", prefs)


service = Service(ChromeDriverManager().install())

# Initialize the driver
driver = webdriver.Chrome(service=service, options=chrome_options)

login_url = 'https://beta.boxofficeessentials.com/login'
driver.get(login_url)

WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, 'login_id'))).send_keys(username)
driver.find_element(By.NAME, 'password').send_keys(password)
driver.find_element(By.NAME, 'password').send_keys(Keys.RETURN)

WebDriverWait(driver, 10).until(EC.url_changes(login_url))

driver.get("https://beta.boxofficeessentials.com/reports/flash/market_share_by_metro?pct_change_same_theater_or_total_gross=same_theater&pct_change_type=prev_week&day_range_rev=RANGE&day_range_rev=2024-09-09&day_range_rev=2024-09-10")

export_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'export_menu'))
)
    
export_button.click()

xlsx_export_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[@title='XLSX Export']"))
)
    
xlsx_export_button.click()

time.sleep(3)

driver.quit()