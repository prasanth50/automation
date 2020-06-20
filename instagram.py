from time import sleep
from selenium import webdriver
#from selenium.webdriver.common.keys import keys
path="C:\Program Files (x86)\chromedriver.exe"
user_id=input('Enter your user_id:')
password=input('Enter your password:')
name=input('Enter the name of person:')
message=input('Enter the message:')
driver= webdriver.Chrome(path)
driver.get('https://www.instagram.com/')
sleep(2)
username=driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input')\
.send_keys(user_id)

psw=driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input')\
.send_keys(password)

login=driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]')\
    .click()
sleep(3)

notnow=driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')\
    .click()
sleep(3)
notnow=driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')\
    .click()
sleep(3)
search=driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[2]/a/div/div')\
    .click()
sleep(3)
search1=driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div/button')\
    .click()
s3=driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div[1]/div/div[2]/input')\
    .send_keys(name)
sleep(3)
s4=driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div[2]/div[1]/div/div[3]/button/span')\
    .click()

next=driver.find_element_by_xpath('/html/body/div[4]/div/div/div[1]/div/div[2]/div/button')\
    .click()
sleep(2)
msg=driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')\
    .send_keys(message)

send=driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button')\
    .click()
