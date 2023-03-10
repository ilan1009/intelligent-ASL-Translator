import sys
from processInput import *
from crawl import *
from makevideo import *
from tqdm import tqdm
from args_handler import parse_arguments

args = parse_arguments()

if args['interactive']:
    x = receiveInput()
    inputted_text = x[0]
    foldername = x[1]
else:
    inputted_text = args['input_text']
    foldername = args['foldername']

speed = float(args['speed'])

foldername = 'videos/' + foldername
processed_text = processInput(inputted_text)

driver = startDriver()

try:
    mkdir(foldername)
except:
    pass

i = 1
progress_bar = tqdm(processed_text, unit="word")
for word in progress_bar:
    progress_bar.set_description("Getting word %s" % word)

    search_box = findSearchBox(driver)
    if len(word) == 1:
        findLetters(word, search_box, driver)
        getVideo(word + "_letter", foldername, i, driver)
        i += 1
    elif findWord(word, search_box, driver) != 0:
        getVideo(word, foldername, i, driver)
        i += 1
    else:
        for letter in tqdm(word, unit="letter", desc="getting letters for unknown word"):
            search_box = findSearchBox(driver)
            findLetters(letter, search_box, driver)
            getVideo(letter + "_letter", foldername, i, driver)
            i += 1

if args['speed'] == None:
    speed = float(input("Select speed for the merged video (Default speed (1) may be slow): " or 1))
vidfile = mergeVids(foldername, speed)
