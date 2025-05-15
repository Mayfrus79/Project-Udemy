# type ignore
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

browser = webdriver.Chrome(options=options)
wait = WebDriverWait(browser, 2)  # 2 seconds max wait time

try:
    browser.get("https://www.google.com")
    browser.maximize_window()

    # Accept cookies if the button exists
    try:
        agree_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[.//div[text()="Accept all"]]')))
        agree_button.click()
    except:
        pass  # If not found, move on

    # Wait for the search bar to appear
    search_box = wait.until(EC.presence_of_element_located((By.NAME, "q")))
    search_box.send_keys("How to use selenium?")
    search_box.send_keys(Keys.ENTER)

    # Wait for results and click on the desired link
    results = wait.until(EC.presence_of_element_located((By.ID, "search")))
    links = results.find_elements(By.TAG_NAME, "a")

    if len(links) > 1:
        links[1].click()
    else:
        print("Link not found.")

    time.sleep(20)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    browser.quit()
