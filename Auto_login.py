from multiprocessing.sharedctypes import Value
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import getpass
import time
import requests
from bs4 import BeautifulSoup
from time import sleep

from selenium.webdriver.firefox.webdriver import WebDriver
import Credential
Username = Credential.username  #import ID from the credential file.
Password = Credential.passkey   #import password from the credential file

#open ms teams main page
browser = webdriver.Chrome("D:\Setups\Chrome webdriver\Chrome93\chromedriver_win32\chromedriver.exe")
browser.get('https://www.microsoft.com/en-in/microsoft-teams/group-chat-software')

#click on the sign-in button on the page
try:
    SignIn_button = browser.find_element_by_xpath('//*[@id="feature-oc73a9"]/div/div/div[1]/div/div[2]/div[2]/a')
    SignIn_button.click()
except:
    browser.find_element_by_xpath('/html/body/section/div[2]/div/section/div[1]/div/div/div/div/div/div[2]/a').click()
#wait for 7 sec before execution of the next code
time.sleep(7)
#switch control to next tab
browser.switch_to_window(browser.window_handles[1])
time.sleep(5)

#input username to the active element that is username box and click to next
browser.switch_to_active_element().send_keys(Username)
time.sleep(5)

Next_button = browser.find_element_by_xpath('//*[@id="idSIButton9"]')
Next_button.click()
time.sleep(5)

#enter password and click to next
browser.switch_to_active_element().send_keys(Password)
time.sleep(2)
browser.find_element_by_xpath('//*[@id="idSIButton9"]').click()

browser.maximize_window() # maximize the window

try:
    browser.find_element_by_xpath('/html/body/div/form/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div[2]/div/div[3]/div[1]/div').click()
    time.sleep(2)
except:    
    browser.find_element_by_xpath('//*[@id="idSIButton9"]').click()

finally:
    print("You are now in ms-teams.......")

el = WebDriverWait(browser).until(lambda d: d.find_element_by_id("0d4a5d3b-7218-4ec3-8519-c5f346bc3b71"),20)
assert el.text == "Hello from JavaScript!"
browser.find_element_by_id("0d4a5d3b-7218-4ec3-8519-c5f346bc3b71").click()
browser.implicitly_wait(10)


#change from grid view to list view
# try:
#     browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[1]/teams-grid/div/div[1]/div/school-app-settings-button/button/svg-include/svg/g/path[1]').click()
# except:
#     browser.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div[1]/teams-grid/div/div[1]/div/school-app-settings-button/button/svg-include/svg').click()
# try:
#     browser.find_element_by_xpath('/html/body/div[7]/ul/li[2]/button/span').click()
# except:
#     browser.find_element_by_xpath('/html/body/div[6]/ul/li[2]/button/span').click()
# try:
#     browser.find_element_by_xpath('/html/body/div[7]/div[2]/div/div/div/div[2]/div/section[2]/div[1]/div/div/div/div[1]/div[2]/ul/li[2]/svg-include/svg/g[1]/path[4]').click()
# except:
#     browser.find_element_by_xpath('/html/body/div[6]/div[2]/div/div/div/div[2]/div/section[2]/div[1]/div/div/div/div[1]/div[2]/ul/li[2]/svg-include/svg/g[1]/path[2]').click()

# link = browser.current_url #get the url of the current webpage
# webpage_content = requests.get(link)
# print(webpage_content.text)
# print("##########################################################################################################################################################")
# page = webpage_content.text
# soup = BeautifulSoup(page,"lxml")
# print(soup.prettify())

# def meet_join():
#     calender = WebDriverWait(browser).until(lambda a: a.find_element_by_text("Calender"))
#     assert calender.click()
#     join = WebDriverWait(browser).until(lambda b:b.find_element_by_text("Join"))
#     assert join.click()                                         

# meet_join()

# print("If you want to close the teams press any key")
# any_key = input()
# try:
#     any_key == ' '
#     browser.quit()
# except:
#     browser.quit()


