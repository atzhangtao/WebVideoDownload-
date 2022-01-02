import urllib.request

import urllib.request
from ffmpy3 import FFmpeg
import os
import glob
import yaml
import time
import math
#废弃
def v1():
    #访问外网需要代理
 header={
      'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.34',
  'referer': 'https://www.youtube.com/'
   }

 request = urllib.request.Request(url,headers=header)

 reponse = urllib.request.urlopen(request)
 print(reponse.getcode())
 with open('./0381.mp4','wb+')as of:
   of.write(reponse.read())
class mp4Down():
    def __init__(self):

        with open('./url.yaml', 'r') as f:
            self.data = yaml.safe_load(f)
            self.i = 0
            self.dirnumber = 0

            self.sign = 0
            if not (len(self.data['logdir'])):
                print(" 日志文件目录不可以为空，请填logdir的路径")
                exit(3)

            if not (len(self.data['outdir'])):
                print(" 输出文件目录不可以为空，请填outdir的路径")
                exit(2)
            if not (len(self.data['url'])):
                print(" url目录不可以为空，请填url的路径")
                exit(4)
            if not (os.path.exists(self.data['outdir'][0])):
                os.makedirs(self.data['outdir'][0])
                print("成功创建目录", self.data['outdir'][0])
            if (len(self.data['outdir']) - 1):
                self.sign = 1
                if (len(self.data['perNumber']) != (len(self.data['outdir']) - 1)):
                    print("分割格式错误，检查perNumber的数量")
                    exit(1)
        self.opener = urllib.request.build_opener()  # 实例化一个OpenerDirector
        self.opener.addheaders = [('user-agent', self.data['user-agent']),
                                  ('referer', self.data['referer'])]  # 添加header,注意格式
        self.opener.add_handler(urllib.request.ProxyHandler({"https":"127.0.0.1:8080"}))#加入代理127.0.0.1:8080
    def reporthook(self,a, b, c):
        """
        显示下载进度
        :param a: 已经下载的数据块
        :param b: 数据块的大小
        :param c: 远程文件大小
        :return: None
        """
        print("\rdownloading: %5.1f%%" % (a * b * 100.0 / c), end="")

    def FFmpeg_path(self, dirnumber):
        urllib.request.install_opener(self.opener)
        print("第" + str(self.i + 1) + "个m4s：")
        urllib.request.urlretrieve(self.data['url'][self.i], self.data['outdir'][dirnumber] + str(
            len(glob.glob(self.data['outdir'][dirnumber] + '*')) + 1) , self.reporthook)
        print("第" + str(self.i + 2) + "个m4s：")
        urllib.request.urlretrieve(self.data['url'][self.i + 1], self.data['outdir'][dirnumber] + str(
            len(glob.glob(self.data['outdir'][dirnumber] + '*')) + 1), self.reporthook)
        a = FFmpeg(
            inputs={self.data['outdir'][dirnumber] + str(
                len(glob.glob(self.data['outdir'][dirnumber] + '*'))): None,
                    self.data['outdir'][dirnumber] + str(
                        len(glob.glob(self.data['outdir'][dirnumber] + '*')) - 1): None},
            outputs={self.data['outdir'][dirnumber] + str(
                len(glob.glob(self.data['outdir'][dirnumber] + '*')) + 1) + '.mp4': '-codec copy'}
        )
        print(a.cmd)
        a.run()

    def downLoad(self):
        with open(self.data['logdir'], 'a+') as fo:
            while (self.i < len(self.data['url'])):
                startTime = time.time()
                if self.sign and (
                        self.i < self.data['perNumber'][self.dirnumber] * 2):  # 通过len（perNumber）判断是否要分割文件夹
                    self.FFmpeg_path(self.dirnumber)
                elif self.sign and (self.dirnumber != len(self.data['outdir']) - 2):  # 文件装满后且不是最后一个文件架，切换下一个文件夹
                    self.dirnumber = self.dirnumber + 1
                    if not (os.path.exists(self.data['outdir'][self.dirnumber])):
                        os.makedirs(self.data['outdir'][self.dirnumber])
                        print("成功创建目录", self.data['outdir'][self.dirnumber])
                    continue
                else:
                    if (self.sign == 1):
                        self.dirnumber = self.dirnumber + 1
                        if not (os.path.exists(self.data['outdir'][self.dirnumber])):
                            os.makedirs(self.data['outdir'][self.dirnumber])
                            print("成功创建目录", self.data['outdir'][self.dirnumber])

                        self.sign = 0
                    self.FFmpeg_path(self.dirnumber)

                endtime = time.time()
                print(str(math.ceil(self.i // 2)) + '完成录制:耗时' + str(endtime - startTime) + '   北京时间：' + str(
                    time.asctime(time.localtime(time.time()))) + "\n")
                fo.write(str(math.ceil(self.i // 2)) + '完成录制:耗时' + str(endtime - startTime) + '   北京时间：' + str(
                    time.asctime(time.localtime(time.time()))) + "\n")
                self.i = self.i + 2
                fo.flush()
# opener = urllib.request.build_opener()  # 实例化一个OpenerDirector
# opener.addheaders = [('user-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.34'),
#                               ('referer', 'https://www.youtube.com/')]  # 添加header,注意格式
#opener.add_handler(urllib.request.ProxyHandler({"https":"127.0.0.1:8080"}))#加入代理127.0.0.1:8080
#urllib.request.install_opener(opener)
#urllib.request.urlretrieve(url,'./0318',reporthook)
#urllib.request.urlretrieve(url1,'./0319',reporthook)

# a = FFmpeg(
#        inputs={'./0318': None,'./0319':None},
#        outputs={'./3333'+'.mp4': '-codec copy'}
#       )
# print(a.cmd)
# a.run()
DownLoad=mp4Down()
DownLoad.downLoad()