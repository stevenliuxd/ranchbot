from selenium import webdriver
from selenium.webdriver.chrome.options import Options  # Add this import
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

url = 'https://car-part.com/'

browser = webdriver.Chrome(options=chrome_options)
browser.get(url)

# Select year
vehicle_year = '2008'
year_dropdown = browser.find_element(By.XPATH, '//*[@id="year"]')
dropdown = Select(year_dropdown)
dropdown.select_by_value(vehicle_year)

# Select Make
vehicle_make = 'Lexus RX350'
make_dropdown = browser.find_element(By.XPATH, '//*[@id="model"]')
dropdown = Select(make_dropdown)
dropdown.select_by_value(vehicle_make)

# Select Part
vehicle_part = 'Fender'
part_dropdown = browser.find_element(By.XPATH, '/html/body/div[1]/table[2]/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/center/table/tbody/tr[3]/td[2]/select')
dropdown = Select(part_dropdown)
dropdown.select_by_value(vehicle_part)

# Select Country
country = 'Canada'
country_dropdown = browser.find_element(By.XPATH, '//*[@id="Loc"]')
dropdown = Select(country_dropdown)
dropdown.select_by_value(country)

# Input Postal Code
postal_code = 'T0L 0X0'
input_element = browser.find_element(By.XPATH, '/html/body/div[1]/table[2]/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/center/table/tbody/tr[6]/td/table/tbody/tr/td[2]/input')
input_element.send_keys(postal_code)

# Click Submit
element_to_click = browser.find_element(By.XPATH, '/html/body/div[1]/table[2]/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/center/table/tbody/tr[7]/td/input[5]')
element_to_click.click()
time.sleep(2)

# Click LH
element_to_click = browser.find_element(By.XPATH, '/html/body/center[2]/table/tbody/tr[2]/td/center/form/input[31]')
element_to_click.click()
time.sleep(2)

search_word = 'Astroid Auto Recyclers'

# Check if the search_word is present in the page source
if search_word.lower() in browser.page_source.lower():
    print(f"The word '{search_word}' is present on the page.")
else:
    print(f"The word '{search_word}' is not found on the page.")


browser.quit()
