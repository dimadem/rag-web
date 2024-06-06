from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from app.services.buffer.utils import write_prompt, write_link, write_text, load_buffer
import time

def Chrome():
    options = Options()
    options.add_argument("--headless")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def search_web(query):
    driver = Chrome()
    driver.get("https://www.google.com")
    wait = WebDriverWait(driver, 3)
    dismiss_button = wait.until(EC.element_to_be_clickable((By.ID, "W0wltc")))
    dismiss_button.click()
    search_input = wait.until(EC.element_to_be_clickable((By.NAME, "q")))
    search_input.send_keys(query)
    search_input.send_keys(Keys.RETURN)
    time.sleep(1)
    search_results = driver.find_elements(By.CSS_SELECTOR, "div.g")[:3]
    for result in search_results:
        href = result.find_element(By.CSS_SELECTOR, "a")
        link = href.get_attribute("href")
        write_link(query, link)
    driver.quit()

def parse_text(query, links):
    for link in links:
        driver = Chrome()
        driver.get(link)
        time.sleep(1)  
        body_content = driver.find_element(By.TAG_NAME, "body").text[:400]
        write_text(prompt=query, text=body_content)
        driver.quit()

def search_and_parse(query):
    write_prompt(query)
    search_web(query)
    buffer = load_buffer()
    links = buffer[query]['links']
    parse_text(query, links)
    buffer = load_buffer()
    return buffer[query]['texts']