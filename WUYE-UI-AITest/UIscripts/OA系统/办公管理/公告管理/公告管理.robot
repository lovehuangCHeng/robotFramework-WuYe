*** Settings ***
Resource          ../../通用组件.txt
Resource          公告_RESOUCE.txt
Variables         ../../../../config/basicConfig.py
Variables         ../../../../config/geturl.py
Resource          ../../../通用方法.robot

*** Test Cases ***
新建公告类别
    登录    ${公告管理}
    新建公告类别
    Close Browser

新建公告
    ${gg1}    Evaluate    random.randint(1000, 9999)    random
    ${公告名称}    Catenate    ${gg1}    公告UITE
    set global variable    ${公告名称}
    登录1    ${账号}    ${密码}    ${basicURL}    ${公告管理}
    Sleep    2
    新建公告    ${公告名称}
    Sleep    3
    Close Browser

搜索我发布的公告
    登录1    ${账号}    ${密码}    ${basicURL}    ${公告管理}
    sleep    2
    搜索公告

发布公告
    发布公告

删除我发布的公告
    删除公告
    sleep    1
    Close Browser

新建并发布公告
    ${gg1}    Evaluate    random.randint(1000, 9999)    random
    ${公告名称1}    Catenate    ${gg1}    公告UITE
    set global variable    ${公告名称1}
    登录1    ${账号}    ${密码}    ${basicURL}    ${公告管理}
    Sleep    2
    : FOR    ${i}    IN RANGE    3
    \    新建并发布公告    ${公告名称1}
    Sleep    3
    Close Browser

查看我收到的公告
    log    跳过

删除/批量删除我收到的公告
    log    跳过
