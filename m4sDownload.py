import urllib.request
from ffmpy3 import FFmpeg
#
# myURL1 = urllib.request.urlopen("https://cn-bj-se-bcache-08.bilivideo.com/upgcxcode/40/25/435852540/435852540_ex1-1-30066.m4s"
#
#                             )
# print(myURL1.getcode())   # 200
import yaml
with open('./url.yaml','r')as f:
  data=yaml.safe_load(f)


# header={
# 'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36 Edg/96.0.1054.29',
# 'referer': 'https://www.bilibili.com/video/BV1fq4y1g7hq?spm_id_from=333.851.b_7265636f6d6d656e64.2'
# }
##两种方式实现下载m4s现在选择选择第二种
# request = urllib.request.Request(url,headers=header)
# reponse = urllib.request.urlopen(request)
# with open('./0381.m4s','wb+')as of:
#  of.write(reponse.read())
#
opener = urllib.request.build_opener()#实例化一个OpenerDirector
opener.addheaders = [('user-agent',data['user-agent']),
                     ('referer',data['referer'])]#添加header,注意格式
urllib.request.install_opener(opener)#将OpenerDirector装进opener
import os
import glob
urllib.request.urlretrieve(data['url'][0],data['outdir'][0]+str(len(glob.glob(data['outdir'][0]+'*.m4s'))+1)+'.m4s')
urllib.request.urlretrieve(data['url'][1],data['outdir'][0]+str(len(glob.glob(data['outdir'][0]+'*.m4s'))+1)+'.m4s')
a = FFmpeg(
    inputs={data['outdir'][0]+str(len(glob.glob(data['outdir'][0]+'*.m4s')))+'.m4s': None,data['outdir'][0]+str(len(glob.glob(data['outdir'][0]+'*.m4s'))-1)+'.m4s':None},
    outputs={data['outdir'][0]+str(len(glob.glob(data['outdir'][0]+'*.mp4'))+1)+'.mp4': '-codec copy'}
)
print(a.cmd)
a.run()
