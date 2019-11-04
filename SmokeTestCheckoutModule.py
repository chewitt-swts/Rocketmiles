from RocketMilesClass import RocketMiles
import time

#Smoke test for basic functionality of the Checkout page for the Rocketmiles.com search app.

#This module contains TCIDs 14-28.

RM = RocketMiles()

#Preconditions
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
except Exception as err:
    print(str(err))

#TCID 14: Checkout - Can a user enter a Guest First Name?
print('Beginning TCID 14: Checkout - Can a user enter a Guest First Name?')
RM.select_guest_first_name()
RM.type_first_name()
print('TCID 14 has been executed.')

#TCID 15: Checkout - Can a user enter a Guest Last Name?
print('Beginning TCID 15: Checkout - Can a user enter a Guest Last Name?')
RM.select_guest_last_name()
RM.type_last_name()
print('TCID 15 has been executed.')

#TCID 16: Checkout - Can a user enter Your First Name?
print('Beginning TCID 16: Checkout - Can a user enter Your First Name?')
RM.select_your_first_name()
RM.type_first_name()
print('TCID 16 has been executed.')

#TCID 17: Checkout - Can a user enter Your Last Name?
print('Beginning TCID 17: Checkout - Can a user enter Your Last Name?')
RM.select_your_last_name()
RM.type_last_name()
print('TCID 17 has been executed.')

#TCID 18: Checkout - Can a user enter an email address?
print('Beginning TCID 18: Checkout - Can a user enter an email address?')
RM.select_email_address()
RM.type_email_address()
print('TCID 18 has been completed.')

#TCID 19: Checkout - Can a user enter a new password?
print('Beginning TCID 19: Checkout - Can a user enter a new password?')
RM.select_new_password()
RM.type_password()
print('TCID 19 has been completed.')

#TCID 20: Checkout - Can a user confirm a new password?
print('Beginning TCID 20: Checkout - Can a user confirm a new password?')
RM.select_confirm_password()
RM.type_password()
print('TCID 20 has been executed.')

#TCID 21: Checkout - Can a user enter a United MileagePlus acount number?
print('Beginning TCID 21: Checkout - Can a user enter a United MileagePlus acount number?')
RM.select_reward_account()
RM.type_reward_account()
print('TCID 21 has been executed.')

#TCID 22: Checkout - Can a user enter a United MileagePlus first name?
print('Beginning TCID 22: Checkout - Can a user enter a United MileagePlus first name?')
RM.select_reward_first_name()
RM.type_first_name()
print('TCID 22 has been executed.')

#TCID 23: Checkout - Can a user enter a United MileagePlus last name?
print('Beginning TCID 23: Checkout - Can a user enter a United MileagePlus last name?')
RM.select_reward_last_name()
RM.type_last_name()
print('TCID 23 has been executed.')

#TCID 24 - 27: Checkout - Can a user enter a credit card number to the credit card number field?
print('Beginning Checkout - Payment test series (TCIDs 24-27)')
time.sleep(3)
RM.enter_cc_info()
print('Checkout - Payment test series (TCIDs 24-27) have been executed.')

#Precondition
RM.switch_to_default_frame()

#TCID 28: Checkout - Can a user enter a billing zip code?
RM.select_billing_zip()
RM.type_billing_zip()

#TCID 29: Checkout - Can a user check the Terms and Conditions checkbox?
RM.click_terms_checkbox()

#Ending smoke test for Checkout module
print('Checkout module smoke test complete. Closing browser.')
RM.close_browser()