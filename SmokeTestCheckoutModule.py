from RocketMilesClass import RocketMiles
import time
import logging.handlers
import datetime
import os

#Smoke test for basic functionality of the Checkout page for the Rocketmiles.com search app.

#This module contains an error logger, test preconditions, and TCIDs 14-28.


#Initializing class object.
RM = RocketMiles()


#Error Logger
    #Creating log filepath. Syntax is an acronym for the module (in this case, Smoke Test Checkout), followed by a Year_Month_Day__Hour_Minute_Second timestamp.
logSuffix = datetime.datetime.now()
logName = "logs/CheckoutModule/STC_log_" + logSuffix.strftime("%Y_%m_%d__%H%M_%S") + ".log"

    #Create a new log folder if none exists, then the log file.
try:
    os.mkdir("logs/CheckoutModule")
except:
    print()

logFileCreate = open(logName,"w+")
logFileCreate.close()

    #Set up logging objects
logsHandler = logging.handlers.WatchedFileHandler(os.environ.get("LOGFILE", logName))
logsFormatting = logging.Formatter(logging.BASIC_FORMAT)
logsHandler.setFormatter(logsFormatting)
root = logging.getLogger()
root.setLevel(os.environ.get("LOGLEVEL", "INFO"))
root.addHandler(logsHandler)

print("Current testing log file is: ", logName)


#Preconditions
logging.info('Starting smoke test preconditions.')
RM.open_checkout_page()
try:
    RM.new_reward_banner()
except Exception as err:
    print(str(err))
try:
    RM.checkout_return_search()
    RM.select_hotel()
    RM.switch_tabs()
    RM.click_select_room_button()
    RM.select_view_button()
    RM.select_button()
    RM.close_cookie_banner()
except Exception as err:
    print(str(err))
    logging.exception(str(err))


#Smoke Test for Checkout (TCIDs 14-29).
try:

    # TCID 14: Checkout - Can a user enter a Guest First Name?
    print('Beginning TCID 14: Checkout - Can a user enter a Guest First Name?')
    logging.info('Beginning TCID 14: Checkout - Can a user enter a Guest First Name?')
    RM.select_guest_first_name()
    RM.type_first_name()
    print('TCID 14 has been executed.')
    logging.info('TCID 14 has been executed.')

    #TCID 15: Checkout - Can a user enter a Guest Last Name?
    print('Beginning TCID 15: Checkout - Can a user enter a Guest Last Name?')
    logging.info('Beginning TCID 15: Checkout - Can a user enter a Guest Last Name?')
    RM.select_guest_last_name()
    RM.type_last_name()
    print('TCID 15 has been executed.')
    logging.info('TCID 15 has been executed.')

    #TCID 16: Checkout - Can a user enter Your First Name?
    print('Beginning TCID 16: Checkout - Can a user enter Your First Name?')
    logging.info('Beginning TCID 16: Checkout - Can a user enter Your First Name?')
    RM.select_your_first_name()
    RM.type_first_name()
    print('TCID 16 has been executed.')
    logging.info('TCID 16 has been executed.')

    #TCID 17: Checkout - Can a user enter Your Last Name?
    print('Beginning TCID 17: Checkout - Can a user enter Your Last Name?')
    logging.info('Beginning TCID 17: Checkout - Can a user enter Your Last Name?')
    RM.select_your_last_name()
    RM.type_last_name()
    print('TCID 17 has been executed.')
    logging.info('TCID 17 has been executed.')

    #TCID 18: Checkout - Can a user enter an email address?
    print('Beginning TCID 18: Checkout - Can a user enter an email address?')
    logging.info('Beginning TCID 18: Checkout - Can a user enter an email address?')
    RM.select_email_address()
    RM.type_email_address()
    print('TCID 18 has been completed.')
    logging.info('TCID 18 has been completed.')

#TCID 19: Checkout - Can a user enter a new password?
    print('Beginning TCID 19: Checkout - Can a user enter a new password?')
    logging.info('Beginning TCID 19: Checkout - Can a user enter a new password?')
    RM.select_new_password()
    RM.type_password()
    print('TCID 19 has been completed.')
    logging.info('TCID 19 has been completed.')

    #TCID 20: Checkout - Can a user confirm a new password?
    print('Beginning TCID 20: Checkout - Can a user confirm a new password?')
    logging.info('Beginning TCID 20: Checkout - Can a user confirm a new password?')
    RM.select_confirm_password()
    RM.type_password()
    print('TCID 20 has been executed.')
    logging.info('TCID 20 has been executed.')

    #TCID 21: Checkout - Can a user enter a United MileagePlus acount number?
    print('Beginning TCID 21: Checkout - Can a user enter a United MileagePlus acount number?')
    logging.info('Beginning TCID 21: Checkout - Can a user enter a United MileagePlus acount number?')
    RM.select_reward_account()
    RM.type_reward_account()
    print('TCID 21 has been executed.')
    logging.info('TCID 21 has been executed.')

    #TCID 22: Checkout - Can a user enter a United MileagePlus first name?
    print('Beginning TCID 22: Checkout - Can a user enter a United MileagePlus first name?')
    logging.info('Beginning TCID 22: Checkout - Can a user enter a United MileagePlus first name?')
    RM.select_reward_first_name()
    RM.type_first_name()
    print('TCID 22 has been executed.')
    logging.info('TCID 22 has been executed.')

    #TCID 23: Checkout - Can a user enter a United MileagePlus last name?
    print('Beginning TCID 23: Checkout - Can a user enter a United MileagePlus last name?')
    logging.info('Beginning TCID 23: Checkout - Can a user enter a United MileagePlus last name?')
    RM.select_reward_last_name()
    RM.type_last_name()
    print('TCID 23 has been executed.')
    logging.info('TCID 23 has been executed.')

    #TCID 24 - 27: Checkout - Can a user enter a credit card number to the credit card number field?
    print('Beginning Checkout - Payment test series (TCIDs 24-27)')
    logging.info('Beginning Checkout - Payment test series (TCIDs 24-27)')
    time.sleep(3)
    RM.enter_cc_info()
    print('Checkout - Payment test series (TCIDs 24-27) have been executed.')
    logging.info('Checkout - Payment test series (TCIDs 24-27) have been executed.')

    #Precondition
    print('Switching to default frame.')
    RM.switch_to_default_frame()
    logging.info('Switched to default frame.')

    #TCID 28: Checkout - Can a user enter a billing zip code?
    print('Beginning TCID 28: Checkout - Can a user enter a billing zip code?')
    logging.info('Beginning Checkout - Can a user enter a billing zip code?')
    RM.select_billing_zip()
    RM.type_billing_zip()
    print('TCID 28 has been executed.')
    logging.info('TCID 28 has been executed.')

    #TCID 29: Checkout - Can a user check the Terms and Conditions checkbox?
    print('Beginning TCID 29: Checkout - Can a user check the Terms and Conditions checkbox?')
    logging.info('Beginning TCID 29: Checkout - Can a user check the Terms and Conditions checkbox?')
    RM.click_terms_checkbox()
    print('TCID 29 has been executed.')
    logging.info('TCID 29 has been executed.')

except Exception as err:
    logging.exception(str(err))

#Ending smoke test for Checkout module
print('Checkout module smoke test complete. Closing browser.')
RM.close_browser()
logging.info('Checkout module smoke test complete. Browser closed.')