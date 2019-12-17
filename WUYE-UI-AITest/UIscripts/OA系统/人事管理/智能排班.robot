*** Settings ***
Resource          智能排班方法.robot
Resource          ../../通用方法.robot

*** Test Cases ***
新建仪表类型
    登录    ${仪表类型}
    新建仪表类型    家庭用水表    吨
    [Teardown]    关闭浏览器