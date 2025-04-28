from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up Chrome options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# Initialize browser
chrome_browser = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=chrome_options
)
chrome_browser.maximize_window()

try:
    # Access the website with correct URL
    chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')
    
    # Wait for page load
    wait = WebDriverWait(chrome_browser, 10)
    
    # Find message input and button
    user_message = chrome_browser.find_element(By.ID, 'user-message')
    show_message_button = chrome_browser.find_element(By.CLASS_NAME, 'btn-default')
    
    # Clear existing text and input new message
    user_message.clear()
    user_message.send_keys('I AM EXTRA COOOOL')
    
    # Click the button
    show_message_button.click()
    
    # Get output message and verify
    output_message = chrome_browser.find_element(By.ID, 'display')
    assert 'I AM EXTRA COOOOL' in output_message.text
    
except Exception as e:
    print(f"An error occurred: {str(e)}")
finally:
    time.sleep(10)
    chrome_browser.quit()
