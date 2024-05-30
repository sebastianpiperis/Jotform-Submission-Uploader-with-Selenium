from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime
import pytz
from config import USERNAME, PASSWORD




# Define Chrome options
option = Options()
option.binary_location = ""  # Set the path to your Chrome binary
option.add_experimental_option("detach", True)
option.add_argument("start-maximized")

# Add other Chrome options as needed (e.g., headless mode, disable extensions, etc.)

# Create the WebDriver instance with the specified options
driver = webdriver.Chrome(options=option)

attachment_path = ""    

# Define the Eastern Time timezone
eastern_timezone = pytz.timezone('US/Eastern')

# Get the attachments and data_list from the main.py function

def uploadFile(data_list):
    driver.get("url_to_ie")  #replace with proper url
    username_input = driver.find_element(By.ID, "username")
    username_input.send_keys(user)
    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys(pw)
    login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.login_button')))
    login_button.click()
            
    for data in data_list:
        job_number = data['content']['answers']['4']['answer']

        
        # Search for the job_number
        search_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#search_master.ui-autocomplete-input')))
        search_box.send_keys(job_number)
        search_box.send_keys(Keys.RETURN)

        # Let's page load so it can open properly and not crash
        time.sleep(3)

        # Define the XPath of the discussion notes element
        discussion_xpath = '//*[@id="txt_discussion"]'
        add_button_xpath = '//*[@id="addDiscussion"]'

        # Wait for the discussion element to be clickable
        discussion_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, discussion_xpath))
        )

        # Send the text "Support Call Logged" to the discussion element
        discussion_element.send_keys("Support Call Logged")

        # Locate and click the "Add" button
        add_button = driver.find_element(By.XPATH, add_button_xpath)
        add_button.click()

        # Navigate to the files section
        files_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'files_tab')))
        files_button.click()

        # Click the "Add File" button
        add_file_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'addfilenew')))
        add_file_button.click()
        
        # Handle the popup window
        window_handles = driver.window_handles
        if len(window_handles) > 1:
            driver.switch_to.window(window_handles[1])

            # Enter file details (e.g., support call and date)
            search_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'txtDocumentName')))
            #search_box.send_keys("support call")
            support_call = "Support Call"
            current_eastern_time = datetime.now(eastern_timezone).strftime("%Y-%m-%d %H:%M:%S")
            file_details = f"{support_call} - {current_eastern_time}"
            search_box.send_keys(file_details)

            # Upload the file
            choose_file_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'flUpload')))
            choose_file_button.send_keys(f"C:/Users/sebas/Downloads/forms/{job_number}.pdf")

            # Click the save button
            save_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'btnUpload')))
            save_button.click()

            # Click the close button
            close_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='pnlDone']/div/div/input")))
            close_button.click()

            

            # Switch back to the main window for multiple jobs
            driver.switch_to.window(window_handles[0])
            
    # Closes Chrome driver
    driver.quit()
    print("Finished, LFG.") # Confirms it closed
 


    exit()


