from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from os import mkdir
import urllib.request


def startDriver():
    chrome_options = Options()
    chrome_options.add_argument("--window-size=800,800")

    caps = DesiredCapabilities().CHROME
    caps["pageLoadStrategy"] = "eager"  #  interactive

    driver = webdriver.Chrome('./chromedriver.exe', chrome_options=chrome_options, desired_capabilities=caps)
    return driver


def findWord(word, driver):
    driver.get("https://handspeak.com/word/")

    # Wait for search bar to appear
    search_box_locator = (By.ID, "search_box")
    search_box = WebDriverWait(driver, 20).until(EC.presence_of_element_located(search_box_locator))

    # Clear search bar and enter search term
    search_box.clear()
    search_box.send_keys(word)

    # Click on first letter of search term
    first_letter_locator = (By.XPATH, '//a[text()="'+word[0].upper()+'"]')
    first_letter = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(first_letter_locator))
    first_letter.click()

    # Click on search term in list of words
    word_locator = (By.XPATH, "//a[translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz') = '"+word.lower()+"']")
    selected_word = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(word_locator))
    selected_word.click()

    print('clicked word')

def getVideo(word, foldername, index, driver):
    element_present = EC.presence_of_element_located((By.CLASS_NAME, "v-asl"))
    WebDriverWait(driver, 5).until(element_present)

    video = driver.find_element("class name", "v-asl")

    video_url = video.get_property('src')

    filename = f"{foldername}/{index}_{word}.mp4"

    urllib.request.urlretrieve(video_url, filename)  
    print(video_url)
