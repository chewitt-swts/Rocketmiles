from RocketMilesClass import RocketMiles
import time
import logging.handlers
import datetime
import os

#Smoke test for basic functionality of the Hotel Details page for the Rocketmiles.com search app.

#This module contains an error logger, test preconditions, and TCIDs 11-13.


#Initializing class object.
RM = RocketMiles()


#Error Logger

    #Create a new log folder if none exists, then the log file.
try:
    os.mkdir('logs/')
except:
    print()

try:
    os.mkdir('logs/SmokeTestHotelDetailsModule')
except:
    print()

 #Creating log filepath. Syntax is an acronym for the module (in this case, Smoke Test Hotel Details), followed by a Year_Month_Day__Hour_Minute_Second timestamp.
logSuffix = datetime.datetime.now()
logName = 'logs/SmokeTestHotelDetailsModule/STHD_log_' + logSuffix.strftime('%Y_%m_%d__%H%M_%S') + '.log'

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


#Precondition for proceeding with smoke test
try:
    logging.info('Starting smoke test preconditions.')
    print('Starting smoke test preconditions.')
    RM.open_hotel_details()
    RM.new_reward_banner()
    RM.close_cookie_banner()
    RM.loadtime()
except Exception as err:
    print(str(err))
    logging.exception(str(err))


#Smoke Test for Hotel Details (TCIDs 11-13).
try:

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

except Exception as err:
    logging.exception(str(err))

#Ending smoke test for Hotel Details module
print('Hotel Details module smoke test complete. Closing browser.')
RM.close_browser()
logging.info('Hotel Details module smoke test complete. Browser closed.')