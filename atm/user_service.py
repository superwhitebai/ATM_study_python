#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2025/7/12 12:04
# @Author  : 地核桃
# @file: user_service.py
# @desc:

from atm import utils
from atm.web.app import transactions

users = utils.load_users()
current_user = None
# 定义注册函数
def register():
    # 打印注册标题
    print('-----注册-----')
    # 输入用户名
    username = input('请输入用户名：').strip()
    password = input("请输入密码：").strip()
    hashed_pwd = utils.encrypt_password(password)
    # 遍历用户列表，判断用户名是否已存在
    for user in users:
        if user['username'] == username:
            # 如果用户名已存在，提示重新输入
            print('用户名已存在，请重新输入')
            return

    # 循环输入密码，直到密码长度大于3位
    while True:
        password = input('请输入密码：').strip()
        if len(password) <= 3:
            # 如果密码长度小于等于3位，提示重新输入
            print('密码长度不能小于3位，请重新输入')
        else:
            break

    # 将用户名、密码和余额添加到用户列表中
    users.append({
        "username": username,
        "password": hashed_pwd,
        "balance": 0,
        "transactions": []
    })
    # 打印注册成功
    print('注册成功')

    utils.save_users(users)

def login():
    # 打印登录提示
    print('-----登录-----')
    # 输入用户名并去除空格
    username = input('请输入用户名：').strip()
    # 输入密码并去除空格
    password = input('请输入密码：').strip()
    # 遍历用户列表
    for user in users:
        # 如果用户名匹配
        if user['username'] == username:
            hashed_pwd = utils.encrypt_password(password)
            # 如果密码匹配
            if user['password'] == hashed_pwd:
                # 打印登录成功
                print("当前 users 数据：", users)
                print('登录成功')
                # 返回用户信息
                return user
            else:
                # 打印密码错误
                print('密码错误')
                # 返回None
                return None
    # 打印用户不存在
    print('用户不存在')

