import time

import requests
import json
import demjson
from bs4 import BeautifulSoup
# from requests_html import HTMLSession
# from selenium import webdriver

URL = 'https://firdavsaroma.ru/o/74367a/'


def get_soup(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, features='html.parser')
    else:
        soup = None
    return soup

def get_data_selenium(url):
    options = webdriver.FirefoxOptions()
    options.set_preference('general.useragent.override', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36')
    try:
        driver = webdriver.Firefox(
            executable_path='geckodriver',
            options = options
        )
        driver.get(url=url)
        time.sleep(5)

        with open('index_selenium.html', 'w') as file:
            file.write(driver.page_source)

    except Exception as ex:
        print(ex)

    finally:
        driver.close()
        driver.quit()

# print(get_soup(URL).text)

soup = get_soup(URL)

# print((soup))

script = soup.find('script').text.strip().replace('window.account = ', '') \
    .replace('window.account = ', '').replace('window.data = ', '').split('};')[0].split(',"html"')[0] + '}'
# print((script))

# found = demjson.decode(script[script.index("{"):script.index("}")] + "}")
# print(found)

data = (json.loads(json.dumps(script)))
# print(data)
# print(type(data))


test = soup.find('script').text.splitlines()[2].strip()[14:-1] #.split('};	')[0][17:-1].split()
# print((test))

data = (json.loads(test))
# print(data)
# print(type(data))
#
#
print(data['product']['title'])
# print(data['variants'][0]['variant_values'])
# print(data['variants_offers']['922193:0']['price'])

volumes = list(data['variants'][0]['variant_values'])
prices = (data['variants_offers'])
print(volumes)

print(prices)

prices_list = []
for n, offer in enumerate(prices):
    price = prices[offer]["price"]
    prices_list.append(price)

print(prices_list)
# print(data['variants_offers'])
#
# for str in data:
#     if 'variants' in str:
#         print(str)




# #create the session
# session = HTMLSession()
#
# #define our URL
# url = 'https://firdavsaroma.ru/m/'
#
# #use the session to get the data
# r = session.get(url)
#
# #Render the page, up the number on scrolldown to page down multiple times on a page
# r.html.render(sleep=5, keep_page=True, scrolldown=10)
# #
# # #take the rendered html and find the element that we are interested in
# # videos = r.html.find('col-xs-6')
# #
# # #loop through those elements extracting the text and link
# # for item in videos:
# #     video = {
# #         'title': item.text,
# #         'link': item.absolute_links
# #     }
# #     print(video)
#
# print(r)

# r = requests.get('https://firdavsaroma.ru/api/market/products/list.json?collection_id=&next=379&filters%5Bquery%5D=').text
#
# print(r)

# driver = Chrome(executable_path=''

volumes_list = []
volumes = list(data['variants'][0]['variant_values'])
for n in range(len(volumes)):
    volume = volumes[n]
    volumes_list.append(volume)

# print(volumes_list)

description = str(soup.find_all('meta')[0])[15:-22].strip()
# print(soup)
print(description)

def main():
    # get_data_selenium('https://firdavsaroma.ru/m')
    pass

if __name__ == '__main__':
    main()