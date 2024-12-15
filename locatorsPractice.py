"""
Extract the upcoming event data from the python.org website. Use Selenium to 
scrape all upcoming event dates and event names (in my case there are 5) and
store them in a nested python dictionary. Print the dictionary to the console.
The event data from python.org should be stored under the keys "time" and "name".
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from pprint import pprint

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

url = "https://www.python.org/"

driver.get(url)

event_time_tags = driver.find_elements(
    By.CSS_SELECTOR, value=".event-widget time")
event_times = [e.text for e in event_time_tags]
event_name_tags = driver.find_elements(
    By.CSS_SELECTOR, value=".event-widget li a")
event_names = [e.text for e in event_name_tags]

events_dict = {}
for i in range(min(len(event_times), len(event_names))):
    events_dict[i] = {"time": event_times[i], "name": event_names[i]}
pprint(events_dict)
driver.quit()
