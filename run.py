from selenium import webdriver

url = 'https://seriale.co/chirurdzy-serial-online/'

driver = webdriver.Chrome('C:/Users/kprokopiuk/Downloads/chromedriver.exe')
driver.get(url)

odc2 = []
odc = driver.find_elements_by_xpath('.//div[contains(@class, "seod")]')
# print(odc)

for i in odc:
    x = i.get_attribute('data')
    odc2.append(x)

print(odc2)
print('lista odcinkow')
driver.find_element_by_xpath(f'.//div[@data="{odc2[0]}"]').click()
print('kliknieto w pierwszy')
# driver.find_element_by_xpath('//div[@class="verystream msg ikona"]').click()
container = driver.find_element_by_xpath('.//div[contains(@class, "przerwa")]')

players = driver.find_elements_by_xpath('.//div[contains(@class, " ikona")]')
print(players)

# nie chce znalesc playerow
