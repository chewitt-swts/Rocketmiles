from RocketMilesClass import RocketMiles
import time
import logging.handlers
import datetime
import os

#Smoke test for basic functionality of the Rocketmiles.com search app. This smoke test navigates through the entire search, selection, and checkout process.

#This module contains an error logger, test preconditions, and TCIDs 1-29.


#Initializing class object.
RM = RocketMiles()


#Error Logger

    #Create a new log folder if none exists.
try:
    os.mkdir('logs/')
except:
    print()

try:
    os.mkdir('logs/SmokeTestAllModules')
except:
    print()

    #Creating a date- and time-stamped filepath for the logfile. The filename syntax is an acronym for the module (in this case, Smoke Test All Modules), followed by a Year_Month_Day__Hour_Minute_Second timestamp.
logSuffix = datetime.datetime.now()
logName = 'logs/SmokeTestAllModules/STAM_log_' + logSuffix.strftime('%Y_%m_%d__%H%M_%S') + '.log'

try:
    logFileCreate = open(logName,"w+")
    logFileCreate.close()
except:
    print()

    #Set up logging objects
logsHandler = logging.handlers.WatchedFileHandler(os.environ.get("LOGFILE", logName))
logsFormatting = logging.Formatter(logging.BASIC_FORMAT)
logsHandler.setFormatter(logsFormatting)
root = logging.getLogger()
root.setLevel(os.environ.get("LOGLEVEL", "INFO"))
root.addHandler(logsHandler)

print("Current testing log file is: ", logName)


#Preconditions for proceeding with smoke test.
try:
    logging.info('Starting smoke test preconditions.')
    RM.open_rocketMiles()
    RM.close_popUp()
    RM.close_cookie_banner()
    RM.loadtime()
    logging.info('Preconditions have been satisfied. Proceeding with test.')
except Exception as err:
    print(str(err))
    logging.exception(str(err))


#Smoke Test for all modules (TCIDs 1-29).
try:
    #TCID 1: Main Page - Can a user enter a destination?
    print('Beginning TCID 1: Main Page - Can a user enter a destination?')
    logging.info('Beginning TCID 1: Main Page - Can a user enter a destination?')
    RM.select_destination_field()
    RM.type_destination()
    RM.loadtime()
    print('TCID 1 has been executed.')
    logging.info('TCID 1 has been executed.')

    #TCID 2: Main Page - Can a user enter a rewards program?
    print('Beginning TCID 2: Main Page - Can a user enter a rewards program?')
    logging.info('Beginning TCID 2: Main Page - Can a user enter a rewards program?')
    RM.select_rewards()
    RM.type_rewards()
    RM.loadtime()
    print('TCID 2 has been executed.')
    logging.info('TCID 2 has been executed.')

    #TCID 3: Main Page - Can a user select the end date field?
    print('Beginning TCID 3: Main Page - Can a user select the end date field?')
    logging.info('Beginning TCID 3: Main Page - Can a user select the end date field?')
    RM.click_end_date()
    RM.loadtime()
    print('TCID 3 has been executed.')
    logging.info('TCID 3 has been executed.')

    #TCID 4: Main Page - Can a user select a start date?
    print('Beginning TCID 4: Main Page - Can a user select a start date?')
    logging.info('Beginning TCID 4: Main Page - Can a user select a start date?')
    RM.click_start_date()
    RM.click_November_21()
    RM.loadtime()
    print('TCID 4 has been executed.')
    logging.info('TCID 4 has been executed.')

    #TCID 5: Main Page - Can a user select an end date from the end date calendar?
    print('Beginning TCID 5: Main Page - Can a user select an end date from the end date calendar?')
    logging.info('Beginning TCID 5: Main Page - Can a user select an end date from the end date calendar?')
    RM.click_November_25()
    RM.loadtime()
    print('TCID 5 has been executed.')
    logging.info('TCID 5 has been executed.')

    #TCID 6: Main Page - Can a user select the number of guests?
    print('Beginning TCID 6: Main Page - Can a user select the number of guests?')
    logging.info('Beginning TCID 6: Main Page - Can a user select the number of guests?')
    RM.select_guest_field()
    RM.click_1_guest()
    RM.loadtime()
    print('TCID 6 has been executed.')
    logging.info('TCID 6 has been executed.')

    #TCID 7: Main Page - Can a user select the number of rooms?
    print('Beginning TCID 7: Main Page - Can a user select the number of rooms?')
    logging.info('Beginning TCID 7: Main Page - Can a user select the number of rooms?')
    RM.select_rooms_field()
    RM.click_1_room()
    RM.loadtime()
    print('TCID 7 has been executed.')
    logging.info('TCID 7 has been executed.')

    #TCID 8: Main Page - Can a user select the Search button?
    print('Beginning TCID 8: Main Page - Can a user select the Search button?')
    logging.info('Beginning TCID 8: Main Page - Can a user select the Search button?')
    RM.click_search_properties_button()
    RM.loadtime()
    print('TCID 8 has been executed.')
    logging.info('TCID 8 has been executed.')

    #TCID 9: Search Page - Can a user sort results by Miles using the Sort By dialogue box?
    print('Beginning TCID 9: Search Page - Can a user sort results by Miles using the Sort By dialogue box?')
    logging.info('Beginning TCID 9: Search Page - Can a user sort results by Miles using the Sort By dialogue box?')
    RM.select_sort_by_field()
    RM.click_miles()
    RM.loadtime()
    print('TCID 9 has been executed.')
    logging.info('TCID 9 has been executed.')

    #TCID 10: Search Page - Can a user select the "Select Now" button for the first listing?
    print('Beginning TCID 10: Search Page - Can a user select the "Select Now" button for the first listing?')
    logging.info('Beginning TCID 10: Search Page - Can a user select the "Select Now" button for the first listing?')
    RM.select_hotel()
    RM.loadtime()
    print('TCID 10 has been executed.')
    logging.info('TCID 10 has been executed.')

    #Precondition for proceeding with smoke test
    RM.switch_tabs()
    print('Precondition: switched to new tab to proceed.')
    logging.info('Precondition: switched to new tab to proceed.')

    # TCID 11: Hotel Details - Can a user select the Select A Room button?
    print('Beginning TCID 11: Hotel Details - Can a user select the Select A Room button?')
    logging.info('Beginning TCID 11: Hotel Details - Can a user select the Select A Room button?')
    RM.click_select_room_button()
    RM.loadtime()
    print('TCID 11 has been executed.')
    logging.info('TCID 11 has been executed.')

    # TCID 12: Hotel Details - Can a user select the View button?
    print('Beginning TCID 12: Hotel Details - Can a user select the View button?')
    logging.info('Beginning TCID 12: Hotel Details - Can a user select the View button?')
    RM.select_view_button()
    RM.loadtime()
    print('TCID 12 has been executed.')
    logging.info('TCID 12 has been executed.')

    # TCID 13: Hotel Details - Can a user select the green Select button to choose a room?
    print('Beginning TCID 13: Hotel Details - Can a user select the green Select button to choose a room?')
    logging.info('Beginning TCID 13: Hotel Details - Can a user select the green Select button to choose a room?')
    RM.select_button()
    RM.loadtime()
    print('TCID 13 has been executed.')
    logging.info('TCID 13 has been executed.')

    # TCID 14: Checkout - Can a user enter a Guest First Name?
    print('Beginning TCID 14: Checkout - Can a user enter a Guest First Name?')
    logging.info('Beginning TCID 14: Checkout - Can a user enter a Guest First Name?')
    RM.select_guest_first_name()
    RM.type_first_name()
    RM.loadtime()
    print('TCID 14 has been executed.')
    logging.info('TCID 14 has been executed.')

    # TCID 15: Checkout - Can a user enter a Guest Last Name?
    print('Beginning TCID 15: Checkout - Can a user enter a Guest Last Name?')
    logging.info('Beginning TCID 15: Checkout - Can a user enter a Guest Last Name?')
    RM.select_guest_last_name()
    RM.type_last_name()
    RM.loadtime()
    print('TCID 15 has been executed.')
    logging.info('TCID 15 has been executed.')

    # TCID 16: Checkout - Can a user enter Your First Name?
    print('Beginning TCID 16: Checkout - Can a user enter Your First Name?')
    logging.info('Beginning TCID 16: Checkout - Can a user enter Your First Name?')
    RM.select_your_first_name()
    RM.type_first_name()
    RM.loadtime()
    print('TCID 16 has been executed.')
    logging.info('TCID 16 has been executed.')

    # TCID 17: Checkout - Can a user enter Your Last Name?
    print('Beginning TCID 17: Checkout - Can a user enter Your Last Name?')
    logging.info('Beginning TCID 17: Checkout - Can a user enter Your Last Name?')
    RM.select_your_last_name()
    RM.type_last_name()
    RM.loadtime()
    print('TCID 17 has been executed.')
    logging.info('TCID 17 has been executed.')

    # TCID 18: Checkout - Can a user enter an email address?
    print('Beginning TCID 18: Checkout - Can a user enter an email address?')
    logging.info('Beginning TCID 18: Checkout - Can a user enter an email address?')
    RM.select_email_address()
    RM.type_email_address()
    RM.loadtime()
    print('TCID 18 has been completed.')
    logging.info('TCID 18 has been completed.')

    # TCID 19: Checkout - Can a user enter a new password?
    print('Beginning TCID 19: Checkout - Can a user enter a new password?')
    logging.info('Beginning TCID 19: Checkout - Can a user enter a new password?')
    RM.select_new_password()
    RM.type_password()
    RM.loadtime()
    print('TCID 19 has been completed.')
    logging.info('TCID 19 has been completed.')

    # TCID 20: Checkout - Can a user confirm a new password?
    print('Beginning TCID 20: Checkout - Can a user confirm a new password?')
    logging.info('Beginning TCID 20: Checkout - Can a user confirm a new password?')
    RM.select_confirm_password()
    RM.type_password()
    RM.loadtime()
    print('TCID 20 has been executed.')
    logging.info('TCID 20 has been executed.')

    # TCID 21: Checkout - Can a user enter a United MileagePlus acount number?
    print('Beginning TCID 21: Checkout - Can a user enter a United MileagePlus acount number?')
    logging.info('Beginning TCID 21: Checkout - Can a user enter a United MileagePlus acount number?')
    RM.select_reward_account()
    RM.type_reward_account()
    RM.loadtime()
    print('TCID 21 has been executed.')
    logging.info('TCID 21 has been executed.')

    # TCID 22: Checkout - Can a user enter a United MileagePlus first name?
    print('Beginning TCID 22: Checkout - Can a user enter a United MileagePlus first name?')
    logging.info('Beginning TCID 22: Checkout - Can a user enter a United MileagePlus first name?')
    RM.select_reward_first_name()
    RM.type_first_name()
    RM.loadtime()
    print('TCID 22 has been executed.')
    logging.info('TCID 22 has been executed.')

    # TCID 23: Checkout - Can a user enter a United MileagePlus last name?
    print('Beginning TCID 23: Checkout - Can a user enter a United MileagePlus last name?')
    logging.info('Beginning TCID 23: Checkout - Can a user enter a United MileagePlus last name?')
    RM.select_reward_last_name()
    RM.type_last_name()
    RM.loadtime()
    print('TCID 23 has been executed.')
    logging.info('TCID 23 has been executed.')

    # TCID 24 - 27: Checkout - Can a user enter a credit card number to the credit card number field?
    print('Beginning Checkout - Payment test series (TCIDs 24-27)')
    logging.info('Beginning Checkout - Payment test series (TCIDs 24-27)')
    time.sleep(3)
    RM.enter_cc_info()
    RM.loadtime()
    print('Checkout - Payment test series (TCIDs 24-27) have been executed.')
    logging.info('Checkout - Payment test series (TCIDs 24-27) have been executed.')

    # Precondition
    print('Switching to default frame.')
    RM.switch_to_default_frame()
    RM.loadtime()
    logging.info('Switched to default frame.')

    # TCID 28: Checkout - Can a user enter a billing zip code?
    print('Beginning TCID 28: Checkout - Can a user enter a billing zip code?')
    logging.info('Beginning Checkout - Can a user enter a billing zip code?')
    RM.select_billing_zip()
    RM.type_billing_zip()
    RM.loadtime()
    print('TCID 28 has been executed.')
    logging.info('TCID 28 has been executed.')

    # TCID 29: Checkout - Can a user check the Terms and Conditions checkbox?
    print('Beginning TCID 29: Checkout - Can a user check the Terms and Conditions checkbox?')
    logging.info('Beginning TCID 29: Checkout - Can a user check the Terms and Conditions checkbox?')
    RM.click_terms_checkbox()
    RM.loadtime()
    print('TCID 29 has been executed.')
    logging.info('TCID 29 has been executed.')

except Exception as err:
    logging.exception(str(err))

#Ending smoke test for all modules
print('All modules smoke test complete. Closing browser.')
RM.close_browser()
logging.info('All modules smoke test complete. Browser closed.')