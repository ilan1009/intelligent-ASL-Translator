from processInput import *
from crawl import *
from makevideo import *
from time import sleep
from tqdm import tqdm

class Main:
    inputted_text = receiveInput()
    processed_text = processInput(inputted_text)
    driver = startDriver()

    try:
        mkdir(inputted_text)
    except:
        pass

    i = 1
    for word in tqdm(processed_text):
        try:
            findWord(word, driver)
            getVideo(word, inputted_text, i, driver)
            i += 1
        except TimeoutException:
            print(f"skipped word {word}, couldnt be found", end=" ")

    vidfile = mergeVids(inputted_text, 1)