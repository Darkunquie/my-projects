from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Chrome options setup
options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')

# Initialize browser
chrome_browser = webdriver.Chrome(options=options)
chrome_browser.maximize_window()

try:
    # Try accessing the website
    chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')
    
    # Wait for popup and close it if present
    wait = WebDriverWait(chrome_browser, 5)
    popup = wait.until(EC.presence_of_element_located((By.ID, 'at-cv-lightbox-close')))
    popup.click()

    # Find and interact with form elements
    user_message = chrome_browser.find_element(By.ID, 'user-message')
    user_message.clear()
    user_message.send_keys('I AM EXTRA COOOOL')

    time.sleep(2)
    show_message_button = chrome_browser.find_element(By.CLASS_NAME, 'btn-default')
    show_message_button.click()

    output_message = chrome_browser.find_element(By.ID, 'display')
    assert 'I AM EXTRA COOOOL' in output_message.text

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Keep browser open for 10 seconds before closing
    time.sleep(10)
    chrome_browser.quit()