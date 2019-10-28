import webbrowser
import time
from bs4 import BeautifulSoup

browser = webbrowser.get('"C:/Program Files (x86)/Google/Chrome/Application/chrome.exe" %s')
# while True:
#     webbrowser.get('"C:/Program Files (x86)/Google/Chrome/Application/chrome.exe" %s').open('google.com', new=0)
#     time.sleep(5)
#     webbrowser.open('bing.com', new=0)

# browser.open('google.com', new=0)
#
# browser.open('reddit.com', new=0)

html_doc = 'kamiprok.github.io'

soup = BeautifulSoup(html_doc, 'lxml')

print(soup.prettify())
print(BeautifulSoup('kamiprok', features='lxml'))
