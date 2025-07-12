#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2025/7/12 12:04
# @Author  : 地核桃
# @file: bank_service.py
# @desc:


from atm import user_service
from atm.user_service import current_user


def deposit(current_user):
    # 打印存款提示
    print('-----存款-----')
    while True:
        # 输入存款金额
        amout = input('请输入存款金额：').strip()
        try:
            # 将输入的金额转换为浮点数
            amout = float(amout)
            # 判断金额是否大于0
            if amout <= 0:
                # 如果金额小于等于0，打印提示信息
                print('金额必须大于0')
            else:
                # 如果金额大于0，将金额加到当前用户的余额上
                current_user['balance'] += amout
                # 打印存款成功信息，并显示当前余额
                print(f"存款成功，当前余额：{current_user['balance']:.2f}")
                # 跳出循环
                break

        except ValueError:
            # 如果输入的金额不是有效的数字，打印提示信息
            print('请输入有效的数字金额')

def withdraw(current_user):
    # 打印取款标题
    print("-----取款-----")
    # 无限循环，直到取款成功
    while True:
        # 输入取款金额
        amout = input('请输入取款金额：').strip()
        try:
            # 将输入的金额转换为浮点数
            amout = float(amout)
            # 如果金额小于等于0，则提示金额必须大于0
            if amout <= 0:
                print('金额必须大于0')
            # 如果金额大于当前余额，则提示取款金额超过了当前余额
            elif amout > current_user['balance']:
                print('取款金额超过了当前余额')
            # 否则，将当前余额减去取款金额，并打印取款成功和当前余额
            else:
                current_user['balance'] -= amout
                print(f"取款成功，当前余额：{current_user['balance']:.2f}")
                # 跳出循环
                break
        # 如果输入的金额不是有效的数字，则提示请输入有效的数字金额
        except ValueError:
            print('请输入有效的数字金额')

def transfer(current_user):
    # 打印转账标题
    print('-----转账-----')
    # 循环输入收款人用户名
    while True:
        # 输入收款人用户名
        recipient_name = input('请输入收款人用户名：').strip()
        # 初始化收款人变量
        recipient = None
        # 遍历用户列表
        for user in user_service.users:
            # 如果用户名匹配
            if user['username'] == recipient_name:
                # 将用户赋值给收款人变量
                recipient = user
                # 跳出循环
                break
        # 如果收款人变量为空
        if not recipient:
            # 打印提示信息
            print(f"{recipient_name} 该用户名不存在，请重新输入")
        else:
            # 跳出循环
            break
    # 循环输入转账金额
    while True:
        # 输入转账金额
        amout = input('请输入转账金额：').strip()
        # 尝试将输入的金额转换为浮点数
        try:
            amout = float(amout)
            # 如果金额小于等于0
            if amout <= 0:
                # 打印提示信息
                print('金额必须大于0')
            # 如果金额大于当前余额
            elif amout > current_user['balance']:
                # 打印提示信息
                print('转账金额超过了当前余额')
            else:
                # 当前用户余额减去转账金额
                current_user['balance'] -= amout
                # 收款人余额加上转账金额
                recipient['balance'] += amout
                # 打印转账成功信息
                print(f"转账成功，当前余额：{current_user['balance']:.2f}")
                # 跳出循环
                break
        # 如果转换失败
        except ValueError:
            # 打印提示信息
            print('请输入有效的数字金额')

