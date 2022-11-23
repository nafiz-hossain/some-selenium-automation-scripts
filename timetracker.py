from re import A
import time
from concurrent.futures import thread
import imp
from lib2to3.pgen2 import driver
from multiprocessing.connection import wait
from time import *
from xml.dom.minidom import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import pyautogui as pya
import pyperclip  # handy cross-platform clipboard text handler
import time



def copy_clipboard():
    sleep(1)
    pya.hotkey('ctrl', 'a')
    pya.hotkey('ctrl', 'c')



def login():
    driver.find_element_by_name("_username").send_keys("nafiz.hossain@tigerit.com")
    #driver.implicitly_wait(1)
    driver.find_element_by_name("_password").send_keys("life129261")
    #driver.implicitly_wait(1)
    button = driver.find_element_by_xpath("//button[text()='Login']")
    #driver.implicitly_wait(10)
    ActionChains(driver).move_to_element(button).click(button).perform()


def createTask():
    duration = 1
    customer= "International Consumer"
    project="CommChat Desktop"
    Activity= "Testing"
    paste = (pyperclip.paste())

    #customer
    driver.get("https://timetracker.tigeritbd.com/index.php/en/timesheet/create")
    timeout = 5
    element_present = EC.presence_of_element_located((By.ID,'timesheet_edit_form_duration'))
    WebDriverWait(driver, timeout).until(element_present)
  

   
    actions = ActionChains(driver) 
    actions.send_keys(duration)
   
    #customer
    actions.send_keys(Keys.TAB)
    actions.send_keys(Keys.TAB)
    actions.send_keys(Keys.ENTER)
    actions.send_keys(customer)
    actions.send_keys(Keys.ENTER)

    #Project
    actions.send_keys(Keys.TAB)
    actions.send_keys(Keys.ENTER)
    actions.send_keys(project)
    actions.send_keys(Keys.ENTER)
    
    #Activity
    if ((paste[:3]) == "Inv"):
        Activity= "Other"
    if ((paste[:3]) == "Mee"):
        Activity= "Meeting"
    if ((paste[:3]) == "Fol"):
            Activity= "Follow up"       
    if ((paste[:3]) == "Rea"):
        Activity= "Research"    

    actions.send_keys(Keys.TAB)
    actions.send_keys(Keys.ENTER)
    actions.send_keys(Activity)
    actions.send_keys(Keys.ENTER)
  
    #Description
    actions.send_keys(Keys.TAB)
    description = "Checking the change of "+ paste
    if ((paste[:3]) == "Inv"):
        description = "Investigation on: " + paste.split(' ', 1)[1]
    if ((paste[:3]) == "Mee"):
        description= "Meeting regarding: "+ paste.split(' ', 1)[1]
    if ((paste[:3]) == "Rea"):
        description= "Studied about: " + paste.split(' ', 1)[1]
    if ((paste[:3]) == "Fol"):
            description= "Following up task: " + paste.split(' ', 1)[1]
    actions.send_keys(description)
    actions.send_keys(Keys.TAB)
    actions.send_keys(Keys.TAB) 
    actions.send_keys(Keys.TAB)
    actions.send_keys(Keys.ENTER)


    #perform all pending actions by Keys
    actions.perform()



if __name__ == '__main__':
    copy_clipboard()

    PATH = '/home/tigerit/TigerIT/projects/Automation/Selenium/chromedriver'
    driver = webdriver.Chrome(PATH)
    driver.get("https://timetracker.tigeritbd.com/index.php/en/login")
    timeout = 5
    element_present = EC.presence_of_element_located((By.ID,'remember_me'))
    WebDriverWait(driver, timeout).until(element_present)
    login()
    createTask()
