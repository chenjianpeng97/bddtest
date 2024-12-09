# 框架功能描述

## 接口测试

### payload为json格式时

* 可设置默认json数据

```gherkin
Background:
Given 默认payload {"hospitalName": "","hospitalCode": "","province": "","city": "","pageNum": 1,"pageSize": 10}
```

默认payload
本Feature下的所有接口以此标准payload为基础

* 使用默认json减少用例编写量

```gherkin
请求 POST /hospital/list payload {"hospitalName": DROP,"pageNum": 2,"pageSize": 20,"extra": "extra"}
```

实际发送的payload json中,编辑默认json的pageNum,pageSize字段,新增extra字段,删除hospitalName字段

### 接口返回值校验

* 支持直接写JsonPath表达式进行校验

```gherkin
Then 响应状态码为 200
And 返回JSON断言:'$.data[2].hospitalName == "深圳市人民医院" and $.data[1].hospitalName == "仁爱妇产医院"'
```

支持断言jsonpath对象逻辑运算：==,!=,>,>=,<,<=
支持断言结果布尔运算：and,or
