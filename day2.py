# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 10:03:17 2019

@author: Think
"""

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

#---------list---------
#创建一个列表，只要把逗号分隔的不同的数据项使用方括号括起来即可
#列表的标志符号是[]
list1 = ['Google', 'Runoob', 1997, 2000]
list2 = [1, 2, 3, 4, 5 ]
list3 = ["a", "b", "c", "d"]
 
print ("list1[0]: ", list1[0])
print ("list2[1:5]: ", list2[1:5])

# del 语句来删除列表的的元素
print ("原始列表 : ", list1)
del list1[2]
print ("删除第三个元素 : ", list1)

#列表对 + 和 * 的操作符与字符串相似。+ 号用于组合列表，* 号用于重复列表。
len(list1) #长度 3
list1+list2 #['Google', 'Runoob', 2000, 1, 2, 3, 4, 5]
['Hi!'*4]
3 in [1, 2, 3]# True
for x in [1, 2, 3]: print(x, end=" ")

print(list1) #['Google', 'Runoob', 2000]
list1[1] 
list1[-1]
list1[1:]

list1 += [1,2,5]
print(list1)  #['Google', 'Runoob', 2000, 1, 2, 5]

#嵌套list
a=[list1,list2]
a  #[['Google', 'Runoob', 2000, 1, 2, 5], [1, 2, 3, 4, 5]]
a[0]  # ['Google', 'Runoob', 2000, 1, 2, 5]
a[0][1]  #'Runoob'

names = ['a','b','c','d']
#追加
names.append('e')
print(names)  #['a', 'b', 'c', 'd', 'e']

#删除：pop，remove，del
names.pop()#如果没有指定下标，则默认会删除最后一个元素
print(names)  #['a', 'b', 'c', 'd']
names.pop(2)#指定下标时，就会删除下标所对应的元素
print(names)  #['a', 'b', 'd']
names.remove('a')
print(names) #['b', 'd']
del names[1]
print(names) #['b']

#查找元素所在位置：index()
names = ['a','b','c','d']
names.index('c')  #2

#统计元素的次数：count()
names.append('d')
print(names)  #['a', 'b', 'c', 'd', 'd']
names.count('d')

#反转：reverse()
names.reverse()
print(names)#['d', 'd', 'c', 'b', 'a']

#清空：clear()
names.clear()
names

#插入：insert()
names = ['a','b','c','d']
names.insert(2,'devilf')
names #['a', 'b', 'devilf', 'c', 'd']
names[3] = 'lebron'
names  #['a', 'b', 'devilf', 'lebron', 'd']

#排序：sort()按照ascii码来进行排序
names.sort()
names #['a', 'b', 'd', 'devilf', 'lebron']

#拼接两个列表：extend()
place=['beijing','changsha']
names.extend(place)
names #['a', 'b', 'd', 'devilf', 'lebron', 'beijing', 'changsha']

#深浅复制
names = ["小明", "小红", "小黑", "小黄", "小白"]
# 把 names 复制，赋值给 names2变量
names2 = names.copy()
# 修改 names 列表中的 小黄
names[3] = "Yellow"
# 分别输出 names names2
print(names) #['小明', '小红', '小黑', 'Yellow', '小白']
print(names2) #['小明', '小红', '小黑', '小黄', '小白']

names = ["小明", "小红", ["张三", "李四", "王五"], "小黑", "小黄", "小白"]
# 复制一份列表
names2 = names.copy()
# 把李四 改成英文
names[2][1] = "Lisi"
print(names) #['小明', '小红', ['张三', 'Lisi', '王五'], '小黑', '小黄', '小白']
print(names2) #['小明', '小红', ['张三', 'Lisi', '王五'], '小黑', '小黄', '小白']

#list.copy() 方法只能 copy 一层，这就是所谓的浅复制。
#浅复制三种方法
import copy

names = ["小明", "小红", "小黑", "小黄", "小白"]
# 浅copy 1.
names1 = copy.copy(names)
name1
# 2.
names2 = names[:]
names2
# 3. 工厂函数
names3 = list(names)
names3

import copy

names = ["小明", "小红", "小黑", ["粉色"], "小黄", "小白"]
# 深复制
deep_names = copy.deepcopy(names)
# 修改粉色为 Pink
names[3][0] = "Pink"
# 分别打印输出两个列表
print(names) #['小明', '小红', '小黑', ['Pink'], '小黄', '小白']
print(deep_names) #['小明', '小红', '小黑', ['粉色'], '小黄', '小白']

#---------tuple---------
#元组与列表类似，不同之处在于元组的元素不能修改。元组标志()
#元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。
tup1 = ('Google', 'Runoob', 1997, 2000)
tup2 = (1, 2, 3, 4, 5 )
tup3 = "a", "b", "c", "d"  #  不需要括号也可以
type(tup3)
#元组中只包含一个元素时，需要在元素后面添加逗号，否则括号会被当作运算符使用：
tup1 = (50)
type(tup1)     # 不加逗号，类型为整型
tup1 = (50,)
type(tup1)     # 加上逗号，类型为元组

print ("tup1[0]: ", tup1[0])  #50
print ("tup2[1:5]: ", tup2[1:5]) #(2, 3, 4, 5)

#以下修改元组元素操作是非法的。
# tup2[0] = 100
 
# 创建一个新的元组
tup4 = tup1 + tup2;
print (tup4)

#元组中的元素值是不允许删除的，del语句来删除整个元组
del(tup4)
print (tup4)

a = 'hello,world' 
b = list(a)    #字符串->列表
c = ''.join(b)    #列表->字符串
print (a)#hello,world
print (b)#['h', 'e', 'l', 'l', 'o', ',', 'w', 'o', 'r', 'l', 'd']
print (c)#hello,world


li = [1,2,3]
tu = tuple(li)    #列表->元组
New_li = list(tu)    #元组->列表
print(li)#[1, 2, 3]
print(tu)#(1, 2, 3)
print(New_li)#[1, 2, 3]

a = 'hello,world'
b = tuple(a)    #字符串->元组
c = ''.join(b)    #元组->字符串
print (a)#hello,world
print (b)#('h', 'e', 'l', 'l', 'o', ',', 'w', 'o', 'r', 'l', 'd')
print (c)#hello,world

#homework
family=['Fang XJ','Zeng Sq','Fang ZY','Fang XY']
family.insert(3,'Zhang F')
print(family)
family.pop(3)
print(family)

