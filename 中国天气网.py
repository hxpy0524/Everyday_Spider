import requests
from bs4 import BeautifulSoup
import time

def get_weather(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Mobile Safari/537.36',
        'Upgrade-Insecure-Requests': '1',
        'Referer': 'http://www.weather.com.cn/textFC/hb.shtml',
        'Host': 'www.weather.com.cn'
    }

    req = requests.get(url, headers=headers)
    content = req.content

    soup = BeautifulSoup(content, 'html.parser')
    conMidtab = soup.find('div', attrs={'class': 'conMidtab'})
    conMidtab2_list = conMidtab.find_all('div', attrs={'class': 'conMidtab2'})

    for con in conMidtab2_list:
        tr_list = con.find_all('tr')[2:]
        province = ""
        for index, tr in enumerate(tr_list):
            if index == 0:
                td_list = tr.find_all('td')
                province = td_list[0].get_text().replace('\n', '')
                city = td_list[1].get_text().replace('\n', '')
                weather_phenomena = td_list[2].get_text().replace('\n', '')
                wind = td_list[3].find('span').get_text().replace('\n', '')
                direction = td_list[3].find('span', attrs={'class': 'conMidtabright'}).get_text().replace('\n', '')
                max_height_tep = td_list[4].get_text().replace('\n', '')
                min_low_tep = td_list[7].get_text().replace('\n', '')
                # print('省/直辖市：%s    市或区：%s    最低温度：%s' % (province, city, min_low_tep))
            else:
                td_list = tr.find_all('td')
                city = td_list[0].get_text().replace('\n', '')
                weather_phenomena = td_list[1].get_text().replace('\n', '')
                wind = td_list[2].find('span').get_text().replace('\n', '')
                direction = td_list[2].find('span', attrs={'class': 'conMidtabright'}).get_text().replace('\n', '')
                max_height_tep = td_list[3].get_text().replace('\n', '')
                min_low_tep = td_list[6].get_text().replace('\n', '')
                # print('     else      市或区：%s    最低温度：%s' % (city, min_low_tep))
            print('省/直辖市：%s    市或区：%s    天气现象：%s    风向：%s    风力：%s    最高温度：%s    最低温度：%s' %
                  (province, city, weather_phenomena, wind, direction, max_height_tep, min_low_tep))


def main():
    urls = ['http://www.weather.com.cn/textFC/hb.shtml',
            'http://www.weather.com.cn/textFC/db.shtml',
            'http://www.weather.com.cn/textFC/hd.shtml',
            'http://www.weather.com.cn/textFC/hz.shtml',
            'http://www.weather.com.cn/textFC/hn.shtml',
            'http://www.weather.com.cn/textFC/xb.shtml',
            'http://www.weather.com.cn/textFC/xn.shtml',
            ]

    for url in urls:
        get_weather(url)
        time.sleep(2)


if __name__ == '__main__':
    main()