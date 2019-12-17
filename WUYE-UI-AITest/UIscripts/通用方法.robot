*** Settings ***
Library           Selenium2Library    implicit_wait=60
Library           DatabaseLibrary
Variables         ../config/sql.py
Variables         ../config/geturl.py
Variables         ../config/basicConfig.py
Library           DateTime

*** Keywords ***
登录
    [Arguments]    ${testurl}
    Open Browser    ${basicURL}    chrome
    Maximize Browser Window
    sleep    1
    input text    name=UserName    ${账号}
    sleep    1
    input text    name=Password    ${密码}
    sleep    1
    Click Button    Xpath=//input[@type='submit']
    sleep    2
    Go To    ${testurl}
    sleep    2

关闭浏览器
    Close Browser

数据库查询操作
    [Arguments]    ${sqlselect}
    Connect To Database Using Custom Params    pyodbc    ${sqlconfig}
    ${var}    Query    ${sqlselect}
    Set Global Variable    ${var}
    Disconnect From Database
    [Return]    ${var}

二次确认
    sleep    2
    Click Button    //button[@class='ant-btn ant-btn-primary ant-btn-sm']

搜索框内置搜索按钮
    Click Element    //span[@class='ant-input-suffix']

断言存在
    [Arguments]    ${var}
    should not be empty    ${var}

断言不存在
    [Arguments]    ${var}
    should be empty    ${var}

断言值等于
    [Arguments]    ${var}    ${i}
    should be equal    ${var}    ${i}

断言值不等于
    [Arguments]    ${var}    ${i}
    should not be equal    ${var}    ${i}

进入iframe
    Select Frame    id=wuYeIframe

退出iframe
    Unselect Frame

断言值包含
    [Arguments]    ${var}    ${i}
    should contain    ${var}    ${i}

等待element元素可见
    [Arguments]    ${var}
    Wait Until Element Is Visible    ${var}    timeout=20

弹出窗确认选项
    Alert Should Be Present

等待button元素可见
    [Arguments]    ${var}
    Wait Until Element Is Enabled    ${var}    timeout=20

等待元素可用
    [Arguments]    ${var}
    Wait Until Element Is Enabled    ${var}

获取元素文本
    [Arguments]    ${locator}
    ${text}    get text    ${locator}
    [Return]    ${text}

获取当前年月日
    ${date}    Get Current Date    result_format=%Y-%m-%d
    [Return]    ${date}

获取一年前的年月日
    ${date}    Get Current Date    result_format=%Y-%m-%d
    ${date2}    Add Time To Date    ${date}    -365days    result_format=%Y-%m-%d
    [Return]    ${date2}
