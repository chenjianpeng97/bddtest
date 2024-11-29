#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Tuner
@contact:chenjianpeng97@outlook.com
@version: 1.0.0
@license: Apache Licence
@file: db_steps.py
@time: 2024/11/28 19:28
"""
from behave import given, when, then
from common.settings import TESTDATA_SQLS_DIR
import os


@given('系统已知医院列表"{sql_file}"')
def step_impl(context, sql_file: str):
    context.db.execute_sql_file(sql_file)
    pass


if __name__ == '__main__':
    pass
