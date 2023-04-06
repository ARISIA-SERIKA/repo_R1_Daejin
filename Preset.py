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

while True:
    pass
