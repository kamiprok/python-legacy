import webbrowser

strona = input('Wpisz adres strony: ')
chrome_path = 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
webbrowser.get('chrome').open(strona)

# pip install --update pyinstaller
# pyinstaller --onefile web.py
# 1. install updated pyinstaller.
# use command to make one file web.exe
