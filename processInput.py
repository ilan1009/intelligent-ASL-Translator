import re


def receiveInput():
    input_request = input("Please input below your request:\n")
    foldername = input("Desired folder name? Duplicates not recommended: ")
    return input_request, foldername

def processInput(request):
    text = re.sub(r'[^\w\s]', '', request)
    print(text)


    blacklist = ['is']
    filterwords = {
        "dont": "do_not_(don't)",
        "i": "I_(me)", 
        "mom": "mother",
        "dad": "father",
        "mister": "Ms._/_Mr.",
        "lonely": "lonely,_lone"
    }

    # Translate according to filter
    for word, replacement in filterwords.items(): 
        pattern = r'\b{}\b'.format(word)
        text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)

    ambiguouswords = {
        "like": ["like_(feeling)", "like_(similar)"],
        # Add more ambiguous words and their possible replacements here
    }

    # Translate according to filter
    for word, replacements in ambiguouswords.items():
        if word in text.lower():
            prompt = f"Which word do you mean by '{word}'?\n"
            for i, option in enumerate(replacements):
                prompt += f"{i+1}. {option}\n"
            choice = input(prompt).strip().lower()
            while choice not in [str(i+1) for i in range(len(replacements))]:
                choice = input(f"Invalid input. Please choose a number between 1 and {len(replacements)}\n").strip().lower()
            text = text.lower().replace(word, replacements[int(choice)-1])


    # Split words to list of words and remove blacklisted words
    words = text.split()
    words = [value for value in words if value not in blacklist]

    words = list(map(lambda st: str.replace(st, "_", " "), words))


    return words
