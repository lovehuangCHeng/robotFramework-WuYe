*** Settings ***
Variables         ../../../../config/geturl.py
Resource          ../../../通用方法.robot
Resource          收费历史记录—resource.txt
Library           Selenium2Library    timeout=20
Library           BuiltIn

*** Test Cases ***
已打印票据号变更
    数据查询    ${GetBillPT1P0}
    Run Keyword If    "${var}"!="[]"    赋值    ${var}
    ...    ELSE    LOG    不存在这样的数据
    sleep    2
    log    ${Skehu}
    log    ${Sregion}
    Run Keyword If    "${var}"!="[]"    登录    ${收费历史记录}
    ...    ELSE    LOG    X    错误原因：无数据请手动执行用例
    进入iframe
    已打印票据更改票据号
    [Teardown]    关闭浏览器

已打印票据号补打、重打
    数据查询    ${GetBillPT1P0}
    Run Keyword If    "${var}"!="[]"    赋值    ${var}
    ...    ELSE    LOG    不存在这样的数据
    sleep    2
    log    ${Skehu}
    log    ${Sregion}
    登录    ${收费历史记录}
    进入iframe
    Run Keyword If    "${var}"!="[]"    已打印票据补打、作废并重打
    ...    ELSE    LOG    X    错误原因：无数据请手动执行用例
    [Teardown]    关闭浏览器

已打印票据回收、不回收票据撤销、多次撤销
    数据查询    ${GetBillPT1P0}
    Run Keyword If    "${var}"!="[]"    赋值    ${var}
    ...    ELSE    LOG    不存在这样的数据
    sleep    2
    log    ${Skehu}
    log    ${Sregion}
    登录    ${收费历史记录}
    进入iframe
    Run Keyword If    "${var}"!="[]"    已打印票据回收、不回收票据撤销、多次撤销
    ...    ELSE    LOG    X    错误原因：无数据请手动执行用例
    [Teardown]    关闭浏览器

按房间、车位搜索历史
    数据查询    ${GetBillPT0P0}
    Run Keyword If    "${var}"!="[]"    赋值    ${var}
    ...    ELSE    LOG    不存在这样的数据
    sleep    2
    log    ${Skehu}
    log    ${Sregion}
    登录    ${收费历史记录}
    进入iframe
    Run Keyword If    "${var}"!="[]"    按房间、车位搜索历史
    ...    ELSE    LOG    X    错误原因：无数据请手动执行用例
    [Teardown]    关闭浏览器

按票据号搜索历史
    登录    ${收费历史记录}
    进入iframe
    按票据号搜索历史
    [Teardown]    关闭浏览器

未打印票据撤销收费不回收票据
    数据查询    ${GetBillPT0P0}
    Run Keyword If    "${var}"!="[]"    赋值    ${var}
    ...    ELSE    LOG    不存在这样的数据
    sleep    2
    登录    ${收费历史记录}
    进入iframe
    Run Keyword If    "${var}"!="[]"    未打印票据撤销收费不回收票据
    ...    ELSE    LOG    X    错误原因：无对应数据请手动执行用例
    [Teardown]    关闭浏览器

未打印票据撤销收费回收票据
    数据查询    ${GetBillPT0P0}
    Run Keyword If    "${var}"!="[]"    赋值    ${var}
    ...    ELSE    LOG    不存在这样的数据
    sleep    2
    登录    ${收费历史记录}
    进入iframe
    Run Keyword If    "${var}"!="[]"    未打印票据撤销收费回收票据
    ...    ELSE    LOG    X    错误原因：无对应数据请手动执行用例
    [Teardown]    关闭浏览器

已退款票据撤销收费回收票据
    数据查询    ${GetBillPT2P0}
    Run Keyword If    "${var}"!="[]"    赋值    ${var}
    ...    ELSE    LOG    不存在这样的数据
    sleep    2
    log    ${Skehu}
    log    ${Sregion}
    登录    ${收费历史记录}
    进入iframe
    Run Keyword If    "${var}"!="[]"    已退款票据撤销收费回收票据
    ...    ELSE    LOG    X    错误原因：无数据请手动执行用例
    [Teardown]    关闭浏览器
