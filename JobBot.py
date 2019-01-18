from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.select import Select
import time

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.binary = 'C:\\chromedriver\\chromedriver.exe'

LOCATION = "London"
JOB_TITLE = "Graduate Software Developer"
DISTANCE = 3 #0  = 1 mile , 1 = 5 miles,2 = 10 miles, 3 = 15 miles, 4 = 25, 5 = 50, 6 = 75, 7 = 100
EMAIL = "EMAIL ADDRESS HERE"
PASSWORD = "PASSWORD HERE"
MAX_APPLIED = 27 #Does not do the first 2

driver = webdriver.Chrome(chrome_options=options)
print("Running in headless mode")
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

#keywords = driver.find_element_by_xpath('//*[@id="txtKey"]')
#keywords.sendKeys();
#keywords.sendKeys(Keys.RETURN);

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

#next_job = driver.find_element_by_xpath('//*[@id="jobreslist_outercontainer"]/div/div[2]/div')
#next_job.click()
#next_job.send_keys(Keys.ARROW_DOWN)
COUNT = 0
while(COUNT <= MAX_APPLIED):
    add_job =  driver.find_element_by_xpath('//*[(@id = "td_addbskt_btn")]')
    add_job.click()
    COUNT+=1
    time.sleep(2)
    actions = ActionChains(driver)
    actions.send_keys(Keys.ARROW_DOWN)
    actions.perform()
    print("Job added")


apply = driver.find_element_by_xpath('//*[@id="basketLinkMini"]')
apply.click()

time.sleep(5)
applyButton = driver.find_element_by_xpath('//*[@id="body"]/div[6]/div[3]/div/button[1]')
applyButton.click()

print("Jobs are ready to be applied for")

