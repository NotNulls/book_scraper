import requests
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Firefox()
driver.get('https://www.delfi.rs/')
search_input= driver.find_element_by_id('autocomplete-input')

title_search = input('Please insert book title: ')

print([str(search_input.text)])
driver.close()

# header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0'}
# response = requests.get()