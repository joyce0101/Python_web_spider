import bs4
from bs4 import BeautifulSoup
import requests
import lxml
from prettytable import PrettyTable
"""
爬取自如上的房源，利用表格进行展示，后面有链接，可以直接访问，修改url为你需要的地区和房型即可，减去了不必要的筛选时间
后面会进行数据的清洗和分析，展示一些房源的价格走势等信息
"""

if __name__ == '__main__':
    http_url = "http://www.ziroom.com/z/nl/z1.html?qwd=%E4%BA%94%E9%81%93%E5%8F%A3"
    adds = []
    mess = []
    hrefs = []
    area = []
    height = []
    huxing = []
    price = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36',
        }
    r = requests.get(url=http_url, headers=headers)
    html = r.content
    soup = BeautifulSoup(html, 'lxml')
    # print(soup)
    house = soup.find('ul', id="houseList")
    house_info = house.find_all('div', class_="txt")
    # print(house_info)
    for house in house_info:
        mess.append(house.h3.a.get_text())
        # print(house.h3.a.get_text())
        hrefs.append(str(house.h3.a["href"]))  # 强制转换成string类型
        adds.append(house.h4.get_text())
        detail_info = house.find_all('div', class_="detail")
        for detail in detail_info:
            # print(detail.p.contents)
            area.append(detail.p.contents[1].get_text())
            height.append(detail.p.contents[3].get_text())
            huxing.append(detail.p.contents[5].get_text())
    price_detail = soup.find_all('div', class_="priceDetail")

    """
    print(type(adds[0]))
    print(type(height[0]))
    print(mess)
    print(adds)
    print(area)
    print(height)
    print(huxing)
    print(hrefs)
    """
    table = PrettyTable()
    table.add_column("小区", mess)
    table.add_column("地址", adds)
    table.add_column("面积", area)
    table.add_column("层数", height)
    table.add_column("户型", huxing)
    table.add_column("链接", hrefs)
    print(table)


