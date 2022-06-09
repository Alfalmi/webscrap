from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
#object of Options class
op = webdriver.ChromeOptions()
#set chromedriver.exe path
driver = webdriver.Chrome(ChromeDriverManager().install())
#maximize browser
driver.maximize_window()
#launch URL
driver.get("https://www.seleniumhq.org/download/");
#get user Agent with execute_script
a= driver.execute_script("return navigator.userAgent")
print("User agent:")
print(a)
#close browser session
driver.quit()