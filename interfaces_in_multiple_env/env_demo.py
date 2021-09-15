#!/usr/bin/env python
# encoding: utf-8
"""
@author:ZhaoLong
@contact: 1452885022@qq.com
@software: Laka
@file: env_demo.py
@time: 2021/9/15 13:18
@desc:
"""
import requests
import yaml

'''
    实现原理
    在请求之前，对请求的url进行替换
    1. 需要二次封装requests，对其进行定制化
    2. 将请求的结构体的url从一个写死的ip地址改为一个（任意的）域名
    3. 使用一个env配置文件，存放各个环境的配置信息
    4. 然后将请求结构体中的url替换为'env'配置文件中个人选择的url
    5. 将env配置文件使用yaml口管理
'''


class Api:
    env = yaml.safe_load(open("env.yaml"))
    def send(self, data: dict):
        # 替换                                                    self.env["testing-studio"]["env"]
        data["url"] = str(data["url"]).replace("testing-studio", self.env["testing-studio"][self.env["default"]])
        r = requests.request(method=data["method"], url=data['url'], headers=data['headers'])
