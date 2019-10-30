from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains as action
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


import time
import random

driver = webdriver.Chrome(r'/home/helkirien/Drivers/chromedriver')

driver.get('http://rocketmiles.com')