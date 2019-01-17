import webbrowser

strona = input('Wpisz adres strony: ')
webbrowser.get('chrome').open(strona)

# pyinstaller.exe --onefile web.py
