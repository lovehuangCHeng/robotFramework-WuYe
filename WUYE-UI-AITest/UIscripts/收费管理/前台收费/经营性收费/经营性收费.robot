*** Settings ***
Variables         ../../../../config/geturl.py
Resource          ../../../通用方法.robot
Resource          经营性收费—resource.txt
Library           Selenium2Library    timeout=20
Library           BuiltIn

*** Test Cases ***
数据查询
    数据查询

经营性收费
    登录    ${经营性收费}
    进入iframe
    经营性收费
    sleep    3
    [Teardown]    关闭浏览器

新增客户
    登录    ${经营性收费}
    进入iframe
    新增客户
    sleep    3
    [Teardown]    关闭浏览器
