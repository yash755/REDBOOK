import requests
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import time

import csv



file = open('do1.txt','r')

for f in file:

    f = f.replace('\n','')
    page_url = 'https://www.redbook.com.au' + f

    # driver.get(page_url)

    response = requests.request("GET", page_url)

    # html2 = driver.page_source
    html = BeautifulSoup(response.content, "lxml", from_encoding="utf-8")

    car_name  = ''
    make_name = ''
    model_name = ''
    micro_spec  = ''

    price = ''
    badge = ''
    series = ''
    body = ''
    seat_capacity = ''
    transmission = ''
    fuel_type = ''
    release_year = ''


    try:
        car_name_html = html.find('h1',{'class':'details-title'})
        car_name = car_name_html.text.strip()

    except:
        print ("Error")




    car_detail = car_name.split(' ')

    if len(car_detail) >=3:

        make_name = car_detail[1]
        model_name = car_detail[2]


    # models = ['1300', '147', '156', '159', '1600', '164', '166', '1750', '2000', '2600', '4C', 'Alfa 33', 'Alfa 75', 'Alfa 90', 'Alfasud', 'Alfetta', 'Brera', 'Giulia', 'Giulietta', 'GT', 'GTV', 'Mito', 'Montreal', 'Spider', 'Sprint', 'Stelvio']
    #
    #
    # make_name = 'Alfa Romeo'
    #
    # for model in models:
    #     if model in car_name:
    #         model_name = model
    #         break


    print (car_name)
    print (make_name)
    print (model_name)

    try:

        desc = html.find('div',{'class':'micro-spec'})
        dds = desc.find_all('dd')

        for dd in dds:
            micro_spec  = micro_spec + dd.text.strip() + '\n'

        print (micro_spec)

    except:
        print ("Error")


    try:
        tds = html.find_all('td',{'class':'item'})

        for td in tds:

            if 'Price' in td.text.strip():
                price = td.text.strip()
                price = price.replace('Price','')
                price = price.replace('(EGC)', '')
                price = price.replace('Guide', '')
                price = price.replace('\n', '')

            if 'Badge' in td.text.strip():
                badge = td.text.strip()
                badge = badge.replace('Badge','')
                badge = badge.replace('\n', '')


            if 'Series' in td.text.strip():
                series = td.text.strip()
                series = series.replace('Series','', 1)
                series = series.replace('\n', '')


            if body == '':
                if 'Body' in td.text.strip():
                    body = td.text.strip()
                    body = body.replace('Body','')
                    body = body.replace('\n', '')

            if 'Seat Capacity' in td.text.strip():
                seat_capacity = td.text.strip()
                seat_capacity = seat_capacity.replace('Seat Capacity','')
                seat_capacity = seat_capacity.replace('\n', '')


            if 'Transmission' in td.text.strip():
                transmission = td.text.strip()
                transmission = transmission.replace('Transmission','')
                transmission = transmission.replace('\n', '')

            if 'FuelType' in td.text.strip():
                fuel_type = td.text.strip()
                fuel_type = fuel_type.replace('FuelType','')
                fuel_type = fuel_type.replace('\n', '')

            if 'Release Year' in td.text.strip():
                release_year = td.text.strip()
                release_year = release_year.replace('Release Year','')
                release_year = release_year.replace('\n', '')


    except:
        print ("Error")


    print (price)
    print (badge)
    print (series)
    print (body)
    print (seat_capacity)
    print (transmission)
    print (fuel_type)
    print (release_year)


    arr = []
    temp = []

    temp.append(page_url)

    temp.append(car_name)
    temp.append(make_name)
    temp.append(model_name)
    temp.append(micro_spec)

    temp.append(price)
    temp.append(badge)
    temp.append(series)
    temp.append(body)
    temp.append(seat_capacity)
    temp.append(transmission)
    temp.append(fuel_type)
    temp.append(release_year)

    arr.append(temp)

    with open('alpina.csv', 'a+') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(arr)

