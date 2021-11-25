import urllib.request
#
# myURL1 = urllib.request.urlopen("https://cn-bj-se-bcache-08.bilivideo.com/upgcxcode/40/25/435852540/435852540_ex1-1-30066.m4s"
#
#                             )
# print(myURL1.getcode())   # 200
url = 'https://upos-sz-mirrorcoso1.bilivideo.com/upgcxcode/31/06/443780631/443780631-1-30280.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1637834109&gen=playurlv2&os=coso1bv&oi=3525208806&trid=fd83e424db4d426492c691ef8e6aa800u&platform=pc&upsig=e1ca1024aa82843685eddc3bc230c3ce&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,platform&mid=305322579&bvc=vod&nettype=0&orderid=0,3&agrr=1&bw=16279&logo=80000000'
# header={
# 'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36 Edg/96.0.1054.29',
# 'referer': 'https://www.bilibili.com/video/BV1fq4y1g7hq?spm_id_from=333.851.b_7265636f6d6d656e64.2'
# }
##两种方式实现下载m4s现在选择选择第二种
# request = urllib.request.Request(url,headers=header)
# reponse = urllib.request.urlopen(request)
# with open('./0381.m4s','wb+')as of:
#  of.write(reponse.read())

opener = urllib.request.build_opener()#实例化一个OpenerDirector
opener.addheaders = [('user-agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36 Edg/96.0.1054.29'),
                     ('referer','https://www.bilibili.com/video/BV1fq4y1g7hq?spm_id_from=333.851.b_7265636f6d6d656e64.2')]#添加header,注意格式
urllib.request.install_opener(opener)#将OpenerDirector装进opener
urllib.request.urlretrieve(url,'./ss.m4s')