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
        self.chrome_options.add_argument('-incognito')
        self.chrome_options.add_argument("--start-maximized")
        self.chrome_options.add_argument('--disable-notifications')
        self.chrome_options.add_argument('--disable-popup-blocking')
        self.driver = webdriver.Chrome(r'/home/helkirien/Drivers/chromedriver', options=self.chrome_options)

#Creating a method to open the Rocketmiles website.
    def open_rocketMiles(self):
        try:
            self.driver.get('http://www.rocketmiles.com')
            print('Rocketmiles.com has opened successfully.')
        except Exception as err:
            print(str(err))

#Creating a helper method to reach the Search Page. This method can be called in order to independently run TCIDs 9-10, which would otherwise be dependent on running TCIDs 1-8. This URL points to a search page with our smoke test data (destination: Los Angeles, trip dates: 11/21/2019 - 11/25/2019, guests: 1, rooms: 1)
    def open_search_page(self):
        try:
            self.driver.get('https://www.rocketmiles.com/search?longitude=-118.253426&latitude=34.05219&placeId=43&query=Los%20Angeles,%20CA&source=HSS&checkIn=11%2F21%2F2019&checkOut=11%2F25%2F2019&program=united&guests=1&rooms=1&currency=USD&includePromoIneligible')
            print('Search Page loaded with smoke test data has opened successfully.')
        except Exception as err:
            print(str(err))

# Creating a helper method to reach the Hotel Details page. This method can be called in order to independently run TCIDs 11-12, which would otherwise be dependent on running TCIDs 1-10.
    def open_hotel_details(self):
        try:
            self.driver.get('https://www.rocketmiles.com/details?averagePrice=637&checkIn=11~2F21~2F2019&checkOut=11~2F25~2F2019&currency=USD&guests=1&id=45381&latitude=34.05219&longitude=-118.253426&program=united&placeId=43&query=Los%20Angeles,%20CA&rewardAmount=32000&rooms=1&source=HSS&searchId=b8b032b7-4924-4662-8013-0f9dc86a5562')
            print('Hotel Details page has opened successfully.')
        except Exception as err:
            print(str(err))

#Creating a method to close a browser at the end of a test.
    def close_browser(self):
        try:
           self.driver.quit()
           print('The browser has closed.')
        except Exception as err:
            print(str(err))

#TODO finish creating a method to close out of the sign up popup that sometimes appears on Main Page. When complete and integrated into test cases, add the incognito argument back to the init ChromeOptions section.
    def close_popUp(self):
        time.sleep(5)
        try:
            closeButton = self.driver.find_element_by_css_selector('#new-sign-up-modal > div > div.modal-header > button')
            closeButton.click()
            print('The close button for the sign up popup has been clicked.')
            time.sleep(3)
        except Exception as err:
            print(str(err))

    def close_cookie_banner(self):
        try:
            #okButton = self.driver.find_element_by_css_selector('#rm3-home-page > gofr-cookie-banner > div > div:nth-child(2) > button')
            #okButton = self.driver.find_element_by_xpath('//*[@class="btn cookie-banner-button ng-scope"]')
            okButton = wait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@class="btn cookie-banner-button ng-scope"]')))
            okButton.click()
            print('The ok button for the cookie banner has been clicked.')
        except Exception as err:
            print(str(err))

#Creating a method to select the destination field for TCID 1.
    def select_destination_field(self):
        try:
            destination = wait(self.driver, 5).until(EC.element_to_be_clickable((By.NAME, 'locationSearch')))
            destination.click()
            print('The destination field has been clicked.')
        except Exception as err:
            print(str(err))

#Creating a method to type "Los Angeles" into the destination field for TCID 1.
    def type_destination(self):
        try:
            action(self.driver).send_keys('Los Angeles').perform()
            print('The test data was typed into the destination field.')
            time.sleep(3)
            action(self.driver).send_keys(Keys.ARROW_DOWN, Keys.ENTER).perform()
            print('The first option from the destination dropdown menu was selected.')
        except Exception as err:
            print(str(err))
        #TODO create click_destination method to simulate an actual mouseclick.

#Creating a method to select the rewards program field for TCID 2.
    def select_rewards(self):
        try:
            rewards = wait(self.driver, 5).until(EC.element_to_be_clickable((By.NAME, 'programAutosuggest')))
            rewards.click()
            print('The rewards program field has been clicked.')
        except Exception as err:
            print(str(err))

#Creating a method to type "United MileagePlus" into the rewards field for TCID 2.
    def type_rewards(self):
        try:
            action(self.driver).send_keys('United MileagePlus').perform()
            print('The test data was typed into the rewards program field.')
            time.sleep(3)
            action(self.driver).send_keys(Keys.ARROW_DOWN, Keys.ENTER).perform()
            print('The first option from the rewards program dropdown menu was selected.')
        except Exception as err:
            print(str(err))
        #TODO create click_destination method to simulate an actual mouseclick.

#Creating a method to click on the end date field for TCID 3.
    def click_end_date(self):
        try:
            endDate = self.driver.find_element_by_css_selector('#rm3-home-page > div.content.ng-scope > div.container-fluid.search-section.ng-scope > div:nth-child(4) > div > form > div.booking-date-range.search-field.col-xs-12.col-sm-6 > div.checkout.booking-date')
            endDate.click()
            print('The end date field was clicked.')
        except Exception as err:
            print(str(err))
        # TODO clean up the CSS selector

#Creating a method to click on the start date field for TCID 4.
    def click_start_date(self):
        try:
            startDate = self.driver.find_element_by_css_selector('#rm3-home-page > div.content.ng-scope > div.container-fluid.search-section.ng-scope > div:nth-child(4) > div > form > div.booking-date-range.search-field.col-xs-12.col-sm-6 > div.checkin.booking-date')
            startDate.click()
            print('The start date field was clicked.')
        except Exception as err:
            print(str(err))
        #TODO clean up the CSS selector

#Creating a method to select 11/21/2019 from the start date calendar for TCID 4.
    def click_November_21(self):
        try:
            november21 = self.driver.find_element_by_css_selector('#ui-datepicker-div > table > tbody > tr:nth-child(4) > td:nth-child(5) > a')
            november21.click()
            print('November 21 was clicked.')
        except Exception as err:
            print(str(err))

#Creating a method to select 11/25/2019 from the end date calendar for TCID 5.
    def click_November_25(self):
        try:
            november25 = self.driver.find_element_by_css_selector('#ui-datepicker-div > table > tbody > tr:nth-child(5) > td:nth-child(2) > a')
            november25.click()
            print('November 25 was clicked.')
        except Exception as err:
            print(str(err))

#Creating a method to select the guest field for TCID 6.
    def select_guest_field(self):
        try:
            guest = wait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#rm3-home-page > div.content.ng-scope > div.container-fluid.search-section.ng-scope > div:nth-child(4) > div > form > div.adults.col-sm-3.search-field')))
            guest.click()
            print('The guest field has been clicked.')
        except Exception as err:
            print(str(err))

#Creating a method to select the 1 guest from the dropdown menu that appears when select_guest_field is executed for TCID 6.
    def click_1_guest(self):
        try:
            guest1 = wait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//a[contains(text(), "1 Guest")]')))
            guest1.click()
            print('1 Guest was clicked from the guest dropdown menu.')
        except Exception as err:
            print(str(err))

#Creating a method to select the rooms field for TCID 7.
    def select_rooms_field(self):
        try:
            rooms = wait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#rm3-home-page > div.content.ng-scope > div.container-fluid.search-section.ng-scope > div:nth-child(4) > div > form > div.rooms.col-sm-3.search-field.ng-scope > div > div')))
            rooms.click()
            print('The rooms field has been clicked.')
        except Exception as err:
            print(str(err))

#Creating a method to click the 1 room option from the dropdown menu that appears when select_rooms_field is executed for TCID 7.
    def click_1_room(self):
        try:
            room1 = wait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//a[contains(text(), "1 Room")]')))
            room1.click()
            print('1 Room was clicked from the rooms dropdown menu.')
        except Exception as err:
            print(str(err))

#Creating a method to click the Search Properties button for TCID 8.
    def click_search_properties_button(self):
        try:
            searchButton = self.driver.find_element_by_xpath('//div[@class="submit col-md-12"]')
            searchButton.click()
            print('Search Properties button has been clicked.')
        except Exception as err:
            print(str(err))

#Creating a method to select the sort by field for TCID 9.
    def select_sort_by_field(self):
        try:
            sortBy = wait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@class="sort-dropdown dropdown-toggle"]')))
            sortBy.click()
            print('Sort By field has been clicked.')
        except Exception as err:
            print(str(err))

#Creating a method to select the Miles option from the dropdown menu that appears when select_sort_by_field is executed for TCID 9.
    def click_miles(self):
        try:
            miles = wait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//a[contains(text(), "Miles")]')))
            miles.click()
            print('The miles option was clicked from the sort by dropdown menu.')
        except Exception as err:
            print(str(err))

#Creating a method to select the first listing that appears after sorting results by executing click_miles for TCID 10.
    def select_hotel(self):
        try:
            selectHotel = self.driver.find_element_by_xpath('//div[@class="rm-btn-orange ng-scope"]')
            selectHotel.click()
            print('1st hotel listing has been clicked.')
        except Exception as err:
            print(str(err))

#Creating a helper method to handle the optional popup banner that might appear on the Hotel Details page, if the reward amount has decreased. This method will click "Continue with the new reward offer" button in order to proceed with the next step in the test.
    def new_reward_banner(self):
        try:
            continueButton = wait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@class="continue-btn btn ng-scope"]')))
            continueButton.click()
            print('The continue button on the new reward offer banner has been clicked.')
        except Exception as err:
            print(str(err))

#Creating a method to click the Select a Room button on the hotel details page for TCID 11
    def click_select_room_button(self):
        try:
            #selectButton = wait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Select a Room")]')))
            selectButton = wait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#details-page > div.content.ng-scope > div > div.row > div.md-right-container.col-md-4.visible-md-block.visible-lg-block > gofr-trip-summary > div > div > div > div > div:nth-child(9) > button')))
            selectButton.click()
            print('Select a Room button has been clicked.')
        except Exception as err:
            print(str(err))

#Creating a method to click the View button next to the 1st room listing for TCID 12.
    def select_view_button(self):
        try:
            viewButton = wait(self.driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, 'options-button-container')))
            viewButton.click()
            print('The view button has been clicked.')
        except Exception as err:
            print(str(err))

#Creating a method to click the Select button next to the 1st room/reward listed displayed when select_view_button executed; for TCID 13.
    def select_button(self):
        try:
            select = wait(self.driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, 'book-container')))
            select.click()
            print('The select button has been clicked.')
        except Exception as err:
            print(str(err))


