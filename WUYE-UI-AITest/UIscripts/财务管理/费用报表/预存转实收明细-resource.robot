*** Settings ***
Library           Selenium2Library    timeout=15
Resource          ../../通用方法.robot
Variables         ../../../config/elements/财务管理/费用报表Xpath.py

*** Keywords ***
预存转实收明细_资源树搜索
    等待element元素可见    ${预存转实收明细_资源树搜索框}
    sleep    0.5
    input text    ${预存转实收明细_资源树搜索框}    123
    sleep    3

预存转实收明细_搜索
    数据库查询操作    ${guanliquID}
    sleep    0.5
    等待element元素可见    //li[@id='${var[0][0]}']/a
    sleep    0.5
    #选中管理区
    click element    //li[@id='${var[0][0]}']/a
    sleep    0.5
    等待element元素可见    ${预存转实收明细_核销时间开始日期}
    sleep    0.5
    input text    ${预存转实收明细_核销时间开始日期}    2019-01-01
    sleep    0.5
    input text    ${预存转实收明细_核销时间结束日期}    2019-12-31
    sleep    0.5
    click element    ${预存转实收明细_只显示本月费用}
    sleep    0.5
    等待element元素可见    ${预存转实收明细_表格}
    sleep    3

预存转实收明细_导出
    数据库查询操作    ${guanliquID}
    sleep    0.5
    等待element元素可见    //li[@id='${var[0][0]}']/a
    sleep    0.5
    #选中管理区
    click element    //li[@id='${var[0][0]}']/a
    sleep    0.5
    断言存在    ${预存转实收明细_导出}
