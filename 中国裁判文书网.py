import requests
import time
import execjs
import uuid
import json

def getJs(cookies):
    base64 = open("base64.js",'r',encoding='UTF-8')
    line = base64.readline()
    htmlstr = ""
    while line:
        htmlstr = htmlstr + line
        line = base64.readline()
    base64.close()
    md5 = open("md5.js", 'r', encoding='UTF-8')
    line = md5.readline()
    while line:
        htmlstr = htmlstr + line
        line = md5.readline()
    md5.close()
    js1 = open("aaa.js", 'r', encoding='UTF-8')
    line = js1.readline()
    htmlstr = htmlstr + 'var myCookies = \''+cookies+'\';'
    while line:
        htmlstr = htmlstr + line
        line = js1.readline()
    js1.close()
    return htmlstr

def getGuid():
    return str(uuid.uuid4())

def getNumber(guid):
    data = {'guid':guid}
    re = session.post('http://wenshu.court.gov.cn/ValiCode/GetCode',data = data)
    re.encoding = 'utf-8'
    return re.text

print("请输入你要爬取的关键词"); info = input()
print("请输入你需要爬取的文书上限数量"); limits = input()
print("正在准备爬取最大[" + limits + "]条与[" + info + "]有关的文书信息(不超过20 * k条)")

#添加关键词参数
payload = {'sorttype': '1'}
#修改header来模拟正常浏览器访问从而防止服务器对爬虫的过滤
myHeaders = {'Referer':'http://wenshu.court.gov.cn/list/list/',
            'User-Agent': 'User-Agent,Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}

#发送请求并获取数据
session = requests.session()
session.headers = myHeaders

#获取cookies
webFile = session.get('http://wenshu.court.gov.cn/list/list/',params = payload)
vjkl5 = webFile.cookies.get('vjkl5')

#生成guid密钥
guid = getGuid()

#通过guid向服务器请求得到number密钥
number = getNumber(guid)

#通过cookies计算密钥key,完成对3个密钥的获取
jsstr = getJs(vjkl5)
ctx = execjs.compile(jsstr)
compileFlag = False
while compileFlag == False:
    try:
        ctx = execjs.compile(jsstr)
        key = ctx.call("getKey")
        compileFlag = True
    except:
        time.sleep(5)
        print('.')

#组织好请求参数后通过密钥向服务器爬取数据
index = (int)(limits) // 20
for i in range(1,index + 1):
    time.sleep(1) #睡眠一下，防止封IP
    postData = {'Param':"全文检索:" + info,
                'Index':i,
                'Page':'20',
                'Order':'法院层级',
                'Direction':'asc',
                'vl5x':key,
                'number':number,
                'guid':guid,}

    cookie = {"vjkl5":vjkl5}
    result = session.post('http://wenshu.court.gov.cn/List/ListContent',data = postData)
    result.encoding = 'utf-8'
    resultData = json.loads(result.text);
    resultData = eval(resultData)
    print((str)(i / index * 100) + "%")
    for j in range(1,21):
        with open("文书概要/" + resultData[j]["案件名称"] + ".txt","w") as f:
            if "裁判要旨段原文" in resultData[j]:
                f.write(resultData[j]["裁判要旨段原文"])


print("已成功输出至文件")