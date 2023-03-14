import re


def receiveInput():
    input_request = input("Please input below your request:\n")
    foldername = input("Desired folder name? Duplicates not recommended: ")
    return input_request, foldername

def processInput(request):
    text = re.sub(r'[^\w\s-]', '', request)
    print(text)


    blacklist = ['is', 'of', 'it', 'to']
    filterwords = {
        "dont": "do_not_(don't)",
        "mom": "mother",
        "dad": "father",
        "mister": "Ms._/_Mr.",
        "lonely": "lonely,_lone"
        "your", "yo": "you",
        "he": "him",
        "her": "she"
    }

    # Translate according to filter
    for word, replacement in filterwords.items(): 
        pattern = r'\b{}\b'.format(word)
        text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)

    ambiguouswords = {
        "like": ["like_(feeling)", "like_(similar)"],
        "i": ["I_(me)", "I"]
        # Add more ambiguous words and their possible replacements here
    }

    # Translate according to filter
    words = []
    for word in text.split():
        # Check if word is ambiguous
        if word.lower() in ambiguouswords:
            # Ask for clarification
            prompt = f"Which word do you mean by '{word}'?\n"
            for i, option in enumerate(ambiguouswords[word.lower()]):
                prompt += f"{i+1}. {option}\n"
            choice = input(prompt).strip().lower()
            while choice not in [str(i+1) for i in range(len(ambiguouswords[word.lower()]))]:
                choice = input(f"Invalid input. Please choose a number between 1 and {len(ambiguouswords[word.lower()])}\n").strip().lower()
            # Add the chosen replacement to the list of words
            words.append(ambiguouswords[word.lower()][int(choice)-1])
        else:
            # Add the original word to the list of words
            words.append(word)


    # Split words to list of words and remove blacklisted words
    words = [value for value in words if value not in blacklist]

    words = list(map(lambda st: str.replace(st, "_", " "), words))


    return words
