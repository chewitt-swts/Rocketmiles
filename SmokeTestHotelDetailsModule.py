from RocketMilesClass import RocketMiles
import time

#Smoke test for basic functionality of the Hotel Details page for the Rocketmiles.com search app.

#This module contains TCIDs 11-13.

RM = RocketMiles()

#Precondition for proceeding with smoke test
RM.open_hotel_details()
RM.new_reward_banner()
RM.close_cookie_banner()

#TCID 11: Hotel Details - Can a user select the Select A Room button?
print('Beginning TCID 11: Hotel Details - Can a user select the Select A Room button?')
RM.click_select_room_button()
print('TCID 11 has been executed.')

#TCID 12: Hotel Details - Can a user select the View button?
print('Beginning TCID 12: Hotel Details - Can a user select the View button?')
RM.select_view_button()
print('TCID 12 has been executed.')

#TCID 13: Hotel Details - Can a user select the green Select button to choose a room?
print('Beginning TCID 13: Hotel Details - Can a user select the green Select button to choose a room?')
RM.select_button()
print('TCID 13 has been executed.')

#Ending smoke test for Hotel Details module
print('Hotel Details module smoke test complete. Closing browser.')
RM.close_browser()