# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 21:38:03 2019

@author: Think
"""
'''【Day 1】
1.环境搭建
anaconda环境配置
解释器
---------------------------
python初体验
print and input
---------------------------
python基础讲解
python变量特性+命名规则
注释方法
python中“：”作用
学会使用dir( )及和help( )
import使用
pep8介绍
---------------------------
python数值基本知识
python中数值类型，int，float，bool，e记法等
算数运算符
逻辑运算符
成员运算符
身份运算符
运算符优先级
---------------------------
string字符串
定义及基本操作（+，*，读取方式）
字符串相关方法
字符串格式化问题
------------------------------------------------------------------------------------【作业】
学习代码分享，200-300行要求。
作业：要求用户依次输入姓名，性别，年龄，并对用户信息进行输出格式如下：您的姓名是：***，您的性别是：***，您是***年出生的。
------------------------------------------------------------------------------------
【作业提交】
1.代码文件链接分享到群
截至日期：2019年1月26日晚22：00
注意：未完成将被清退
------------------------------------------------------------------------------------
【点评方式】
学员按照次序顺延进行点评，例如，2号对1号进行点评，3号对2号点评，依次类推。1号对29号进行点评。
截止时间：2019年1月27日中午八点
注意：未完成将被清退'''

print('Hello World!')
#print input
name=input()
name=input('please input a string')
#Python所有的输入都是以字符串形式接收

a=input().split(' ') 
n=int(a[0])
m=int(a[1])

n,m=input().split()
#输入两个数字或字符串，以空格隔开
    
print("Hello,",name)
print(name,"Mary",sep=',',end='.')
print ("His name is %s"%("Aviad"))#字符串
print ("He is %d years old"%(25))#整数
print ("His height is %f m"%(1.83))#浮点
print ("His height is %.2f m"%(1.83))#指定两位浮点
print ("Name:%10s Age:%8d Height:%8.2f"%("Aviad",25,1.83))
print ("Name:%-10s Age:%-8d Height:%-8.2f"%("Aviad",25,1.83))#-表示左对齐

#python 区分大小写
s='apple'
s+'s'
x,y,z=1,'two',3.0
(x,y,z)

#python单行注释符号(#)
#批量、多行注释符号(""" """)三个单引号或三个双引号
'''python多行注释符  三对引号
python多行注释符  三对引号
python多行注释符  三对引号'''

#python中“：”作用
name='python'
if name=='python':
    print("My name is %s"%("python"))
    
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

L = list(range(100)) #0-99
L
L[:10] #0-9
L[-10:]#90-99
L[:-10]#0-89

dir(L)

help(":")#查看python中： 的作用
help("keywords")#查看python中所有关键字

#在开始使用一个模块中的函数之前，必须用import语句导入该模块
# 导入一个模块
import sklearn
import matplotlib.pyplot as plt  #as 后接的是新名字
# 导入多个模块
import numpy,pandas
# 导入模块中的指定的属性、方法（不加括号）、类
from sklearn.ensemble import RandomForestRegressor as rfr

#没有任何输入参数，那么创建 float 实例值为 0.0
m=float()
m#0.0
#用float构造无穷大、无穷小量
n=float('inf')
n

#精度低可以转换为精度高的
#布尔型（bool）可以转换为整型（int），整型（int）可以转换为浮点型（float）
a=bool(1)
a#True
type(a)#bool
b=int(a)
b#1
type(b)#int

#精度高转换为精度低会损失精度
c=float(33.45)
c#33.45
type(c)#float
d=int(c)
d#33
type(d)#int

print ("%e"%12)#12 科学计数法表示
s=1.2e-4
s#0.00012

a=True+False
a#1
b=99.2-True
b#98.2
c=3*False
c#0

a = 21
b = 10
c = 0
print(a+b)
print(a-b)
print(a/b)
print(a//b)
print(a%b)
print(2**3)

print(1 or 2)   # 1
print(3 or 2)   # 3
print(0 or 2)   # 2
print(0 or 100) # 100
print(0 or 0)#0

print(1 and 2)  # 2
print(3 and 0)  # 0
print(0 and 2)  # 0
print(3 and 2)  # 2
print(0 and 0)  # 0

print(1 > 2 and 3 or 4 and 3 < 2 or not 4 > 5) #True

a = [1, 2, 3]
b = [1, 2, 3]
print( a == b )#True
print( a is b )#False

b = 15
print(a is not b)

str = "Python stRING"
str.upper()#转大写
str.lower()#转小写
str.capitalize()#字符串首为大写，其余小写   
str.swapcase()         #大小写对换 
str.title()     #以分隔符为标记，首字符为大写，其余为小写

str.find('z')              #查找字符串，没有则返回-1，有则返回查到到第一个匹配的索引
str.find('s')

str[0]#p

#可以使用引号('，"，''')来创建字符串
c= "Hello World!"
print(c)
c = c[:6] + 'Python'
print(c)

#通过使用%来实现操作符的格式化。
'My computer name is: %s' % 'Jef'

a='Hello'
b='Python'
a+b
a*3#*重复输出字符串
a[1:3]#截取字符串中的一部分，遵循左闭右开原则，a[1:3] 是不包含第 3 个字符的。  el

name=input("请输入您的名字： ")
sex=input("请输入您的性别： ")
age=int(input("请输入您的年龄: "))
birth=2019-age
print("您的姓名是:%s,您的性别是:%s,您是%d年出生的。"%(name,sex,birth))


'''
【Day 2】
基础
列表
标志
基本操作(创建，append( )，pop( ) ,del( ), 深浅拷贝）
列表相关方法
元组
标志
基本操作（创建及不可变性）
提升
序列类型，相互转换及方法
【作业构想】
学习代码200-300行
定义一个列表，包含自己的家庭成员，并在指定位置插入给定元素，例如你的男女朋友名称等。再将男女朋友名字移除等操作。
----------------------------------------------------------------
【作业提交】
1.代码文件链接分享到群
截至日期：2019年1月27日晚22：00
注意：未完成将被清退
------------------------------------------------------------------ 
【点评】
第一天点评截止时间1月27晚12点
注意：未完成将被清退'''


