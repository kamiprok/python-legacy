from selenium import webdriver
import selenium
import time
from selenium.webdriver.common.by import By

# "https://occ-0-1299-1432.1.nflxso.net/dnm/api/v6/0DW6CdE4gYtYx8iy3aj8gs9WtXE/AAAABTS9zxZzCI50PUvcdVfs0M5PgiUAYgRzyko1ZXP3RCGH19OXDbuyL0I5Q-Dfs-2PS-s3QMbv8o4FLqTeO6Nurw7a7cMx584s.webp?r=07e
# page = 'https://netflix.com/watch/70153404?tctx=2%2C1%2C%2C%2C'
# chrome_path = 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'
# webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
# webbrowser.get('chrome').open(page)

# pip install --update pyinstaller
# pyinstaller --onefile web.py
# 1. install updated pyinstaller.
# use command to make one file web.exe

driver = webdriver.Chrome('C:\\Users\\kprokopiuk\\Downloads\\chromedriver.exe')
driver.maximize_window()
driver.get('https://netflix.com/pl/Login')
login = driver.find_element_by_name('userLoginId')
login.send_keys('usr')
pwd = driver.find_element_by_name('password')
pwd.send_keys('pwd')
submit = driver.find_element_by_css_selector('.btn.login-button.btn-submit.btn-small').click()
time.sleep(1)
select_player = driver.find_element_by_xpath('//a[@href="/SwitchProfile?tkn=NRGZW7WK5BFBZASGM77GRHD2CQ"]').click()
time.sleep(3)
# driver.get('https://netflix.com/watch/70153404?tctx=2%2C1%2C%2C%2C')
# find_friends = driver.find_element_by_css_selector('.href="/watch/70153404?tctx=4%2C0%2C%2C%2C').click()
# find_friends = driver.find_element_by_xpath('//a[@href="/watch/70153404?tctx=4%2C0%2C%2C%2C"]').click()
search = driver.find_element_by_css_selector('.icon-search').click()
time.sleep(1)
find_friends = driver.find_element_by_xpath('//input[@type="text"]').send_keys('friends')
time.sleep(3)
# continue_watching = driver.find_element_by_xpath('//a[@href="/watch/70153404?tctx=4%2C0%2C%2C%2C"]').click()
continue_watching = driver.find_element_by_css_selector('.boxart-image.boxart-image-in-padded-container').click()
time.sleep(1)
continue_watching = driver.find_element_by_css_selector('.nf-flat-button-icon.nf-flat-button-icon-play').click()
#continue_watching = driver.find_element_by_xpath('//a[@href="/watch/70274039?trackId=14170287&tctx=0%2C0%2C525b09d0-d3f8-42a4-adf7-cfdb14f99ba3-106136389%2C4f3d7dee-0c01-4842-b6ed-c701815b42a5_23255056X3XX1553952494911%2C4f3d7dee-0c01-4842-b6ed-c701815b42a5_ROOT"]').click()
time.sleep(1)
# change_options = driver.find_elements_by_css_selector('.touchable.PlayerControls--control-element.nfp-button-control.default-control-button.button-nfplayerSubtitles').click()
# time.sleep(1)
# audio = driver.find_element_by_xpath('//li[@data-uia="track-audio-polski"]').click()
watch_fullscreen = driver.find_element_by_css_selector('.touchable.PlayerControls--control-element.nfp-button-control.default-control-button.button-nfplayerFullscreen').click()
