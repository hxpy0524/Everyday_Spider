import requests
import re

def getBdMsg(keyword,page):
    headers = {
        'User-Agent':'Mozilla/5.0(WindowsNT10.0;Win64;x64;rv: 59.0)Gecko/20100101Firefox/59.0'
    }
    res = requests.get('https://www.baidu.com/s?wd={}&pn={}'.format(keyword,page),headers=headers).text

    # req = res.replace(,)
    # replace_reg = re.compile(r'//www.baidu.com/img/baidu_jgylogo3.gif')
    # print(replace_reg.sub('static/images/tz.png', res))
    return res.replace('//www.baidu.com/img/baidu_jgylogo3.gif','static/images/tz.png')
                       # '<input id="su" value="百度一下" class="bg s_btn" type="submit">',
                       # '<input id="su" value="韩爸爸一下" class="bg s_btn" type="submit">')
    # return res.replace('//www.baidu.com/img/baidu_jgylogo3.gif','static/images/tz.png')


if __name__ == '__main__':
    print(getBdMsg('python',0))

