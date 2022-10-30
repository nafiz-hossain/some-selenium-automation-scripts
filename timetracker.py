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




def login():
    driver.find_element_by_name("_username").send_keys("nafiz.hossain@tigerit.com")
    driver.find_element_by_name("_password").send_keys("life129261")
    
    button = driver.find_element_by_xpath("//button[text()='Login']")
    driver.implicitly_wait(10)
    ActionChains(driver).move_to_element(button).click(button).perform()


def createTask():
    #customer
    driver.get("https://timetracker.tigeritbd.com/index.php/en/timesheet/create")
    button = driver.find_element_by_id("select2-timesheet_edit_form_customer-container")
    driver.implicitly_wait(10)
    ActionChains(driver).move_to_element(button).click(button).perform()
    button.send_keys("International consumer")


    #button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'select2-timesheet_edit_form_customer-container')))
    #driver.find_element_by_class_name("select2-search__field").send_keys("International Consumer")

    # #project
    # button = driver.find_element_by_class_name("timesheet_edit_form_duration")
    # driver.implicitly_wait(10)
    # ActionChains(driver).move_to_element(button)
    driver.find_element_by_id("timesheet_edit_form_duration").send_keys("2")
    #button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'timesheet_edit_form_duration')))





if __name__ == '__main__':
    PATH = '/home/tigerit/TigerIT/projects/Automation/Selenium/chromedriver'
    driver = webdriver.Chrome(PATH)
    driver.get("https://timetracker.tigeritbd.com/index.php/en/login")
    login()
    createTask()