"""
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
"""
        
"""      
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import time

if __name__ == "__main__":
    url = "https://etherscan.io/token/0xdac17f958d2ee523a2206206994597c13d831ec7#balances"
    
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(2)  # Give the page a moment to load
    
    try:
        # Wait for table to load using the exact class structure
        table = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "table.table.mb-0"))
        )
        
        # Find tbody with specific class
        tbody = table.find_element(By.CSS_SELECTOR, "tbody.align-middle.text-nowrap")
        rows = tbody.find_elements(By.TAG_NAME, "tr")
        
        holders_data = []
        
        for row in rows:
            try:
                cells = row.find_elements(By.TAG_NAME, "td")
                
                # Get the address text from the nested structure
                address_element = cells[1].find_element(By.TAG_NAME, "a")
                
                # Extract the quantity from the span element
                quantity_element = cells[2].find_element(By.TAG_NAME, "span")
                
                holder_data = {
                    "rank": cells[0].text.strip(),
                    "address": address_element.text.strip(),
                    "quantity": quantity_element.text.strip(),
                    "percentage": cells[3].text.split()[0].strip(),  # Get just the percentage number
                    "value": cells[4].text.strip()
                }
                
                holders_data.append(holder_data)
                print(f"Processed holder: Rank {holder_data['rank']}")
            
            except Exception as e:
                print(f"Error processing row: {e}")
                continue
        
        # Save the data to a file
        with open('holders_data.json', 'w') as f:
            json.dump(holders_data, f, indent=2)
        
        print(f"\nSuccessfully scraped {len(holders_data)} holders")
        
        # Print the first entry as an example
        if holders_data:
            print("\nExample of first holder data:")
            print(json.dumps(holders_data[0], indent=2))
            
    except Exception as e:
        print(f"An error occurred: {e}")
        
    finally:
        driver.quit()
"""

"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import json
import time

if __name__ == "__main__":
    url = "https://etherscan.io/token/0xdac17f958d2ee523a2206206994597c13d831ec7#balances"
    
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    
    try:
        # Wait longer for the page to load completely
        time.sleep(5)
        
        print("Waiting for table to load...")
        # Wait for the specific table with ID 'maintable'
        table = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.ID, "maintable"))
        )
        
        print("Table found, looking for rows...")
        # Get all rows directly
        rows = driver.find_elements(By.CSS_SELECTOR, "#maintable tbody tr")
        
        print(f"Found {len(rows)} rows")
        
        holders_data = []
        
        for row in rows:
            try:
                cells = row.find_elements(By.TAG_NAME, "td")
                if len(cells) >= 5:  # Make sure we have enough cells
                    # Print raw cell text for debugging
                    print(f"Processing row with {len(cells)} cells")
                    for i, cell in enumerate(cells):
                        print(f"Cell {i}: {cell.text}")
                    
                    holder_data = {
                        "rank": cells[0].text.strip(),
                        "address": cells[1].text.strip().split('\n')[0],  # Get first line of address
                        "quantity": cells[2].text.strip(),
                        "percentage": cells[3].text.strip().split('\n')[0],  # Get percentage without progress bar
                        "value": cells[4].text.strip()
                    }
                    
                    holders_data.append(holder_data)
                    print(f"Successfully processed holder: Rank {holder_data['rank']}")
            
            except Exception as e:
                print(f"Error processing row: {str(e)}")
                continue
        
        # Save the data to a file
        with open('holders_data.json', 'w') as f:
            json.dump(holders_data, f, indent=2)
        
        print(f"\nSuccessfully scraped {len(holders_data)} holders")
        
        # Print the first entry as an example
        if holders_data:
            print("\nExample of first holder data:")
            print(json.dumps(holders_data[0], indent=2))
        else:
            print("\nNo data was scraped. Printing page source for debugging...")
            print(driver.page_source[:500])  # Print first 500 chars of page source
            
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        print("Printing page source for debugging...")
        print(driver.page_source[:500])
        
    finally:
        driver.quit()
    """
   
""" 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import json
import time

def setup_driver():
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    
    return webdriver.Chrome(options=chrome_options)

if __name__ == "__main__":
    url = "https://etherscan.io/token/0xdac17f958d2ee523a2206206994597c13d831ec7#balances"
    
    driver = setup_driver()
    driver.get(url)
    
    try:
        # Wait for initial page load
        time.sleep(5)
        
        print("Waiting for table to load...")
        
        # Wait for the table container
        table_container = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.table-responsive"))
        )
        
        # Wait for actual table rows
        rows = WebDriverWait(driver, 15).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.table-respnsive tr"))
        )
        
        print(f"Found {len(rows)} rows")
        
        holders_data = []
        
        # Skip first row (header)
        for row in rows[1:]:
            try:
                # Wait for cells to be present in this row
                cells = WebDriverWait(row, 10).until(
                    EC.presence_of_all_elements_located((By.TAG_NAME, "td"))
                )
                
                if len(cells) >= 5:
                    # Print raw data for debugging
                    print("\nProcessing row:")
                    for i, cell in enumerate(cells):
                        print(f"Cell {i} content: {cell.text}")
                    
                    # Extract address from the div containing the link
                    address_div = cells[1].find_element(By.CSS_SELECTOR, "div.d-flex")
                    address_text = address_div.text.split('\n')[0]  # Get first line
                    
                    holder_data = {
                        "rank": cells[0].text.strip(),
                        "address": address_text,
                        "quantity": cells[2].find_element(By.TAG_NAME, "span").text.strip(),
                        "percentage": cells[3].text.split('\n')[0].strip(),
                        "value": cells[4].text.strip()
                    }
                    
                    holders_data.append(holder_data)
                    print(f"Successfully processed holder: Rank {holder_data['rank']}")
            
            except Exception as e:
                print(f"Error processing row: {str(e)}")
                continue
        
        # Save the data
        with open('holders_data.json', 'w') as f:
            json.dump(holders_data, f, indent=2)
        
        print(f"\nSuccessfully scraped {len(holders_data)} holders")
        
        if holders_data:
            print("\nExample of first holder data:")
            print(json.dumps(holders_data[0], indent=2))
        else:
            print("\nNo data was scraped. Debug information:")
            print("Page title:", driver.title)
            print("Current URL:", driver.current_url)
            
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        
    finally:
        driver.quit()
        """
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import json
import time

def setup_driver():
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    
    return webdriver.Chrome(options=chrome_options)

if __name__ == "__main__":
    url = "https://etherscan.io/token/0xdac17f958d2ee523a2206206994597c13d831ec7#balances"
    
    driver = setup_driver()
    driver.get(url)
    
    try:
        # Wait for initial page load
        time.sleep(5)
        
        print("Waiting for table to load...")
        
        # Wait for the table container
        table_container = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.table-responsive"))
        )
        
        table = driver.find_element(By.CLASS_NAME, "table.mb-0")
        tbody = table.find_element(By.TAG_NAME, "tbody")
        rows = tbody.find_elements(By.TAG_NAME, "tr")  # Get all table rows
        # Wait for actual table rows
        print(f"rows is: {rows}")
        
        print(f"Found {len(rows)} rows")
        
        holders_data = []
        
        # Skip first row (header)
        for row in rows[1:]:
            try:
                # Wait for cells to be present in this row
                cells = WebDriverWait(row, 10).until(
                    EC.presence_of_all_elements_located((By.TAG_NAME, "td"))
                )
                
                if len(cells) >= 5:
                    # Print raw data for debugging
                    print("\nProcessing row:")
                    for i, cell in enumerate(cells):
                        print(f"Cell {i} content: {cell.text}")
                    
                    # Extract address from the div containing the link
                    address_div = cells[1].find_element(By.CSS_SELECTOR, "div.d-flex")
                    address_text = address_div.text.split('\n')[0]  # Get first line
                    
                    holder_data = {
                        "rank": cells[0].text.strip(),
                        "address": address_text,
                        "quantity": cells[2].find_element(By.TAG_NAME, "span").text.strip(),
                        "percentage": cells[3].text.split('\n')[0].strip(),
                        "value": cells[4].text.strip()
                    }
                    
                    holders_data.append(holder_data)
                    print(f"Successfully processed holder: Rank {holder_data['rank']}")
            
            except Exception as e:
                print(f"Error processing row: {str(e)}")
                continue
        
        # Save the data
        with open('holders_data.json', 'w') as f:
            json.dump(holders_data, f, indent=2)
        
        print(f"\nSuccessfully scraped {len(holders_data)} holders")
        
        if holders_data:
            print("\nExample of first holder data:")
            print(json.dumps(holders_data[0], indent=2))
        else:
            print("\nNo data was scraped. Debug information:")
            print("Page title:", driver.title)
            print("Current URL:", driver.current_url)
            
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        
    finally:
        driver.quit()