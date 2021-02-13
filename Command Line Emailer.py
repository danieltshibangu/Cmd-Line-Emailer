# program takes email address and string of text on command line
# uses selenium to log into email address and send message to given email

'''
1. create a program that lets you read the command line 
    for a given email and a string. 
2. use selenium to log into your personal email address
3. send a message from your email to the given email
'''

from selenium import webdriver 
import sys
from selenium.common.exceptions import NoSuchElementException
import time

# TODO: create a function to get info from the command line 

if len(sys.argv) > 1: 
    address = ' '.join( sys.argv[1])
    message = ' '.join( sys.argv[2:])
else:
    print("INVALID ENTRY." +\
    "Provide a target email and an address.")

# TODO: use selenium to get to personal email 

MY_EMAIL = '*****'
PATH = '/Users/danieltshibangu/Desktop/geckodriver'
browser = webdriver.Firefox(executable_path=PATH)

# open to my email path 
browser.get('https://login.yahoo.com/')

try:
    # target the class that lets me enter the input 
    login_id = browser.find_element_by_id('login-username')
    if login_id.is_displayed():
        print('Found <%s> element with that id name!' % (login_id.tag_name))
except: 
    print( "Was not able to find that id name")

# once we find the tag we can modify it
# webElement onjects have a built in method to send it data
# this sends data to the login box we have found 
login_id.send_keys(MY_EMAIL)

# find the next element that will confirm the email message 
# this is the button to comfirm email and take you to password screen
try: 
    confirm_button = browser.find_element_by_id('login-signin')
    if confirm_button.is_displayed():
        print( 'Found <%s> element with that id name!' % (confirm_button.tag_name))
except: 
    print( "Couldn't find that button.")

#click on the button to go to the password screen
confirm_button.click()
print( "CONFIRMING EMAIL . . . ")

# a special case if the email is not correct or ws entered incorrectly
try: 
    entry_error = browser.find_element_by_id('username-error')
    if entry_error.is_displayed():
        print( "Email address denied. Enter a correct email address.")
    else: 
        print( 'EMAIL CONFIRMED!')
except: 
    print( "Error message wasn't displayed.")
time.sleep(10)



# TODO: Enter password for given email address using selenium 
PASSWORD = '*****!'

try: 
    password_login = browser.find_element_by_id('login-passwd')
    if password_login.is_displayed():
        print( 'Found <%s> element with that id name!' % (password_login.tag_name))
        password_login.send_keys(PASSWORD)
except:
    print("Was not able to find tag with that id!")





# find the next element that will confirm the email message 
# this button will NOW take you into your email
try: 
    confirm_button = browser.find_element_by_id('login-signin')
    if confirm_button.is_displayed():
        print( 'Found <%s> element with that id name!' % (confirm_button.tag_name))
except: 
    print( "Couldn't find that button.")

#click on the button to go to the password screen
confirm_button.click()
print( "CONFIRMING PASSWORD . . . ")







