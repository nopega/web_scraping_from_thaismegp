import time 
import datetime 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
from selenium.webdriver.support.ui import Select
import mysql.connector
connection = mysql.connector.connect(
    host ='localhost',
    port = 3306,
    user = 'root',
    password = 'password1234',
    database ="database_1"
)
import mysql.connector
connection = mysql.connector.connect(
    host ='localhost',
    port = 3306,
    user = 'root',
    password = 'password1234',
    database ="database_1"
)
mycursor = connection.cursor()
def timer():
    date_target_array = (input("pls input your target date EXAMPLE:2021,11,30,24,58,11"))
    date_target_array = date_target_array.split(",")
    date_target = datetime.datetime(int(date_target_array[0]),int(date_target_array[1]),int(date_target_array[2]),int(date_target_array[3]),int(date_target_array[4]),int(date_target_array[5]))
    date_now = datetime.datetime.now()
    diff = date_target - date_now
    for i in range (diff.seconds,-1,-1):
        seconds = i % 60
        minutes = int(i/60)%60
        hours = int(i/3600)
        print(f"{hours:02}:{minutes:02}:{seconds:02}")
        time.sleep(1)
mycursor = connection.cursor()
mycursor.execute("SELECT*FROM customer")
result = mycursor.fetchall()
result

def fill(data):
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")
    driver.find_element(By.XPATH,'//*[@id="my-text-id"]').send_keys(data[0])
    driver.find_element(By.XPATH,'/html/body/main/div/form/div/div[1]/label[2]/input').send_keys(data[1])
    driver.find_element(By.XPATH,'/html/body/main/div/form/div/div[1]/label[3]/textarea').send_keys(data[2])
    Select(driver.find_element(By.XPATH,'/html/body/main/div/form/div/div[2]/label[1]/select')).select_by_visible_text(data[4])
    driver.find_element(By.XPATH,'/html/body/main/div/form/div/div[2]/label[2]/input').send_keys(data[5])
    driver.find_element(By.XPATH,'/html/body/main/div/form/div/div[2]/label[3]/input').send_keys("C:\\Users\\pongk\\Documents\\web_selenium\\"+str(data[3]))
    driver.find_element(By.XPATH,'//*[@id="my-check-1"]').click()
    driver.find_element(By.XPATH,'//*[@id="my-radio-1"]').click()
    driver.find_element(By.XPATH,'/html/body/main/div/form/div/div[3]/label[1]/input').send_keys(data[6])
    driver.find_element(By.XPATH,'/html/body/main/div/form/div/div[3]/label[2]/input').send_keys(data[7])
    #driver.find_element(By.XPATH,"/html/body/main/div/form/div/div[3]/label[3]/input").send_keys(right)
    elem=driver.find_element_by_class_name("form-range")
    elem.clear()
    driver.execute_script("arguments[0].value = arguments[1];", elem, data[8])

def start(data):
    timer()
    for i in range (0,len(data)):
        fill(data[i])

start(result)