from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
print("Enter your mathslab version > 1/2/3/4")
a=int(input())

#if a==1 :
#    driver.get("http://ulc.srmuniv.ac.in/mathslab1/")
#elif a==2 :
#    driver.get("http://ulc.srmuniv.ac.in/mathslab2/")
#elif a==3 :
#    driver.get("http://ulc.srmuniv.ac.in/mathslab3/")
#elif a==4 :
#    driver.get("http://ulc.srmuniv.ac.in/mathslab4/")
#else :
#    print("no match found")
a=str(a)
driver.get("http://ulc.srmuniv.ac.in/mathslab"+a)

print("Enter your Registration Number > ")
RegNo = input()

print("Enter your Password >")
Pass = input()


elemId = driver.find_element_by_id('username')
elemId.send_keys(RegNo)
elemPass = driver.find_element_by_id('password')
elemPass.send_keys(Pass)
driver.find_element_by_id('button').click()

#element = wait.until(EC.presence_of_element_located((By.ID, 'someid')))
#wait = WebDriverWait(driver, 5)
time.sleep(2)
driver.find_element_by_css_selector("div.card-content.white-text").click()
#driver.find_element_by_class_name('card-action').click()
#for i in range(0,100) :
#Quest=driver.find_elements_by_class_name('rgraph_tooltip')
#for i in Quest :
#print(Quest)
#time.sleep(5)
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.ID, 'graphCanvas_rgraph_domtext_wrapper')))
time.sleep(1)
#if a==1 :
for v in range(0,100):
        v=str(v)
        driver.get('http://ulc.srmuniv.ac.in/mathslab'+a+'/login/student/code/mathslab/mathslab.code.php?id=1&value='+v)
        wait.until(EC.presence_of_element_located((By.ID, 'evaluateButton')))
        time.sleep(1)
        driver.find_element_by_id("evaluateButton").click()
        #driver.find_element_by_id("evaluateButton").click()
        #wait.until(EC.presence_of_element_located((By.ID, 'printMsg'))
        time.sleep(1)
        #driver.find_element_by_id("printMsg").click()
        t=driver.find_element_by_id("resultMsg")
        driver.get('http://ulc.srmuniv.ac.in/mathslab'+a+'/login/student/code/getReport.php')
        time.sleep(1)


#elif a==2 :
#    for v in range(0,100):
#        v=str(v)
#        driver.get('http://ulc.srmuniv.ac.in/mathslab2/login/student/code/mathslab/mathslab.code.php?id=1&value='+v)
#elif a==3 :
#    for v in range(0,100):
#        v=str(v)
#        driver.get('http://ulc.srmuniv.ac.in/mathslab3/login/student/code/mathslab/mathslab.code.php?id=1&value='+v)
#elif a==4 :
#    for v in range(0,100):
#        v=str(v)
#        driver.get('http://ulc.srmuniv.ac.in/mathslab4/login/student/code/mathslab/mathslab.code.php?id=1&value='+v)


#http://ulc.srmuniv.ac.in/mathslab1/login/student/code/mathslab/mathslab.code.php?id=1&value=80


#Quest=driver.find_element_by_id('__rgraph_tooltip_graphCanvas_74993304-a5e1-4980-bc93-598e02b55466_15')
#                                 __rgraph_tooltip_graphCanvas_dd29daaa-a4a0-4d9f-a5a4-21e503b9d3fe_18
#                                 __rgraph_tooltip_graphCanvas_22c779e3-5a92-44f1-ac8e-5efc26e9605d_20
#Quest.click()

#elem.clear()
#elem.send_keys("face")
#elem.send_keys(Keys.RETURN)
#assert "No results found." not in driver.page_source
#driver.close()
