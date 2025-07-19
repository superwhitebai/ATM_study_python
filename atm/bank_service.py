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
    # 打印存款提示
    print("--- 存款 ---")
    while True:
        # 输入存款金额
        amount = input("请输入存款金额：").strip()
        try:
            # 将输入的金额转换为浮点数
            amount = float(amount)
            # 如果金额小于等于0，打印提示信息
            if amount <= 0:
                print("金额必须大于0")
            else:
                # 将存款金额加到当前用户的余额中
                current_user['balance'] += amount
                # 将存款记录添加到当前用户的交易记录中
                current_user['transactions'].append(f"存款 {amount:.2f} 元")
                # 打印存款成功信息，并显示当前余额
                print(f"存款成功，当前余额：{current_user['balance']:.2f}")
                # 更新文件中的用户信息
                utils.save_users(utils.load_users())  # 更新文件
                break
        except ValueError:
            # 如果输入的不是有效的数字金额，打印提示信息
            print("请输入有效的数字金额")

def withdraw(current_user):
    # 打印取款标题
    print("--- 取款 ---")
    # 无限循环，直到取款成功
    while True:
        # 输入取款金额
        amount = input("请输入取款金额：").strip()
        try:
            # 将输入的金额转换为浮点数
            amount = float(amount)
            # 如果金额小于等于0，打印提示信息
            if amount <= 0:
                print("金额必须大于0")
            # 如果金额大于余额，打印提示信息
            elif amount > current_user['balance']:
                print("取款金额超过余额")
            # 否则，将金额从余额中扣除，并将取款记录添加到交易记录中
            else:
                current_user['balance'] -= amount
                current_user['transactions'].append(f"取款 {amount:.2f} 元")
                # 打印取款成功信息，并保存用户信息
                print(f"取款成功，当前余额：{current_user['balance']:.2f}")
                utils.save_users(utils.load_users())
                # 跳出循环
                break
        # 如果输入的金额不是有效的数字，打印提示信息
        except ValueError:
            print("请输入有效的数字金额")

def transfer(current_user):
    # 打印转账标题
    print("--- 转账 ---")
    # 导入user_service模块
    from atm import user_service
    # 获取所有用户
    users = user_service.users

    # 循环输入收款人用户名
    while True:
        # 输入收款人用户名
        recipient_name = input("请输入收款人用户名：").strip()
        # 初始化收款人
        recipient = None
        # 遍历所有用户
        for user in users:
            # 如果用户名匹配
            if user['username'] == recipient_name:
                # 设置收款人
                recipient = user
                # 跳出循环
                break
        # 如果收款人不存在
        if not recipient:
            # 打印提示信息
            print(f"{recipient_name} 该用户名不存在，请重新输入")
        else:
            # 跳出循环
            break

    # 循环输入转账金额
    while True:
        # 输入转账金额
        amount = input("请输入转账金额：").strip()
        # 尝试将输入的金额转换为浮点数
        try:
            amount = float(amount)
            # 如果金额小于等于0
            if amount <= 0:
                # 打印提示信息
                print("金额必须大于0")
            # 如果金额大于当前用户的余额
            elif amount > current_user['balance']:
                # 打印提示信息
                print("转账金额超过余额")
            else:
                # 当前用户的余额减去转账金额
                current_user['balance'] -= amount
                # 收款人的余额加上转账金额
                recipient['balance'] += amount

                # 当前用户的交易记录添加转账信息
                current_user['transactions'].append(
                    f"转出 {amount:.2f} 元给 {recipient['username']}"
                )
                # 收款人的交易记录添加收款信息
                recipient['transactions'].append(
                    f"收到 {amount:.2f} 元来自 {current_user['username']}"
                )

                # 打印转账成功信息
                print(f"转账成功，当前余额：{current_user['balance']:.2f}")
                # 保存用户信息
                utils.save_users(users)
                # 跳出循环
                break
        except ValueError:
            # 打印提示信息
            print("请输入有效的数字金额")

# 定义一个函数，用于查看当前用户的交易记录
def view_transactions(current_user):
    # 打印交易记录标题
    print("--- 交易记录 ---")
    # 遍历当前用户的交易记录
    for record in current_user.get('transactions', []):
        # 打印每条交易记录
        print(record)
