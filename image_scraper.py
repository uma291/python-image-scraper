from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
import os
import urllib
import argparse

#below is the search term you want to search on google images (first try out manually, which term fetches you more relevant images)
searchterm = 'handgun shootings' 
url = "https://www.google.co.in/search?q="+searchterm+"&source=lnms&tbm=isch"
browser = webdriver.Chrome(executable_path='C:/chrome_driver/chromedriver.exe')
browser.get(url)
header={'User-Agent':"Chrome/76.0.3809.36"}
counter = 0
succounter = 0

if not os.path.exists(searchterm):
    os.mkdir(searchterm)

for _ in range(1000):
    browser.execute_script("window.scrollBy(0,10000)")

for x in browser.find_elements_by_xpath('//div[contains(@class,"rg_meta")]'):
    counter = counter + 1
    print("Total Count:", counter)
    print("Succsessful Count:", succounter)
    print("URL:",json.loads(x.get_attribute('innerHTML'))["ou"])
    img = json.loads(x.get_attribute('innerHTML'))["ou"]
    imgtype = json.loads(x.get_attribute('innerHTML'))["ity"]
    try:
        path = os.path.join(searchterm , searchterm + "_" + str(counter) + "." + imgtype)
        urllib.request.urlretrieve(img, path)
        succounter = succounter + 1
    except:
        print("can't get img")

print(succounter, "pictures succesfully downloaded")
browser.close()