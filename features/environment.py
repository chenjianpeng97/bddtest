#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Tuner
@contact:chenjianpeng97@outlook.com
@version: 1.0.0
@license: Apache Licence
@file: environment.py.py
@time: 2024/11/27 15:49
"""
from behave import fixture, use_fixture
from common.settings import *
from common.sql.sql_handler import SQLHandler


def before_all(context):
    # 连接数据库
    context.db = SQLHandler()
    context.db.create_cursor()
    pass


def before_feature(context, feature):
    pass


def before_scenario(context, scenario):
    pass


def before_step(context, step):
    pass


def after_step(context, step):
    pass


def after_scenario(context, scenario):
    pass


def after_feature(context, feature):
    pass


def after_all(context):
    # 初始化测试库
    context.db.execute_sql_file("初始化测试环境库.sql")
    # 关闭释放数据库连接
    context.db.close()
    pass


if __name__ == '__main__':
    pass
