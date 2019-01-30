# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 09:54:20 2019

@author: Think
"""

'''【Day 5】
正则表达式re
os模块
datetime模块
http请求
--------------------------------------
【作业构想】
请用户输入一个时间，输出选项所对应的现在时间，告诉用户这两个时间相隔的天数，小时数，分钟数和秒数。
请用户输入电话及邮箱，判断用户输入是否合法。
对http://www.baidu.com 进行请求，并用正则化匹配图片内容。将百度图标爬取下来保存至本地'''

#--------------------------正则表达式--------------------------------
'''
正则表达式是一种用来匹配字符串的强有力的武器。它的设计思想是用一种描述性的语言来给字符串定义一个规则，
凡是符合规则的字符串，我们就认为它“匹配”了，否则，该字符串就是不合法的。
#预备知识
在正则表达式中，如果直接给出字符，就是精确匹配。用\d可以匹配一个数字，\w可以匹配一个字母或数字
.匹配任意字符（不包括换行符）,\s可以匹配一个空格（也包括Tab等空白符），\s+表示至少有一个空格
要匹配变长的字符，在正则表达式中，用*表示任意个字符（包括0个），
用+表示至少一个字符，用?表示0个或1个字符，用{n}表示n个字符，用{n,m}表示n-m个字符：
特殊字符，在正则表达式中，要用'\'转义
要做更精确地匹配，用[]表示范围
A|B可以匹配A或B，^表示行的开头，^\d表示必须以数字开头。$表示行的结束，\d$表示必须以数字结束。
'''
#Python的字符串本身也用\转义
s = 'ABC\\-001' # Python的字符串
# 对应的正则表达式字符串变成：'ABC\-001’
s = r'ABC\-001' # Python的字符串  使用Python的r前缀，不用考虑转义的问题
# 对应的正则表达式字符串不变：'ABC\-001'

#match()方法判断是否匹配，如果匹配成功，返回一个Match对象，否则返回None
import re
re.match(r'^\d{3}\-\d{3,8}$', '010-12345') #<_sre.SRE_Match object; span=(0, 9), match='010-12345'>
re.match(r'^\d{3}\-\d{3,8}$', '010 12345')

#split  以匹配到的字符当做列表分隔符
'a b   c'.split(' ') #['a', 'b', '', '', 'c']  无法识别连续的空格
re.split(r'\s+', 'a b   c') #['a', 'b', 'c']
re.split(r'[\s\,]+', 'a,b, c  d')  #['a', 'b', 'c', 'd']
re.split(r'[\s\,\;]+', 'a,b;; c  d')    #['a', 'b', 'c', 'd']

#group()方法  正则表达式中定义了组，就可以在Match对象上用group()方法提取出子串来。
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
m
m.group(0) #group(0)永远是原始字符串，group(1)、group(2)……表示第1、2、……个子串
m.group(1)
m.group(2)

#compile()预编译正则表达式
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
# 使用：
re_telephone.match('010-12345').groups() #('010', '12345')
re_telephone.match('010-8086').groups()   #('010', '8086')

#search() 扫描整个字符串并返回第一个成功的匹配。
print(re.search('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.search('com', 'www.runoob.com').span())         # 不在起始位置匹配

#findall() 返回string中所有与pattern相匹配的全部字串，返回形式为数组
kk = re.compile(r'\d+')
kk.findall('one1two2three3four4')#[1,2,3,4] 
#注意此处findall()的用法，可传两个参数;
kk = re.compile(r'\d+')
re.findall(kk,"one123")#[1,2,3]
string="2345  3456  4567  5678"
regex=re.compile("\w+\s+\w+")
print(regex.findall(string))#['2345 3456', '4567 5678']  贪婪模式
regex1=re.compile("(\w+)\s+\w+")
print(regex1.findall(string))  #['2345', '4567']  只输出括号中的内容
regex2=re.compile("((\w+)\s+\w+)")
print(regex2.findall(string))#[('2345  3456', '2345'), ('4567  5678', '4567')]
#当正则表达式中有两个括号时，其输出是一个list 中包含2个 tuple,从输出的结果看，
#有两个元组，每一个元组中有两个字符串 : 其中第一个字符串"2345 3456"是最外面的括号输出的结果，
#第二个是里面括号(/w+)输出的结果 "2345", 第二个元组是第二次匹配的
#--------------------------os模块----------------------------------
import os
retval = os.getcwd()    # 查看当前工作目录
print("当前工作目录为 %s" % retval)
os.chdir("E:\\")    # 修改当前工作目录
retval = os.getcwd()    # 查看修改后的工作目录
print("目录修改成功 %s" % retval)
a = os.curdir   #返回当前目录  
print(a)   # .
a = os.pardir   #获取当前目录的父目录字符串名  
print(a)   #..
#os.makedirs("div1/div2/div3")   创建多层递归目录
#os.removedirs("div1/div2/div3")   若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推
#os.mkdir("dsr")   生成单级目录
#os.rmdir("dsr")   删除单级空目录，若目录不为空则无法删除，报错
#os.listdir("lib")   列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印
#remove("2.txt")   删除一个文件
#rename("1.txt", "2.txt")   重命名文件或目录
#os.stat("22")   获取文件或者目录信息
'''os.path.abspath(path)       返回path规范化的绝对路径
os.path.split(path)         将path分割成目录和文件名二元组返回
os.path.dirname(path)       返回path的目录。其实就是os.path.split(path)的第一个元素
os.path.basename(path)      返回path最后的文件名。如何path以／或\结尾，那么就会返回空值。即os.path.split(path)的第二个元素
os.path.exists(path)        如果path存在，返回True；如果path不存在，返回False
os.path.isabs(path)         如果path是绝对路径，返回True
os.path.isfile(path)        如果path是一个存在的文件，返回True。否则返回False
os.path.isdir(path)         如果path是一个存在的目录，则返回True。否则返回False
os.path.join(path1[, path2[, ...]])  将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
os.path.getatime(path)      返回path所指向的文件或者目录的最后存取时间
os.path.getmtime(path)      返回path所指向的文件或者目录的最后修改时间'''
#--------------------------datetime模块---------------------------
from datetime import date,datetime, timedelta, timezone
import time 
print   ('date.max:', date.max) # date对象所能表示的最大日期
print   ('date.min:', date.min) # date对象所能表示的最小日期
print   ('date.today():', date.today()) # 返回一个表示当前本地日期的date对象
print   ('date.fromtimestamp():', date.fromtimestamp(time.time())) #根据给定的时间戮，返回一个date对象

t=datetime(2019,1,30,13,30).timestamp()#timestamp是一个浮点数，小数位表示毫秒数
print(datxszetime.fromtimestamp(t))

str=input("请按照Y-m-d H:M:S的格式输入一个日期：")
cday=datetime.strptime(str,'%Y-%m-%d %H:%M:%S')#str转datetime
print(cday)

now=datetime.now()
print(now.strftime('%a,%b %d %H:%M:%S')) # datetime转str

now = date(2019, 1, 30)
tomorrow = now.replace(day = 31) #生成一个新的日期对象，用参数指定的年，月，日代替原有对象中的属性。（原有对象仍保持不变）
print ('now:', now, ', tomorrow:', tomorrow)
print ('timetuple():', now.timetuple()) # 返回日期对应的time.struct_time对象
print ('weekday():', now.weekday()) # 如果是星期一，返回0；如果是星期2，返回1，以此类推；
print ('isoweekday():', now.isoweekday()) # 返回weekday，如果是星期一，返回1；如果是星期2，返回2，以此类推；

print  ('datetime.max:', datetime.max)
print  ('datetime.min:', datetime.min)
print  ('datetime.resolution:', datetime.resolution)
print  ('today():', datetime.today()) #返回一个表示当前本地时间的datetime对象；
print  ('now():', datetime.now()) # 返回一个表示当前本地时间的datetime对象，如果提供了参数tz，则获取tz参数所指时区的本地时间；
print  ('utcnow():', datetime.utcnow()) #返回一个当前utc时间的datetime对象
print  ('fromtimestamp(tmstmp):', datetime.fromtimestamp(time.time())) #根据时间戮创建一个datetime对象，参数tz指定时区信息
print  ('utcfromtimestamp(tmstmp):', datetime.utcfromtimestamp(time.time())) # 根据时间戮创建一个datetime对象

dt=datetime.now()#datetime对象
dt.year、month、day、hour、minute、second、microsecond、tzinfo：
dt.date() # 获取date对象；
dt.time()#获取time对象；
dt. ctime () #返回一个日期时间的C格式字符串，等效于time.ctime(time.mktime(dt.timetuple()))；

#日期减一天
dt1 = dt + timedelta(days=-1)#昨天 #2019-01-29 19:50:34.343826
dt2 = dt - timedelta(days=1)#昨天 #2019-01-29 19:50:34.343826
dt3 = dt + timedelta(days=1)#明天 #2019-01-31 19:50:34.343826
delta_obj = dt3-dt #1 day, 0:00:00
print(dt1,dt2,dt3,delta_obj)
print (type(delta_obj),delta_obj)#<type 'datetime.timedelta'> 1 day, 0:00:00
print (delta_obj.days ,delta_obj.total_seconds())#1 86400.0

#--------------------------http请求-------------------------------
'''Python实现HTTP请求有三种方式——
urllib2/urllib
httplib/urllib
Requests  '''

import requests
# 以下为GET请求
url = 'https://www.csdn.net/'
r = requests.get(url)
print (r.content)  # 返回字节形式

if r.status_code == requests.codes.ok:
    print ('=== status_code === ', r.status_code)  # 响应码
    print ('=== headers === ', r.headers)  # 响应头
    print ('=== Content-Type === ', r.headers.get('Content-Type'))  # 获取响应头中的Content-Type字段
else:
    r.raise_for_status()  # 抛出异常

from urllib import request# urlib2在python3中在urlib.request中
url = "http://www.baidu.com/"
#urlopen()
sock = request.urlopen(url)
htmlCode = sock.read()
sock.close
fp = open("E:/ml_code/100days/1.html","wb") #将爬取的网页保存在本地
fp.write(htmlCode)
fp.close
#urlretrieve()
request.urlretrieve(url, 'E:/ml_code/100days/c')

'''urllib.urlretrieve(url[, filename[, reporthook[, data]]])
参数说明：
url：外部或者本地url
filename：指定了保存到本地的路径（如果未指定该参数，urllib会生成一个临时文件来保存数据）；
reporthook：是一个回调函数，当连接上服务器、以及相应的数据块传输完毕的时候会触发该回调。我们可以利用这个回调函数来显示当前的下载进度。
data：指post到服务器的数据。该方法返回一个包含两个元素的元组(filename, headers)，filename表示保存到本地的路径，header表示服务器的响应头。'''

#-------------------------作业------------------------------------
'''【作业构想】
请用户输入一个时间，输出选项所对应的现在时间，告诉用户这两个时间相隔的天数，小时数，分钟数和秒数。
请用户输入电话及邮箱，判断用户输入是否合法。
对http://www.baidu.com 进行请求，并用正则化匹配图片内容。将百度图标爬取下来保存至本地'''

from datetime import datetime , timedelta,
str=input("请按照Y-m-d H:M:S的格式输入一个日期：")
_date=datetime.strptime(str,'%Y-%m-%d %H:%M:%S')
now=datetime.now()
delta = now-_date  #days 表示相差天数  seconds 表示去掉天数之后的秒数   #total_seconds 表示总共相差秒数 没去天数
print("现在离输入的时间相差%d天，%d时，%d分，%d秒"%(delta.days,delta.seconds/3600,delta.seconds%3600/60,delta.total_seconds()%60))
print('相隔的天数为：{}'.format(delta))  #第二种方法

import re
tel = input("请输入电话：")
res1 = re.compile('^1[3,5,6,7,8]\d{9}$')
if res1.match(tel):
    print("输入的电话合法")
else:
    print("输入的电话不合法")
email = input("请输入邮箱：")
res2=re.compile(r'^[a-zA-Z0-9_][a-zA-Z0-\_\-\.]+@[a-zA-Z0-9]+\.[com,cn,net]{1,3}$')
if res2.match(email):
    print("输入的邮箱合法")
else:
    print("输入的邮箱不合法")

from urllib import request
with request.urlopen('http://www.baidu.com') as f:
    data=f.read()
    print("Status:",f.status,f.reason)
    buf=data.decode('utf-8')
    img=r'src="(.+?\.png)"'
    imglist=re.findall(img,buf)
    for addr in imglist:
        print(addr)
        request.urlretrieve("https:"+addr,r"E:/ml_code/100days/n.png")

