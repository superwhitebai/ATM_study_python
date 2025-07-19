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
    # 无限循环，直到用户选择退出
    while True:
        # 如果当前用户为空，则提示用户选择操作
        if user_service.current_user is None:
            print("\n欢迎使用Wenl的 ATM,请选择操作：取款、存款、转账、查看交易记录、退出登录")
            action = input().strip()
            # 如果用户选择退出，则打印感谢信息并退出循环
            if action == "退出":
                print("感谢使用，再见！")
                break
            # 如果用户选择注册，则调用注册函数
            elif action == "注册":
                user_service.register()
            # 如果用户选择登录，则调用登录函数，并将返回的用户信息赋值给当前用户
            elif action == "登录":
                user_service.current_user = user_service.login()
                # 如果登录成功，则进入用户操作循环
                if user_service.current_user:
                    while True:
                        # 打印当前余额
                        print(f"\n当前余额：{user_service.current_user['balance']:.2f}")
                        # 提示用户选择操作
                        print("请选择操作：取款、存款、转账、退出登录")
                        operation = input().strip()
                        # 如果用户选择退出登录，则将当前用户置为空，并退出循环
                        if operation == "退出登录":
                            user_service.current_user = None
                            break
                        # 如果用户选择存款，则调用存款函数
                        elif operation == "存款":
                            bank_service.deposit(user_service.current_user)
                        # 如果用户选择取款，则调用取款函数
                        elif operation == "取款":
                            bank_service.withdraw(user_service.current_user)
                        # 如果用户选择转账，则调用转账函数
                        elif operation == "转账":
                            bank_service.transfer(user_service.current_user)
                        # 如果用户选择查看交易记录，则调用查看交易记录函数
                        elif operation == "查看交易记录":
                            bank_service.view_transactions(user_service.current_user)
                        # 如果用户输入的操作无效，则提示用户重新输入
                        else:
                            print("无效操作，请重新输入")
            else:
                print("无效操作，请重新输入")
        else:
            pass
