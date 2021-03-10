import requests
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import time



mail_url = 'https://www.redbook.com.au/cars/results?s=49470&evnt=pagination&sort=MakeModel'

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

chrome_options = Options()
# chrome_options.add_argument('--proxy-server=%s' % PROXY)
# chrome_options.add_argument("--headless")
# chrome_options.add_argument('--user-agent="Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 640 XL LTE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10166"')
chrome_options.add_argument("--window-size=1920x1080")
driver = webdriver.Chrome(options=chrome_options, executable_path=ChromeDriverManager().install())

driver.get(mail_url)

time.sleep(30)


# html2 = driver.page_source
# html = BeautifulSoup(html2, "lxml", from_encoding="utf-8")
#
# links = html.find_all('a',{'class':'item'})
#
# for link in links:
#     print (link.get('href'))
#
#     file = open('cars.txt','a+')
#     file.write(link.get('href'))
#     file.write('\n')
#     file.close()

page = 55875

while page < 69990:



    driver.get('https://www.redbook.com.au/cars/results?s=' + str(page) + '&evnt=pagination&sort=MakeModel')

    html2 = driver.page_source
    html = BeautifulSoup(html2, "lxml", from_encoding="utf-8")

    links = html.find_all('a', {'class': 'item'})

    for link in links:
        print (link.get('href'))
        file = open('cars.txt', 'a+')
        file.write(link.get('href'))
        file.write('\n')
        file.close()

    page = page+15