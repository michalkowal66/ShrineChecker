from selenium import webdriver

PATH = "C:\Program Files (x86)/chromedriver.exe"
#Set the path for the chrome driver

driver = webdriver.Chrome(PATH)

driver.get("https://tech-with-tim.teachable.com/")
#Access the website
driver.close()
#Clsoes the window