*** Settings ***
Library           Selenium2Library    timeout=25
Resource          ../../通用方法.robot
Variables         ../../../config/elements/财务管理/费用报表Xpath.py

*** Keywords ***
往年收欠率表_搜索
    等待element元素可见    ${往年收欠率表_截止日期}
    sleep    0.5
    click element    ${往年收欠率表_截止日期}
    sleep    0.5
    click element    ${往年收欠率表_选择开始日期}
    sleep    0.5
    click element    ${往年收欠率表_选择截止日期}
    sleep    0.5
    click element    ${往年收欠率表_管理区}
    sleep    0.5
    搜索输入中的管理区
    sleep    0.5
    click element    ${往年收欠率表_收费项目}
    sleep    0.5
    click element    ${往年收欠率表_选择收费项目}
    sleep    0.5
    click button    ${往年收欠率表_搜索}
    sleep    0.5
    等待element元素可见    ${往年收欠率表_表格}
    sleep    0.5
    等待元素可用    ${往年收欠率表_重置}
    sleep    0.5
    click button    ${往年收欠率表_重置}
    sleep    2

往年收欠率表_导出
    等待element元素可见    ${往年收欠率表_截止日期}
    sleep    0.5
    click element    ${往年收欠率表_截止日期}
    sleep    0.5
    click element    ${往年收欠率表_选择截止日期}
    sleep    0.5
    click element    ${往年收欠率表_管理区}
    sleep    0.5
    搜索输入中的管理区
    sleep    0.5
    click button    ${往年收欠率表_搜索}
    sleep    0.5
    等待元素可用    ${往年收欠率表_导出}
    sleep    0.5
    click button    ${往年收欠率表_导出}
    sleep    2

搜索输入中的管理区
    数据库查询操作    ${fenGongSiName}
    sleep    0.5
    等待element元素可见    //span[text()='${var[0][0]}']/../../span[1]
    sleep    0.5
    #选中分公司
    click element    //span[text()='${var[0][0]}']/../../span[1]
    sleep    0.5
    数据库查询操作    ${guanliqu}
    sleep    0.5
    等待element元素可见    //span[text()='${var[0][0]}']
    sleep    0.5
    #选中管理区
    click element    //span[text()='${var[0][0]}']
    sleep    0.5

查询分公司是否存在
    [Arguments]    ${var}
    等待element元素可见    //span[text()='${var}']/../../span[1]
    sleep    0.5
    #选中分公司
    click element    //span[text()='${var}']/../../span[1]
    sleep    0.5
    [Teardown]
