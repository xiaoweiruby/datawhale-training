# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 12:33:27 2019

@author: Think
"""

'''【Day 4】
判断语句（要求掌握多条件判断）
循环语句
三目表达式
容器
可迭代对象
迭代器
生成器
--------------------------------------
【作业构想】
学习代码200-300行
请对方输入一个0-9之间的数字，进行检查，若不是数字提示：您输入的不是数字，请输入0-9间的数字，
若数字不在0-9范围内，提示用户输入0-9之间的数字，直至用户输入正确。系统随机生成一个长度为3的数字列表，
且列表中元素在0-9之间并且不相等。将用户输入与该列表进行比较，若为列表第一个元素，则荣获第一名，
列表第二个元素，则荣获第二名，列表第三个名字，则荣获第三名，否则提示用户未得奖，输入1重新开始游戏，
输入2则结束游戏。
注意：每次游戏中列表中数字要求随机生成，每轮游戏都不相等。
-------------------------------------'''

#-------------判断语句---------------------------------
flag = False
name = 'luren'
if name == 'python':         # 判断变量否为'python'
    flag = True          # 条件成立时设置标志为真
    print ('welcome boss')    # 并输出欢迎信息
else:
    print (name)              # 条件不成立时输出变量名称

num = 5     
if num == 3:            # 判断num的值
    print ('boss')        
elif num == 2:
    print ('user')
elif num == 1:
    print ('worker')
elif num < 0:           # 值小于零时输出
    print ('error')
else:
    print ('roadman')     # 条件均不成立时输出
    
#-------------循坏语句---------------------------------

#while循环
n = 100
sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1
print("1 到 %d 之和为: %d" % (n,sum))

#在 while … else 在条件语句为 false 时执行 else 的语句块：
count = 0
while count < 5:
   print (count, " 小于 5")
   count = count + 1
else:
   print (count, " 大于或等于 5")
   
#for 循环可以遍历任何序列的项目，如一个列表或者一个字符串
sites = ["Baidu", "Google","Runoob","Taobao"]
for site in sites:
    if site == "Runoob":
        print("菜鸟教程!")
        break # break 语句可以跳出 for 和 while 的循环体。如果你从 for 或 while 循环中终止，任何对应的循环 else 块将不执行。
    print("循环数据 " + site)
else:
    print("没有循环数据!")
print("完成循环!")

seq = ['one', 'two', 'three']
for i, element in enumerate(seq): #使用内置 enumerate 函数进行遍历
    print (i, element)

for i in range(5):  #遍历数字序列，可以使用内置range()函数。
    print(i) # 0 1 2 3 4
for i in range(5,9):#用range指定区间的值
	print(i) # 5 6 7 8 
for i in range(0, 10, 3):#以指定数字开始并指定不同的增量(甚至可以是负数，有时这也叫做'步长')
	print(i) # 0 3 6 9 

#continue语句被用来告诉Python跳过当前循环块中的剩余语句，然后继续进行下一轮循环。
for letter in 'Runoob':     
   if letter == 'o':        # 字母为 o 时跳过输出
      continue
   print ('当前字母 :', letter)
'''当前字母 : R
当前字母 : u
当前字母 : n
当前字母 : b'''
    
var = 10                   
while var > 0:              
   var = var -1
   if var == 5:             # 变量为 5 时跳过输出
      continue
   print ('当前变量值 :', var)
print ("Good bye!")
'''当前变量值 : 9
当前变量值 : 8
当前变量值 : 7
当前变量值 : 6
当前变量值 : 4
当前变量值 : 3
当前变量值 : 2
当前变量值 : 1
当前变量值 : 0
Good bye!'''

#-------------三目表达------------------------------- 
#为真时的结果 if 判定条件 else 为假时的结果    
x,y = 50,25
small = x if x<y else y
print(small)
#嵌套使用
a,b,c=10,20,6
min_num = a if a<b and a<c else (b if b<a and b<c else c)
print(min_num)

#---------------- 容器---------------------------------
'''1、list
list。是一种有序的集合，可以随时添加和删除其中的元素
用索引来访问list中每一个位置的元素，记得索引是从0开始的：当索引超出了范围时，Python会报一个IndexError错误，所以，要确保索引不要越界，记得最后一个元素的索引是len(classmates) - 1
。如果要取最后一个元素，除了计算索引位置外，还可以用-1做索引，list[-1]直接获取最后一个元素。
1)、可以往list中追加元素到末尾list.append(要添加的元素)
2)、也可以把元素插入到指定的位置，比如索引号为1的位置：list.insert(1,要添加的数据)
3)、要删除list末尾的元素，用pop()方法：list.pop(),不填东西默认删除最后一个。要删除指定位置的元素，用pop(i)方法，其中i是索引位置，例：list.pop(1)删除索引为1的数据信息。
4)、要把某个元素替换成别的元素，可以直接赋值给对应的索引位置：list[1] = '替换元素'
5)、list元素也可以是另一个list，比如：list[1,2,3,[1,2,3],4]

2、字典
可变容器模型，且可存储任意类型对象。
字典的每个键值 key=>value 对用冒号 : 分割，每个键值对之间用逗号 , 分割，整个字典包括在花括号 {} 中 ,格式如下所示：
d = {key1 : value1, key2 : value2 }
字典值可以没有限制地取任何python对象，既可以是标准的对象，也可以是用户定义的，但键不行。
1）不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住
2）键必须不可变，所以可以用数字，字符串或元组充当，所以用列表就不行。

3、tuple
tuple和list非常类似，但是tuple一旦初始化就不能修改，它也没有append()，insert()这样的方法，
其他获取元素的方法和list是一样的，可以正常地使用tupe[0]， tupe[-1]，但不能赋值成另外的元素。
count() 统计元组中某个元素出现的次数
index() 获取某个元素在元组中的第一个位置索引，若有返回索引值，若没有抛出异常错误

4、集合
集合中可以存储任意类型的数据，集合中不会出现重复的数据
集合的添加有两种常用方法，分别是add和update。  set1.add(要添加的数据)、set1.update（）
'''

#---------------------可迭代对象-------------------------
''' 迭代是指对集合元素遍历的一种方式，迭代器是可以实现对集合从前向后依次遍历的一个对象
表面来看，只要可以用 for...in...进行遍历的对象就是     可迭代对象    
语法层面，如果一个对象实现了__iter__方法，那么这个对象就是    可迭代对象
字符串、字典、list是可迭代对象
两种方法：
1.可迭代对象.__iter__()
2.iter(可迭代对象)'''
#  isinstance()  判断一个对象是否是 可迭代 对象：
from collections import Iterable#载入模块
isinstance('abc',Iterable) #字符串是可迭代对象吗？  True

#字典迭代
d={'python':1,'php':2,'java':3}
#默认迭代的是key
for i in d:
    print(i)
# 迭代value    
for value in d.values():
    print(value)
#同时迭代key,value
for k , v in d.items():
    print(k,v)

#列表和元组的下标循环
lanage=['python','php','java','c++']
#第一种：
for x in range(len(lanage)):
    print(x,lanage[x])
#第二种：
for i ,value in enumerate(lanage):
    print(i,value)

#自定义可迭代对象
class MyList(object): #自定义一个类Mylist
     def __init__(self): #__init__()方法是类的构造函数或初始化方法
         self.list = []  #self代表类的实例，而非类
     def add(self,item):
         self.list.append(item)
         
mylist = MyList()
isinstance(mylist,Iterable) # 不是可迭代对象

class MyList(object):
     def __init__(self):
         self.list = []
     def add(self,item):
         self.list.append(item)
     def __iter__(self):  #给MyList类添加一个iter方法
         pass    #pass是空语句，是为了保持程序结构的完整性。pass 不做任何事情，一般用做占位语句

mylist = MyList()
isinstance(mylist,Iterable) #True

##-------------生成器---------------------------------
#生成器是迭代器的一种，使用yield返回值函数，每次调用yield会暂停，而可以使用next()函数和send()函数恢复生成器。
#1、只有把一个列表生成式的[]中括号改为（）小括号，就创建一个generator
#列表生成式
lis = [x*x for x in range(10)]
print(lis)  #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
#生成器
generator_ex = (x*x for x in range(10))
print(generator_ex)  #<generator object <genexpr> at 0x000000042415EEB8>
#通过next（）函数获得generator的下一个返回值
generator_ex = (x*x for x in range(10))
print(next(generator_ex))
print(next(generator_ex))
print(next(generator_ex))
print(next(generator_ex))
print(next(generator_ex))
print(next(generator_ex))
print(next(generator_ex))
print(next(generator_ex))
print(next(generator_ex))
print(next(generator_ex))
print(next(generator_ex))  #没有更多的元素时，抛出StopIteration的错误
#创建一个generator后，基本上永远不会调用next()，而是通过for循环来迭代
generator_ex = (x*x for x in range(10))
for i in generator_ex:
    print(i)
 # 实例
import sys
 
def fibonacci(n): # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n): 
            return
        yield a
        a, b = b, a + b
        counter += 1
f = fibonacci(10) # f 是一个迭代器，由生成器返回生成
 
while True:
    try:  # 异常处理
        print (next(f), end=" ")
    except StopIteration:
        sys.exit()

#-----------------作业----------------------------------
'''请对方输入一个0-9之间的数字，进行检查，若不是数字提示：您输入的不是数字，请输入0-9间的数字，
若数字不在0-9范围内，提示用户输入0-9之间的数字，直至用户输入正确。系统随机生成一个长度为3的数字列表，
且列表中元素在0-9之间并且不相等。将用户输入与该列表进行比较，若为列表第一个元素，则荣获第一名，
列表第二个元素，则荣获第二名，列表第三个名字，则荣获第三名，否则提示用户未得奖，输入1重新开始游戏，
输入2则结束游戏。
注意：每次游戏中列表中数字要求随机生成，每轮游戏都不相等。'''
# 导入 random(随机数) 模块
import random
start = 1
while start != 2:
    award = random.sample(range(9), 3)  #从range(9)中随机获取3个元素，作为一个片断返回
    num = input("请输入0-9之间的一个数字：")
    while num.isdigit()==False:
        num = input("请输入0-9之间的一个数字：")
    num=int(num)
    while num>=9:
        num = input("数字必须在0-9之间哦，请重新输入：")
    num=int(num)
    if num == award[0]:
        print("恭喜您荣获第一名")
    elif num == award[1]:
        print("恭喜您荣获第二名")
    elif num == award[2]:
        print("恭喜您荣获第二名")
    else:
        print("很遗憾，未得奖")
    start = int(input('输入1重新开始游戏，输入2则结束游戏'))
    if start == 2:
        break

    
    