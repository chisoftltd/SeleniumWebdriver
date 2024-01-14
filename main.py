from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome browser open after program finishes

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org")
# driver.get("https://www.amazon.co.uk/ProCase-Samsung-SM-T510-SM-T515-Translucent-Navy/dp/B07RW5Y9DZ/ref=psdc_1499996031_t1_B07QS4P6YV?th=1")

# price_pound = driver.find_element(By.CLASS_NAME, value= "a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value= "a-price-fraction")
# print(f"The price is {price_pound.text}.{price_cents.text}")

search_bar = driver.find_element(By.NAME, value="q")
print(search_bar.get_attribute("placeholder"))

button = driver.find_element(By.ID, value="submit")
print(button)

documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
print(documentation_link.text)

bug_link = driver.find_element(By.XPATH, value = '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_link.text)

driver.quit()


#driver.quit()