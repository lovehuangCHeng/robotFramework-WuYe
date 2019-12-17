*** Settings ***
Library           Selenium2Library    timeout=15
Resource          ../../通用方法.robot
Variables         ../../../config/elements/财务管理/月报表Xpath.py

*** Keywords ***
收入月度分摊_资源树筛选
    等待element元素可见    ${收入月度分摊_资源树搜索框}
    sleep    0.5
    Input Text    ${收入月度分摊_资源树搜索框}    123
    sleep    5

收入月度分摊_按年度月份筛选
    数据库查询操作    ${guanliquID}
    sleep    0.5
    等待element元素可见    //li[@id='${var[0][0]}']/a
    sleep    0.5
    #选中管理区
    click element    //li[@id='${var[0][0]}']/a
    sleep    0.5
    click element    ${收入月度分摊_选择年份下拉框}
    sleep    0.5
    click element    ${收入月度分摊_选择年份}
    sleep    0.5
    click element    ${收入月度分摊_选择月份}
    sleep    0.5
    click button    ${收入月度分摊_搜索按钮}
    sleep    3

收入月度分摊_导出汇总
    数据库查询操作    ${guanliquID}
    sleep    0.5
    等待element元素可见    //li[@id='${var[0][0]}']/a
    sleep    0.5
    #选中管理区
    click element    //li[@id='${var[0][0]}']/a
    sleep    0.5
    click button    ${收入月度分摊_搜索按钮}
    等待元素可用    ${收入月度分摊_导出汇总按钮}
    sleep    0.5
    click button    ${收入月度分摊_导出汇总按钮}

收入月度分摊_导出明细
    数据库查询操作    ${guanliquID}
    sleep    0.5
    等待element元素可见    //li[@id='${var[0][0]}']/a
    sleep    0.5
    #选中管理区
    click element    //li[@id='${var[0][0]}']/a
    sleep    0.5
    click button    ${收入月度分摊_搜索按钮}
    等待element元素可见    ${收入月度分摊_点击本期收往期非0金额}
    sleep    0.5
    click element    ${收入月度分摊_点击本期收往期非0金额}
    sleep    0.5
    等待元素可用    ${收入月度分摊_导出明细按钮}
    sleep    0.5
    click button    ${收入月度分摊_导出明细按钮}

收入月度分摊_点击金额查看明细
    数据库查询操作    ${guanliquID}
    sleep    0.5
    等待element元素可见    //li[@id='${var[0][0]}']/a
    sleep    0.5
    #选中管理区
    click element    //li[@id='${var[0][0]}']/a
    sleep    0.5
    click button    ${收入月度分摊_搜索按钮}
    等待element元素可见    ${收入月度分摊_点击本期收往期非0金额}
    sleep    0.5
    click element    ${收入月度分摊_点击本期收往期非0金额}

收入月度分摊_查看资源详情
    数据库查询操作    ${guanliquID}
    sleep    0.5
    等待element元素可见    //li[@id='${var[0][0]}']/a
    sleep    0.5
    #选中管理区
    click element    //li[@id='${var[0][0]}']/a
    sleep    0.5
    click button    ${收入月度分摊_搜索按钮}
    sleep    0.5
    等待element元素可见    ${收入月度分摊_点击本期收往期非0金额}
    sleep    0.5
    click element    ${收入月度分摊_点击本期收往期非0金额}
    sleep    3
    click element    ${收入月度分摊_查看资源代码详情}
    sleep    2
    断言存在    ${收入月度分摊_资源详情页面}

收入月度分摊_查看客户详情
    数据库查询操作    ${guanliquID}
    sleep    0.5
    等待element元素可见    //li[@id='${var[0][0]}']/a
    sleep    0.5
    #选中管理区
    click element    //li[@id='${var[0][0]}']/a
    sleep    0.5
    click button    ${收入月度分摊_搜索按钮}
    sleep    0.5
    等待element元素可见    ${收入月度分摊_点击本期收往期非0金额}
    sleep    0.5
    click element    ${收入月度分摊_点击本期收往期非0金额}
    sleep    3
    click element    ${收入月度分摊_查看客户详情}
    sleep    2
    断言存在    ${收入月度分摊_客户详情页面客户名称}
