*** Settings ***
Library           Selenium2Library    timeout=15
Resource          ../../通用方法.robot
Variables         ../../../config/elements/财务管理/年度报表Xpath.py

*** Keywords ***
欠费年度统计_按应收时间段查询
    等待element元素可见    ${欠费年度统计_应收时间段选择框}
    sleep    0.5
    click element    ${欠费年度统计_应收时间段选择框}
    sleep    0.5
    click element    ${欠费年度统计_应收时间段选择上个月}
    sleep    5

欠费年度统计_汇总到楼宇
    等待element元素可见    ${欠费年度统计_应收时间段选择框}
    sleep    0.5
    click element    ${欠费年度统计_应收时间段选择框}
    sleep    0.5
    click element    ${欠费年度统计_应收时间段选择上个月}
    sleep    0.5
    click element    ${欠费年度统计_汇总到楼宇勾选框}
    sleep    2
    click element    ${欠费年度统计_所有管理区展开}
    sleep    0.5
    click element    ${欠费年度统计_所有楼宇展开}

欠费年度统计_汇总到收费项目
    等待element元素可见    ${欠费年度统计_应收时间段选择框}
    sleep    0.5
    click element    ${欠费年度统计_应收时间段选择框}
    sleep    0.5
    click element    ${欠费年度统计_应收时间段选择上个月}
    sleep    0.5
    click element    ${欠费年度统计_汇总到收费项目勾选框}
    sleep    2
    click element    ${欠费年度统计_所有月份展开}
    sleep    0.5
    click element    ${欠费年度统计_所有月份展开}
    sleep    0.5
    click element    ${欠费年度统计_所有项目展开}
    sleep    3

欠费年度统计_导出年汇总
    等待元素可用    ${欠费年度统计_导出年汇总按钮}
    sleep    0.5
    click button    ${欠费年度统计_导出年汇总按钮}
    sleep    3

欠费年度统计_导出年欠费详情
    等待元素可用    ${欠费年度统计_导出年欠费详情按钮}
    sleep    0.5
    click button    ${欠费年度统计_导出年欠费详情按钮}
    sleep    3

欠费年度统计_点击金额跳转
    等待element元素可见    ${欠费年度统计_应收时间段选择框}
    sleep    0.5
    click element    ${欠费年度统计_汇总到楼宇勾选框}
    sleep    0.5
    click element    ${欠费年度统计_所有管理区展开}
    sleep    0.5
    click element    ${欠费年度统计_所有楼宇展开}
    sleep    0.5
    等待element元素可见    ${欠费年度统计_一个列表金额}
    sleep    0.5
    click element    ${欠费年度统计_一个列表金额}
    sleep    1
    等待element元素可见    ${欠费年度统计_跳转页面title验证}
    sleep    1
    断言值包含    ${欠费年度统计_跳转页面title验证}		欠费月度统计


