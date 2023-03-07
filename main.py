from processInput import *
from crawl import *
from makevideo import *
from tqdm import tqdm

class Main:
    x = receiveInput()  # Recieve user input, text and folder name
    inputted_text = x[0]  # Initialize text requested
    foldername = "videos/" + x[1]  # Folder name

    processed_text = processInput(inputted_text)  #"Pre process" text to find out ambiguous words, filter and translate words.
    
    driver = startDriver()  # Init driver

    try:
        mkdir(foldername)
    except:
        pass

    i = 1
    # Progress bar using tqdm
    progress_bar = tqdm(processed_text, unit="word")
    for word in progress_bar:
        progress_bar.set_description("Getting word %s" % word)  # Display which word we're using
        
        if findWord(word, driver) != 0:  # If the word was found properly, get it normally
            getVideo(word, foldername, i, driver)
            i += 1
        else:  # Else, get each letter manually
            for letter in tqdm(word, unit="letter", desc="getting letters for unknown word"):
                findLetters(letter, driver)
                getVideo(letter + "_letter", foldername, i, driver)  # Add "_letter" suffix for each video of a letter being signed
                i += 1

    response = "y"  # You could ignore this.
    if response.lower() == "y":
        speed = float(input("Select speed for the merged video (Default speed (1) may be slow): " or 1))
        vidfile = mergeVids(foldername, speed)