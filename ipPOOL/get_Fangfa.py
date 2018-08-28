from lxml import etree
import redis
import requests

r = redis.Redis(host='localhost',port=6379,db=1)
def get_source(url, headers, data=None, menth='get'):
    ip = r.rpop('the_ip')
    n = 0
    while True:
        try:
            if menth == 'get':
                if data == None:
                    source = requests.get(url,headers=headers,proxies={'http':ip,'https':ip,},timeout=5)
                    r.lpush('the_ip', ip)
                    print('请求成功，归还ip',ip)
                    return source
                else:
                    source = requests.get(url, headers=headers,proxies={'http':ip,'https':ip,},params=data,timeout=5)
                    r.lpush('the_ip', ip)
                    print('请求成功，归还ip',ip)
                    return source
            else:
                if data == None:
                    source = requests.post(url, headers=headers,proxies={'http':ip,'https': ip},timeout=5)
                    r.lpush('the_ip', ip)
                    print('请求成功，归还ip',ip)
                    return source
                else:
                    source = requests.post(url, headers=headers,proxies={'http':ip,'https': ip},data=data,timeout=5)
                    r.lpush('the_ip', ip)
                    print('请求成功，归还ip',ip)
                    return source
        except:
            n+=1
            if n == 3:
                return get_source(url, headers, data, menth)




