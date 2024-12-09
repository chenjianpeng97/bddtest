# Created by chenj at 2024/11/27
Feature: 获取医院主数据列表
  POST /hospital/list

  Background:
    Given 系统已知医院列表"初始化医院主数据列表.sql"
    And 默认payload {"hospitalName": "","hospitalCode": "","province": "","city": "","pageNum": 1,"pageSize": 10}

  @happy_path@P0
  Scenario: 成功获取医院主数据列表
    When 请求 POST /hospital/list payload {"hospitalName": "","hospitalCode": "","province": "","city": "","pageNum": 1,"pageSize": 10}
    Then 状态码:200
    And 返回值JSON数据:"成功获取医院主数据列表.json"

  @pagination@P1
  Scenario Outline: 分页查询医院数据
    When 请求 POST /hospital/list payload <分页策略>
    Then 状态码:200
    And 返回JSON断言:"<返回JSON>"
    Examples: 正向分页使用
      | 分页策略                         | 返回JSON                              |
      | {"pageNum": 1,"pageSize": 3} | $.data[2].hospitalName == "深圳市人民医院" |
      | {"pageNum": 2,"pageSize": 3} | $.data[2].hospitalName ==  "仁爱妇产医院" |
    Examples: 分页大小*分页超出数据总数
      | 分页策略                          | 返回JSON            |
      | {"pageNum": 3,"pageSize": 10} | $.data[0] == None |

  @search@P2
  Scenario Outline: 根据条件查询医院数据
    When 请求 POST /hospital/list payload <搜索条件>
    Then 状态码:200
    And 返回JSON断言:"<返回JSON>"
    Examples: 单条件搜索
      | 搜索条件                         | 返回JSON                                                           |
      | {"hospitalName": "深圳市人民医院"}  | $.data[0].HospitalName == "深圳市人民医院" and $.data.length() == 1     |
      | {"hospitalCode": "H004"}     | $.data[0].HospitalName == "广州中医药大学附属医院" and $.data.length() == 1 |
      | {"province": "广东"}           | $.data.length() == 2                                             |
      | {"city":"上海"}                | $.data.length() == 2                                             |
      | {"hospitalName": "不存在的医院名称"} | $.data.length() == 0                                             |
    Examples: 组合条件搜索
      | 搜索条件                                                          | 返回JSON                                                       |
      | {"province": "广东","city":"深圳市"}                               | $.data[0].HospitalName == "深圳市人民医院" and $.data.length() == 1 |
      | {"hospitalName":"广州中医药大学附属医院","province": "广东省","city":"深圳市"} | $.data.length() == 0                                         |

  @robustness@P3
  Scenario Outline: 传参异常情况
    When 请求 POST /hospital/list payload <传参>
    Then 返回状态码!= 200
    Examples: 必填参数缺失
      | 传参                                                                               |
      | {"hospitalName": "","hospitalCode": "","province": "","city": "","pageSize": 10} |
      | {"hospitalName": "","hospitalCode": "","city": "","pageNum": 1}                  |
    Examples: 参数类型错误
      | 传参                                                                                              |
      | {"hospitalName": "","hospitalCode": "","province": "","city": "","pageNum": "1","pageSize": 10} |
      | {"hospitalName": "","hospitalCode": "","province": "","city": "","pageNum": 1,"pageSize": "10"} |
    Examples: 参数传数值错误
      | 传参                                                                                            |
      | {"hospitalName": "","hospitalCode": "","province": "","city": "","pageNum": -1,"pageSize": 1} |
      | {"hospitalName": "","hospitalCode": "","province": "","city": "","pageNum": 1,"pageSize": 0}  |
