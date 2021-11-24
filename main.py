
import time

from ffmpy3 import FFmpeg


def ffmpeg_path(inputs_path, outputs_path):
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
import yaml
import os

if os.path.exists('./url.yaml'):
    print("url.yaml存在")


# if __name__ == '__main__':
a={'logdir':'E:\大鹏教育\转录记录.txt','url':[
'https://hls.videocc.net/ef4825bc7e/6/ef4825bc7e9c3debacc3e64b6cc34da6.m3u8',
'https://hls.videocc.net/ef4825bc7e/6/ef4825bc7ed727a9402c7e9885c378a6.m3u8',
'https://hls.videocc.net/ef4825bc7e/4/ef4825bc7e6b983761f0c45469623904.m3u8',
'https://hls.videocc.net/ef4825bc7e/8/ef4825bc7ee0889a0a0a15ab57eaaa98.m3u8',
'https://hls.videocc.net/ef4825bc7e/6/ef4825bc7e5c49c2ddcfa03f3b5099a6.m3u8',
'https://hls.videocc.net/ef4825bc7e/4/ef4825bc7ec48ce2fd4d9bbb0bb48c04.m3u8',
'https://hls.videocc.net/ef4825bc7e/1/ef4825bc7e6ea5c3f910eab675a3d831.m3u8',
'https://hls.videocc.net/ef4825bc7e/7/ef4825bc7e7405f815efddf8651a17d7.m3u8',
'https://hls.videocc.net/ef4825bc7e/2/ef4825bc7e98264b10acab1e555a7862.m3u8',
'https://hls.videocc.net/ef4825bc7e/7/ef4825bc7ee947d9c780430aff922c67.m3u8',
'https://hls.videocc.net/ef4825bc7e/3/ef4825bc7e29cf327b92b2735c6b4923.m3u8',
'https://hls.videocc.net/ef4825bc7e/f/ef4825bc7e56c3b305973a51daf5db4f.m3u8',
'https://hls.videocc.net/ef4825bc7e/a/ef4825bc7e606efebe6b2913cef1fc1a.m3u8',
'https://hls.videocc.net/ef4825bc7e/e/ef4825bc7ea3d3475300b32774a1d90e.m3u8',
'https://hls.videocc.net/ef4825bc7e/f/ef4825bc7e598a0e3faf7011ea429bcf.m3u8',
'https://hls.videocc.net/ef4825bc7e/c/ef4825bc7eb8eca5fd08b1563dffc97c.m3u8',
'https://hls.videocc.net/ef4825bc7e/b/ef4825bc7e6e020600c829b6609ded5b.m3u8',
'https://hls.videocc.net/ef4825bc7e/6/ef4825bc7eb94f1b302e3886debd45f6.m3u8',
'https://hls.videocc.net/ef4825bc7e/0/ef4825bc7e74eab232a50fc7f72f3900.m3u8' ,

'https://hls.videocc.net/ef4825bc7e/c/ef4825bc7e36348a7ec7352065d0d49c.m3u8',
'https://hls.videocc.net/ef4825bc7e/e/ef4825bc7e7e9af50ca4b5c0d94d597e.m3u8',
'https://hls.videocc.net/ef4825bc7e/b/ef4825bc7e23e0a245cd74045499132b.m3u8',
'https://hls.videocc.net/ef4825bc7e/0/ef4825bc7eed80993daa8860792ef070.m3u8',
'https://hls.videocc.net/ef4825bc7e/a/ef4825bc7e3dba35cb6a9cf276e394ba.m3u8',
'https://hls.videocc.net/ef4825bc7e/b/ef4825bc7ecf266ebb7b0ffec6255b8b.m3u8',
'https://hls.videocc.net/ef4825bc7e/8/ef4825bc7e4c09a681c269ec4fabc008.m3u8',
'https://hls.videocc.net/ef4825bc7e/1/ef4825bc7e4c8cc9a91bf77a37e114d1.m3u8',
'https://hls.videocc.net/ef4825bc7e/c/ef4825bc7e749441c63577de7ed032dc.m3u8',
'https://hls.videocc.net/ef4825bc7e/1/ef4825bc7e2652f8460897bc41b72701.m3u8',
'https://hls.videocc.net/ef4825bc7e/9/ef4825bc7ece41fce5db38b38b770ea9.m3u8',
'https://hls.videocc.net/ef4825bc7e/1/ef4825bc7e17f49c3f674a886e544d71.m3u8',
'https://hls.videocc.net/ef4825bc7e/3/ef4825bc7e2fb2ed6c7aba009febdb83.m3u8',
'https://hls.videocc.net/ef4825bc7e/4/ef4825bc7e0b89bcdce9ea790feaa9c4.m3u8',
'https://hls.videocc.net/ef4825bc7e/c/ef4825bc7e171410a6ff2a4485e08aec.m3u8',
'https://hls.videocc.net/ef4825bc7e/1/ef4825bc7e7e45f8f9f88b80db34d611.m3u8',
'https://hls.videocc.net/ef4825bc7e/1/ef4825bc7e13ba54633af3c9b312c431.m3u8',
'https://hls.videocc.net/ef4825bc7e/6/ef4825bc7eb26269dd3de1ff09476626.m3u8',
'https://hls.videocc.net/ef4825bc7e/5/ef4825bc7e7d08b97ba878bcc14f2e75.m3u8',
'https://hls.videocc.net/ef4825bc7e/f/ef4825bc7ee8ac9e77cc14167dcb4c5f.m3u8',
'https://hls.videocc.net/ef4825bc7e/e/ef4825bc7efe785a6f424ee8a3bcfa0e.m3u8',
'https://hls.videocc.net/ef4825bc7e/f/ef4825bc7e0b412bd0716ae5cf3695af.m3u8',
'https://hls.videocc.net/ef4825bc7e/5/ef4825bc7e5fe045f504f7c0bc0705e5.m3u8',
'https://hls.videocc.net/ef4825bc7e/b/ef4825bc7e04f644f4fd4fbe1b706f8b.m3u8',
'https://hls.videocc.net/ef4825bc7e/6/ef4825bc7e0aa8a42f8ca106835e6556.m3u8',
'https://hls.videocc.net/ef4825bc7e/8/ef4825bc7e0182ffffc43b3e4f86a288.m3u8',
'https://hls.videocc.net/ef4825bc7e/7/ef4825bc7e9af2795194ee5b91ec3437.m3u8',
'https://hls.videocc.net/ef4825bc7e/0/ef4825bc7eae9bdc8c78b6c08c0e17d0.m3u8',
'https://hls.videocc.net/ef4825bc7e/e/ef4825bc7e8a6afb5f6659e28f01b76e.m3u8',
'https://hls.videocc.net/ef4825bc7e/0/ef4825bc7eb268f3f4c0ac6e03810000.m3u8',
'https://hls.videocc.net/ef4825bc7e/5/ef4825bc7e2a128911d390772309ed65.m3u8',
'https://hls.videocc.net/ef4825bc7e/8/ef4825bc7eb0a77af4377dda693e6048.m3u8',
'https://hls.videocc.net/ef4825bc7e/0/ef4825bc7efa2a421fa556263c761ec0.m3u8',
'https://hls.videocc.net/ef4825bc7e/1/ef4825bc7e743fbc34a9373e826a7dd1.m3u8',
'https://hls.videocc.net/ef4825bc7e/7/ef4825bc7e337d8ef22f06536fcd6d77.m3u8',
'https://hls.videocc.net/ef4825bc7e/1/ef4825bc7edd4ae918b91b441e0447f1.m3u8',
'https://hls.videocc.net/ef4825bc7e/3/ef4825bc7ec22e953ed2de5af7d1cfb3.m3u8',
'https://hls.videocc.net/ef4825bc7e/8/ef4825bc7e18fcbc5ca13088f5af6818.m3u8',
'https://hls.videocc.net/ef4825bc7e/6/ef4825bc7ec30b8c3214031f33e10e16.m3u8',
'https://hls.videocc.net/ef4825bc7e/1/ef4825bc7e2d6eff5dd626f9ec9f2a71.m3u8',
'https://hls.videocc.net/ef4825bc7e/0/ef4825bc7e75f0936445e2e0e8e7b670.m3u8',
'https://hls.videocc.net/ef4825bc7e/1/ef4825bc7ea4702f3980759e7e420591.m3u8',
'https://hls.videocc.net/ef4825bc7e/9/ef4825bc7e04849fcdc65d0413037829.m3u8',
'https://hls.videocc.net/ef4825bc7e/0/ef4825bc7e968eb69a2bafa64173ed60.m3u8',
'https://hls.videocc.net/ef4825bc7e/d/ef4825bc7e20a9339a84798e9f9b85fd.m3u8',
'https://hls.videocc.net/ef4825bc7e/8/ef4825bc7e03212dac992925b2b0bf08.m3u8'
],'outdir':['E:\大鹏教育\est\\','E:\大鹏教育\est2\\','E:\大鹏教育\est3\\'],'perNumber':[1,3],'proName':'test_'}

with open('./url.yaml','r')as f:
    data=yaml.safe_load(f)



with open(data['logdir'],'a+') as fo:
  i = 0
  dirnumber = 0
  suffix=0
  sign=0
  if  not(len(data['logdir'])):
      print(" 日志文件目录不可以为空，请填logdir的路径")
      exit(3)

  if  not(len(data['outdir'])):
      print(" 输出文件目录不可以为空，请填outdir的路径")
      exit(2)
  if  not(len(data['url'])):
      print(" url目录不可以为空，请填url的路径")
      exit(4)
  if not(os.path.exists(data['outdir'][0])):
      os.makedirs(data['outdir'][0])
      print("成功创建目录",data['outdir'][0])
  if(len(data['perNumber'])):
      sign=1
      if(len(data['perNumber'])!=(len(data['outdir'])-1)):
          print("分割格式错误，检查perNumber的数量")
          exit(1)



  while (i<len(data['url'])):


    startTime=time.time()



    if len(data['perNumber'])and(i<data['perNumber'][dirnumber]): #通过len（perNumber）判断是否要分割文件夹
       suffix=suffix+1
       ffmpeg_path(data['url'][i], data['outdir'][dirnumber]+str(data['proName'])+str(suffix)+ '.mp4')
    elif(dirnumber!=len(data['perNumber'])-1):#文件装满后且不是最后一个文件架，切换下一个文件夹
        suffix = 0
        dirnumber=dirnumber+1
        if not (os.path.exists(data['outdir'][dirnumber])):
            os.makedirs(data['outdir'][dirnumber])
            print("成功创建目录", data['outdir'][dirnumber])
        continue
    else:#如果是最后一个文件则dirnumber+1
        #如果是非分割的文件则先进行dirnumber-1，再dirnumber+1
        #并且只运行一次设定初始值之后，就令sign为3，不再运行
        if (sign == 1):
            if not (os.path.exists(data['outdir'][dirnumber])):
                os.makedirs(data['outdir'][dirnumber])
                print("成功创建目录", data['outdir'][dirnumber])
            suffix=0
            sign=3
        elif(sign==0):
            dirnumber=dirnumber-1
            sign=3
        suffix=suffix+1
        ffmpeg_path(data['url'][i], data['outdir'][dirnumber+1]+str(data['proName'])+str(suffix) + '.mp4')

    endtime=time.time()
    print(str(i +1) + '完成录制:耗时' + str(endtime-startTime) + '   北京时间：' + str(time.asctime(time.localtime(time.time()))) + "\n")
    fo.write(str(i +1) + '完成录制:耗时' + str(endtime-startTime)+ '   北京时间：' + str(time.asctime(time.localtime(time.time()))) + "\n")
    i=i+1
    fo.flush()






