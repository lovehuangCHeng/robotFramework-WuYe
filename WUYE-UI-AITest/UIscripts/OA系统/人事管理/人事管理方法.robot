*** Settings ***
Library           Selenium2Library
Variables         ../../../config/elements/OA系统/活动人事.py
Resource          ../../通用方法.robot

*** Keywords ***
房间仪表新建
    [Arguments]    ${name}
    Click Element    ${房间仪表新增}
    sleep    4
    Click Element    ${房间仪表房间}
    sleep    2
    Click Element    ${房间仪表列表数据}
    sleep    2
    Click Element    ${房间仪表房间列表确定}
    sleep    2
    Click Element    ${房间仪表类型}
    sleep    2
    Click Element    ${房间仪表类型数据}
    sleep    2
    Input Text    ${房间仪表名称}    ${name}
    sleep    2
    Input Text    ${房间仪表初始读数}    0
    sleep    2
    Input Text    ${房间仪表倍率}    1
    sleep    2
    Input Text    ${房间仪表最大读数}    9999
    sleep    2
    Click Element    ${房间仪表初始日期}
    sleep    2
    等待element元素可见    ${房间仪表选择日期}
    sleep    2
    Click Element    ${房间仪表选择日期}
    sleep    2
    Click Element    ${房间仪表保存}
    sleep    2
