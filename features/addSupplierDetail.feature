# Created by chenj at 2024/11/27
Feature: 新增经销商
  # Enter feature description here

  Scenario: 成功增加经销商
    # Enter steps here
    Given 前置条件
    When 管理员用户请求 POST /supplierData/addSupplierDetail Body './成功增加经销商.json'
    Then 数据库中增加经销商数据
