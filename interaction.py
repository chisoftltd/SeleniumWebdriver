from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

# Keep Chrome browser open after program finishes

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.nairaland.com/search?q=&search=Search")

# all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# all_portals.click()

search = driver.find_element(By.NAME, value="q")
search.send_keys("Tinubu", Keys.ENTER)

# article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
# print(article_count.text)
# article_count.click()

