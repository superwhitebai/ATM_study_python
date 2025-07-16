#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2025/7/12 12:05
# @Author  : 地核桃
# @file: utils.py
# @desc:

import json
import os
import hashlib

USER_DATA_FILE= 'user_data.json'

# 定义一个函数，用于保存用户数据
def save_users(users):
    # 打开用户数据文件，以写入模式，编码为utf-8
    with open(USER_DATA_FILE, "w", encoding="utf-8") as f:
        # 将用户数据以json格式写入文件，不使用ascii编码，缩进为4
        json.dump(users, f, ensure_ascii=False, indent=4)

# 定义一个函数，用于加载用户数据
def load_users():
    # 判断用户数据文件是否存在
    if not os.path.exists(USER_DATA_FILE):
        # 如果不存在，则返回空列表
        return []
    # 打开用户数据文件，以只读方式打开，编码格式为utf-8
    with open(USER_DATA_FILE, "r", encoding="utf-8") as f:
        # 将文件中的数据加载为json格式，并返回
        return json.load(f)

def encrypt_password(password):
    return hashlib.sha256(password.encode()).hexdigest()
