from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains as action
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
import logging.handlers

class RocketMiles:

#Creating our Selenium Webdriver and Chrome settings for use in all test cases.
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument('-incognito')
        self.chrome_options.add_argument("--start-maximized")
        self.chrome_options.add_argument('--disable-notifications')
        self.chrome_options.add_argument('--disable-popup-blocking')

         #Below is our driver object that we are storing our Webdriver in. Replace the filepath with the location of your local Webdriver.
        self.driver = webdriver.Chrome(r'/home/helkirien/Drivers/chromedriver', options=self.chrome_options)

        #Optional setting to decrease TimeOutException errors. Can be removed for faster execution, but you are more likely to encounter errors based on your internet connection.
        self.driver.implicitly_wait(3)

#Creating method to collect the load time of each test. Useful for performance testing. All time values are in milliseconds.
    def loadtime(self):
        navigationStart = self.driver.execute_script("return window.performance.timing.navigationStart")
        responseStart = self.driver.execute_script("return window.performance.timing.responseStart")
        domComplete = self.driver.execute_script("return window.performance.timing.domComplete")

        # Calculating website/network performance
        backendPerformance_calc = responseStart - navigationStart
        frontendPerformance_calc = domComplete - responseStart

        #Displaying loadtimes in console
        print('\t' + "Back End: %s" % backendPerformance_calc)
        print('\t' + "Front End: %s" % frontendPerformance_calc)

        #Writing loadtimes to log
        backEnd = "Back End: %s" % backendPerformance_calc
        frontEnd = "Front End: %s" % frontendPerformance_calc
        logging.info(backEnd)
        logging.info(frontEnd)
        return

#Creating a method to open the Rocketmiles website.
    def open_rocketMiles(self):
        try:
            self.driver.get('http://www.rocketmiles.com')
            print('\t' + 'Precondition: Rocketmiles.com has opened successfully.')
        except Exception as err:
            print(str(err))

#Creating a helper method to reach the Search Page. This method can be called in order to independently run TCIDs 9-10, which would otherwise be dependent on running TCIDs 1-8. This URL points to a search page with our smoke test data (destination: Los Angeles, trip dates: 11/21/2019 - 11/25/2019, guests: 1, rooms: 1)
    def open_search_page(self):
        try:
            self.driver.get('https://www.rocketmiles.com/search?longitude=-118.253426&latitude=34.05219&placeId=43&query=Los%20Angeles,%20CA&source=HSS&checkIn=11%2F21%2F2019&checkOut=11%2F25%2F2019&program=united&guests=1&rooms=1&currency=USD&includePromoIneligible')
            print('\t' + 'Precondition: Search Page loaded with smoke test data has opened successfully.')
        except Exception as err:
            print(str(err))

# Creating a helper method to reach the Hotel Details page. This method can be called in order to independently run TCIDs 11-12, which would otherwise be dependent on running TCIDs 1-10.
    def open_hotel_details(self):
        try:
            self.driver.get('http://rocketmiles.com/details?averagePrice=680&checkIn=11~2F21~2F2019&checkOut=11~2F25~2F2019&currency=USD&guests=1&id=775459&latitude=34.0522342&longitude=-118.2436849&program=united&placeId=ChIJE9on3F3HwoAR9AhGJW_fL-I&query=Los%20Angeles,%20CA,%20USA&rewardAmount=31000&rooms=1&source=GOOGLE&badge=travelerfavorite&searchId=977569e0-ea17-47ee-8d9a-f92d7bf83250')
            print('\t' + 'Precondition: Hotel Details page has opened successfully.')
        except Exception as err:
            print(str(err))
        return

# Creating a helper method to reach the Checkout page. This method can be called in order to independently run TCIDs 11-12, which would otherwise be dependent on running TCIDs 1-13.
    def open_checkout_page(self):
        try:
            self.driver.get('https://www.rocketmiles.com/booking?averagePrice=637&checkIn=11~2F21~2F2019&checkOut=11~2F25~2F2019&currency=USD&guests=1&id=45381_e2263db5f6ad185fd56b20e3c3d4153547654fe3eb63705f08d64e0047d5d459&latitude=34.05219&longitude=-118.253426&placeId=43&program=united&query=Los%20Angeles,%20CA&rewardAmount=30000&rooms=1&source=HSS&hotelId=45381&defaultRoomPrice=637&defaultRewardAmount=30000&searchId=8f3ba5a2-288e-4e6e-8a97-052eff7d53be')
            print('\t' + 'Precondition: Checkout page has opened successfully.')
        except Exception as err:
            print(str(err))

#Creating a method to close a browser at the end of a test.
    def close_browser(self):
        try:
           self.driver.quit()
           print('\t' + 'The browser has closed.')
        except Exception as err:
            print(str(err))

#Creating a helper method to handle the sign up popup that occasionally appears on the Main Page when the page first loads. We need to close the popup in order to proceed with the test cases.
    def close_popUp(self):
        try:
            closeButton = wait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[class="close"]')))
            closeButton.click()
            print('\t' + 'Precondition: The close button for the sign up popup has been clicked.')
            time.sleep(3)
        except Exception as err:
            print('\t' + 'The sign up popup was not located. Proceeding with next test.')

#Creating a helper method to close the cookie banner that appears at multiple locations through the app.
    def close_cookie_banner(self):
        try:
            okButton = wait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[class="btn cookie-banner-button ng-scope"]')))
            okButton.click()
            print('\t' + 'Precondition: The ok button for the cookie banner has been clicked.')
        except Exception as err:
            print(err)

#Creating a helper method to handle the possible error on the Checkout page, "Unfortunately, availability of this room changed when we reached out to finalize the reservation. We're sorry, and have alerted our systems team as well as our hotel partners to investigate. Please select a different hotel."
    def checkout_return_search(self):
        time.sleep(5)
        try:
            returnSearch = self.driver.find_element_by_css_selector('a[class="return-btn btn ng-scope"]')
            returnSearch.click()
        except Exception as err:
            print(str(err))
            raise Exception()

#Creating a method to select the destination field for TCID 1.
    def select_destination_field(self):
        try:
            destination = wait(self.driver, 5).until(EC.element_to_be_clickable((By.NAME, 'locationSearch')))
            destination.click()
            print('\t' + 'The destination field has been clicked.')
        except Exception as err:
            print(str(err))

#Creating a method to type "Los Angeles" into the destination field for TCID 1.
    def type_destination(self):
        try:
            action(self.driver).send_keys('Los Angeles').perform()
            print('\t' + 'The test data was typed into the destination field.')
            time.sleep(3)

            destination1 = self.driver.find_element_by_css_selector('a[class="ng-binding ng-scope"]')
            destination1.click()
            print('\t' + 'The first option from the destination dropdown menu was selected.')
        except Exception as err:
            print(str(err))

#Creating a method to select the rewards program field for TCID 2.
    def select_rewards(self):
        try:
            rewards = wait(self.driver, 5).until(EC.element_to_be_clickable((By.NAME, 'programAutosuggest')))
            rewards.click()
            print('\t' + 'The rewards program field has been clicked.')
        except Exception as err:
            print(str(err))

#Creating a method to type "United MileagePlus" into the rewards field for TCID 2.
    def type_rewards(self):
        try:
            action(self.driver).send_keys('United MileagePlus').perform()
            print('\t' + 'The test data was typed into the rewards program field.')
            time.sleep(3)

            rewards1 = self.driver.find_element_by_css_selector('a[class="ng-binding ng-scope"]')
            rewards1.click()
            print('\t' + 'The first option from the rewards program dropdown menu was selected.')
        except Exception as err:
            print(str(err))

#Creating a method to click on the end date field for TCID 3.
    def click_end_date(self):
        try:
            endDate = wait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[class="checkout booking-date"]')))
            endDate.click()
            print('\t' + 'The end date field was clicked.')
        except Exception as err:
            print(str(err))

#Creating a method to click on the start date field for TCID 4.
    def click_start_date(self):
        try:
            startDate = wait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[class="checkin booking-date"]')))
            startDate.click()
            print('\t' + 'The start date field was clicked.')
        except Exception as err:
            print(str(err))

#Creating a method to select 11/21/2019 from the start date calendar for TCID 4.
    def click_November_21(self):
        try:
            november21 = wait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//a[contains(text(), "21")]')))
            november21.click()
            print('\t' + 'November 21 was clicked.')
        except Exception as err:
            print(str(err))

#Creating a method to select 11/25/2019 from the end date calendar for TCID 5.
    def click_November_25(self):
        try:
            november25 = wait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//a[contains(text(), "25")]')))
            november25.click()
            print('\t' + 'November 25 was clicked.')
        except Exception as err:
            print(str(err))

#Creating a method to select the guest field for TCID 6.
    def select_guest_field(self):
        try:
            #guest = self.driver.find_element_by_css_selector('div[class="adults col-sm-3 search-field"]')
            guest =  wait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[class="adults col-sm-3 search-field"]')))
            guest.click()
            print('\t' + 'The guest field has been clicked.')
        except Exception as err:
            print(str(err))

#Creating a method to select the 1 guest from the dropdown menu that appears when select_guest_field is executed for TCID 6.
    def click_1_guest(self):
        try:
            guest1 = wait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//a[contains(text(), "1 Guest")]')))
            guest1.click()
            print('\t' + '1 Guest was clicked from the guest dropdown menu.')
        except Exception as err:
            print(str(err))

#Creating a method to select the rooms field for TCID 7.
    def select_rooms_field(self):
        try:
            rooms = wait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[class="rooms col-sm-3 search-field ng-scope"]')))
            rooms.click()
            print('\t' + 'The rooms field has been clicked.')
        except Exception as err:
            print(str(err))

#Creating a method to click the 1 room option from the dropdown menu that appears when select_rooms_field is executed for TCID 7.
    def click_1_room(self):
        try:
            room1 = wait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//a[contains(text(), "1 Room")]')))
            room1.click()
            print('\t' + '1 Room was clicked from the rooms dropdown menu.')
        except Exception as err:
            print(str(err))

#Creating a method to click the Search Properties button for TCID 8.
    def click_search_properties_button(self):
        try:
            searchButton = self.driver.find_element_by_css_selector('*[class="rm-btn-orange search-submit-btn"]')
            searchButton.click()
            print('\t' + 'Search Properties button has been clicked.')
        except Exception as err:
            print(str(err))

#Creating a method to select the sort by field for TCID 9.
    def select_sort_by_field(self):
        try:
            sortBy = wait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@class="sort-dropdown dropdown-toggle"]')))
            sortBy.click()
            print('\t' + 'Sort By field has been clicked.')
        except Exception as err:
            print(str(err))

#Creating a method to select the Miles option from the dropdown menu that appears when select_sort_by_field is executed for TCID 9.
    def click_miles(self):
        try:
            miles = wait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//a[contains(text(), "Miles")]')))
            miles.click()
            print('\t' + 'The miles option was clicked from the sort by dropdown menu.')
            time.sleep(2)
        except Exception as err:
            print(str(err))

#Creating a method to select the first listing that appears after sorting results by executing click_miles for TCID 10.
    def select_hotel(self):
        try:
            #selectHotel = self.driver.find_element_by_xpath('//div[@class="rm-btn-orange ng-scope"]')
            selectHotel = wait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="rm-btn-orange ng-scope"]')))
            selectHotel.click()
            print('\t' + '1st hotel listing has been clicked.')
        except Exception as err:
            print(str(err))

#Creating a helper method to switch to a new tab.
    def switch_tabs(self):
        try:
            self.driver.switch_to.window(self.driver.window_handles[1])
            print('\t' + 'Tab has been switched.')
        except Exception as err:
            print(str(err))

#Creating a helper method to handle the optional popup banner that might appear on the Hotel Details page, if the reward amount has decreased. This method will click "Continue with the new reward offer" button in order to proceed with the next step in the test.
    def new_reward_banner(self):
        try:
            continueButton = wait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@class="continue-btn btn ng-scope"]')))
            continueButton.click()
            print('\t' + 'The continue button on the new reward offer banner has been clicked.')
        except Exception as err:
            print(str(err))

#Creating a method to click the Select a Room button on the hotel details page for TCID 11
    def click_select_room_button(self):
        try:
            time.sleep(3)
            selectButton = self.driver.find_element_by_css_selector('span[class="rm-animate-fade ng-scope"]')
            selectButton.click()
            print('\t' + 'Select a Room button has been clicked.')
        except Exception as err:
            print(err)

#Creating a method to click the View button next to the 1st room listing for TCID 12.
    def select_view_button(self):
        try:
            viewButton = wait(self.driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, 'options-button-container')))
            viewButton.click()
            print('\t' + 'The view button has been clicked.')
        except Exception as err:
            print(str(err))

#Creating a method to click the Select button next to the 1st room/reward listed displayed when select_view_button executed; for TCID 13.
    def select_button(self):
        try:
            select = wait(self.driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, 'book-container')))
            select.click()
            print('\t' + 'The select button has been clicked.')
        except Exception as err:
            print(str(err))

#Creating a method to select the Guest First Name field for TCID 14
    def select_guest_first_name(self):
        try:
            guestFirstName = wait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, 'guestFirstName')))
            guestFirstName.click()
            print('\t' + 'The guest first name field has been clicked.')
        except Exception as err:
            print(str(err))

#Creating a method to type "John" into the Guest First Name field for TCIDs 14, 16, and 22.
    def type_first_name(self):
        try:
            firstName = action(self.driver).send_keys('John').perform()
            print('\t' + 'The test data was typed into the first name field.')
        except Exception as err:
            print(str(err))

#Creating a method to select the Guest Last Name field for TCID 15.
    def select_guest_last_name(self):
        try:
            guestLastName = wait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, 'guestLastName')))
            guestLastName.click()
            print('\t' + 'The guest last name field has been clicked.')
        except Exception as err:
            print(str(err))

#Creating a method to type "Smith" into the Guest Last Name field for TCIDs 15, 17, and 23.
    def type_last_name(self):
        try:
            lastName = action(self.driver).send_keys('Smith').perform()
            print('\t' + 'The test data was typed into the last name field.')
        except Exception as err:
            print(str(err))

#Creating a method to select the Your First Name field for TCID 16.
    def select_your_first_name(self):
        try:
            firstName = wait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, 'firstname')))
            firstName.click()
            print('\t' + 'Your first name field has been clicked.')
        except Exception as err:
            print(str(err))

#Creating a method to select the Your Last Name field for TCID 17.
    def select_your_last_name(self):
        try:
            lastName = wait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, 'lastname')))
            lastName.click()
            print('\t' + 'Your last name field has been clicked.')
        except Exception as err:
            print(str(err))

#Creating a method to select the email address field for TCID 18.
    def select_email_address(self):
        try:
            emailField = wait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, 'newUsername')))
            emailField.click()
            print('\t' + 'The email address field has been clicked.')
        except Exception as err:
            print(str(err))

#Creating a method to type "test@test.com" into the Email Address field for TCID 18.
    def type_email_address(self):
        try:
            emailAddress = action(self.driver).send_keys('test@test.com').perform()
            print('\t' + 'The test data was typed into the Email Address field.')
        except Exception as err:
            print(str(err))

#Creating a method to select the New Rocketmiles Password field for TCID 19.
    def select_new_password(self):
        try:
            passwordField = wait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, 'newPassword')))
            passwordField.click()
            print('\t' + 'The new password field has been clicked.')
        except Exception as err:
            print(str(err))

#Creating a method to type "12345abc!#^" into the New Rocketmiles Password field for TCIDs 19 and 20.
    def type_password(self):
        try:
            action(self.driver).send_keys('12345abc!#^').perform()
            print('\t' + 'The test data was typed into the new password field.')
        except Exception as err:
            print(str(err))

#Creating a method to select the Confirm Rocketmiles Password field for TCID 20.
    def select_confirm_password(self):
        try:
            confirmPassword = wait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, 'confirmPassword')))
            confirmPassword.click()
            print('\t' + 'The confirm password field has been clicked.')
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
            print('\t' + 'The test data was typed into the rewards program account number field.')
        except Exception as err:
            print(str(err))

#Creating a method to select the rewards program first name field for TCID 22.
    def select_reward_first_name(self):
        try:
            rewardFirst = wait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, 'newRewardAccountFirstName')))
            rewardFirst.click()
            print('\t' + 'The rewards program First Name field has been clicked.')
        except  Exception as err:
            print(str(err))

#Creating a method to select the rewards program last name field for TCID 23.
    def select_reward_last_name(self):
        try:
            rewardLast = wait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, 'newRewardAccountLastName')))
            rewardLast.click()
            print('\t' + 'The rewards program Last Name field has been clicked.')
        except  Exception as err:
            print(str(err))

#Creating a method to enter credit card information for the Credit Card Details section of the Check Page for TCIDs
    def enter_cc_info(self):
        #Switching to the iframe which contains the credit card information fields.
        try:
            iframe = self.driver.find_element_by_id('eProtect-iframe')
            self.driver.switch_to.frame(iframe)
            print('\t' + 'iFrame switched.')

            #Selecting the credit card number field and entering test data "0123456789876543210" for TCID 24.
            try:
                #time.sleep(1)
                ccField = wait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, 'accountNumber')))
                action(self.driver).click(ccField).send_keys('0123456789876543210').perform()
                print('\t' + 'The credit card number field has been clicked.')
            except Exception as err:
                print(str(err))

            #Selecting the credit card expiration month dropdown menu for TCID 25.
            try:
                expMonthField = self.driver.find_element_by_id('expMonth')
                expMonthField.click()
                print('\t' + 'The credit card expiration month dropdown menu has been selected.')
            except Exception as err:
                print(str(err))

            #Selecting "July" as test data from the expiration month dropdown menu for TCID 25.
            try:
                expirationMonth = self.driver.find_element_by_xpath('//option[@value="07"]')
                expirationMonth.click()
                print('\t' + 'The credit card expiration month test data has been set from the dropdown menu options.')
            except Exception as err:
                print(str(err))

            #Selecting the credit card expiration year dropdown menu for TCID 26.
            try:
                expYearField = self.driver.find_element_by_id('expYear')
                expYearField.click()
                print('\t' + 'The credit card expiration year dropdown menu has been selected.')
            except Exception as err:
                print(str(err))

            #Selecting "2021" from the expiration year dropdown menu for TCID 26.
            try:
                expirationYear = self.driver.find_element_by_xpath('//option[@value="21"]')
                expirationYear.click()
                print('\t' + 'The credit card expiration year test data has been set from the dropdown menu options.')
            except Exception as err:
                print(str(err))

            #Selecting the credit card security code field for TCID 27.
            try:
                time.sleep(2)
                securityCodeField = self.driver.find_element_by_id('cvv')
                securityCodeField.click()
                print('\t' + 'The credit card security code field has been selected.')
            except Exception as err:\
                print(str(err))

            #Typing test data into the security code field for TCID 27.
            try:
                time.sleep(2)
                action(self.driver).send_keys('012').perform()
                print('\t' + 'The credit card security code test data has been typed into the security code field.')
            except Exception as err:
                print(str(err))
        except Exception as err:
            print(str(err))

#Switching out of the iframe to default browser frame.
    def switch_to_default_frame(self):
        try:
            self.driver.switch_to.default_content()
            print('\t' + 'Switched back to default frame.')
        except Exception as err:
            print(str(err))

#Selecting the billing zip code field for TCID 28.
    def select_billing_zip(self):
        try:
            zipCodeField = self.driver.find_element_by_name('zipcode')
            zipCodeField.click()
            print('\t' + 'The billing zip code field has been selected.')
        except Exception as err:
            print(str(err))

#Typing test data into the billing zip code field for TCID 28.
    def type_billing_zip(self):
        try:
            time.sleep(2)
            action(self.driver).send_keys('60640').perform()
            print('\t' + 'The billing zip code test data has been typed into the field.')
        except Exception as err:
            print(str(err))

#Creating a method to check the Terms and Conditions checkbox for TCID 29.
    def click_terms_checkbox(self):
        try:
            time.sleep(5)
            termsCheckbox = self.driver.find_element_by_xpath('//input[@id="agreeToTermsAndPolicies"]')
            action(self.driver).move_to_element(termsCheckbox).click().perform()
            print('\t' + 'The Terms and Conditions checkbox has been clicked.')
        except Exception as err:
            print(str(err))