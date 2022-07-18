from concurrent.futures import thread
import imp
from lib2to3.pgen2 import driver
from time import sleep, time
from xml.dom.minidom import Element
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


PATH = '/home/tigerit/TigerIT/projects/Automation/Selenium/chromedriver'
driver = webdriver.Chrome(PATH)

driver.get("https://app.asana.com/0/search?completion=complete&assignees.ids=1178664664160119&any_projects.ids=1202018702285777")
print(driver.title)
#buttons = driver.find_element_by_xpath("//*[contains(text(), 'Continue with Google')]").click()
elem = driver.find_element_by_link_text("Continue with Google")
print('##########'+ elem)

#em = driver.find_element_by_id("email")
#em.send_keys("nhremon")
#passw = driver.find_element_by_id("pass")
#passw.send_keys("123456")
#passw.send_keys(Keys.RETURN)

actions = ActionChains(driver)
actions.send_keys('nafiz.hossain@tigerit.com')
actions.perform()

driver.find_element_by_xpath("//*[contains(text(), 'পরবর্তী')]").click()

actions1 = ActionChains(driver)
actions1.send_keys('life129261121366')
actions1.perform()
driver.find_element_by_xpath("//*[contains(text(), 'পরবর্তী')]").click()


driver.quit()