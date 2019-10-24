import webbrowser, time

webbrowser.get('"C:/Program Files (x86)/Google/Chrome/Application/chrome.exe" %s')
while True:
    webbrowser.get('"C:/Program Files (x86)/Google/Chrome/Application/chrome.exe" %s').open('google.com', new=0)
    time.sleep(5)
    webbrowser.open('bing.com', new=0)


