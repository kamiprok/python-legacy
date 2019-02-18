from selenium import webdriver
from getpass import getpass
from selenium.webdriver.common.keys import Keys

#usr = input("Login: ")
#pwd = getpass("Haslo: ")

usr = 'user'
pwd = 'password'

driver = webdriver('C:/Users/kprokopiuk/Downloads/chromedriver.exe')
driver.get('https://mmorpg.org.pl')

loguj = driver.find_element_by_class_name('btn-login')
loguj.click()

usr_box = driver.find_element_by_id('user_login')
usr_box.send_keys(usr)

pwd_box = driver.find_element_by_id('user_password')
pwd_box.send_keys(pwd)

login_button = driver.find_element_by_xpath("//input[@value='Zaloguj się']")
login_button.click()


# auto logowanie mmorpg druga metoda
