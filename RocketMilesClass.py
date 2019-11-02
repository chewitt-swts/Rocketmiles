from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains as action
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait

class RocketMiles:

    # Creating up our Selenium Webdriver settings for use in all test cases.
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        #self.chrome_options.add_argument('-incognito')
        self.chrome_options.add_argument('--disable-notifications')
        self.chrome_options.add_argument('--disable-popup-blocking')
        self.driver = webdriver.Chrome(r'/home/helkirien/Drivers/chromedriver', options=self.chrome_options)

#Creating a method to open the Rocketmiles website.
    def open_rocketMiles(self):
        self.driver.get('http://www.rocketmiles.com')

#Creating a method to close a browser at the end of a test.
    def close_browser(self):
        self.driver.quit()

#TODO finish creating a method to close out of the sign up popup that sometimes appears on Main Page. When complete and integrated into test cases, add the incognito argument back to the init ChromeOptions section.
    def close_popUp(self):
        self.driver.find_element_by_css_selector('#new-sign-up-modal > div > div.modal-header > button')

#Creating a method to select the destination field for TCID 1.
    def select_destination_field(self):
        destination = wait(self.driver, 20).until(EC.element_to_be_clickable((By.NAME, 'locationSearch')))
        destination.click()

#Creating a method to type "Los Angeles" into the destination field for TCID 1.
    def type_destination(self):
        action(self.driver).send_keys('Los Angeles').perform()
        time.sleep(2)
        action(self.driver).send_keys(Keys.ARROW_DOWN, Keys.ENTER).perform()

#Creating a method to click on the 1st listing in the destination field's dropdown menu after executing type_destination for TCID 1.
    def click_destination(self):
        dropdownOption1 = wait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, 'typeahead-49-923-option-0')))

#Creating a method to select the rewards program field for TCID 2.
    def select_rewards(self):
        rewards = wait(self.driver, 20).until(EC.element_to_be_clickable((By.NAME, 'programAutosuggest')))
        rewards.click()

#Creating a method to type "United MileagePlus" into the rewards field for TCID 2.
    def type_rewards(self):
        action(self.driver).send_keys('United MileagePlus').perform()



