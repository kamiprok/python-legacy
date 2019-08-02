from selenium import webdriver
import getpass

login = input('Login: ')
pwd = getpass.getpass('Password: ')
browser = webdriver.Chrome('C:/Users/kprokopiuk/Downloads/chromedriver.exe')
browser.get('https://mmorpg.org.pl')
loguj = browser.find_element_by_class_name('btn-login')
loguj.click()
userElem = browser.find_element_by_id('user_login')
userElem.send_keys(login)  # admn no here
passwordElem = browser.find_element_by_id('user_password')
passwordElem.send_keys(pwd)  # password here
loginElem = browser.find_element_by_xpath("//input[@value='Zaloguj się']")
loginElem.submit()


# auto logowanie do mmorpg
