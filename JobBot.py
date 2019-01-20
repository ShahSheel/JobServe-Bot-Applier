from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time

options = webdriver.ChromeOptions()
options.add_argument('headless')
print("Running in headless mode")
options.binary = 'C:\\chromedriver\\chromedriver.exe'

LOCATION = "London"
JOB_TITLE = "Graduate Software Developer"
DISTANCE = 3 #0  = 1 mile , 1 = 5 miles,2 = 10 miles, 3 = 15 miles, 4 = 25, 5 = 50, 6 = 75, 7 = 100
EMAIL = "shahsheel@outlook.com"
PASSWORD = "NthQwA3J8DXsm7S"
MAX_APPLIED = 27 #Does not do the first 2
COUNT = 0
APPLIEDJOBS = []

driver = webdriver.Chrome(chrome_options=options)
path = "https://www.jobserve.com/gb/en/Candidate/Login.aspx"
driver.get(path)

#------------------LOGIN ---------------------------------
print("Accepting cookies")

accept_cookes = driver.find_element_by_xpath('//*[@id="PolicyOptInLink"]')
accept_cookes.click()

email = driver.find_element_by_xpath('//*[@id="txbEmail"]')
email.click()
email.send_keys(EMAIL)

password = driver.find_element_by_xpath('//*[@id="txbPassword"]')
password.click()
password.send_keys(PASSWORD)
password.send_keys(Keys.RETURN)

home = driver.find_element_by_xpath('//*[@id="mnuouter"]/ul[1]/li[1]/a') #Takes to home screen
home.click()

print("Logged in")

#------------------SEARCH ---------------------------------
ps = driver.find_element_by_xpath('//*[@id="tab_pqs"]')
ps.click()

job_title = driver.find_element_by_xpath('//*[@id="txtTitle"]')
job_title.click()
job_title.send_keys(JOB_TITLE)

location = driver.find_element_by_xpath('//*[@id="txtLoc"]')
location.click()
location.send_keys(LOCATION)
#location.send_keys(Keys.RETURN)

select = Select(driver.find_element_by_xpath('//*[@id="selRad"]'))
select.select_by_index(DISTANCE)

location.click()
location.send_keys(Keys.RETURN)


#-------------Adding jobs to basket --------------------------
print("Waiting 30 seconds")
time.sleep(30) #Safe wait. Depends on internet connection.
print("Adding jobs to the basket")
actions = ActionChains(driver)

while(COUNT <= MAX_APPLIED):
    try:
        add_job =  driver.find_element_by_xpath('//*[(@id = "td_addbskt_btn")]')
        add_job.click()
        COUNT+=1
        actions.send_keys(Keys.ARROW_DOWN)
        actions.perform()
        time.sleep(1)
        print("Job added #1")
    except ElementNotVisibleException:
        print("Already applied")
        actions.send_keys(Keys.ARROW_DOWN)
        actions.perform()
        time.sleep(2)


