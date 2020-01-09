*** Settings ***
Variables         ../../../config/elements/租赁管理/合同列表Xpath.py
Library           Selenium2Library
Resource          ../../通用方法.robot

*** Keywords ***
新建合同
    ${Cname}    按时间自定义变量    UI合同
    Set Suite Variable    ${Cname}
    等待element元素可见    ${新建合同按钮}
    Click Button    ${新建合同按钮}
    sleep    3
    等待element元素可见    ${选择管理区下拉按钮 }
    Click element    ${选择管理区下拉按钮 }
    等待element元素可见    ${下拉选择第一个管理区 }
    sleep    3
    Click element    ${下拉选择第一个管理区}
    sleep    3
    Click element    ${选择租户下拉按钮}
    sleep    3
    Click element    ${下拉选择第一个租户}
    sleep    3
    input text    ${合同编号输入框}    ${Cname}
    sleep    3
    input text    ${合同名称输入框}    ${Cname}
    sleep    3
    input text    ${合同备注输入框}    ${Cname}
    sleep    3
    等待element元素可见    ${添加房间按钮}
    sleep    3
    Click Button    ${添加房间按钮}
    sleep    3
    Click element    ${楼栋下拉按钮}
    sleep    3
    Click element    ${楼栋下拉选择房间}
    sleep    3
    Click Button    ${确认添加房间}
    sleep    3
    Click Button    ${合同下一步按钮}
    等待element元素可见    ${合同规则添加按钮}
    sleep    3
    Click Button    ${合同规则添加按钮}
    sleep    3
    input text    ${保证金额输入}    100
    sleep    3
    Click Button    ${合同规则添加按钮}
    sleep    3
    Click element    ${减免标准下拉}
    sleep    3
    Click element    ${选择减免标准}
    sleep    3
    Click element    ${选择减免周期}
    sleep    3
    等待element元素可见    ${选择减免日期开始}
    Click element    ${选择减免日期开始}
    sleep    3
    Click element    ${选择减免日期结束}
    sleep    3
    Click Button    ${生成账单按钮保存}
    sleep    3
    等待element元素可见    ${生成账单按钮保存}
    Click Button    ${生成账单按钮保存}
    sleep    3
    等待element元素可见    ${核对账单保存}
    Click Button    ${核对账单保存}
    sleep    3

普通搜索
    [Arguments]    ${fiteri}
    等待element元素可见    ${搜索合同输入框}
    sleep    3
    input text    ${搜索合同输入框}    ${fiteri}
    等待element元素可见    ${搜索结果断言}
    sleep    2
    click element    ${搜索结果断言}

高级搜索
    [Arguments]    ${fitername}    ${fiterid}
    等待element元素可见    ${搜索合同输入框}
    sleep    3
    click button    ${高级搜索展开按钮}
    等待element元素可见    ${搜索合同编号输入框}
    input text    ${搜索合同编号输入框}    ${fiterid}
    input text    ${搜索合同名称输入框}    ${fitername}
    sleep    1
    click button    ${高级搜索按钮}
    等待element元素可见    ${搜索结果断言}
    sleep    2
    click element    ${搜索结果断言}

合同变更
    等待element元素可见    ${合同变更按钮}
    Click Button    ${合同变更按钮}
    sleep    3
    input text    ${合同备注输入框}    变更合同
    sleep    3
    Click Button    ${合同下一步按钮}
    等待element元素可见    ${保证金额输入}
    sleep    3
    input text    ${保证金额输入}    200
    sleep    3
    Click Button    ${生成账单按钮保存}
    sleep    3
    等待element元素可见    ${生成账单按钮保存}
    Click Button    ${生成账单按钮保存}
    等待element元素可见    ${核对账单保存}
    sleep    3
    Click Button    ${核对账单保存}
    sleep    3

获取合同名称
