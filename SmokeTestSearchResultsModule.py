from RocketMilesClass import RocketMiles
import time

#Smoke test for basic functionality of the Search Results page for the Rocketmiles.com search app.

#This module contains TCIDs 9-10.

RM = RocketMiles()

#Preconditions
RM.open_search_page()
RM.close_cookie_banner()

#TCID 9: Search Page - Can a user sort results by Miles using the Sort By dialogue box?
print('Beginning TCID 9: Search Page - Can a user sort results by Miles using the Sort By dialogue box?')
RM.select_sort_by_field()
RM.click_miles()
print('TCID 9 has been executed.')

#TCID 10: Search Page - Can a user select the "Select Now" button for the first listing?
print('Beginning TCID 10: Search Page - Can a user select the "Select Now" button for the first listing?')
RM.select_hotel()
print('TCID 10 has been executed.')

#Ending smoke test for Searc Results module
print('Search Results module smoke test complete. Closing browser.')
RM.close_browser()