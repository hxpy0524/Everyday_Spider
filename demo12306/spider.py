import requests
from demo12306 import config
# cookie保持
session = requests.Session()


# 下载验证码
captcha_url = 'https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand&0.6123313878197223'

# 下载图片
response = session.get(captcha_url)

img_content = response.content

# 写入图片 wb w写入文件 b以2进制
# fb = open('captcha.jpg', 'wb')
# fb.write(img_content)
# fb.close()
with open('captcha.jpg', 'wb') as f:
    f.write(img_content)


# 检验验证码
check_captcha_api = 'https://kyfw.12306.cn/passport/captcha/captcha-check'
code = input('请输入验证码的坐标以空格隔开>>>')
data = {
    'answer': code.split(' '),
    'login_site': 'E',
    'rand': 'sjrand'
}

check_response = session.post(url=check_captcha_api,data=data)
print(check_response.text)

# 登陆
login_url_api = 'https://kyfw.12306.cn/passport/web/login'
login_data = {
    'username':config.username,
    'password':config.password,
    'appid':'otn'
}

login_response = session.post(url=login_url_api,data=login_data)
print(login_response.text)