import requests
import redis
import time
import json


r = redis.Redis(host='localhost',port=6379,db=1)
num = r.llen('the_ip')

while True:
    if num < 10:
        data = requests.get('http://piping.mogumiao.com/proxy/api/get_ip_al?appKey=0739b9bb45b0467685dbe5b796c170e4&count=1&expiryDate=0&format=1&newLine=2').text
        response = json.loads(data)
        code = response['code']
        if code == '0':
            ip_text = response['msg'][0]['ip']
            port = response['msg'][0]['port']
            ip = ip_text + ':' + port
            r.lpush('the_ip',ip)
            print('存入ip',ip)
        elif code == '3001':
            print('请求接口频繁,5秒提取一次',)
            num = r.llen('the_ip')
            time.sleep(5)
        else:
            print('请求接口错误',code)
            num = r.llen('the_ip')
            time.sleep(1)
    else:
        print('redis ip池已经存满')
        num = r.llen('the_ip')
        time.sleep(1)