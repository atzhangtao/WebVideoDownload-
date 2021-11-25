'''对代码进行规范化修改：
优化整体代码结构
主要对下载文件的后缀名进行优化可以支持文件夹内不为空'''
import time
from ffmpy3 import FFmpeg
import yaml
import os

class m3u8Down:
 def ffmpeg_path(self,inputs_path, outputs_path):
    '''
    :param inputs_path: 输入的文件传入字典格式{文件：操作}
    :param outputs_path: 输出的文件传入字典格式{文件：操作}
    :return:
    '''
    a = FFmpeg(
                inputs={inputs_path: None},
                outputs={outputs_path: '-c copy',
                         }
    )
    print(a.cmd)
    a.run()
 def __init__(self):
  if os.path.exists('./url.yaml'):
    print("url.yaml存在")
  else:
      print("请加入./url.yaml后再次运行")
      exit(5)
  with open('./url.yaml','r')as f:
    self.data=yaml.safe_load(f)
    self.i = 0
    self.dirnumber = 0
    self.suffix = 0
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
    if (len(self.data['perNumber'])):
        sign = 1
        if (len(self.data['perNumber']) != (len(self.data['outdir']) - 1)):
            print("分割格式错误，检查perNumber的数量")
            exit(1)


 def downLoad(self):
  with open(self.data['logdir'],'a+') as fo:
   while (self.i < len(self.data['url'])):
    startTime = time.time()
    if len(self.data['perNumber']) and (self.i <self. data['perNumber'][self.dirnumber]):  # 通过len（perNumber）判断是否要分割文件夹
      self.suffix = len(os.listdir(self.data['outdir'][self.dirnumber]))+1
      self.ffmpeg_path(self.data['url'][self.i], self.data['outdir'][self.dirnumber] + str(self.data['proName']) + str(self.suffix) + '.mp4')
    elif (self.dirnumber != len(self.data['perNumber']) - 1):  # 文件装满后且不是最后一个文件架，切换下一个文件夹
      self.dirnumber =self. dirnumber + 1
      if not(os.path.exists(self.data['outdir'][self.dirnumber])):
        os.makedirs(self.data['outdir'][self.dirnumber])
        print("成功创建目录", self.data['outdir'][self.dirnumber])
      continue
    else:  # 如果是最后一个文件则dirnumber+1
      # 如果是非分割的文件则先进行dirnumber-1，再dirnumber+1
      # 并且只运行一次设定初始值之后，就令sign为3，不再运行
      if (self.sign == 1):
          if not (os.path.exists(self.data['outdir'][self.dirnumber])):
              os.makedirs(self.data['outdir'][self.dirnumber])
              print("成功创建目录", self.data['outdir'][self.dirnumber])

          self.sign = 3
      elif (self.sign == 0):
          self.dirnumber = self.dirnumber - 1
          self.sign = 3
      self.suffix = len(os.listdir(self.data['outdir'][self.dirnumber])) + 1
      self.ffmpeg_path(self.data['url'][self.i], self.data['outdir'][self.dirnumber + 1] + str(self.data['proName']) + str(self.suffix) + '.mp4')

    endtime = time.time()
    print(str(self.i + 1) + '完成录制:耗时' + str(endtime - startTime) + '   北京时间：' + str(
      time.asctime(time.localtime(time.time()))) + "\n")
    fo.write(str(self.i + 1) + '完成录制:耗时' + str(endtime - startTime) + '   北京时间：' + str(
      time.asctime(time.localtime(time.time()))) + "\n")
    self.i = self.i + 1
    fo.flush()
m3u8=m3u8Down()
m3u8.downLoad()














