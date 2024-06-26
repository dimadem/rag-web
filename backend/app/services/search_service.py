from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from app.services.buffer.utils import write_prompt, write_link, write_text, load_buffer
import time
from bs4 import BeautifulSoup

def Firefox():
    service = Service()
    options = Options()
    options.add_argument("--headless")
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-extensions')
    options.add_argument('--disable-infobars')
    options.add_argument('--start-maximized')
    options.add_argument('window-size=1200x800')
    driver = webdriver.Firefox(service=service, options=options)
    return driver

def search_web(query):
    driver = Firefox()
    driver.get("https://en.wikipedia.org/wiki/Main_Page")
    print("page loaded")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((
            By.NAME, "search"
            ))).send_keys(query, Keys.RETURN)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "content"))
    )
    content = BeautifulSoup(driver.page_source, 'html.parser')
    article = content.select_one(".mw-parser-output")
    article_text = ''
    if article:
        paragraphs = article.find_all('p')
        for paragraph in paragraphs:
            article_text += paragraph.text

    print(article_text)
    driver.quit()

def parse_text(query, links):
    for link in links:
        driver = Firefox()
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