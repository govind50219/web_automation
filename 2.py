from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

i=0 #no need to do so but doing is better
for i in range (0,2):
    #a for loop to execute the code 100 times
    browser = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')#connection to the browser to use selenium

    browser.get('https://docs.google.com/forms/d/e/1FAIpQLSfxsg59ggPdonbOLakPTwn_qQk-P0euw531kGt2pdDxSlnB9Q/viewform')#opening google form in chrome

    name = browser.find_element_by_name('entry.1156409')
    name.send_keys('Govind Gupta')
    #acces the element by name and input text Govind Gupta
    roll = browser.find_element_by_name('entry.210055283')
    roll.send_keys('190346')
    #filling roll no.
    python_script = browser.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[3]/div/div[2]/div/span/div/div[1]/label/div/div[1]/div')
    python_script.click()
    #clicking on the Yes option of using python script
    time.sleep(5)
    #time to sleep for 5 sec so that all data can fill
    github_page = browser.find_element_by_name('entry.446099277')
    github_page.send_keys('https://github.com/govind50219/web_automation')
    #provinding the link to this code
    time.sleep(5)
    #time to sleep for 5 sec so that all data can fill
    button=browser.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[3]/div[1]/div/div')
    button.click()
    #submitting the form
    time.sleep(5)
    #sleep for 5 sec to upload the form
    browser.close()
    #close the browser
    print(i)# print to know no. of times form filled
