#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2025/7/12 12:04
# @Author  : 地核桃
# @file: main.py
# @desc:
# atm/main.py

from atm import user_service
from atm import bank_service

def main():
    while True:
        if user_service.current_user is None:
            print("\n欢迎使用Wenl的 ATM,请选择操作：取款、存款、转账、查看交易记录、退出登录")
            action = input().strip()
            if action == "退出":
                print("感谢使用，再见！")
                break
            elif action == "注册":
                user_service.register()
            elif action == "登录":
                user_service.current_user = user_service.login()
                if user_service.current_user:
                    while True:
                        print(f"\n当前余额：{user_service.current_user['balance']:.2f}")
                        print("请选择操作：取款、存款、转账、退出登录")
                        operation = input().strip()
                        if operation == "退出登录":
                            user_service.current_user = None
                            break
                        elif operation == "存款":
                            bank_service.deposit(user_service.current_user)
                        elif operation == "取款":
                            bank_service.withdraw(user_service.current_user)
                        elif operation == "转账":
                            bank_service.transfer(user_service.current_user)
                        elif operation == "查看交易记录":
                            bank_service.view_transactions(user_service.current_user)
                        else:
                            print("无效操作，请重新输入")
            else:
                print("无效操作，请重新输入")
        else:
            pass
