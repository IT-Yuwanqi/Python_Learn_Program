# -*- coding: utf-8 -*-
"""
@file        : Python_Learn_Week_03.py
@date        : 2026/6/22 14:07
@author      : wanqi.yu1
@email       : 2395512467@qq.com
@description : TODO
"""
import random
import functools
from unittest import result

'''
Learning
| 1 | 装饰器实战 | `*args/**kwargs` 在 wrapper 中的使用，手写 `@logger` 打印调用信息 | 为之前写的函数添加装饰器并测试 |
| 2 | 带参数装饰器 | 三层嵌套，实现 `@retry(max_retries, delay)` | 模拟不稳定的函数，验证重试逻辑 |
| 3 | `functools.wraps` 与装饰器叠加 | 修复 `__name__` 和 docstring，叠加多个装饰器（洋葱模型） | `@timer` + `@logger` 同时使用 |
| 4 | map / filter / reduce 强化 | 用 `map` 转换数据，`filter` 过滤异常，`reduce` 做累积计算 | 处理设备状态列表（如 `[1,0,1,1,2]`） |
| 5 | 闭包 | 自由变量，`nonlocal`，闭包工厂（计数器、平均值器） | 实现一个“设备启动次数计数器”闭包 |
'''



#day 1 装饰器实战 | `*args/**kwargs` 在 wrapper 中的使用，手写 `@logger` 打印调用信息 | 为之前写的函数添加装饰器并测试 |
# def logger(func):
#     def wrapper(*args,**kwargs):
#         print(f"装饰器开始使用，使用函数{func.__name__}")
#         result = func(*args,**kwargs)
#
#         print("装饰器使用完成")
#         return result
#     return wrapper
#
# @logger
# def add(a,b):
#     result = a+b
#     return result
# result = add(1,2)
# print(result)


#day 2 带参数装饰器 | 三层嵌套，实现 `@retry(max_retries, delay)` | 模拟不稳定的函数，验证重试逻辑 |
# def print_number(num = 3):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             for i in range(num):
#                 result = func(*args, **kwargs)
#             return result
#         return wrapper
#     return decorator
#
# @print_number(3)
# def say_hello():
#     print('hello')
# say_hello()
#
# def retry(max_retries):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             for i in range(max_retries):
#                 print(f"开始尝试重新链接，当前是第{i+1}次")
#                 result = func(*args, **kwargs)
#             return result
#         return wrapper
#     return decorator
#
# @retry(max_retries = 3)
# def connect():
#     number = random.randint(1, 10)
#     if number <= 5:
#         print("链接失败")
#     else:
#         print("链接成功")
#
# connect()





#day 3 `functools.wraps` 与装饰器叠加 | 修复 `__name__` 和 docstring，叠加多个装饰器（洋葱模型） | `@timer` + `@logger` 同时使用 |
# def simple_decorator(func):
#     def wrapper(*args, **kwargs):
#         """这是 wrapper 的文档"""
#         return func(*args, **kwargs)
#     return wrapper
#
# @simple_decorator
# def greet():
#     """打招呼"""
#     print("Hello!")
#
# print(greet.__name__)   # 输出: wrapper   （期望是 greet）
# print(greet.__doc__)    # 输出: 这是 wrapper 的文档  （期望是 "打招呼"）
#
#
# def decorator_a(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         print(f"装饰器A开始运行，调用函数{func.__name__},函数文档:{func.__doc__}")
#         result = func(*args, **kwargs)
#         print("装饰器A运行结束")
#         return result
#     return wrapper
#
# def decorator_b(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         print(f"装饰器B开始运行,调用函数{func.__name__},函数文档:{func.__doc__}")
#         result = func(*args, **kwargs)
#         print("装饰器B运行结束")
#         return result
#     return wrapper
#
# #一个函数使用两个装饰器 先执行A 再执行 B
# @decorator_a
# @decorator_b
# def say_hi():
#     '''
#     说你好
#     :return:
#     '''
#     print("你好")
#
# say_hi()

'''
个人笔记:多个装饰器 执行时是函数上面第一个装饰器最先执行 但结束时是挨着函数的最先退出
'''

#day 4 map / filter / reduce 强化 | 用 `map` 转换数据，`filter` 过滤异常，`reduce` 做累积计算 | 处理设备状态列表（如 `[1,0,1,1,2]`） |

# number = [1,2,3,4,5,6,7,8,9,10]
# #map(处理用的函数,可迭代数据，可以是列表 字典 元组等) 对每个元素应用函数 映射为新值
# new_list = list(map(lambda x:x **2,number))
# print(new_list)
# #filter(处理用的条件) 对每个元素应用函数 返回判定为true的数据
# result = filter(lambda x:x%2==0,number)
# print(list(result))
# #累加 reduce(处理条件，可迭代数据,从几开始累加)
# total_number = functools.reduce(lambda x,y : x+y,number,0)
# print(int(total_number))
#
#
# total_number = functools.reduce(lambda x,y : x+y,number,1)
# print(int(total_number))


#day 5 |闭包 | 自由变量，`nonlocal`，闭包工厂（计数器、平均值器） | 实现一个“设备启动次数计数器”闭包 |
'''
一个函数内部定义了另一个函数，内层函数引用了外层函数的变量，并且外层函数的返回值是内层函数本身，这就构成了闭包。
经典三要素：
函数嵌套定义。
内层函数使用外层函数的变量（自由变量）。
外层函数返回内层函数。
'''

def outer(x):
    def inner(y):
        return x + y   # x 是自由变量，来自外层作用域
    return inner

f = outer(10)   # f 现在是一个闭包，记住了 x=10
print(f(5))     # 15
print(f(20))    # 30










