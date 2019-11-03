from RocketMilesClass import RocketMiles

RM = RocketMiles()

#Sandbox Preconditions
#Sandbox




#Preconditions
RM.open_rocketMiles()
RM.close_popUp()
RM.close_cookie_banner()

#TCID 1: Main Page - Can a user enter a destination?
RM.select_destination_field()
RM.type_destination()

#TCID 2: Main Page - Can a user enter a rewards program?
RM.select_rewards()
RM.type_rewards()

#TCID 3: Main Page - Can a user select the end date field?
RM.click_end_date()

#TCID 4: Main Page - Can a user select a start date?
RM.click_start_date()
RM.click_November_21()

#TCID 5: Main Page - Can a user select an end date from the end date calendar?
RM.click_November_25()

#TCID 6: Main Page - Can a user select the number of guests?
RM.select_guest_field()
RM.click_1_guest()

#TCID 7: Main Page - Can a user select the number of rooms?
RM.select_rooms_field()
RM.click_1_room()

#TCID 8: Main Page - Can a user select the Search button?
RM.click_search_properties_button()

#TCID 9: Search Page - Can a user sort results using the Sort By dialogue box?
RM.select_sort_by_field()
RM.click_miles()

#TCID 10: Search Page - Can a user select the "Select Now" button for the first listing?
RM.select_hotel()

#Preconditions
#RM.open_hotel_details()
RM.new_reward_banner()
RM.close_cookie_banner()

#TCID 11: Hotel Details - Can a user select the Select A Room button?
RM.click_select_room_button()

#TCID 12: Hotel Details - Hotel Details - Can a user select the View button?
RM.select_view_button()

#TCID 13: Hotel Details - Can a user select the green Select button to choose a room?
RM.select_button()





