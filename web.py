import webbrowser
# "https://occ-0-1299-1432.1.nflxso.net/dnm/api/v6/0DW6CdE4gYtYx8iy3aj8gs9WtXE/AAAABTS9zxZzCI50PUvcdVfs0M5PgiUAYgRzyko1ZXP3RCGH19OXDbuyL0I5Q-Dfs-2PS-s3QMbv8o4FLqTeO6Nurw7a7cMx584s.webp?r=07e
strona = 'https://netflix.com/watch/70153404?tctx=2%2C1%2C%2C%2C'
chrome_path = 'C:\\Users\\KAMSON-PC\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe'
firefox_path = 'C:\\Program Files\\Mozilla Firefox\\firefox.exe'
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
webbrowser.register('firefox', None, webbrowser.BackgroundBrowser(firefox_path))
webbrowser.get('firefox').open(strona)

# how to make bat
# @py C:\Users\KAMSON-PC\PycharmProjects\python-random\web.py %*

# pip install --update pyinstaller
# pyinstaller --onefile web.py
# 1. install updated pyinstaller.
# use command to make one file web.exe
