# author    : Charles
# time      ：2020/7/22  14:04 
# file      ：get_temperature.PY
# project   ：apiToy
# IDE       : PyCharm

import requests
from lxml import etree


def get_temperature_shanghai():
    headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1 Trident/5.0;"}
    url = "https://www.baidu.com/s?wd=%E4%B8%8A%E6%B5%B7%E6%B0%94%E6%B8%A9&ie=UTF-8"
    html = requests.get(url, headers=headers)
    selector = etree.HTML(html.text)
    path1 = "/html/body/div/div[3]/div[1]/div[3]/div[1]/div[1]/div[1]/a[1]/div[1]/div[2]/span[1]"
    results = selector.xpath(path1)
    return results[0].text


if __name__ == '__main__':
    a = get_temperature_shanghai()
    print(a)