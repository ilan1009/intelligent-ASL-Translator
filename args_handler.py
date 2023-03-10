import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description='Create sign language video from input text.')
    parser.add_argument('-i', '--interactive', action='store_true', help='enable interactive mode for input text')
    parser.add_argument('-t', '--text', metavar='input_text', type=str, help='input text as command-line argument')
    parser.add_argument('-f', '--file', metavar='input_file', type=str, help='input text file')
    parser.add_argument('-o', '--output', metavar='foldername', type=str, help='name of folder to store output')
    parser.add_argument('-s', '--speed', metavar='speed', type=float, help='speed of rendered output video')

    args = parser.parse_args()
    speed = args.speed

    if args.text and args.file:
        raise ValueError("Error: Only one of --text or --file can be provided.")
    elif args.text and args.output:
        inputted_text = args.text
        foldername = args.output
    elif args.file and args.output:
        with open(args.file, 'r') as f:
            inputted_text = f.read()
        foldername = args.output
    elif args.interactive:
        print("Using interactive mode...")
        if speed != None:
            print("Speed defined: " + str(speed))
    else:
        raise ValueError('Missing arguments, use -i for interactive mode, or try --help for help')

import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description='Create sign language video from input text.')
    parser.add_argument('-i', '--interactive', action='store_true', help='enable interactive mode for input text')
    parser.add_argument('-t', '--text', metavar='input_text', type=str, help='input text as command-line argument')
    parser.add_argument('-f', '--file', metavar='input_file', type=str, help='input text file')
    parser.add_argument('-o', '--output', metavar='foldername', type=str, help='name of folder to store output')
    parser.add_argument('-s', '--speed', metavar='speed', type=float, help='speed of rendered output video')

    args = parser.parse_args()
    speed, inputted_text, foldername, interactive = None, None, None, None

    speed = args.speed
    if args.interactive:
        interactive = True
    if args.text and args.file:
        raise ValueError("Error: Only one of --text or --file can be provided.")
    elif args.text and args.output:
        inputted_text = args.text
        foldername = args.output
    elif args.file and args.output:
        with open(args.file, 'r') as f:
            inputted_text = f.read()
        foldername = args.output
    elif args.interactive:
        print("Using interactive mode...")
        if speed != None:
            print("Speed defined: " + str(speed))
        else:
            print("Speed will be defined during interactive mode")
    else:
        raise ValueError('Missing arguments, use -i for interactive mode, or try --help for help')

    return {
        'interactive': interactive,
        'input_text': inputted_text,
        'foldername': foldername,
        'speed': speed,
    }

