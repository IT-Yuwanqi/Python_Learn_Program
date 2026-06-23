# -*- coding: utf-8 -*-
"""
@file        : Python_Learn_Week_02.py
@date        : 2026/6/9 02:50
@author      : wanqi.yu1
@email       : 2395512467@qq.com
@description :
高阶函数 匿名函数 装饰器
高阶函数:一个函数可以接收另一个函数作为参数，或返回一个函数
匿名函数: 语法 lambda 参数列表:返回值 用于临时 一次性小函数 尤其适合作为高阶函数的参数
装饰器:在不更改函数的情况下增加功能
"""
from unittest import result


#高阶函数
def add(a,b):
    return a+b
def square(a):
    return a*a
def math_get(a,b,name):
    return name(a,b)
print(math_get(1,2,add))

#使用匿名函数简化


def math_call(a, b, name):
    if name == "add":
        return (lambda x, y: x + y)(a, b)   # 立刻用 a,b 调用
    elif name == "square":
        return (lambda x, y: x ** y)(a, b)

print(math_call(1, 2, "add"))    # 输出 3
print(math_call(2, 3, "square")) # 输出 8


#装饰器 无参装饰器
def log_before_after(func):
    def wrapper():
        print(f"Calling {func.__name__}...")
        result = func()
        print(f"{func.__name__} returned.")
        return result
    return wrapper

# 原来的函数
def say_hello():
    print("Hi there!")










