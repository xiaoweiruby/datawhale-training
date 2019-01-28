# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 09:19:29 2019

@author: Think
"""

'''【Day 3】
【dict字典】
定义
创建
字典的相关方法
-----------------------------------
【set集合】
特性
创建
方法
-------------------------------------
【file文件读取】
打开文件方式（读写两种方式）
文件对象的操作方法
*学习对excel及csv文件进行操作*
**内容为选做内容，可根据自己基础决定是否做此内容
--------------------------------------
【作业构想】
学习代码200-300行
读取一个文件【文件将在之后给出】，将文件中转换为字典，key值为学习项目，value值为一个负责人列表，
并判断字典中是否有负责人负责多个学习项目。
-------------------------------------'''
#---------------dictionary--------------------
#字典是另一种可变容器模型，且可存储任意类型对象。
#字典的每个键值(key=>value)对用冒号(:)分割，每个对之间用逗号(,)分割，整个字典包括在花括号({})中
#键必须是唯一的，但值则不必。
#值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组。
dict1 = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
#访问字典里的值,把相应的键放入到方括号中
print ("dict['Name']: ", dict['Name'])
print ("dict['Age']: ", dict['Age'])

#修改字典
dict1['Age'] = 8;               # 更新 Age
dict1['School'] = "菜鸟教程"  # 添加信息
print ("dict1['Age']: ", dict1['Age'])
print ("dict1['School']: ", dict1['School'])

#删除字典元素
del dict1['Name'] # 删除键 'Name'
print(dict1) #{'Age': 8, 'Class': 'First', 'School': '菜鸟教程'}
dict.clear()     # 清空字典 
print(dict1) #{}
del dict1         # 删除字典
print ("dict1['Age']: ", dict1['Age']) #会报错 已删除

#字典内置函数
dict1 = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
len(dict1)              #计算字典元素个数，即键的总数。
str(dict1)              #输出字典可打印的字符串表示。
type(dict1)     #返回输入的变量类型，如果变量是字典就返回字典类型。  
#python3 中没有了cmp函数

dict1.copy()    #返回一个字典的浅复制
#fromkeys(指定一个列表，把列表中的值作为字典的key,生成一个字典)
name = ['tom','lucy','sam']
print(dict1.fromkeys(name))
print(dict1.fromkeys(name,25))  #指定默认值
#输出：{'tom': None, 'lucy': None, 'sam': None}
#     {'tom': 25, 'lucy': 25, 'sam': 25}

dict1 = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
#get(指定key，获取对应的值)
dict1.get('Name')   
#items(返回由“键值对组成元素“的列表)
print(dict1.items())#输出：dict_items([('Name', 'Runoob'), ('Age', 7), ('Class', 'First')])
# keys(获取字典所有的key)
print(dict1.keys())#dict_keys(['Name', 'Age', 'Class'])
# pop(获取指定key的value，并在字典中删除)
dict2 = dict1.pop('Name')
print(dict2)#Runoob
print(dict1)#{'Age': 7, 'Class': 'First'}

dict1 = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
#popitem(随机获取某个键值对，并在字典中删除)
dict3 = dict1.popitem()
print(dict1,dict3)  #{'Name': 'Runoob', 'Age': 7} ('Class', 'First')
#setdefault(获取指定key的value，如果key不存在，则创建)
dict1.setdefault('Class')
print(dict1)#{'Name': 'Runoob', 'Age': 7, 'Class': None}
#update(添加键 - 值对到字典)
dict1.update({'School':'DataWhale'})
print(dict1)#{'Name': 'Runoob', 'Age': 7, 'Class': None, 'School': 'DataWhale'}
dict2 = {'num1':'Tom','num2':'Lucy','num3':'Sam'}
dict1.update(dict2) #把字典dict2的键/值对更新到dict里
print(dict1)

#-------------------set----------------------------
#集合（set）是一个无序的不重复元素序列。可以使用大括号 { } 或者 set() 函数创建集合，
#创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)                      # 这里演示的是去重功能
'orange' in basket                 # 快速判断元素是否在集合内
'crabgrass' in basket

#集合间运算
a = set('abracadabra')
b = set('alacazam')
a # {'a', 'b', 'c', 'd', 'r'}
b #{'a', 'c', 'l', 'm', 'z'}
a-b#{'b', 'd', 'r'}   # 集合a中包含而集合b中不包含的元素
a|b # 集合a或b中包含的所有元素
a&b # 集合a和b中都包含了的元素
a^b  # 不同时包含于a和b的元素
#集合推导式
a = {x for x in 'abracadabra' if x not in 'abc'}
a #  {'d', 'r'}

# 添加元素
set1 = set(("Google", "Runoob", "Taobao"))
set1.add("Facebook") 
print(set1)  # {'Runoob', 'Taobao', 'Facebook', 'Google'}
set1.update({1,3})
print(set1)  #{1, 3, 'Facebook', 'Google', 'Runoob', 'Taobao'}
set1.update([1,4],[5,6])  
print(set1) # {1, 3, 'Facebook', 'Google', 4, 5, 'Runoob', 'Taobao', 6}

# 移除元素
set1 = set(("Google", "Runoob", "Taobao"))
set1.remove("Google") 
print(set1)  # {'Runoob', 'Taobao'}
set1.remove("Facebook") #不存在会发生错误
set1.discard("Facebook") 
print(set1)  # {'Runoob', 'Taobao'}

# 计算集合元素个数
set1 = set(("Google", "Runoob", "Taobao"))
len(set1) # 3

# 清空集合
set1.clear()
print(set1) # set()

#--------------file------------------
# 读文件
'''1）打开文件，得到文件句柄并赋值给一个变量
2）通过句柄对文件进行操作
3）关闭文件'''
f = open('E:\\ml_code\\100days\\your_file.txt', 'r', encoding='utf-8')
'''第二个参数为对文件的操作方式，’w’是写文件，已存在的同名文件会被清空，不存在则会创建一个；
’r’是读取文件，不存在会报错；’a’是在文件尾部添加内容，不存在会创建文件，存在则直接在尾部进行添加；
还有’wb’是写二进制文件；’rb’是读取二进制文件，比如图片之类的'''
first_line = f.readline()
print('first line:',first_line) #读一行
data = f.read()# 读取剩下的所有内容,文件大时不要用
print(data) #打印读取内容
f.close() #关闭文件

#三个方法来处理文件内容的读取：
read() #一次读取全部的文件内容。
readline() #每次读取文件的一行。
readlines() #读取文件的所有行，返回一个字符串列表。

#判断文件是否是r模式打开的
print(f.readable())    

#判断文件是否是关闭状态
print(f.closed) 　　　

 #截取文件到最大size个字节，默认为当前文件位置
file.truncate(size=file.tell())   

# 向文本文件中写内容
s = 'Hello world\n文本文件的读取方法\n文本文件的写入方法\n'
# 需要写入文件的字符串
print('显示需要写入的内容:\n{0:s}'.format(s))
f = open('E:\\ml_code\\100days\\your_file.txt', 'a+')  # 以追加（a）和读写（+）的模式打开并创建文件对象f
f.write(s) # 对文件对象f使用write方法
f.close()  # 关闭文件
# 使用上下文管理关键字with方法
s = 'Hello world\n文本文件的读取方法\n文本文件的写入方法\n'
with open('E:\\ml_code\\100days\\your_file.txt', 'a+') as f:
    f.write(s)
      
with open('E:\\ml_code\\100days\\your_file.txt', 'r',encoding='utf-8') as fp:
    for line in fp:
        print(line)

#移动文件指针       
file = open('E:\\ml_code\\100days\\your_file.txt', 'r',encoding='utf-8')
file.tell()  #0　　　　　　　#返回指针当前位置
file.read(11) # '\ufeff谢谢给我看作业的同学' # 读取10个字符
file.seek(3) #从文件开始移动指针
file.read(11) # '谢谢给我看作业的同学！'

#-------------Excel、CSV读取---------------------
import pandas as pd
 
excel_path = 'example.xlsx'
df = pd.read_excel(excel_path, sheetname=None)
print(df['sheet1'].example_column_name)

pandas.read_csv(filepath_or_buffer, sep=', ',header='infer')

#作业
f = open('E:\\ml_code\\100days\\homework.txt', 'r',encoding='utf-8')
lines = f.readlines() #9
f = open('E:\\ml_code\\100days\\homework.txt', 'r',encoding='utf-8')
project=[]
people=[]
for i in range(len(lines)):
    linestr = f.readline()
    m = linestr.split()
    project.append(m[0])
    n=m[1:3]
    people.append(n)   
f.close()
dict1={}
dict=dict1.fromkeys(project)
i=0
for key in dict:
    dict[key]=people[i]
    i+=1

list2 = []
for v in dict.values():
    list2.extend(v)

set2 = set(list2)
if len(list2)>len(set2):
    print('有负责人负责多个项目')
else:
    print('无负责人负责多个项目')
#有负责人负责多个项目