from selenium import webdriver
from selenium.webdriver.common.by import By
from pprint import pprint

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
# Flipkart scraper - price check
# driver.get("https://www.flipkart.com/pigeon-kettle-water-bottle-electric-kettle/p/itm32c6ca69157d7?pid=EKTGDJSYWGR7GGMS&lid=LSTEKTGDJSYWGR7GGMS6F1GVR&marketplace=FLIPKART&q=kettle&store=j9e%2Fm38%2Fxrv&spotlightTagId=BestsellerId_j9e%2Fm38%2Fxrv&srno=s_1_4&otracker=search&otracker1=search&fm=Search&iid=52a1d6b2-bf03-43ce-8bdb-7d509b48b632.EKTGDJSYWGR7GGMS.SEARCH&ppt=sp&ppn=sp&ssid=5lqwt3cvuo0000001734150505551&qH=a442b5469d33091d")
# price_rupee = driver.find_element(By.CSS_SELECTOR, ".Nx9bqj.CxhGGd")
# print("price: ", price_rupee.text)
# # driver.close()# closes single tab
# driver.quit()  # quits the entire browser

# python.org scraper - practice selenium locators
driver.get("https://www.python.org/")
# find element by name
search_bar = driver.find_element(By.NAME, value="q")
print(search_bar.get_attribute("placeholder"))
# find element by id
button = driver.find_element(By.ID, value="submit")
print(button.size)  # properties of the attribute found
# find element by css selector
# if we want to find a link at a specific location
documentation_link = driver.find_element(
    By.CSS_SELECTOR, value=".documentation-widget a")

print(documentation_link.text)

# if hard to find by selectors, we can find elements by xpath - specify the path to the element
# element is not unique

bug_link = driver.find_element(
    By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_link.text)

# find elements
# to find all elements corresponding to the selector.

event_element = driver.find_element(
    By.CLASS_NAME, "event-widget.last")

event_time_tags = event_element.find_elements(By.TAG_NAME, "time")
event_times = [e.text for e in event_time_tags]
event_name_tags = event_element.find_elements(By.TAG_NAME, "a")
event_names = [e.text for e in event_name_tags][1:]

events_dict = {}
for i in range(min(len(event_times), len(event_names))):
    events_dict[i] = {"time": event_times[i], "name": event_names[i]}
pprint(events_dict)

driver.quit()
