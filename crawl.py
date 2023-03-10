from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from os import mkdir
from selenium.common.exceptions import StaleElementReferenceException
import urllib.request
import re
from webdriver_manager.chrome import ChromeDriverManager
import time
import traceback
import string


nums = {
    "0": "zero (0)",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six (6)",
    "7": "seven (7)",
    "8": "eight (8)",
    "9": "nine (9)"
    }

def startDriver():
    options = Options()
    options.add_argument("--window-size=800,1000")
    options.add_argument("--disable-gpu")
    options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    options.add_argument('--headless') #  testing

    caps = DesiredCapabilities().CHROME
    caps["pageLoadStrategy"] = "eager"  #  interactive

    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options, desired_capabilities=caps)
    return driver

class ElementClickException(Exception):
    pass

def clickItem(elementLocator, driver):
    try:
        element = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(elementLocator))
        element.click()
    except (TimeoutException, StaleElementReferenceException) as exception:
        for i in range(2):
            try:
                element = WebDriverWait(driver, 1).until(EC.element_to_be_clickable(elementLocator))
                element.click()
                break
            except StaleElementReferenceException as exception:
                pass
    except Exception as exception:
        raise ElementClickException("An error occurred while clicking the element") from exception


def findSearchBox(driver):
    driver.get("https://handspeak.com/word/")
    search_box_locator = (By.ID, "search_box")
    search_box = WebDriverWait(driver, 20).until(EC.presence_of_element_located(search_box_locator))
    return search_box;

def findWord(word, search_box, driver):
    try:
        # Clear search bar and enter search term
        search_box.clear()
        search_box.send_keys(word)


        time.sleep(0.5)
        first_letter_locator = (By.XPATH, '//a[text()="'+word[0].upper()+'"]')
        clickItem(first_letter_locator, driver)

        word_locator = (By.XPATH, '//a[translate(text(), "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz") = "'+word.lower()+'"]')
        clickItem(word_locator, driver)
    except TimeoutException:
        return 0

def findLetters(letter, search_box, driver):
    try:
        search_box.clear()

        if letter.isnumeric():
            letter = nums[str(letter)]
            findNumber(letter, search_box, driver)
            return "checking num"

        search_box.send_keys(letter)

        time.sleep(0.5)
        first_letter_locator = (By.XPATH, '//a[contains(@class, "abc-btn") and text()="'+letter.upper()+'"]')
        clickItem(first_letter_locator, driver)

        word_locator = (By.XPATH, '//a[contains(@title, "Click on this link for") and text()="'+letter.upper()+'"]')
        clickItem(word_locator, driver)

    except Exception as e:
        return 0

def findNumber(numberstr, search_box, driver):
    search_box.send_keys(numberstr)
    time.sleep(0.5)
    print(numberstr)

    if numberstr[0].isalpha():
        first_letter_locator = (By.XPATH, '//a[text()="'+numberstr[0].upper()+'"]')
        clickItem(first_letter_locator, driver)
        time.sleep(0.5)
    
    xpath = f'//a[text()="{numberstr}"]'
    number_locator = (By.XPATH, xpath)
    clickItem(number_locator, driver)


def getVideo(word, foldername, index, driver):
    element_present = EC.presence_of_element_located((By.CLASS_NAME, "v-asl"))
    WebDriverWait(driver, 20).until(element_present)

    video = driver.find_element("class name", "v-asl")

    video_url = video.get_property('src')

    filename = f"{foldername}/{index}_" + re.sub(r'[^\w\s]', '', word) + ".mp4"

    urllib.request.urlretrieve(video_url, filename)  

"""driver = startDriver()
j = 1
for i in ["6", "8", "7", "5"]:
    findLetters(i, driver)
    getVideo(i + "_letter", 'videos/amongusporn69', j, driver)
    j+=1"""
