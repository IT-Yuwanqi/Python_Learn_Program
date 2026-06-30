# -*- coding: utf-8 -*-
"""
@file        : Python_Practice_Week_01.py
@date        : 2026/6/29 9:14
@author      : wanqi.yu
@email       : 2395512467@qq.com
综合练习 | 用装饰器+闭包增强你的 `Equipment` 类（计时、重试、统计） | 改造第一周的 `Equipment` 代码 |
将你第1–2周的 Equipment 类升级为带有日志、计时、重试、独立故障计数器的工业级基础类。
所有装饰器可以从前几天的代码中复用。
"""
import typing
import functools
import time
import random
from datetime import datetime
from functools import reduce

def logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"装饰器开始使用，使用函数{func.__name__}")
        result = func(*args, **kwargs)
        print("装饰器使用完成")
        return result

    return wrapper


def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print(f"装饰器开始使用,使用函数{func.__name__}")
        result = func(*args, **kwargs)
        end_time = time.time()
        run_time = end_time - start_time
        print(f"装饰器使用完成，耗时{run_time}")
        return result
    return wrapper

def retry(max_retries:int, delay:float):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for i in range(max_retries):
                try:
                    print(f"  [retry] 第 {i+1} 次尝试")
                    return func(*args, **kwargs)   # 成功直接返回
                except Exception as e:
                    print(f"  [retry] 失败: {e}")
                    last_exception = e
                    if i < max_retries - 1:
                        time.sleep(delay)
            raise last_exception   # 全部失败后抛出异常
        return wrapper
    return decorator

def make_failure_counter(equipment_name):
    count = 0
    def record():
        nonlocal count
        count += 1
        print(f"⚠️  {equipment_name} 发生第 {count} 次故障")
        return count
    return record


class Equipment:
    def __init__(self,id:int,name:str,eq_type:str) ->None:
        self.id = id
        self.name = name
        self.eq_type = eq_type
        self.Status = "Idle"
        self._failure_recorder = make_failure_counter(self.name)

    @timer
    @logger
    def Start(self):
        if self.Status != "Idle":
            print("设备当前状态不是初始化，请确认设备状态")
        else:
            self.Status = "Running"
            print("设备启动成功")


    @logger
    @timer
    def Stop(self):
        if self.Status != "Running":
            print("设备当前不是运行中状态，请确认设备状态")
        else:
            self.Status = "Stopped"
            print("设备停止成功")

    @logger
    @timer
    def Equ_Init(self):
        if self.Status != "Stopped":
            print("设备当前不是停止状态，请确认设备状态")
        else:
            self.Status = "Idle"
            print("设备初始化成功")
    @retry(max_retries=3,delay=0.5)
    def send_status_to_server(self):
        number = random.randint(1,10)
        if number <= 4:
            raise ConnectionError(f"{self.name} 通信失败")
        return f"{self.name} 状态上报成功"

    def report_failure(self):
        return self._failure_recorder()


# 创建5台设备并手动设置状态
devices = [
    Equipment(1, "CNC-01", "CNC"),
    Equipment(2, "CNC-02", "CNC"),
    Equipment(3, "Robot-01", "Robot"),
    Equipment(4, "Robot-02", "Robot"),
    Equipment(5, "AGV-01", "AGV"),
]
# 设置不同状态
devices[0].Status = "Running"
devices[1].Status = "Idle"
devices[2].Status = "Running"
devices[3].Status = "Idle"
devices[4].Status = "Idle"

# map：提取所有运行中设备的名称
running_names = list(map(lambda d: d.name, filter(lambda d: d.Status == "Running", devices)))
print("运行中设备:", running_names)

# filter：统计空闲设备数量
idle_count = len(list(filter(lambda d: d.Status == "Idle", devices)))
print("空闲设备数:", idle_count)

# reduce：生成状态分布字典

def count_status(acc, d):
    acc[d.Status] = acc.get(d.Status, 0) + 1
    return acc
status_summary = reduce(count_status, devices, {})
print("状态分布:", status_summary)