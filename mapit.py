import webbrowser, sys, pyperclip

sys.argv    # sys.argv lets you intercept arguments from cmd

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
