*** Settings ***
Library           Selenium2Library    timeout=15
Resource          ../../通用方法.robot
Variables         ../../../config/elements/系统管理/系统管理Xpath.py

*** Keywords ***
新建用户
    等待element元素可见    ${新建用户按钮}
    sleep    0.5
    click button    ${新建用户按钮}
    等待element元素可见    ${用户名称输入框}
    sleep    0.5
    Input Text    ${用户名称输入框}    RF用户名称
    sleep    0.5
    Input Text    ${用户电话输入框}    RF用户备注
    sleep    0.5
    click button    ${新建编辑用户保存按钮}

搜索用户
    等待element元素可见    ${简单搜索用户输入框}
    sleep    0.5
    Input Text    ${简单搜索用户输入框}    RF
    sleep    0.5
    click button    ${简单搜索用户按钮}

编辑用户
    等待element元素可见    ${一条用户数据}
    sleep    0.5
    click element    ${一条用户数据}
    sleep    0.5
    click button    ${编辑用户按钮}
    等待element元素可见    ${用户名称输入框}
    sleep    0.5
    Input Text    ${用户名称输入框}    RF用户名称1
    sleep    0.5
    Input Text    ${用户电话输入框}    RF用户备注1
    sleep    0.5
    click button    ${新建编辑用户保存按钮}

禁用用户
    等待element元素可见    ${显示下拉框}
    sleep    0.5
    mouse over    ${显示下拉框}
    sleep    0.5
    click element    ${显示启用}
    等待element元素可见    ${一条用户数据}
    sleep    1
    click element    ${一条用户数据}
    sleep    0.5
    click button    ${禁用用户按钮}

启用用户
    等待element元素可见    ${显示下拉框}
    sleep    0.5
    mouse over    ${显示下拉框}
    sleep    0.5
    click element    ${显示禁用}
    等待element元素可见    ${一条用户数据}
    sleep    0.5
    click element    ${一条用户数据}
    sleep    0.5
    click button    ${启用用户按钮}

显示禁用用户
    等待element元素可见    ${显示下拉框}
    sleep    0.5
    mouse over    ${显示下拉框}
    sleep    0.5
    click element    ${显示禁用}
    sleep    1

显示启用用户
    等待element元素可见    ${显示下拉框}
    sleep    0.5
    mouse over    ${显示下拉框}
    sleep    0.5
    click element    ${显示启用}
    sleep    1

下载用户导入模板
    等待element元素可见    ${显示下拉框}
    sleep    0.5
    mouse over    ${导入用户下拉框}
    sleep    0.5
    click element    ${下载导入用户模板}
    sleep    1

高级搜索用户
    等待element元素可见    ${高级搜索展开框}
    sleep    0.5
    click element    ${高级搜索展开框}
    sleep    0.5
    Input Text    ${用户名称输入框}    RF
    sleep    0.5
    click button    ${用户高级搜索按钮}

组织机构添加职员
    等待element元素可见    ${职员组织机构Tab}
    sleep    0.5
    click element    ${职员组织机构Tab}
    等待element元素可见    ${职员组织机构_选择左侧组织架构}
    sleep    0.5
    click element    ${职员组织机构_选择左侧组织架构}
    sleep    0.5
    click button    ${选择职员按钮}
    等待element元素可见    ${选择一个职员添加}
    sleep    0.5
    click element    ${选择一个职员添加}
    sleep    0.5
    click button    ${添加员工保存按钮}

组织机构移除职员
    等待element元素可见    ${职员组织机构Tab}
    sleep    0.5
    click element    ${职员组织机构Tab}
    等待element元素可见    ${职员组织机构_选择左侧组织架构}
    sleep    0.5
    click element    ${职员组织机构_选择左侧组织架构}
    sleep    0.5
    等待element元素可见    ${选择一个职员移除}
    sleep    0.5
    click element    ${选择一个职员移除}
    sleep    0.5
    click button    ${移除职员按钮}

岗位添加职员
    等待element元素可见    ${职员岗位Tab}
    sleep    0.5
    click element    ${职员岗位Tab}
    等待element元素可见    ${职员岗位_选择左侧组织架构}
    sleep    0.5
    click element    ${职员岗位_选择左侧组织架构}
    sleep    0.5
    click button    ${选择职员按钮}
    sleep    0.5
    等待element元素可见    ${选择一个职员添加}
    sleep    0.5
    click element    ${选择一个职员添加}
    sleep    0.5
    click button    ${添加员工保存按钮}

岗位移除职员
    等待element元素可见    ${职员岗位Tab}
    sleep    0.5
    click element    ${职员岗位Tab}
    等待element元素可见    ${职员岗位_选择左侧组织架构}
    sleep    0.5
    click element    ${职员岗位_选择左侧组织架构}
    sleep    0.5
    等待element元素可见    ${选择一个职员移除}
    sleep    0.5
    click element    ${选择一个职员移除}
    sleep    0.5
    click button    ${移除职员按钮}

删除用户
    等待element元素可见    ${简单搜索用户输入框}
    sleep    0.5
    Input Text    ${简单搜索用户输入框}    RF
    sleep    0.5
    click button    ${简单搜索用户按钮}
    等待element元素可见    ${一条用户数据}
    sleep    0.5
    click element    ${一条用户数据}
    sleep    0.5
    click button    ${删除用户按钮}
    sleep    0.5
    click element    ${确认删除用户按钮}
