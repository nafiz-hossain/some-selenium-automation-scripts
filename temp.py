from ast import Return
import time
from concurrent.futures import thread
import imp
from lib2to3.pgen2 import driver
from multiprocessing.connection import wait
from time import sleep, time
from xml.dom.minidom import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


PATH = '/home/tigerit/TigerIT/projects/Automation/Selenium/chromedriver'
driver = webdriver.Chrome(PATH)

driver.get("https://app.asana.com/0/search?completion=complete&assignees.ids=1178664664160119&any_projects.ids=1202018702285777")


buttons = driver.find_element_by_xpath("//*[contains(text(), 'Continue with Google')]").click()

driver.find_element_by_name("identifier").send_keys("nafiz.hossain@tigerit.com")
driver.find_element_by_xpath("//*[contains(text(), 'পরবর্তী')]").click()


# #Find a element by class name and click on it
# driver.find_element_by_class_name("ThemeableRectangularButton--isEnabled ThemeableRectangularButton ThemeableRectangularButton--xlarge SecondaryButton--standardTheme SecondaryButton GoogleSignInButton--sparse GoogleSignInButton LoginDefaultView-ssoButton").click()


# #click on email and send keys
# driver.find_element_by_id("identifier").send_keys("nafiz.hossain@tigerit.com")
# time.sleep(1)
# driver.find_element_by_class_name("VfPpkd-dgl2Hf-ppHlrf-sM5MNb").click()

# #click on pass and send keys
# driver.find_element_by_name("password").send_keys("123456")
# time.sleep(1)
# driver.find_element_by_class_name("VfPpkd-dgl2Hf-ppHlrf-sM5MNb").click()


