#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2025/7/12 12:04
# @Author  : 地核桃
# @file: bank_service.py
# @desc:
# bank_service.py
from atm import utils

# 避免循环导入：在需要时再导入 user_service

def deposit(current_user):
    print("--- 存款 ---")
    while True:
        amount = input("请输入存款金额：").strip()
        try:
            amount = float(amount)
            if amount <= 0:
                print("金额必须大于0")
            else:
                current_user['balance'] += amount
                current_user['transactions'].append(f"存款 {amount:.2f} 元")
                print(f"存款成功，当前余额：{current_user['balance']:.2f}")
                utils.save_users(utils.load_users())  # 更新文件
                break
        except ValueError:
            print("请输入有效的数字金额")

def withdraw(current_user):
    print("--- 取款 ---")
    while True:
        amount = input("请输入取款金额：").strip()
        try:
            amount = float(amount)
            if amount <= 0:
                print("金额必须大于0")
            elif amount > current_user['balance']:
                print("取款金额超过余额")
            else:
                current_user['balance'] -= amount
                current_user['transactions'].append(f"取款 {amount:.2f} 元")
                print(f"取款成功，当前余额：{current_user['balance']:.2f}")
                utils.save_users(utils.load_users())
                break
        except ValueError:
            print("请输入有效的数字金额")

def transfer(current_user):
    print("--- 转账 ---")
    from atm import user_service
    users = user_service.users

    while True:
        recipient_name = input("请输入收款人用户名：").strip()
        recipient = None
        for user in users:
            if user['username'] == recipient_name:
                recipient = user
                break
        if not recipient:
            print(f"{recipient_name} 该用户名不存在，请重新输入")
        else:
            break

    while True:
        amount = input("请输入转账金额：").strip()
        try:
            amount = float(amount)
            if amount <= 0:
                print("金额必须大于0")
            elif amount > current_user['balance']:
                print("转账金额超过余额")
            else:
                current_user['balance'] -= amount
                recipient['balance'] += amount

                current_user['transactions'].append(
                    f"转出 {amount:.2f} 元给 {recipient['username']}"
                )
                recipient['transactions'].append(
                    f"收到 {amount:.2f} 元来自 {current_user['username']}"
                )

                print(f"转账成功，当前余额：{current_user['balance']:.2f}")
                utils.save_users(users)
                break
        except ValueError:
            print("请输入有效的数字金额")

def view_transactions(current_user):
    print("--- 交易记录 ---")
    for record in current_user.get('transactions', []):
        print(record)
