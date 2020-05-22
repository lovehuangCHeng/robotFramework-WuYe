*** Settings ***
Variables         ../../../../config/geturl.py
Resource          ../../../通用方法.robot
Resource          房间仪表抄表-resource.txt
Library           Selenium2Library

*** Test Cases ***
抄表进度概况
    登录    ${房间仪表抄表}
    进入iframe
    抄表进度概况
    [Teardown]    关闭浏览器

抄表进度明细(抄表)
    登录    ${房间仪表抄表}
    进入iframe
    抄表进度明细(抄表)
    [Teardown]    关闭浏览器

抄表历史记录
    登录    ${房间仪表抄表}
    进入iframe
    抄表历史记录
    [Teardown]    关闭浏览器
