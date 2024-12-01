import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
import time
import logging
from typing import List, Dict, Optional, Union
import json

if __name__ == "__main__":
    # Replace with your API key
    API_KEY = "NERFKF4U5G89AYZNU2MGQEFQUCNI4C23S6"
    
    # USDT contract address
    USDT_CONTRACT = "0xdac17f958d2ee523a2206206994597c13d831ec7"
    url = "https://etherscan.io/token/0xdac17f958d2ee523a2206206994597c13d831ec7#balances"
    driver = webdriver.Chrome()
    driver.get(url)
   
    try:
        # Wait for the table to load
        table = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "table.mb-0"))
        )
        
        # Get rows
        table = driver.find_element(By.CLASS_NAME, "table.mb-0")
        tbody = table.find_element(By.TAG_NAME, "tbody")
        rows = tbody.find_elements(By.TAG_NAME, "tr") 
        print(len(rows))
        #rows = table_body.find_element(By.TAG_NAME, "tr")
        # page_source = driver.page_source
        # soup = BeautifulSoup(page_source, 'html.parser')
        # table = soup.select('table.table.mb-0')
        # table_body = soup.select('table.align-middle.text-nowrap')
        #rows = table.find('tbody').find_all('tr')
        # rows = table.find_elements(By.TAG_NAME, "tr")
        # print(len(rows))
            
            
        # holders_data = []
        # for row in table_body:  # Skip header row
        #     rank = row.find_element(By.XPATH,'.//*[@id="maintable"]/div[2]/table/tbody/tr[1]/td[1]').text
        #     address =  row.find_element(By.XPATH,'.//*[@id="maintable"]/div[2]/table/tbody/tr[1]/td[2]/div').text
        #     quantity = row.find_element(By.XPATH,'.//*[@id="maintable"]/div[2]/table/tbody/tr[1]/td[3]').text
        #     percentage = row.find_element(By.XPATH,'.//*[@id="maintable"]/div[2]/table/tbody/tr[1]/td[4]').text
        #     value = row.find_element(By.XPATH,'.//*[@id="maintable"]/div[2]/table/tbody/tr[1]/td[3]').text
        #     analytics = row.find_element(By.XPATH,'.//*[@id="maintable"]/div[2]/table/tbody/tr[1]/td[6]').text
        #     holders_data.append({
        #         "rank": rank,
        #         "address": address,
        #         "quantity": quantity,
        #         "percentage": percentage,
        #         "value": value,
        #         "analytics": ~analytics})
        # print(holders_data)
                        
    finally:
        driver.quit()
    