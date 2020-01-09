*** Settings ***
Library           Selenium2Library
Variables         ../../../config/elements/基础信息/客户管理.py

*** Keywords ***
新建客户数据
    [Arguments]    ${name}    ${phoneNum}
    sleep    2
    Click Element    ${客户新建}
    sleep	    2
    Input Text    ${客户名称}    ${name}
    sleep    2
    Click Element    ${选择管理区}
    sleep    2
    Click Element    ${管理区数据}
    sleep    2
    Input Text    ${电话号码}    ${phoneNum}
    sleep    2
    Click Element    ${客户档案保存}
    sleep    2

查询客户数据
    [Arguments]    ${name}
    Input Text    ${客户档案搜索框}    ${name}
    sleep    2
    Click Element    ${客户档案搜索按钮}
    sleep    2

客户数据高级搜索
    [Arguments]    ${name}
    Click Element    ${客户向下展开按钮}
    Click Element    ${选择管理区}
    sleep    2
    Input Text    ${客户名称}    ${name}
    sleep    2
    Click Element    ${高级搜索按钮}
    sleep    2

编辑客户档案
    Click Element    ${表格中管理区数据}
    sleep    2
    Click Element    ${客户编辑}
    sleep    2
    Click Element    ${客户档案保存}
    sleep    2

合并重名客户
    Click Element    ${合并重名客户}
    sleep    2
    Click Element    ${关闭合并同名客户}
    sleep    2

删除新建客户
    Click Element    ${客户档案列表名称}
    sleep    2
    Click Element    ${客户删除}
    sleep    2
    Click Element    ${确认删除按钮}
    sleep    2
	
新建业主委员会
	Click Element    ${新增成员}
    sleep    2
	Click Element    ${委员会取消}
    sleep    2
	
查询业主委员会
	Click Element    ${委员会选择管理区}
    sleep    2
	Click Element    ${委员会管理区数据}
    sleep    2

iframr 切换
    Select Frame    id=wuYeIframe
    sleep    2
	
	
	
	
