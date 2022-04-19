from random import random
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
from urllib.parse import quote
import time, random

options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
user_ag = UserAgent().random
options.add_argument('user-agent=%s'%user_ag)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("prefs", {"prfile.managed_default_content_setting.images": 2})
driver = webdriver.Chrome(r'./chromedriver', options=options)

driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source" :
            """
            Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
            })
            """
})
wait = WebDriverWait(driver, 5)
url = 'https://login.taobao.com/member/login.jhtml?style=miniall&newMini2=true&full_redirect=true&from=worldlogin&redirectURL=https://world.taobao.com'
driver.get(url=url)

check = False

while check:
    check = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#fm-login-id")))
    time.sleep(3)

time.sleep(100)

driver.execute_script("document.querySelector('#fm-login-id').value = '" + id + "';")
driver.execute_script("document.querySelector('#fm-login-password').value = '" + pw + "';")
driver.execute_script("document.querySelector('.password-login').click();")