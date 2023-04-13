from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import json
import pymysql
from selenium.webdriver.common.alert import Alert
import time
import pymysql
import random

option = Options()
option.add_argument("disable-infobars")
option.add_argument("disable-extensions")
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1309.0 Safari/537.17"
option.add_argument('user-agent=' + user_agent)
option.add_argument('disable-gpu')
option.add_argument('incognito')
# option.add_argument('headless')
s = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=s, options=option)
browser.get("https://naver.com")
browser.find_element(By.CSS_SELECTOR, "#query").send_keys("코로나")
browser.find_element(By.CSS_SELECTOR, "#query").send_keys(Keys.ENTER)
a = browser.find_element(By.CSS_SELECTOR, "#main_pack > section.sc_new.sp_nsite._project_site_channel_root._section_nsite_._sp_ntotal._prs_vsd_bas > div > div").text
print(a)
b = browser.find_elements(By.CLASS_NAME, "bx")
for n in b :
    print(n.text)

while True:
    pass
