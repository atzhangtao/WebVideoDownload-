import urllib.request

from ffmpy3 import FFmpeg


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

def reporthook(a, b, c):
        """
        显示下载进度
        :param a: 已经下载的数据块
        :param b: 数据块的大小
        :param c: 远程文件大小
        :return: None
        """
        print("\rdownloading: %5.1f%%" % (a * b * 100.0 / c), end="")
url='https://r3---sn-un57en7s.googlevideo.com/videoplayback?expire=1638444418&ei=IlmoYfTyFpTa4QKInLCwCg&ip=114.46.80.124&id=o-AHPKHQY1JKlIE6ijRhXLixiqD1LfDROfVSqtJBzpXqf1&itag=244&aitags=133%2C134%2C135%2C160%2C242%2C243%2C244%2C278&source=youtube&requiressl=yes&pcm2=no&vprv=1&mime=video%2Fwebm&ns=tAKYYoW7y7a7WJpLXJOrVIcG&gir=yes&clen=174871362&dur=3760.541&lmt=1513839627803082&keepalive=yes&fexp=24001373,24007246&c=WEB&n=au56zQ5QXmf8xA&sparams=expire%2Cei%2Cip%2Cid%2Caitags%2Csource%2Crequiressl%2Cpcm2%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRQIgUH2zifFZLwOUmb_EdxW9cF5qYGwBanHjdZTdi5gib2oCIQDBUCCpKWUIjy8QO7yQ_Yrll9M7U_9G76kdq_HAsRMl2w%3D%3D&alr=yes&cpn=9exB6TqhYsRjfaLH&cver=2.20211129.09.00&redirect_counter=1&cm2rm=sn-ipoxu-umbr7s&cms_redirect=yes&ipbypass=yes&mh=yP&mm=29&mn=sn-un57en7s&ms=rdu&mt=1638421965&mv=u&mvi=3&pl=23&lsparams=ipbypass,mh,mm,mn,ms,mv,mvi,pl&lsig=AG3C_xAwRQIgHmBg_-GXbGhWwKBtNQjnd9izMT-WemAbjPnyWI9S__ACIQCqaOFE9J6cBG6-bb5auRM-pkiVKmyPGpuCWiHVEzMS9Q%3D%3D'
url1='https://r3---sn-ipoxu-umbr.googlevideo.com/videoplayback?expire=1638444418&ei=IlmoYfTyFpTa4QKInLCwCg&ip=114.46.80.124&id=o-AHPKHQY1JKlIE6ijRhXLixiqD1LfDROfVSqtJBzpXqf1&itag=251&source=youtube&requiressl=yes&mh=yP&mm=31%2C29&mn=sn-ipoxu-umbr%2Csn-un57sn7y&ms=au%2Crdu&mv=m&mvi=3&pl=23&pcm2=no&initcwndbps=626250&vprv=1&mime=audio%2Fwebm&ns=tAKYYoW7y7a7WJpLXJOrVIcG&gir=yes&clen=60555025&dur=3760.601&lmt=1513839135278398&mt=1638422457&fvip=3&keepalive=yes&fexp=24001373%2C24007246&c=WEB&n=au56zQ5QXmf8xA&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cpcm2%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRQIgRU5cLh5pc62k_pM4IgmAsoL8jQrCvJzeiUT0dt6VNxwCIQDim7HiEw5udBe9k8t4f6Gadd1SyUArp2DMg6fnqzwOdA%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRAIgNUa98ndB-TMxIV35qIWfdqMsPtOGooOfob_JSNVN2zgCIGwTvh_orsV2SRLa6XvllSFrzqac04o3L_GI20b2Mwi1&alr=yes&cpn=9exB6TqhYsRjfaLH&cver=2.20211129.09.00'
opener = urllib.request.build_opener()  # 实例化一个OpenerDirector
opener.addheaders = [('user-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.34'),
                              ('referer', 'https://www.youtube.com/')]  # 添加header,注意格式
opener.add_handler(urllib.request.ProxyHandler({"https":"127.0.0.1:8080"}))#加入代理127.0.0.1:8080
urllib.request.install_opener(opener)
urllib.request.urlretrieve(url,'./0318',reporthook)
urllib.request.urlretrieve(url1,'./0319',reporthook)

a = FFmpeg(
       inputs={'./0318': None,'./0319':None},
       outputs={'./3333'+'.mp4': '-codec copy'}
      )
print(a.cmd)
a.run()