import requests
from bs4 import BeautifulSoup
import pandas as pd


def scrapemetro(categoryurl, n_pages):
    data = []

    for pagenum in range(1, n_pages + 1):

        url = f'{categoryurl}?page={pagenum}'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')

        productblocks = soup.find_all('div', class_='product-card')

        for productblock in productblocks:
            id = productblock.get('data-product-id') if productblock.get('data-product-id') else ''
            name = productblock.get('data-name') if productblock.get('data-name') else ''
            link = categoryurl + productblock.get('data-product-url') if productblock.get('data-product-url') else ''
            regularprice = productblock.get('data-price-value') if productblock.get('data-price-value') else ''
            promoprice = productblock.get('data-price-discount') if productblock.get('data-price-discount') else ''
            brand = productblock.get('data-brand') if productblock.get('data-brand') else ''

            data.append([id, name, link, regularprice, promoprice, brand])

    df = pd.DataFrame(data, columns=['id', 'name', 'link', 'regular_price', 'promo_price', 'brand'])

    return df

category_url = 'https://online.metro-cc.ru/category/bakaleya/konservy/myasnye-konservy'  #URL категории товаров

n_pages = 100  #количество страниц для парсинга

df = scrapemetro(category_url, n_pages)

df.to_csv('metroproducts.csv', index=False)
df.to_csv('metro_products.csv', index=False)  # сохраняем данные в csv