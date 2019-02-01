import time
import numpy as np
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
 
url = 'http://bit.sikkou.jp/app/top/pt001/h01/'
 
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--window-size=1024,768')
 
driver = webdriver.Chrome(chrome_options=options)
driver.implicitly_wait(3)
 
driver.get(url)
aomori=driver.find_element_by_xpath("//*[@id='aomori']")
aomori.click()

areasearch=driver.find_element_by_xpath("//*[@id='areaSearch']")
areasearch.click()

aomori=driver.find_element_by_xpath('//*[@id="municipalityIds1"]')
aomori.click()

kamikita=driver.find_element_by_xpath('//*[@id="municipalityIds2"]')
kamikita.click()

towada=driver.find_element_by_xpath('//*[@id="municipalityIds9"]')
towada.click()

hachinohe=driver.find_element_by_xpath('//*[@id="municipalityIds12"]')
hachinohe.click()

misawa=driver.find_element_by_xpath('//*[@id="municipalityIds16"]')
misawa.click()

search=driver.find_element_by_xpath('//*[@id="btnSearch"]')
search.click()

case=driver.find_elements_by_xpath('//*[@id="listbox01"]/table/tbody/tr[1]/td/ul/li[2]')
price=driver.find_elements_by_xpath('//*[@id="listbox01"]/table/tbody/tr[1]/td/ul/li[3]/span')
ad=driver.find_elements_by_xpath('//*[@id="listbox01"]/table/tbody/tr[4]/td[2]')
caselst=[]
adlst=[]
prlst=[]

for i in case:
    caselst.append([i.text.strip("事件番号\n")])
for i in ad:
    adlst.append([i.text])
for i in price:
    prlst.append([i.text])




linkbox=driver.find_element_by_xpath('//*[@id="listbox01"]/div[13]/div')
linkbox.click()

case=driver.find_elements_by_xpath('//*[@id="listbox01"]/table/tbody/tr[1]/td/ul/li[2]')
price=driver.find_elements_by_xpath('//*[@id="listbox01"]/table/tbody/tr[1]/td/ul/li[3]/span')
ad=driver.find_elements_by_xpath('//*[@id="listbox01"]/table/tbody/tr[4]/td[2]')

for i in case:
    caselst.append([i.text.strip("事件番号\n")])
for a in ad:
    adlst.append([a.text])
for i in price:
    prlst.append([i.text])


lst=np.concatenate((caselst,adlst,prlst),axis=1)


print(lst)
driver.quit()
