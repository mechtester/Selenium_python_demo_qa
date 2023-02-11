from selenium import webdriver
from selenium.webdriver.chrome.service import  Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

chrome_options = webdriver.ChromeOptions()
prefs = {'download.default_directory' : "/home/vignesh/Downloads/delete/"}
chrome_options.add_experimental_option('prefs', prefs)

browser=Service(executable_path="/usr/local/bin/chromedriver")
driver=webdriver.Chrome(service=browser,options=chrome_options)

url="https://demoqa.com/upload-download"
driver.get(url)
driver.maximize_window()

# #upload
# my_wait=WebDriverWait(driver,10)
# my_wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='uploadFile']")))
# driver.find_element(By.XPATH,"//input[@id='uploadFile']").send_keys("/home/vignesh/Downloads/delete/vign.jpeg")
# a=driver.find_element(By.XPATH,"//p[@id='uploadedFilePath']").text
# print("Uploaded file name:",a[12:])

#Download
driver.find_element(By.XPATH,"//a[@id='downloadButton']").click()


driver.quit()
# C:\fakepath\vign.jpeg
