from RocketMilesClass import RocketMiles
import time

RM = RocketMiles()

#Sandbox Preconditions
RM.open_checkout_page()
RM.close_cookie_banner()

#Sandbox
RM.select_guest_first_name()
RM.type_first_name()
RM.select_guest_last_name()
RM.type_last_name()
RM.select_your_first_name()
RM.type_first_name()
RM.select_your_last_name()
RM.type_last_name()
RM.select_email_address()
RM.type_email_address()
RM.select_new_password()
RM.type_password()
RM.select_confirm_password()
RM.type_password()
RM.select_reward_account()
RM.type_reward_account()
RM.select_reward_first_name()
RM.type_first_name()
RM.select_reward_last_name()
RM.type_last_name()
RM.select_cc_number()

'''
#Preconditions
RM.open_rocketMiles()
RM.close_popUp()
RM.close_cookie_banner()

#TCID 1: Main Page - Can a user enter a destination?
RM.select_destination_field()
RM.type_destination()
print('TCID 1 has been executed.')

#TCID 2: Main Page - Can a user enter a rewards program?
RM.select_rewards()
RM.type_rewards()
print('TCID 2 has been executed.')

#TCID 3: Main Page - Can a user select the end date field?
RM.click_end_date()
print('TCID 3 has been executed.')

#TCID 4: Main Page - Can a user select a start date?
RM.click_start_date()
RM.click_November_21()
print('TCID 4 has been executed.')

#TCID 5: Main Page - Can a user select an end date from the end date calendar?
RM.click_November_25()
print('TCID 5 has been executed.')

#TCID 6: Main Page - Can a user select the number of guests?
RM.select_guest_field()
RM.click_1_guest()
print('TCID 6 has been executed.')

#TCID 7: Main Page - Can a user select the number of rooms?
RM.select_rooms_field()
RM.click_1_room()
print('TCID 7 has been executed.')

#TCID 8: Main Page - Can a user select the Search button?
RM.click_search_properties_button()
print('TCID 8 has been executed.')

#TCID 9: Search Page - Can a user sort results by Miles using the Sort By dialogue box?
RM.select_sort_by_field()
RM.click_miles()
print('TCID 9 has been executed.')

#TCID 10: Search Page - Can a user select the "Select Now" button for the first listing?
RM.select_hotel()

#Preconditions for Hotel Details page tests, if they are run independently from the Main Page TCIDs (1-10).
#RM.open_hotel_details()
#RM.new_reward_banner()
#RM.close_cookie_banner()

#TCID 11: Hotel Details - Can a user select the Select A Room button?
RM.click_select_room_button()
print('TCID 11 has been executed.')

#TCID 12: Hotel Details - Hotel Details - Can a user select the View button?
RM.select_view_button()
print('TCID 12 has been executed.')

#TCID 13: Hotel Details - Can a user select the green Select button to choose a room?
RM.select_button()
print('TCID 13 has been executed.')

'''

