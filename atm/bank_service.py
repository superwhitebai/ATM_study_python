#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2025/7/12 12:04
# @Author  : 地核桃
# @file: bank_service.py
# @desc:


from atm import user_service
from atm.user_service import current_user


def deposit():
    print('-----存款-----')
    while True:
        amout = input('请输入存款金额：').strip()
        try:
            amout = float(amout)
            if amout <= 0:
                print('金额必须大于0')
            else:
                current_user['balance'] += amout
                print(f"存款成功，当前余额：{current_user['balance']:.2f}")
                break

        except ValueError:
            print('请输入有效的数字金额')

def withdraw(current_user):
    print("-----取款-----")
    while True:
        amout = input('请输入取款金额：').strip()
        try:
            amout = float(amout)
            if amout <= 0:
                print('金额必须大于0')
            elif amout > current_user['balance']:
                print('取款金额超过了当前余额')
            else:
                current_user['balance'] -= amout
                print(f"取款成功，当前余额：{current_user['balance']:.2f}")
                break
        except ValueError:
            print('请输入有效的数字金额')