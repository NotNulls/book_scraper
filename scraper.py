import requests
from bs4 import BeautifulSoup
from pprint import pprint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

title_search = input('Please insert search keyword: ')

def search_funct():

    driver = webdriver.Firefox()
    driver.get('https://www.delfi.rs/')
    time.sleep(3)
    driver.find_element(By.ID,'autocomplete-input').send_keys(title_search)


    action =ActionChains(driver)
    time.sleep(1)
    action.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()


    wait = WebDriverWait(driver,1)
    time.sleep(2)
    wait.until(EC.url_changes('https://www.delfi.rs/'))

    driver.find_element(By.CLASS_NAME,'modal-title')

    soup = BeautifulSoup(driver.page_source, "html.parser")



    search_result = soup.find_all('h1')
    s = [' '.join(s.getText().split()) for s in search_result]
    print('Web app search results: ',s)
    print('----------')
    print('Number of mathces: ', s[1][0])

    data = []
    
    if int(s[1][0]) != 0:
        try:
            soup = BeautifulSoup(driver.page_source,'html.parser')
            find_by_class = soup.find_all(class_="body")
            #print (find_by_class)
            print('------type(i) and type(i.find_all("a",class_=""))----')
            
            for i in find_by_class:
                title = ["".join(i.text) for i in i.find_all("a",class_="")][0]
                author = [i.text for i in i.find_all("a",class_="")][1]
                price = [i.text.split()[0] for i in i.find_all("span",class_="price")]
                
                
                data.append([title,author, price[1]])
            print('-------------------------')
            # e = [[" ".join(item.getText().split()),] for item in 
        except ValueError:
            pass
    else:
        print('Please type in a correct keyword!')
        
    
    #print(data)

    try:
        data_frame = pd.DataFrame(data)
        data_frame.columns = ['Title','Author','Price']
        print(data_frame)
    except ValueError:
        pass

    driver.close()

search_funct()

