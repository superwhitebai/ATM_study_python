#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2025/7/16 17:34
# @Author  : 地核桃
# @file: app.py
# @desc:
from flask import Flask, request, render_template, redirect, session
from atm import user_service, bank_service, utils

app = Flask(__name__)
app.secret_key = 'mysecretkey'  # session 用

@app.route('/')
def home():
    if 'username' in session:
        user = next((u for u in user_service.users if u['username'] == session['username']), None)
        return f"欢迎 {user['username']}！当前余额：{user['balance']:.2f} <br><a href='/deposit'>存款</a> | <a href='/withdraw'>取款</a> | <a href='/transactions'>交易记录</a> | <a href='/logout'>退出登录</a>"
    return "欢迎！<br><a href='/register'>注册</a> | <a href='/login'>登录</a>"

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        for u in user_service.users:
            if u['username'] == username:
                return "用户名已存在"
        hashed = utils.encrypt_password(password)
        user_service.users.append({
            'username': username,
            'password': hashed,
            'balance': 0.0,
            'transactions': []
        })
        utils.save_users(user_service.users)
        return redirect('/login')
    return '''
        <form method='post'>
            用户名：<input name='username'><br>
            密码：<input name='password' type='password'><br>
            <input type='submit' value='注册'>
        </form>
    '''

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_pwd = utils.encrypt_password(password)
        for u in user_service.users:
            if u['username'] == username and u['password'] == hashed_pwd:
                session['username'] = username
                return redirect('/')
        return "登录失败"
    return '''
        <form method='post'>
            用户名：<input name='username'><br>
            密码：<input name='password' type='password'><br>
            <input type='submit' value='登录'>
        </form>
    '''

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/')

@app.route('/deposit', methods=['GET', 'POST'])
def deposit():
    if 'username' not in session:
        return redirect('/login')
    user = next((u for u in user_service.users if u['username'] == session['username']), None)
    if request.method == 'POST':
        amount = float(request.form['amount'])
        user['balance'] += amount
        user['transactions'].append(f"存款 {amount} 元")
        utils.save_users(user_service.users)
        return redirect('/')
    return '''
        <form method='post'>
            存款金额：<input name='amount'><br>
            <input type='submit' value='存款'>
        </form>
    '''

@app.route('/withdraw', methods=['GET', 'POST'])
def withdraw():
    if 'username' not in session:
        return redirect('/login')
    user = next((u for u in user_service.users if u['username'] == session['username']), None)
    if request.method == 'POST':
        amount = float(request.form['amount'])
        if amount > user['balance']:
            return "余额不足"
        user['balance'] -= amount
        user['transactions'].append(f"取款 {amount} 元")
        utils.save_users(user_service.users)
        return redirect('/')
    return '''
        <form method='post'>
            取款金额：<input name='amount'><br>
            <input type='submit' value='取款'>
        </form>
    '''

@app.route('/transactions')
def transactions():
    if 'username' not in session:
        return redirect('/login')
    user = next((u for u in user_service.users if u['username'] == session['username']), None)
    history = "<br>".join(user.get('transactions', []))
    return f"<h3>交易记录</h3>{history}<br><a href='/'>返回</a>"

if __name__ == '__main__':
    app.run(debug=True)
