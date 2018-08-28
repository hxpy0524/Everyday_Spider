import requests
from lxml import etree
import re
import time
import json


def get_html(page):
    url = 'https://search.jd.com/s_new.php'

    params = {
        'keyword':'周杰伦',
        'enc': 'utf-8',
        'qrst': '1',
        'rt':'1',
        'stop': '1',
        'vt': '2',
        'page': page,
        's': '112',
        'click': '0'
    }
    headers = {
            'cookie': '__jdu=1491168338; PCSYCityID=1; shshshfp=eaaf7392dd9d0e86086c09390fae21ab; shshshfpa=c2e33698-dc0e-6856-8d55-abef387af62b-1526259080; shshshfpb=08593f5a679667056d369373c180f46798dc2fc3511d5f25e5af8dd862; user-key=cfca7fde-d593-451c-9994-bf41a97f87d0; cn=0; xtest=4022.cf6b6759; ipLoc-djd=1-72-2799-0; qrsc=3; unpl=V2_ZzNtbUdWRkZ2D0cAKBkJA2JTFF9KUUUXd1sVVnhMCQFjUBoKclRCFXwUR1BnGVkUZwQZWUJcQBZFCHZXchBYAWcCGllyBBNNIEwHDCRSBUE3XHxcFVUWF3RaTwEoSVoAYwtBDkZUFBYhW0IAKElVVTUFR21yVEMldQl2VH4RXAVgChBfS2dzEkU4dlx%2bH10EYTMTbUNnAUEpCkFWcxtbSGcGGl1CUEoXdwF2VUsa; CCC_SE=ADC_FkhJWEGyRxrUqx3AJN1rCyJsOh%2bDxyBOEKZ0doRuz%2fnIzwbVza4OXGKiIT6sIVZBco7IcvyNze9DVgufWCFsA3iZoK%2bIiBnDfnr3ykzY%2bSj44xBlg6iVXNazwS7YW630xPpYL8R9b1%2bv834rCmnwECXicCG6XMRNwpyKEpsenlFraDQ177ZbYwO0%2foKMiMhd9GF4cEHlexpj47v7rHPsENVlQxqZuQryXp9ZI5h%2fJ9at%2bQ7sv%2bLuI%2f3ydLCSbfkFjNyKmOMnXjcro7nISQQMGcOgUhqrzh15zqDh3z%2f7GRHrUX6%2bM8%2biXC5FGu5YIJk4tlZPoFw1kMGIvxE6aPZFltRpzMxoT%2b7nKa%2fBxFVf90EPJ1bhuJu4%2bXoG9iCZWc4jbEQyD7uqY33m%2fBHQPJjMcHnLXjh0juv6SOGgFvXefCCNm7oD9Ll6rJ%2bnspbbZQNupZw0J1IZfDbmrz30QH%2fHMsrpe8NOmCQkph19i6S%2b%2f4SYFAxryNOIirvYXcjtx%2b2ngITFXKAbfaIvGLZ%2bRz5uZODo8wMEVs2YFL0cjKC0CI9X%2b61qN6RfCkl7Zvo9hJUp; __jda=122270672.1491168338.1526259077.1526276609.1526287883.3; __jdc=122270672; __jdv=122270672|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_404b260eb1d74a7397733bb32dd55b9f|1526287883455; shshshsID=5a25bd3966d10d74ac93343ee61491f4_1_1526287886998; rkv=V0300; _jrda=1; _jrdb=1526288736201; wlfstk_smdl=kxuq2d6owlafj6ljuhx0zg98fo60hf72; _pst=jd_4e5886aea9ee6; logintype=wx; unick=jd_4e5886aea9ee6; pin=jd_4e5886aea9ee6; npin=jd_4e5886aea9ee6; thor=D8276A41F6FB071C5E766AA1B328257A66D5D4EC654917DF043FBBA12E9E1F44665EC077CFCA7C6522508096859917E94260C68DA027ACF40F5A730361BAD243AFFA863D5903534444E9083765B4323661580DE87707D43D1CDBBC330F30541A653B990B3DF1AA6C3857124BD4A21CD32A3BF850821C423047116C165652E26124535E53B6875C45225FCF38CAE0F084B47CE94909EAF34CE25CFFB889BC77FA; _tp=9A8oXKzFEdM%2BYwFpDu6UuHC6iJkLft6SrgBOHZL%2FsdU%3D; pinId=x-AZ3d0Upjkyqpe8Mqp9RLV9-x-f3wj7; __jdb=122270672.14.1491168338|3.1526287883; 3AB9D23F7A4B3C9B=7DLSHVTFX3PSD4IV3HN4GOBDZL2TW3BHTWBRNF5QGDOVRHVNC5R2DDKCNRDWOL34WJWDJOOXDSV6NTA4V5OUG67AIQ',
            'referer': 'https://search.jd.com/Search?keyword=%E5%91%A8%E6%9D%B0%E4%BC%A6&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&page=5&s=112&click=0',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'

    }
    html = requests.get(url,headers=headers,params=params).text
    return html


def look_detail(mark,href,i):
    if mark and href is not None:
        headers = {
            'cookie': '__jdu=1491168338; PCSYCityID=1; shshshfp=eaaf7392dd9d0e86086c09390fae21ab; shshshfpa=c2e33698-dc0e-6856-8d55-abef387af62b-1526259080; shshshfpb=08593f5a679667056d369373c180f46798dc2fc3511d5f25e5af8dd862; user-key=cfca7fde-d593-451c-9994-bf41a97f87d0; cn=0; ipLoc-djd=1-72-2799-0; unpl=V2_ZzNtbUdWRkZ2D0cAKBkJA2JTFF9KUUUXd1sVVnhMCQFjUBoKclRCFXwUR1BnGVkUZwQZWUJcQBZFCHZXchBYAWcCGllyBBNNIEwHDCRSBUE3XHxcFVUWF3RaTwEoSVoAYwtBDkZUFBYhW0IAKElVVTUFR21yVEMldQl2VH4RXAVgChBfS2dzEkU4dlx%2bH10EYTMTbUNnAUEpCkFWcxtbSGcGGl1CUEoXdwF2VUsa; CCC_SE=ADC_FkhJWEGyRxrUqx3AJN1rCyJsOh%2bDxyBOEKZ0doRuz%2fnIzwbVza4OXGKiIT6sIVZBco7IcvyNze9DVgufWCFsA3iZoK%2bIiBnDfnr3ykzY%2bSj44xBlg6iVXNazwS7YW630xPpYL8R9b1%2bv834rCmnwECXicCG6XMRNwpyKEpsenlFraDQ177ZbYwO0%2foKMiMhd9GF4cEHlexpj47v7rHPsENVlQxqZuQryXp9ZI5h%2fJ9at%2bQ7sv%2bLuI%2f3ydLCSbfkFjNyKmOMnXjcro7nISQQMGcOgUhqrzh15zqDh3z%2f7GRHrUX6%2bM8%2biXC5FGu5YIJk4tlZPoFw1kMGIvxE6aPZFltRpzMxoT%2b7nKa%2fBxFVf90EPJ1bhuJu4%2bXoG9iCZWc4jbEQyD7uqY33m%2fBHQPJjMcHnLXjh0juv6SOGgFvXefCCNm7oD9Ll6rJ%2bnspbbZQNupZw0J1IZfDbmrz30QH%2fHMsrpe8NOmCQkph19i6S%2b%2f4SYFAxryNOIirvYXcjtx%2b2ngITFXKAbfaIvGLZ%2bRz5uZODo8wMEVs2YFL0cjKC0CI9X%2b61qN6RfCkl7Zvo9hJUp; __jdc=122270672; __jdv=122270672|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_404b260eb1d74a7397733bb32dd55b9f|1526287883455; _jrda=1; wlfstk_smdl=kxuq2d6owlafj6ljuhx0zg98fo60hf72; _pst=jd_4e5886aea9ee6; logintype=wx; unick=jd_4e5886aea9ee6; pin=jd_4e5886aea9ee6; npin=jd_4e5886aea9ee6; _tp=9A8oXKzFEdM%2BYwFpDu6UuHC6iJkLft6SrgBOHZL%2FsdU%3D; pinId=x-AZ3d0Upjkyqpe8Mqp9RLV9-x-f3wj7; 3AB9D23F7A4B3C9B=7DLSHVTFX3PSD4IV3HN4GOBDZL2TW3BHTWBRNF5QGDOVRHVNC5R2DDKCNRDWOL34WJWDJOOXDSV6NTA4V5OUG67AIQ; __jda=122270672.1491168338.1526259077.1526287883.1526296071.4; ipLocation=%u5317%u4EAC; areaId=1; mt_xid=V2_52007VwMXWl1YVVMdSxBsA24LGgFbW1BGS00YXRliVBQBQVEHXBtVHQ9SNAYVBQ9cBltKeRpdBW4fE1ZBWFdLH0ESXw1sBxpiX2hSahZLGlsMbwQaVlxQW1sXThFaBmAzEldbXw%3D%3D; thor=AB732380AB5D58B72DE201BE7D52E7A43298725478E3CF436B67AC430E8A269D8A0EC04A27CE870B393CFE70DE6D5A0A978E321313183CB0DFE7BABD2A3D3DF60DBF85DA3ED47A0D89349110BD9B1995D22B772110505EA73B6499D58B6F385F1752CA46CBD0B26DD6C36F8C131D31D11F939C3BBC3F4C87404E0A38A249FFAA7321C3F0CBF594D2B3F949688743CB481952AF1962FF4E23F68AD4F7BB440474; __jdb=122270672.13.1491168338|4.1526296071',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
        }
        params = {

            'productId':mark,
            'score': '0',
            'sortType': '5',
            'page': i,
            'pageSize': '10',
            'isShadowSku': '0',
            'fold': '1',
        }
        url2 = 'https://sclub.jd.com/comment/productPageComments.action'
        time.sleep(2)
        detail_html = requests.get(url2,headers=headers,params=params).text
        time.sleep(2)
        return detail_html


def look_ping(detail_html):
    if detail_html:
        detail_html = json.loads(detail_html)
        comments = detail_html.get('comments')

        for comm in comments:

            content = comm.get('content')

            return content



def get_info(html):
    if html:
        x_html = etree.HTML(html)

        info_list = x_html.xpath('//li[@class="gl-item"]/div[@class="gl-i-wrap"]')

        # info_list = x_html.xpath('//*[@id="J_goodsList"]/ul/li')
        for info in info_list:
            title = info.xpath('./div[@class="p-img"]/a/@title')[0]
            href = info.xpath('./div[@class="p-img"]/a/@href')[0]
            price = info.xpath('./div[@class="p-price"]/strong/i/text()')[0]
            shop = info.xpath('./div[@class="p-shopnum"]/a/text()')
            if shop:
                shop = shop[0]
            pattern = re.compile('//item.jd.com/(\d+).html')
            mark = pattern.findall(href)
            if mark:
                mark = mark[0]
                print(mark)
                for i in range(5):
                    detail_html = look_detail(mark,href,i)
                    content = look_ping(detail_html)
                    it = {
                        'title':title,
                        'price':price,
                        'shop':shop,
                        'content':content
                    }
                    print(it)

def main():
    for page in range(1,5):
        html = get_html(page)
        get_info(html)

if __name__ == '__main__':
    # main()
    a, *b, c = 1, 2,3,3,4,5, *range(1,5,2), 6
    print(*b)