from aip import AipOcr
import configparser


class BaiDuAPI:
    # 调用百度云API来实现文字识别

    def __init__(self, filePath):
        # 配置工单信息
        target = configparser.ConfigParser()
        target.read(filePath)
        app_id = target.get('工单密码', 'app_id')
        api_key = target.get('工单密码', 'api_key')
        Secret_Key = target.get('工单密码', 'Secret_Key')
        self.client = AipOcr(app_id, api_key, Secret_Key)

    def picture2Text(self,filePath):
        # 识别图片文字
        image = self.getFileContent(filePath)
        texts = self.client.basicGeneral(image)
        allTexts = ''
        for words in texts['words_result']:
            allTexts = allTexts + ''.join(words.get('words',''))
        # print(allTexts)
        return allTexts


    @classmethod
    def getFileContent(cls, filePath):
        # 读取图片
        with open(filePath, 'rb') as fp:
            return fp.read()

if __name__ == '__main__':
    baiduapi = BaiDuAPI('file.ini')
    baiduapi.picture2Text('img.png')