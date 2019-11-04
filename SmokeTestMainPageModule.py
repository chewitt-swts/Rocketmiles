from RocketMilesClass import RocketMiles
import time

#Smoke test for basic functionality of the Main Page for the Rocketmiles.com search app.

#This module contains TCIDs 1-8.

RM = RocketMiles()

#Preconditions
RM.open_rocketMiles()
RM.close_popUp()
RM.close_cookie_banner()

#TCID 1: Main Page - Can a user enter a destination?
print('Beginning TCID 1: Main Page - Can a user enter a destination?')
RM.select_destination_field()
RM.type_destination()
print('TCID 1 has been executed.')

#TCID 2: Main Page - Can a user enter a rewards program?
print('Beginning TCID 2: Main Page - Can a user enter a rewards program?')
RM.select_rewards()
RM.type_rewards()
print('TCID 2 has been executed.')

#TCID 3: Main Page - Can a user select the end date field?
print('Beginning TCID 3: Main Page - Can a user select the end date field?')
RM.click_end_date()
print('TCID 3 has been executed.')

#TCID 4: Main Page - Can a user select a start date?
print('Beginning TCID 4: Main Page - Can a user select a start date?')
RM.click_start_date()
RM.click_November_21()
print('TCID 4 has been executed.')

#TCID 5: Main Page - Can a user select an end date from the end date calendar?
print('Beginning TCID 5: Main Page - Can a user select an end date from the end date calendar?')
RM.click_November_25()
print('TCID 5 has been executed.')

#TCID 6: Main Page - Can a user select the number of guests?
print('Beginning TCID 6: Main Page - Can a user select the number of guests?')
RM.select_guest_field()
RM.click_1_guest()
print('TCID 6 has been executed.')

#TCID 7: Main Page - Can a user select the number of rooms?
print('Beginning TCID 7: Main Page - Can a user select the number of rooms?')
RM.select_rooms_field()
RM.click_1_room()
print('TCID 7 has been executed.')

#TCID 8: Main Page - Can a user select the Search button?
print('Beginning TCID 8: Main Page - Can a user select the Search button?')
RM.click_search_properties_button()
print('TCID 8 has been executed.')

#Ending smoke test for Main Page module
print('Main Page module smoke test complete. Closing browser.')
RM.close_browser()