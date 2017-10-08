#NOT REEADY YET....COMMMENT LINES OUT AND TRY AT YOUR OWN RISK.
#PROGRAMS MAY EVALUATE TO 0%
#CODE WRITTEN MIGHT GET ERASED

#INSTALL PYTHON ON YOUR SYSTEM
#INSTALL SELENIUM WEBDRIVER ON YOUR SYSTEM
#COPY THE PROGRAM AND SAVE IT IN A TEXT FILE WITH EXTENSION .py
#       FOR EXAMPLE : scilabprintreport.py
#OPEN TERMINAL/COMMAND PROMPT
#CHANGE YOUR DIRECTORY TO WHERE YOU HAVE SAVED THE TEXT FILE
#RUN THE PROGRAM BY TYPING - python scilabprintreport.py

#############################################################################################################################################
#IMPORTS

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

#############################################################################################################################################
#INPUT PAGE DETAILS

print("Enter your branch\n1>CSE\n2>IT\n3>Software\n> ")
branch = int(input())
print("\n1>OOPS\n2>DS\n> ")
lab = int(input())

#############################################################################################################################################
#OPEN REQUESTED PAGE

if branch == 1 and lab == 1 :
    driver.get("http://ulc.srmuniv.ac.in/elabcsecpp/") #CSE OOPS
elif branch == 1 and lab == 2 :
    driver.get("http://ulc.srmuniv.ac.in/elabcseds/") #CSE DS
elif branch == 2 and (lab == 1 or lab == 2) :
    driver.get("http://ulc.srmuniv.ac.in/elabitcppds/") #IT OOPS/DS
elif branch == 3 and (lab == 1 or lab == 2) :
    driver.get("http://ulc.srmuniv.ac.in/elabswecppds/") #SOFT OOPS/DS

#############################################################################################################################################
#INPUT LOGIN DETAILS

print("Enter your Registration Number\n> ")
RegNo = input()
print("\nEnter your Password\n>")
Pass = input()

#############################################################################################################################################
#EXECUTE LOGIN PROCESS

elemId = driver.find_element_by_id('username')
elemId.send_keys(RegNo)
elemPass = driver.find_element_by_id('password')
elemPass.send_keys(Pass)
driver.find_element_by_id('button').click()

#############################################################################################################################################
#CSE OOPS
if branch == 1 and lab == 1 :

    time.sleep(3)

    driver.find_element_by_class_name('card-action').click()

    time.sleep(5)
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.ID, 'graphCanvas_rgraph_domtext_wrapper')))
    time.sleep(3)

    for v in range(0,99):
            v=str(v)
            driver.get('http://ulc.srmuniv.ac.in/elabcsecpp/login/student/code/cpp/cpp.code.php?id=1&value='+v)
            time.sleep(2)
            wait.until(EC.presence_of_element_located((By.ID, 'evaluateButton')))
            time.sleep(1)
            #driver.find_element_by_id("evaluateButton").click()
            #driver.find_element_by_id("printMsg").click()
            #t=driver.find_element_by_id("resultMsg")
            #driver.get('http://ulc.srmuniv.ac.in/mathslab'+a+'/login/student/code/getReport.php')
            #time.sleep(1)
    time.sleep(5)


#############################################################################################################################################
#CSE DS
elif branch == 1 and lab == 2 :

    time.sleep(3)

    driver.find_element_by_class_name('card-action').click()

    time.sleep(5)
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.ID, 'graphCanvas_rgraph_domtext_wrapper')))
    time.sleep(3)

    for v in range(0,99):
            v=str(v)
            driver.get('http://ulc.srmuniv.ac.in/elabcseds/login/student/code/cpp/cpp.code.php?id=1&value='+v)
            time.sleep(2)
            wait.until(EC.presence_of_element_located((By.ID, 'evaluateButton')))
            time.sleep(1)
            #driver.find_element_by_id("evaluateButton").click()
            #driver.find_element_by_id("printMsg").click()
            #t=driver.find_element_by_id("resultMsg")
            #driver.get('http://ulc.srmuniv.ac.in/mathslab'+a+'/login/student/code/getReport.php')
            #time.sleep(1)
    time.sleep(5)

#############################################################################################################################################
#IT DS
elif branch == 2 and lab == 2 :

    time.sleep(3)

    driver.find_element_by_xpath("//div[@class = 'row']//div[@class = 'col s12 m6 l4 course-data']//div[@class = 'card-content white-text']//span[text()='DATA-STRUCTURE']").click()

    time.sleep(5)
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.ID, 'graphCanvas_rgraph_domtext_wrapper')))
    time.sleep(3)

    for v in range(0,99):
            v=str(v)
            driver.get('http://ulc.srmuniv.ac.in/elabitcppds/login/student/code/cpp/cpp.code.php?id=1&value='+v)
            time.sleep(2)
            wait.until(EC.presence_of_element_located((By.ID, 'evaluateButton')))
            time.sleep(1)
            #driver.find_element_by_id("evaluateButton").click()
            #driver.find_element_by_id("printMsg").click()
            #t=driver.find_element_by_id("resultMsg")
            #driver.get('http://ulc.srmuniv.ac.in/mathslab'+a+'/login/student/code/getReport.php')
            #time.sleep(1)
    time.sleep(5)

#############################################################################################################################################
#IT OOPS

elif branch == 2 and lab == 1 :

    time.sleep(3)

    driver.find_element_by_xpath("//div[@class = 'row']//div[@class = 'col s12 m6 l4 course-data']//div[@class = 'card-content white-text']//span[text()='CPP']").click()

    time.sleep(5)
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.ID, 'graphCanvas_rgraph_domtext_wrapper')))
    time.sleep(3)

    for v in range(0,99):
            v=str(v)
            driver.get('http://ulc.srmuniv.ac.in/elabitcppds/login/student/code/cpp/cpp.code.php?id=1&value='+v)
            time.sleep(2)
            wait.until(EC.presence_of_element_located((By.ID, 'evaluateButton')))
            time.sleep(1)
            #driver.find_element_by_id("evaluateButton").click()
            #driver.find_element_by_id("printMsg").click()
            #t=driver.find_element_by_id("resultMsg")
            #driver.get('http://ulc.srmuniv.ac.in/mathslab'+a+'/login/student/code/getReport.php')
            #time.sleep(1)
    time.sleep(5)

#############################################################################################################################################
#SOFT OOPS

elif branch == 3 and lab == 1 :

    time.sleep(3)

    driver.find_element_by_xpath("//div[@class = 'row']//div[@class = 'col s12 m6 l4 course-data']//div[@class = 'card-content white-text']//span[text()='CPP']").click()

    time.sleep(5)
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.ID, 'graphCanvas_rgraph_domtext_wrapper')))
    time.sleep(3)

    for v in range(0,99):
            v=str(v)
            driver.get('http://ulc.srmuniv.ac.in/elabswecppds/login/student/code/cpp/cpp.code.php?id=1&value='+v)
            time.sleep(2)
            wait.until(EC.presence_of_element_located((By.ID, 'evaluateButton')))
            time.sleep(1)
            #driver.find_element_by_id("evaluateButton").click()
            #driver.find_element_by_id("printMsg").click()
            #t=driver.find_element_by_id("resultMsg")
            #driver.get('http://ulc.srmuniv.ac.in/mathslab'+a+'/login/student/code/getReport.php')
            #time.sleep(1)
    time.sleep(5)


#############################################################################################################################################
#SOFT DS

elif branch == 3 and lab == 2 :

    time.sleep(3)

    driver.find_element_by_xpath("//div[@class = 'row']//div[@class = 'col s12 m6 l4 course-data']//div[@class = 'card-content white-text']//span[text()='CPP']").click()

    time.sleep(5)
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.ID, 'graphCanvas_rgraph_domtext_wrapper')))
    time.sleep(3)

    for v in range(0,99):
            v=str(v)
            driver.get('http://ulc.srmuniv.ac.in/elabswecppds/login/student/code/cpp/cpp.code.php?id=1&value='+v)
            time.sleep(2)
            wait.until(EC.presence_of_element_located((By.ID, 'evaluateButton')))
            time.sleep(1)
            #driver.find_element_by_id("evaluateButton").click()
            #driver.find_element_by_id("printMsg").click()
            #t=driver.find_element_by_id("resultMsg")
            #driver.get('http://ulc.srmuniv.ac.in/mathslab'+a+'/login/student/code/getReport.php')
            #time.sleep(1)
    time.sleep(5)
