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
            print('Precondition: Rocketmiles.com has opened successfully.')
        except Exception as err:
            print(str(err))

#Creating a helper method to reach the Search Page. This method can be called in order to independently run TCIDs 9-10, which would otherwise be dependent on running TCIDs 1-8. This URL points to a search page with our smoke test data (destination: Los Angeles, trip dates: 11/21/2019 - 11/25/2019, guests: 1, rooms: 1)
    def open_search_page(self):
        try:
            self.driver.get('https://www.rocketmiles.com/search?longitude=-118.253426&latitude=34.05219&placeId=43&query=Los%20Angeles,%20CA&source=HSS&checkIn=11%2F21%2F2019&checkOut=11%2F25%2F2019&program=united&guests=1&rooms=1&currency=USD&includePromoIneligible')
            print('Precondition: Search Page loaded with smoke test data has opened successfully.')
        except Exception as err:
            print(str(err))

# Creating a helper method to reach the Hotel Details page. This method can be called in order to independently run TCIDs 11-12, which would otherwise be dependent on running TCIDs 1-10.
    def open_hotel_details(self):
        try:
            self.driver.get('http://rocketmiles.com/details?averagePrice=680&checkIn=11~2F21~2F2019&checkOut=11~2F25~2F2019&currency=USD&guests=1&id=775459&latitude=34.0522342&longitude=-118.2436849&program=united&placeId=ChIJE9on3F3HwoAR9AhGJW_fL-I&query=Los%20Angeles,%20CA,%20USA&rewardAmount=31000&rooms=1&source=GOOGLE&badge=travelerfavorite&searchId=977569e0-ea17-47ee-8d9a-f92d7bf83250')
            print('Precondition: Hotel Details page has opened successfully.')
        except Exception as err:
            print(str(err))

# Creating a helper method to reach the Checkout page. This method can be called in order to independently run TCIDs 11-12, which would otherwise be dependent on running TCIDs 1-13.
    def open_checkout_page(self):
        try:
            self.driver.get('https://www.rocketmiles.com/booking?averagePrice=637&checkIn=11~2F21~2F2019&checkOut=11~2F25~2F2019&currency=USD&guests=1&id=45381_e2263db5f6ad185fd56b20e3c3d4153547654fe3eb63705f08d64e0047d5d459&latitude=34.05219&longitude=-118.253426&placeId=43&program=united&query=Los%20Angeles,%20CA&rewardAmount=30000&rooms=1&source=HSS&hotelId=45381&defaultRoomPrice=637&defaultRewardAmount=30000&searchId=8f3ba5a2-288e-4e6e-8a97-052eff7d53be')
            print('Precondition: Checkout page has opened successfully.')
        except Exception as err:
            print(str(err))

#Creating a method to close a browser at the end of a test.
    def close_browser(self):
        try:
           self.driver.quit()
           print('The browser has closed.')
        except Exception as err:
            print(str(err))

    def close_popUp(self):
        #time.sleep(5)
        try:
            closeButton = wait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[class="close"]')))
            closeButton.click()
            print('Precondition: The close button for the sign up popup has been clicked.')
            time.sleep(3)
        except Exception as err:
            print('The sign up popup was not located. Proceeding with next test.')
            print(str(err))

    def close_cookie_banner(self):
        try:
            #okButton = wait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@class="btn cookie-banner-button ng-scope"]')))
            okButton = wait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[class="btn cookie-banner-button ng-scope"]')))
            okButton.click()
            print('Precondition: The ok button for the cookie banner has been clicked.')
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

            destination1 = self.driver.find_element_by_css_selector('a[class="ng-binding ng-scope"]')
            destination1.click()
            #action(self.driver).send_keys(Keys.ARROW_DOWN, Keys.ENTER).perform()
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
            time.sleep(2)
        except Exception as err:
            print(str(err))

#Creating a method to select the first listing that appears after sorting results by executing click_miles for TCID 10.
    def select_hotel(self):
        try:
            #selectHotel = self.driver.find_element_by_xpath('//div[@class="rm-btn-orange ng-scope"]')
            selectHotel = wait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="rm-btn-orange ng-scope"]')))
            selectHotel.click()
            print('1st hotel listing has been clicked.')
        except Exception as err:
            print(str(err))

#Creating a helper method to switch to a new tab.
    def switch_tabs(self):
        try:
            self.driver.switch_to.window(self.driver.window_handles[1])
            print('Tab has been switched.')
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
            time.sleep(3)
            #selectButton = wait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[class="rm-btn-green open-rooms-btn"]')))
            #selectButton = wait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#details-page > div.content.ng-scope > div > div.row > div.md-right-container.col-md-4.visible-md-block.visible-lg-block > gofr-trip-summary > div > div > div > div > div:nth-child(9) > button')))
            selectButton = self.driver.find_element_by_css_selector('span[class="rm-animate-fade ng-scope"]')
            selectButton.click()
            print('Select a Room button has been clicked.')
        except Exception as err:
            print(err)

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

#Creating a method to select the Guest First Name field for TCID 14
    def select_guest_first_name(self):
        try:
            guestFirstName = wait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, 'guestFirstName')))
            guestFirstName.click()
            print('The guest first name field has been clicked.')
        except Exception as err:
            print(str(err))

#Creating a method to type "John" into the Guest First Name field for TCIDs 14, 16, and 22.
    def type_first_name(self):
        try:
            firstName = action(self.driver).send_keys('John').perform()
            print('The test data was typed into the first name field.')
        except Exception as err:
            print(str(err))

#Creating a method to select the Guest Last Name field for TCID 15.
    def select_guest_last_name(self):
        try:
            guestLastName = wait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, 'guestLastName')))
            guestLastName.click()
            print('The guest last name field has been clicked.')
        except Exception as err:
            print(str(err))

#Creating a method to type "Smith" into the Guest Last Name field for TCIDs 15, 17, and 23.
    def type_last_name(self):
        try:
            lastName = action(self.driver).send_keys('Smith').perform()
            print('The test data was typed into the last name field.')
        except Exception as err:
            print(str(err))

#Creating a method to select the Your First Name field for TCID 16.
    def select_your_first_name(self):
        try:
            firstName = wait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, 'firstname')))
            firstName.click()
            print('Your first name field has been clicked.')
        except Exception as err:
            print(str(err))

#Creating a method to select the Your Last Name field for TCID 17.
    def select_your_last_name(self):
        try:
            lastName = wait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, 'lastname')))
            lastName.click()
            print('Your last name field has been clicked.')
        except Exception as err:
            print(str(err))

#Creating a method to select the email address field for TCID 18.
    def select_email_address(self):
        try:
            emailField = wait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, 'newUsername')))
            emailField.click()
            print('The email address field has been clicked.')
        except Exception as err:
            print(str(err))

#Creating a method to type "test@test.com" into the Email Address field for TCID 18.
    def type_email_address(self):
        try:
            emailAddress = action(self.driver).send_keys('test@test.com').perform()
            print('The test data was typed into the Email Address field.')
        except Exception as err:
            print(str(err))

#Creating a method to select the New Rocketmiles Password field for TCID 19.
    def select_new_password(self):
        try:
            passwordField = wait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, 'newPassword')))
            passwordField.click()
            print('The new password field has been clicked.')
        except Exception as err:
            print(str(err))

#Creating a method to type "12345abc!#^" into the New Rocketmiles Password field for TCIDs 19 and 20.
    def type_password(self):
        try:
            action(self.driver).send_keys('12345abc!#^').perform()
            print('The test data was typed into the new password field.')
        except Exception as err:
            print(str(err))

#Creating a method to select the Confirm Rocketmiles Password field for TCID 20.
    def select_confirm_password(self):
        try:
            confirmPassword = wait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, 'confirmPassword')))
            confirmPassword.click()
            print('The confirm password field has been clicked.')
        except Exception as err:
            print(str(err))

#Creating a method to select the reward program account number for TCID 21. This method can be reused to select any reward program account number for exhaustive testing; it is not unique to the United MileagePlus account.
    def select_reward_account(self):
        try:
            accountField = wait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, 'accountNumber')))
            accountField.click()
            print("The rewards program account number field has been clicked.")
        except Exception as err:
            print(str(err))

#Creating a method to type "123456789a" into the reward program account number for TCID 21.
    def type_reward_account(self):
        try:
            accountNumber = action(self.driver).send_keys('123456789a').perform()
            print('The test data was typed into the rewards program account number field.')
        except Exception as err:
            print(str(err))

#Creating a method to select the rewards program first name field for TCID 22.
    def select_reward_first_name(self):
        try:
            rewardFirst = wait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, 'newRewardAccountFirstName')))
            rewardFirst.click()
            print('The rewards program First Name field has been clicked.')
        except  Exception as err:
            print(str(err))

#Creating a method to select the rewards program last name field for TCID 23.
    def select_reward_last_name(self):
        try:
            rewardLast = wait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, 'newRewardAccountLastName')))
            rewardLast.click()
            print('The rewards program Last Name field has been clicked.')
        except  Exception as err:
            print(str(err))

#Creating a method to enter credit card information for the Credit Card Details section of the Check Page for TCIDs
    def enter_cc_info(self):
        #Switching to the iframe which contains the credit card information fields.
        try:
            iframe = self.driver.find_element_by_id('eProtect-iframe')
            self.driver.switch_to.frame(iframe)
            print('iFrame switched.')

            #Selecting the credit card number field for TCID
            try:
                #time.sleep(1)
                ccField = wait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, 'accountNumber')))
                action(self.driver).click(ccField).send_keys('0123456789876543210').perform()
                print('The credit card number field has been clicked.')
            except Exception as err:
                print(str(err))

            #Selecting the credit card expiration month dropdown menu for TCID
            try:
                expMonthField = self.driver.find_element_by_id('expMonth')
                expMonthField.click()
                print('The credit card expiration month dropdown menu has been selected.')
            except Exception as err:
                print(str(err))

            #Selecting "July" as test data from the expiration month dropdown menu for TCID
            try:
                expirationMonth = self.driver.find_element_by_xpath('//option[@value="07"]')
                expirationMonth.click()
                print('The credit card expiration month test data has been set from the dropdown menu options.')
            except Exception as err:
                print(str(err))

            #Selecting the credit card expiration year dropdown menu for TCID
            try:
                expYearField = self.driver.find_element_by_id('expYear')
                expYearField.click()
                print('The credit card expiration year dropdown menu has been selected.')
            except Exception as err:
                print(str(err))

            #Selecting "2021" from the expiration year dropdown menu for TCID
            try:
                expirationYear = self.driver.find_element_by_xpath('//option[@value="21"]')
                expirationYear.click()
                print('The credit card expiration year test data has been set from the dropdown menu options.')
            except Exception as err:
                print(str(err))

            #Selecting the credit card security code field for TCID
            try:
                time.sleep(2)
                securityCodeField = self.driver.find_element_by_id('cvv')
                securityCodeField.click()
                print('The credit card security code field has been selected.')
            except Exception as err:\
                print(str(err))

            #Typing test data into the security code field for TCID
            try:
                time.sleep(2)
                action(self.driver).send_keys('012').perform()
                print('The credit card security code test data has been typed into the security code field.')
            except Exception as err:
                print(str(err))
        except Exception as err:
            print(str(err))

#Switching out of the iframe to default browser frame.
    def switch_to_default_frame(self):
        try:
            self.driver.switch_to.default_content()
        except Exception as err:
            print(str(err))

#Selecting the billing zip code field for TCID
    def select_billing_zip(self):
        try:
            zipCodeField = self.driver.find_element_by_name('zipcode')
            zipCodeField.click()
            print('The billing zip code field has been selected.')
        except Exception as err:
            print(str(err))
#Typing test data into the billing zip code field for TCID
    def type_billing_zip(self):
        try:
            time.sleep(2)
            action(self.driver).send_keys('60640').perform()
            print('The billing zip code test data has been typed into the field.')
        except Exception as err:
            print(str(err))


'''
#Creating a method to select the credit card number field under the Credit Card Details section for TCID
    def select_cc_field(self):
        time.sleep(3)
        iframe = self.driver.find_element_by_id('eProtect-iframe')
        self.driver.switch_to.frame(iframe)
        print('iFrame switched.')
        ccField = wait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, 'accountNumber')))
        ccField.click()
        print('The credit card number field has been clicked.')

#Creating a method to type "0123456789876543210" into the credit card number for TCID
    def type_cc_number(self):
        try:
            action(self.driver).send_keys('0123456789876543210').perform()
            print('The test data was typed into the credit card number field.')
        except Exception as err:
            print(str(err))

#Creating a method to select the credit card expiration month for TCID
    def select_exp_month_field(self):
        try:
            iframe = self.driver.find_element_by_id('eProtect-iframe')
            self.driver.switch_to.frame(iframe)
        except Exception as err:
            print(str(err))
        try:
            expirationField = self.driver.find_element_by_id('expMonth')
            expirationField.click()
            print('The credit card expiration month dropdown menu has been selected.')
        except Exception as err:
            print(str(err))
'''