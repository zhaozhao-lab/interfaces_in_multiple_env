#!/usr/bin/env python
# encoding: utf-8
"""
@author:ZhaoLong
@contact: 1452885022@qq.com
@software: Laka
@file: test_yaml.py
@time: 2021/9/15 14:44
@desc:
"""
import yaml
def test_yaml():
    env = {
        "default": "dev",
        "testing-studio": {
            "dev": "127.0.0.1",
            "test": "127.0.0.2"
        }

    }
    with open("env.yaml", "w") as f:
        yaml.safe_dump(data=env, stream=f)