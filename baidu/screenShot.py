import sys
from time import sleep
from PIL import Image,ImageGrab
import keyboard
from baidu.Baidu import BaiDuAPI


def screenShot():
    # 监控键盘事件，并保存图片
    if keyboard.wait(hotkey='ctrl+alt+a') == None:
        if keyboard.wait(hotkey='esc') == None:
            # 获取剪切板内容
            sleep(0.01)
            im = ImageGrab.grabclipboard()
            im.save('img.png')

if __name__ == '__main__':
    baiduapi = BaiDuAPI('file.ini')
    for _ in range(sys.maxsize):
        screenShot()
        text = baiduapi.picture2Text('img.png')
        print(text)