from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

item_ls = []
item_url_ls = []

# ブラウザの設定
options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# ブラウザの起動
browser = webdriver.Chrome(options=options)
browser.implicitly_wait(3)

# キーワード設定
KEYWORD = 'macbook pro 2019 i7 16gb 256gb 15inch'

def get_url():
    # 売り切れ表示
    url = 'https://jp.mercari.com/search?keyword=' + KEYWORD + '&status=sold_out%7Ctrading'
    browser.get(url)
    browser.implicitly_wait(5)

    # 商品の詳細ページのURLを取得する
    item_box = browser.find_elements(By.CSS_SELECTOR, '#item-grid > ul > li')
    for item_elem in item_box:
        item_url_ls.append(item_elem.find_element(By.CSS_SELECTOR, 'a').get_attribute('href'))

def get_data():
    # 商品情報の詳細を取得する
    for item_url in item_url_ls:
        browser.get(item_url)
        time.sleep(3)
        # 商品名
        item_name = browser.find_element(By.CSS_SELECTOR, '#item-info > section:nth-child(1) > div.mer-spacing-b-12 > div > div > h1').text
        item_ex = browser.find_element(By.CSS_SELECTOR, '#item-info > section:nth-child(2) > div.merShowMore.mer-spacing-b-16 > div > pre').text
        src = browser.find_element(By.CSS_SELECTOR, '#main > article > div.sc-a6b7d8a7-2.WrJQp > section > div > div > div > div > div.sc-a6b7d8a7-2.ishIRQ > div > div.slick-slider.slick-initialized > div.slick-list > div > div.slick-slide.slick-active.slick-current > div > div > div > div > figure > div.imageContainer__f8ddf3a2 > picture > img').get_attribute('src')
        item_price = browser.find_element(By.CSS_SELECTOR, '#item-info > section:nth-child(1) > section:nth-child(2) > div > div > span:nth-child(2)').text

        data = {
            '商品名': item_name,
            '商品説明': item_ex,
            '価格': item_price,
            'URL': item_url,
            '画像URL': src
        }

        item_ls.append(data)

def main():
    get_url()
    get_data()
    pd.DataFrame(item_ls).to_csv('メルカリデータ.csv')

if __name__ == '__main__':
    main()
