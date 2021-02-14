# program takes email address and string of text on command line
# uses selenium to log into email address and send message to given email

'''
1. create a program that lets you read the command line 
    for a given email and a string. 
2. use selenium to log into your personal email address
3. send a message from your email to the given email
'''

from selenium import webdriver 
import sys, time

MY_EMAIL = '*****'
PASSWORD = '*****'
PATH = '/Users/danieltshibangu/Desktop/geckodriver'
browser = webdriver.Firefox(executable_path=PATH)
# open to my email path 
browser.get('https://login.yahoo.com/')

def found_tag(wd_obj):
    return 'Found <%s> element with that id name!' % (wd_obj.tag_name)

# TODO: create a function to get info from the command line 

if len(sys.argv) > 1: 
    target_address = ''.join( sys.argv[1])
    subject = ''.join(sys.argv[2])
    message = ' '.join( sys.argv[3:])
    complete_msg = "Hi\n\n" + message + "\n\nKind Regards"
else:
    print("INVALID ENTRY." +\
          "Provide a target email and an address.")



# TODO: use selenium to get to personal email 

try:
    # target the class that lets me enter the input 
    login_id = browser.find_element_by_id('login-username')
    # this sends data to the login box we have found 
    login_id.send_keys(MY_EMAIL)
except: 
    print( "Was not able to find that id name")

# find the next element that will confirm the email message 
# this is the button to comfirm email and take you to password screen
try: 
    confirm_button = browser.find_element_by_id('login-signin')
    #click on the button to go to the password screen
    confirm_button.click()
except: 
    print( "Couldn't find that button.")

# prompt message
print( "CONFIRMING EMAIL . . . ")



# TODO: add a special case if the username is wrong
try: 
    entry_error = browser.find_element_by_id('username-error')
    print( 'EMAIL CONFIRMED!')
except: 
    print( "Error message wasn't displayed.")
time.sleep(5)


# prompt message to confirm password
print( "CONFIRMING PASSWORD . . . ")



# TODO: Enter password for given email address using selenium 
try: 
    password_login = browser.find_element_by_id('login-passwd')
    password_login.send_keys(PASSWORD)
except:
    print("Was not able to find tag with that id!")

# find the next element that will confirm the email message 
# this button will NOW take you into your email
try: 
    confirm_button = browser.find_element_by_id('login-signin')
    #click on the button to go to the password screen
    confirm_button.click()
except: 
    print( "Couldn't find that button.")



# TODO: scan the page to get into the mail 
try:
    get_mail_link = browser.find_element_by_id('ybarMailLink')
    #click on the link to get into the mailbox 
    get_mail_link.click()
except:
    print( "Couldn't find link to mailbox.")

# click compose to start creating message 
try: 
    time.sleep(3)
    compose_message = browser.find_element_by_link_text('Compose')
    compose_message.click() 
except:
    print( "That class name was not found.")


# TODO: now send the email to the specified email address 

# first fill in the 'to' field 
try: 
    to_field = browser.find_element_by_id("message-to-field")
    to_field.send_keys(target_address)
except:
    print("The id name was not found!")


# second fill out the 'subject' field 
try: 
    subject_field = browser.find_element_by_xpath("//input[@placeholder='Subject']") 
    subject_field.send_keys(subject)
except:
    print("The id name was not found!")


#lastly fill out the message field 
try: 
    msg_field = browser.find_element_by_xpath("//div[@role='textbox']") 
    msg_field.send_keys(complete_msg)
except:
    print("The id name was not found!")

# press the send button 
try: 
    send_button = browser.find_element_by_xpath("//button[@title='Send this email']") 
    send_button.click()
except:
    print("The id name was not found!")

print( 'Successfully Completed.')
