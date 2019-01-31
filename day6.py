# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 09:56:46 2019

@author: Think
"""

'''
【Day 6】
函数关键字
函数的定义
函数参数与作用域
函数返回值
--------------------------------------
【作业构想】
实现random.sample方法
实现Max方法
实现判断两个字符串是否相等的方法
-------------------------------------'''

#--------------------函数关键字-----------------
#函数代码块以 def 关键词开头，后接函数标识符名称和圆括号 ()
def hello() :
   print("Hello World!")
hello()
#--------------------函数定义-------------------
#函数是组织好的，可重复使用的，用来实现单一，或相关联功能的代码段。
#函数能提高应用的模块性，和代码的重复利用率。
#--------------------函数参数与作用域-------------
#传不可变对象
def ChangeInt( a ):
    a = 10
b = 2
ChangeInt(b)
print( b ) # 结果是 2

#传可变对象
def changeme( mylist ):
   "修改传入的列表"
   mylist.append([1,2,3,4])
   print ("函数内取值: ", mylist)
   return
mylist = [10,20,30]
changeme( mylist ) # 调用changeme函数
print ("函数外取值: ", mylist)
#函数内取值:  [10, 20, 30, [1, 2, 3, 4]]  函数外取值:  [10, 20, 30, [1, 2, 3, 4]]

#必须参数  须以正确的顺序传入函数。调用时的数量必须和声明时的一样。
def printme( str ):
   "打印任何传入的字符串"
   print (str)
   return
printme() # 调用printme()函数，必须传入一个参数，不然会出现语法错误

#关键字参数  允许函数调用时参数的顺序与声明时不一致
printme( str = "菜鸟教程")

#默认参数 调用函数时，如果没有传递参数，则会使用默认参数
def printinfo( name, age = 35 ):
   "打印任何传入的字符串"
   print ("名字: ", name)
   print ("年龄: ", age)
   return
printinfo( age=50, name="runoob" )#调用printinfo函数
print ("------------------------")
printinfo( name="runoob" )

# 不定长参数 一个函数能处理比当初声明时更多的参数，声明时不会命名
def printinfo( arg1, *vartuple ):  # 星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数
   "打印任何传入的参数"
   print ("输出: ")
   print (arg1)
   print (vartuple)
   print (vartuple[0])
printinfo( 70, 60, 50 )
printinfo( 10 ) #在函数调用时没有指定参数，*参数是一个空元组

def printinfo( arg1, **vardict ): # 加了两个星号 ** 的参数会以字典的形式导入
   "打印任何传入的参数"
   print ("输出: ")
   print (arg1)
   print (vardict)
printinfo(1, a=2,b=3)

#可单独出现星号 * 后的参数必须用关键字传入
def f(a,b,*,c):
    return a+b+c
f(1,2,3)   # 报错
f(1,2,c=3)  #6

'''变量的作用域决定了在哪一部分程序可以访问哪个特定的变量名称。Python的作用域一共有4种，分别是：
L （Local） 局部作用域、  E （Enclosing） 闭包函数外的函数中
G （Global） 全局作用域、 B （Built-in） 内建作用域
以 L –> E –> G –>B 的规则查找，即：在局部找不到，便会去局部外的局部找（例如闭包），再找不到就会去全局找，再者去内建中找。'''
x = int(2.9)  # 内建作用域
g_count = 0  # 全局作用域
def outer():
    o_count = 1  # 闭包函数外的函数中
    def inner():
        i_count = 2  # 局部作用域

#局部变量只能在其被声明的函数内部访问，而全局变量可以在整个程序范围内访问
total = 0 # 这是一个全局变量
# 可写函数说明
def sum( arg1, arg2 ):
    #返回2个参数的和."
    total = arg1 + arg2 # total在这里是局部变量.
    print ("函数内是局部变量 : ", total)
    return total
sum( 10, 20 )
print ("函数外是全局变量 : ", total)

num = 1
def fun1():
    global num  # 需要使用 global 关键字声明 修改全局变量
    print(num) # 1
    num = 123
    print(num)  #123
fun1()
print(num)  #123

def outer():
    num = 10
    def inner():
        nonlocal num   # nonlocal关键字声明 改嵌套作用域（enclosing 作用域，外层非全局作用域）中的变量u                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
        num = 100
        print(num) #100
    inner()
    print(num)  #100
outer()

#-------------------函数返回值-------------------
#如果没有return语句，函数执行完毕后也会返回结果，只是结果为None
#------------------作业----------------------------
#实现random.sample方法
def randomsample(start,end,num):
    import random
    res = []
    while len(res)<num:
        res.append(random.randint(start,end))
    return(res)
#实现Max方法
def MAX(m,*n):
    def MAX1(a,b):
        if a >= b:
            return a
        else:
            return b
    i = 0
    ma = m
    while i<len(n):
        ma = MAX1(ma,n[i])
        i +=1
    return ma         
#实现判断两个字符串是否相等的方法
def chaeql(a,b):
    i = 0
    if len(a) == len(b):
        while i < len(a):
            if a[i]!=b[i]:
                return False
                break
            if a[i]==b[i]:
                i +=1
        return True
    else:
        return False
         
     