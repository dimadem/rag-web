from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time


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

def search_wiki(query):
    driver = Firefox()
    driver.get("https://en.wikipedia.org/wiki/Main_Page")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((
            By.NAME, "search"
            ))).send_keys(query, Keys.RETURN)
    time.sleep(1)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "content"))
    )
    content = BeautifulSoup(driver.page_source, 'html.parser')
    article = content.select_one(".mw-parser-output")
    print(f"article\n", article)
    if article is None:
        article_text = "There are no articles on Wikipedia with this title."
        return article_text
    article_text = ''
    if article:
        paragraphs = article.find_all('p')
        for paragraph in paragraphs:
            article_text += paragraph.text
    driver.quit()
    print(f"article\n", article_text)
    return article_text