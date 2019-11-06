from RocketMilesClass import RocketMiles
import time
import logging.handlers
import datetime
import os

#Smoke test for basic functionality of the Search Results page for the Rocketmiles.com search app.

#This module contains an error logger, test preconditions, and TCIDs 9-10.


#Initializing class object.
RM = RocketMiles()


#Error Logger

    #Create a new log folder if none exists, then the log file.
try:
    os.mkdir('logs/')
except:
    print()

try:
    os.mkdir('logs/SearchResultsModule')
except:
    print()

    #Creating log filepath. Syntax is an acronym for the module (in this case, Smoke Test Checkout), followed by a Year_Month_Day__Hour_Minute_Second timestamp.
logSuffix = datetime.datetime.now()
logName = 'logs/SearchResultsModule/STSR_log_' + logSuffix.strftime('%Y_%m_%d__%H%M_%S') + '.log'

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
    RM.open_search_page()
    RM.close_cookie_banner()
    RM.loadtime()
except Exception as err:
    print(str(err))
    logging.exception(str(err))


#Smoke Test for Search Results (TCIDs 9-10),
try:
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

except Exception as err:
    logging.exception(str(err))

#Ending smoke test for Search Results module.
print('Search Results module smoke test complete. Closing browser.')
RM.close_browser()
logging.info('Search Results module smoke test complete. Browser closed.')