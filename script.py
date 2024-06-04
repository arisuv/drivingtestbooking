from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import  ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
import smtplib
import time
from win32com.client import Dispatch

go = True

while go == True:
    USERNAME = "username"
    PASSWORD = "password"
    sender = "sender@gmail.com"
    reciver = "reciver@gmail.com"
    sender_password = "senderpassord"
    message = "avilable dates DS"
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.minimize_window()
    driver.get("https://jeddahds.com.sa/Home/Timetable")
    user_input = driver.find_element_by_id('IDNumber')
    user_input.send_keys(USERNAME)
    time.sleep(2)
    password_input = driver.find_element_by_id('Password')
    password_input.send_keys(PASSWORD)
    time.sleep(2)
    password_input.submit()
    driver.execute_script("window.scrollTo(0, 1000)") 
    time.sleep(2)
    driver.implicitly_wait(200)
    time.sleep(2)
    account = driver.find_element_by_xpath('//*[@id="tt-header"]/div[3]/div/div/div[2]/div/a')
    driver.execute_script("arguments[0].click();", account)
    time.sleep(2)
    book = driver.find_element_by_xpath('//*[@id="kt_content"]/div/div/div/div[1]/div/div[2]/div[2]/div[2]/div[2]/a').click()
    time.sleep(2)
    driver.execute_script("document.body.style.zoom='90%'")
    time.sleep(2)
    driver.execute_script("window.scrollTo(0,400)")
    time.sleep(1)
    dates = driver.find_element_by_xpath('//*[@id="kt_content"]/div/div/div/div/div[2]/div/div/div/table/tbody/tr[10]/td[11]/a')
    driver.execute_script("arguments[0].click();", dates)
    time.sleep(2)
    driver.implicitly_wait(200)
    time.sleep(1)
    accept = driver.find_element_by_xpath('//*[@id="kt_body"]/div[5]/div[3]/div/button[1]')
    driver.execute_script("arguments[0].click();", accept)
    aug15 = "15-Aug-2021"
    aug16 = "16-Aug-2021"
    speak = Dispatch("SAPI.SpVoice").Speak
    if aug15 in driver.page_source or aug16 in driver.page_source:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender, sender_password)
        server.sendmail(sender,reciver,message)
        speak("avilable dates")
        speak("avilable dates")
        speak("avilable dates")
        speak("avilable dates")
        driver.close()
        time.sleep(400) #go = False break 
    else:		
        driver.close()
        time.sleep(1800)
