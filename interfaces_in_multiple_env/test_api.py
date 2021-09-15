#!/usr/bin/env python
# encoding: utf-8
"""
@author:ZhaoLong
@contact: 1452885022@qq.com
@software: Laka
@file: test_api.py
@time: 2021/9/15 13:36
@desc:
"""
from interfaces_in_multiple_env import env_demo


class TestApi:
    data = {
        "method": "get",
        "url": "http://testing-studio:9999/demo1.text",
        "headers": None
    }

    def test_send(self):
        api = env_demo.Api()
        print(api.send(self.data).text)
