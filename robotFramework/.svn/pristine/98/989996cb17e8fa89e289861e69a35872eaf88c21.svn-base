*** Settings ***
Variables         ../../../../config/geturl.py
Resource          ../../../通用方法.robot
Resource          客户零头账户—resource.txt
Library           Selenium2Library    timeout=20
Library           BuiltIn

*** Test Cases ***
数据查询
    数据查询

查询零头账户明细
    登录    ${客户零头账户}
    进入iframe
    查询零头账户
    sleep    3
    [Teardown]    关闭浏览器
