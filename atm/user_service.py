#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2025/7/12 12:04
# @Author  : 地核桃
# @file: user_service.py
# @desc:

users = []
current_user = None

def register():
    print('-----注册-----')
    username = input('请输入用户名：').strip()
    for user in users:
        if user['username'] == username:
            print('用户名已存在，请重新输入')
            return

    while True:
        password = input('请输入密码：').strip()
        if len(password) <= 3:
            print('密码长度不能小于3位，请重新输入')
        else:
            break

    users.append({
        "username": username,
        "password": password,
        "balance": 0,
    })
    print('注册成功')

def login():
    print('-----登录-----')
    username = input('请输入用户名：').strip()
    password = input('请输入密码：').strip()
    for user in users:
        if user['username'] == username:
            if user['password'] == password:
                print('登录成功')
                return user
            else:
                print('密码错误')
                return None
    print('用户不存在')
    return None

zwl = register()
zwllist = login()
