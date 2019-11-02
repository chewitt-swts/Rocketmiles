from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains as action
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

from RocketMilesClass import RocketMiles

RM = RocketMiles()
EC = expected_conditions
wait = WebDriverWait

#Preconditions
RM.open_rocketMiles()

#TCID 1: Main Page - Can a user enter a destination?
RM.select_destination_field()
RM.type_destination()

#TCID 2: Main Page - Can a user enter a rewards program?
RM.select_rewards()
RM.type_rewards()




"""
driver.get('http://rocketmiles.com')
time.sleep(5)
destinationInput = driver.find_element_by_css_selector("#rm3-home-page > div.content.ng-scope > div.container-fluid.search-section.ng-scope > div:nth-child(4) > div > form > div.col-sm-6.region.search-field > gofr-location-search > div > input")
time.sleep(5)
destinationInput.click()

#PopUpClose = driver.find_element_by_css_selector("#new-sign-up-modal > div > div.modal-header > button > span.sr-only")"""