# WebVideoDownload_暂时只支持m3u8
##首先推荐下载一款网页插件
https://microsoftedge.microsoft.com/addons/detail/%E8%A7%86%E9%A2%91%E4%B8%8B%E8%BD%BD%E7%A5%9E%E5%99%A8/mpheaeopmnhokmilcdjopinhnadabilf
####在edge上的一款网页插件
![img.png](./images/img.png)
注意：拿edge浏览器打开下载，安装之后就在其右上角
理由：
这款插件可以自动解析当前网页上的视频链接
如果不想安装就F12，去网络中找视频对应的链接，比较麻烦，故推荐
##其次填写配置文件
###url.yaml
![img.png](images/img1.png)
#####如上图
下面介绍如何填写
#####logdir 为日志目录：输出格式为 E://XXXX/xxxx.txt记录下载log
#####outdir 为下载文件目录：可以设置为多个目录，每个文件下可以设置存放数量
#####pernumber 为分割参数： 若outdir存在多个，此参数为控制每个目录里存放文件的序号，比如[2,5]表示第一个文件夹下放序号1到2，第二个文件夹下放3到5，其余都放到最后一个中
#####preName 为视频前缀 
#####url 为用之前视频解析工具解析出来的链接
填写完之后：
直接运行main.py  即可
注意：要存放的目录下必须是空的 
#m4s
![img.png](images/img3.png)
现在网址似乎都会分析其请求地址，所以好像你不从它们的网站请求链接，就会被墙，返回403
解决办法是使用urllib.request模拟网站发出请求
现在对b站进行测试

