from selenium import webdriver
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

option = Options()
option.headless = True
option.add_argument('window-size=1920,1080')

url = "https://www.audible.com/adblbestsellers"
driver = webdriver.Chrome(ChromeDriverManager().install(), options=option)
driver.get(url)
# driver.maximize_window()



l_name, l_author = [], []

last_page_number = int(driver.find_elements_by_css_selector('.bc-link.refinementFormLink.pageNumberElement')[1].text)

for _ in range(1,last_page_number):
    box = driver.find_elements_by_css_selector(".bc-col-responsive.bc-col-6")
    for item in box:
        name = item.find_element_by_css_selector('h3 a').text
        temp = item.find_elements_by_css_selector('.bc-list-item.authorLabel a')

        author = ", ".join([i.text for i in temp])

        l_name.append(name)
        l_author.append(author)

    new_page = driver.find_element_by_css_selector('bc-button.bc-button-secondary.nextButton.refinementFormButton.bc-button-small.bc-button-inline')
    new_page.click()
driver.quit()

data = {"book name":l_name, "author":l_author}
df = pd.DataFrame(data)
df.to_csv("audible_best_sellers_1_page.csv", index=False)