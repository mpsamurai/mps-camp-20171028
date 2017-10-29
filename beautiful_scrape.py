from urllib.parse import urlencode
import requests
import bs4

url = 'https://item.mercari.com/jp/m72248239238/'
detail_dir = {'title': '', 'seller': '', 'ratings_good': '', 'ratings_normal': '', 'ratings_bad': '',
              'category_1': '', 'category_2': '', 'category_3': '', 'size': '', 'state': '',
              'shipping_fee': '', 'delivery': '', 'shipping_area': '', 'shipping_date': '',
              'price': '', 'sold_out': ''}
def get_details_value(url):
    resp = requests.get(url)
    details = bs4.BeautifulSoup(resp.text)
    # タイトル
    detail_dir['title'] = details.select('h2.item-name')[0].text
    # 出品者
    detail_dir['seller'] = details.select('table a')[0].text
    # レーティングgood
    detail_dir['ratings_good'] = details.select('div.item-user-ratings')[0]('span')[0].text
    # レーティングnormal
    detail_dir['ratings_normal'] = details.select('div.item-user-ratings')[1]('span')[0].text
    # レーティングbad
    detail_dir['ratings_bad'] = details.select('div.item-user-ratings')[2]('span')[0].text
    # カテゴリー
    detail_dir['category_1'] = details.select('table.item-detail-table')[0]('a')[1].text
    detail_dir['category_2'] = details.select('table.item-detail-table')[0]('a')[2].text
    detail_dir['category_3'] = details.select('table.item-detail-table')[0]('a')[3].text

    # サイズ
    detail_dir['size'] = details.select('table.item-detail-table')[0]('tr')[3]('td')[0].text
    # 商品の状態
    detail_dir['state'] = details.select('table.item-detail-table')[0]('tr')[4]('td')[0].text
    # 配送料の負担
    detail_dir['shipping_fee'] = details.select('table.item-detail-table')[0]('tr')[5]('td')[0].text
    # 配送の方法
    detail_dir['delivery'] = details.select('table.item-detail-table')[0]('tr')[6]('td')[0].text
    # 配送元地域
    detail_dir['shipping_area'] = details.select('table.item-detail-table')[0]('tr')[7]('td')[0].text
    # 配送元地域
    detail_dir['shipping_date'] = details.select('table.item-detail-table')[0]('tr')[8]('td')[0].text
    # 金額
    detail_dir['price'] = details.select('span.item-price')[0].text
    # 売り切れ情報
    detail_dir['sold_out'] = details.select('div.item-buy-btn.disabled.f18-24')[0].text

    return detail_dir


print(get_details_value(url))