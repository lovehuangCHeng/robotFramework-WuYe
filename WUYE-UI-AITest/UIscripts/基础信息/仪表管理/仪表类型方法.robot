*** Settings ***
Variables         ../../../config/elements/基础信息/仪表管理.py
Library           Selenium2Library

*** Keywords ***
新建仪表类型
    [Arguments]    ${name}    ${unit}
    Click Element    ${仪表类型新增}
    sleep    2
    Input Text    ${仪表类型名称}    ${name}
    sleep    2
    Input Text    ${计量单位}    ${unit}
    sleep    2
    Click Element    ${仪表类型保存}
    sleep    2

仪表类型编辑
    Click Element    ${仪表类型列表数据}
    sleep    2
    Click Element    ${仪表类型编辑}
    sleep    2
    Click Element    ${仪表类型保存}
    sleep    2

仪表类型搜索
    [Arguments]    ${name}
    Input Text    ${仪表类型搜索框}    ${name}
    sleep    2
    Click Element    ${仪表类型搜索按钮}
    sleep    2

仪表类型删除
    Click Element    ${仪表类型列表数据}
    sleep    2
    Click Element    ${仪表类型删除}
    sleep    2
    Click Element    ${仪表类型确认删除}
    sleep    2

仪表类型高级搜索
    [Arguments]    ${name}
    Click Element    ${仪表类型高级搜索}
    sleep    2
    Input Text    ${仪表类型名称高}    ${name}
    sleep    2
    Click Element    ${仪表类型高级搜索按钮}
    sleep    2
