import requests

url = "https://www.redbook.com.au/cars/details/2013-abarth-595-50th-anniversary-manual/SPOT-ITM-450861/"

headers = {
    'sec-ch-ua': "\"Chromium\";v=\"88\", \"Google Chrome\";v=\"88\", \";Not A Brand\";v=\"99\"",
    'sec-ch-ua-mobile': "?0",
    'upgrade-insecure-requests': "1",
    'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36",
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    'sec-fetch-site': "none",
    'sec-fetch-mode': "navigate",
    'sec-fetch-user': "?1",
    'sec-fetch-dest': "document",
    'cache-control': "no-cache",
    'postman-token': "f29fd632-08eb-6f9e-2834-62ba170bcd52"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)