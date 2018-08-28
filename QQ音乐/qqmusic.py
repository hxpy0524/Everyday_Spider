from ipPOOL.get_Fangfa import get_source
import json


# 控制台
def main():
    url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp?'
    name = input('请输入要下载的歌手名字：')
    index_response = load_page(url, name, headers)
    for music,med_cid,title in detail_page(index_response):
        detail_music_page(music,med_cid,title)


# 搜索页参数
def load_page(url,name,headers):
    params = {
        'cr':'1',
        'p':'2',
        'n':'40',
        'w':name
    }
    req = get_source(url,headers,params).text
    return req


def detail_page(index_response):
    # res = re.compile(r'callback\((.*?)\)',re.I|re.S)
    # lis = re.findall(res,index_response)[0]
    # print(lis+')'+'"'+'}')
    #callback({})去掉
    lis = index_response.strip('callback()')
    content = json.loads(lis)
    for i in content['data']['song']['list']:
        # 歌曲名字
        print(i['songname'])
        url = 'https://c.y.qq.com/base/fcgi-bin/fcg_music_express_mobile3.fcg?'
        params = {
            'g_tk': '551824926',
            'jsonpCallback': 'MusicJsonCallback3405639285923652',
            'loginUin': '925363894',
            'format': 'json',
            'inCharset': 'utf8',
            'outCharset': 'utf-8',
            'platform': 'yqq',
            'cid': '205361747',
            'callback': 'MusicJsonCallback3405639285923652',
            'uin': '925363894',
            'songmid': i['songmid'],
            'filename': 'C400'+i['media_mid']+'.m4a',
            'guid': '4395081716',
        }
        detail = get_source(url,headers,params).text
        yield detail,i['media_mid'],i['songname']


# 歌曲详情页
def detail_music_page(music,med_cid,title):
    lis = music.strip('MusicJsonCallback3405639285923652()')
    content = json.loads(lis)
    for item in content['data']['items']:
        url = 'http://dl.stream.qqmusic.qq.com/C400'+med_cid+'.m4a?vkey='+item['vkey']+'&guid=4395081716&uin=925363894&fromtag=66'
        music_url = get_source(url,headers).content
        with open('D:\\'+title+'.mp4','wb') as fp:
            fp.write(music_url)



if __name__ == '__main__':
    # url = 'https://y.qq.com/portal/search.html'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
        'referer': 'https://y.qq.com/portal/search.html',
        'cookie': 'pgv_pvi=5815862272; RK=2Vo1+iXFYM; pgv_pvid=4395081716; ptui_loginuin=925363894; pt2gguin=o0925363894; ptcz=cddc410efc498828218b2de6b170185628b5cbc94892872de8779e59028197f2; tvfe_boss_uuid=77de753ee3b00ea6; o_cookie=925363894; pac_uid=1_925363894; LW_uid=M1u5S2F8s0Q2Y8S9h121A6O1C3; eas_sid=21D5f2g89032N8a9o1B1W6U530; mobileUV=1_163cd76e2e8_b0a8d; ts_uid=2682514080; LW_sid=u155B2q8S2Q6x6l773t007n7v2; pgv_si=s1969783808; _qpsvr_localtk=0.5501784286471261; ptisp=cnc; pgv_info=ssid=s2777661898; uin=o0925363894; skey=@E8ZDLOm7S; luin=o0925363894; lskey=0001000030b5f5c6345ca5be2d648ce56f3e020d7f0a2c2288ca4bf2b039d58e713cf614fb52526f9a3cdc64; uid=10772929; yqq_stat=0; qqmusic_fromtag=66; yq_index=0; yq_playschange=0; yq_playdata=; player_exist=1; ts_last=y.qq.com/portal/player.html; yplayer_open=0'
    }
    main()