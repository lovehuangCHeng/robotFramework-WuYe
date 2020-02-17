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
    sleep    2
    合同变更
    [Teardown]    关闭浏览器


