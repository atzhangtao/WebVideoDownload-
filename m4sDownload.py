import urllib.request
from ffmpy3 import FFmpeg
import os
import glob
import yaml
import time
import math
class m4sDownload():

    def __init__(self):

      with open('./url.yaml','r')as f:
           self.data=yaml.safe_load(f)
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
           if (len(self.data['outdir'])-1):
               self.sign = 1
               if (len(self.data['perNumber']) != (len(self.data['outdir']) - 1)):
                   print("分割格式错误，检查perNumber的数量")
                   exit(1)
       ##两种方式实现下载m4s现在选择选择第二种
       # header={
       #       'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36 Edg/96.0.1054.29',
       # 'referer': 'https://www.bilibili.com/video/BV1fq4y1g7hq?spm_id_from=333.851.b_7265636f6d6d656e64.2'
       # }

       # request = urllib.request.Request(url,headers=header)
       # reponse = urllib.request.urlopen(request)
       # with open('./0381.m4s','wb+')as of:
       #  of.write(reponse.read())

      self.opener = urllib.request.build_opener()#实例化一个OpenerDirector
      self.opener.addheaders = [('user-agent',self.data['user-agent']),
                     ('referer',self.data['referer'])]#添加header,注意格式
     #将OpenerDirector装进opener
    def FFmpeg_path(self,dirnumber):
      urllib.request.install_opener(self.opener)
      urllib.request.urlretrieve(self.data['url'][self.i],self.data['outdir'][dirnumber]+str(len(glob.glob(self.data['outdir'][dirnumber]+'*.m4s'))+1)+'.m4s')
      urllib.request.urlretrieve(self.data['url'][self.i+1],self.data['outdir'][dirnumber]+str(len(glob.glob(self.data['outdir'][dirnumber]+'*.m4s'))+1)+'.m4s')
      a = FFmpeg(
       inputs={self.data['outdir'][dirnumber]+str(len(glob.glob(self.data['outdir'][dirnumber]+'*.m4s')))+'.m4s': None,self.data['outdir'][dirnumber]+str(len(glob.glob(self.data['outdir'][dirnumber]+'*.m4s'))-1)+'.m4s':None},
       outputs={self.data['outdir'][dirnumber]+str(len(glob.glob(self.data['outdir'][dirnumber]+'*.mp4'))+1)+'.mp4': '-codec copy'}
      )
      print(a.cmd)
      a.run()
    def downLoad(self):
        with open(self.data['logdir'], 'a+') as fo:
            while (self.i < len(self.data['url'])):
                startTime = time.time()
                if self.sign and (
                        self.i < self.data['perNumber'][self.dirnumber]*2):  # 通过len（perNumber）判断是否要分割文件夹
                    self.FFmpeg_path(self.dirnumber)
                elif self.sign and(self.dirnumber != len(self.data['outdir']) - 2):  # 文件装满后且不是最后一个文件架，切换下一个文件夹
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
                print(str(math.ceil(self.i//2)) + '完成录制:耗时' + str(endtime - startTime) + '   北京时间：' + str(
                    time.asctime(time.localtime(time.time()))) + "\n")
                fo.write(str(math.ceil(self.i//2)) + '完成录制:耗时' + str(endtime - startTime) + '   北京时间：' + str(
                    time.asctime(time.localtime(time.time()))) + "\n")
                self.i = self.i + 2
                fo.flush()
