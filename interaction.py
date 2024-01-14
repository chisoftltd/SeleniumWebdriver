from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

# Keep Chrome browser open after program finishes

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("http://secure-retreat-92358.herokuapp.com/")

# all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# all_portals.click()

search_f = driver.find_element(By.NAME, value="fName")
search_f.send_keys("Benjamin")
search_l = driver.find_element(By.NAME, value="lName")
search_l.send_keys("Chinwe")
search_e = driver.find_element(By.NAME, value="email")
search_e.send_keys("Chinwe@kth.se", Keys.ENTER)

# article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
# print(article_count.text)
# article_count.click()

