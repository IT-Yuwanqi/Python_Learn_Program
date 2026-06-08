# -*- coding: utf-8 -*-
"""
@file        : Python_Learn_Week_01.py
@date        : 2026/6/1 11:00
@author      : wanqi.yu
@email       : 2395512467@qq.com
@description : Python基础学习
"""

'''
变量 数据类型 列表 字典 循环 条件语句 函数 类 输入/输出 注释
Python中有两种注释方式 #号 和 三个引号 三个引号不被使用的情况下 Python会把它们直接跳过
'''
#输出 print(要输出的内容)
print("Python Learning Program")
#输入 input(提示) input函数获取到的值 默认为字符串类型 如果要在计算中使用 需要转换类型
#Python会自动判断数据类型
#基础数据类型
name = 'Wanqi.yu' #字符串
age = 26 #整数
height = 1.74 #浮点数
flag = True #布尔类型
#查看变量类型
print(type(name))
#类型转换 str会将所有其他类型转换为字符串
#注意点 int 整数 float 在转换时如果被转换的值里有不是数值的部分 会导致转换失败
print(f"转换前的类型是{type(age)},被转换后的类型是{type(str(age))}")
#列表 用于存储多个数据 类似于C#中的列表 但稍微有不同 Python中的元素 数据类型可以是不一致的 数据可以排序 可以按索引查询 索引从0开始
#列表使用 []括号定义
user_list = []
user_list.append(name)  #向列表中添加数据 添加到列表末尾
user_list.insert(0,"Hongyu.sun")
user_list.append("Lei.liu")
user_list.append("Hao.shen")
print(user_list) #输出整个列表
print(user_list[0]) #输出列表中索引值为0的元素

user_list.pop() #弹出列表中的值 默认从末尾开始 也可以输入索引 弹出的值可以使用
print(user_list) #弹出末尾值之后的列表

print(sorted(user_list)) #输出排序后的列表 临时排序
user_list.sort() #永久排序
user_list.sort(reverse=True) #翻转列表

#字典 存储键值对数据 可以与列表互相嵌套 字典使用 {}括号
user_address = {}
#字典添加键值对 语法 字典名[键] = 值 如果字典中不存在这个键 则创建 如果存在 则覆盖之前的值
user_address["user_1"] = "xx市xx街道xx小区"
user_address["user_2"] = "xx市xx街道xx小区"
user_address["user_3"] = "xx市xx街道xx小区"
user_address["user_4"] = "xx市xx街道xx小区"
user_address["user_5"] = "xx市xx街道xx小区"
print(user_address)
#删除字典中的键值对 删除时使用 del关键字 后面跟字典名称[键] 如果字典名称后面没有键的话 表示删除整个字典
del user_address["user_1"]

#列表嵌套字典 Python中 可以列表嵌套列表 列表嵌套字典 字典嵌套列表
user_1 = {"name":'user_1','age':26}
user_2 = {"name":'user_2','age':26}
user_3 = {"name":'user_3','age':26}
user_list_dict = [user_1,user_2,user_3]
print(user_list_dict)




#Python中的循环分为两种 for循环和while循环 for循环适合遍历和固定次数的循环运行代码
#range(开始位置，结束位置，步长)
for i in range(1,11):
    print(i)

#for循环遍历列表
for i in user_list:
    print(i)

#while循环 按次数循环 while更适合按特定条件循环
num = 0
while num <= 10:
    print(num)
    num += 1


'''
函数:一组代码块 可以重复使用
'''

def User_BMI(weight:float, height:flag)->float:
    user_bmi = weight / (height * height)
    return user_bmi

'''
类:现实世界实物的抽象 
包含了构造函数 类方法
构造函数定义了对象的属性
对象:类的实例 类就像是设计图 对象就是实际的物品
'''

class Equipment:
    def __init__(self, name,id,type:list):
        self.name = name
        self.id = id
        self.type = type
        self.Status = "Idle"

    def Start(self):
        if self.Status == "Idle":
            self.Status = "Running"
            print(f"设备启动成功，当前状态为{self.Status}")
        else:
            print(f"设备启动失败，当前状态为{self.Status}")

    def Stop(self):
        if self.Status == "Running":
            self.Status = "Stopped"
            print(f"设备停止成功,当前状态{self.Status}")
        else:
            print(f"设备停止失败，当前状态{self.Status}")

    def Init_Equipment(self):
        if self.Status == "Stopped":
            self.Status = "Idle"
            print(f"设备初始化成功,当前状态为{self.Status}")
        else:
            print(f"设备初始化失败，当前状态为{self.Status}")






equ_01 = Equipment("切叠一体机",1001,"电芯")
equ_01.Start()
equ_01.Start()
equ_01.Stop()
equ_01.Init_Equipment()