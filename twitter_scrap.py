import webbrowser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from time import sleep
from selenium.webdriver.chrome.options import Options

option = Options()
option.headless = True
option.add_argument('window-size=1920,1080')

keyword = '#'

url = "https://www.twitter.com/"
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url) 

sleep(5)
# search_bar = driver.find_element_by_class_name("nav-search-input")
# search_bar.clear()
# search_bar.send_keys("iphone 12")
# search_bar.send_keys(Keys.RETURN)
# sleep(1)


# box = driver.find_elements_by_xpath("//li[@class='ui-search-layout__item']")
# for item in box:
#         title = item.find_element_by_xpath("//li[@class='ui-search-layout__item']//div[@class='ui-search-result__wrapper']//div[@class='ui-search-item__group ui-search-item__group--title']//a[@class='ui-search-item__group__element ui-search-link']//h2[@class='ui-search-item__group ui-search-item__group--title'"]).text
#         temp = item.find_elements_by_css_selector('.bc-list-item.authorLabel a')

#         author = ", ".join([i.text for i in temp])

#         l_name.append(name)
#         l_author.append(author)
# # title_products = driver.find_elements_by_xpath("//h2[@class='ui-search-item__title']")
# # title_produts = [title.text for title in title_products]


# # price_products = driver.find_elements_by_xpath('//*[@id="root-app"]/div/div[1]/section/ol/li')



# driver.close()