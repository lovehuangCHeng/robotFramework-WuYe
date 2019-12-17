*** Settings ***
Resource          活动方法.robot
Resource          ../../通用方法.robot

*** Test Cases ***
新建活动
    登录    ${活动列表}
    活动新建    4    1    1    1
    [Teardown]    关闭浏览器
