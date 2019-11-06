from RocketMilesClass import RocketMiles
import time
import logging.handlers
import datetime
import os

#Smoke test for basic functionality of the Main Page for the Rocketmiles.com search app.

#This module contains an error logger, test preconditions, and TCIDs 1-8.


#Initializing class object.
RM = RocketMiles()


#Error Logger

    #Create a new log folder if none exists, then the log file.
try:
    os.mkdir("logs/")
except:
    print()

try:
    os.mkdir('logs/SmokeTestMainPageModule')
except:
    print()

    #Creating log filepath. Syntax is an acronym for the module (in this case, Smoke Test Checkout), followed by a Year_Month_Day__Hour_Minute_Second timestamp.
logSuffix = datetime.datetime.now()
logName = "logs/SmokeTestMainPageModule/STMP_log_" + logSuffix.strftime("%Y_%m_%d__%H%M_%S") + ".log"

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
    print('Starting smoke test preconditions.')
    RM.open_rocketMiles()
    RM.close_popUp()
    RM.close_cookie_banner()
    RM.loadtime()
except Exception as err:
    print(str(err))
    logging.exception(str(err))


#Smoke Test for all modules (TCIDs 1-8).
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

except Exception as err:
    logging.exception(str(err))

#Ending smoke test for Main Page module,
print('Main Page module smoke test complete. Closing browser.')
RM.close_browser()
logging.info('Main Page module smoke test complete. Browser closed.')