*** Settings ***
Resource          合同列表-source.robot

*** Test Cases ***
新建合同
    登录    ${合同列表}
    sleep    3
    进入iframe
    sleep    3
    新建合同
    [Teardown]    关闭浏览器

变更合同
    登录    ${合同列表}
    sleep    3
    进入iframe
    高级搜索    UI合同20191230035505    UI合同20191230035505
    sleep    3
    合同变更
    [Teardown]    关闭浏览器

编辑会议记录
    登录    ${会议记录}
    sleep    1
    搜索会议记录
    编辑会议记录
    [Teardown]    关闭浏览器

删除会议记录
    登录    ${会议记录}
    sleep    1
    搜索会议记录
    删除会议记录
    sleep    1
    二次确认
    断言存在    //div[@class='ant-message-custom-content ant-message-success']/span[text()='删除成功']
    [Teardown]    关闭浏览器
