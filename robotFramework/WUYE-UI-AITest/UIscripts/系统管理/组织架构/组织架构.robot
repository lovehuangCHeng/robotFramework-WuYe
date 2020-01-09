*** Settings ***
Library           Selenium2Library
Variables         ../../../config/geturl.py
Resource          ../../通用方法.robot
Resource          组织架构-resource.robot

*** Test Cases ***
新建分公司
    登录    ${组织机构}
    进入iframe
    新建分公司
    [Teardown]    关闭浏览器

新建部门
    登录    ${组织机构}
    进入iframe
    新建部门
    [Teardown]    关闭浏览器

编辑组织架构
    登录    ${组织机构}
    进入iframe
    编辑组织架构
    [Teardown]    关闭浏览器

搜索组织架构
    登录    ${组织机构}
    进入iframe
    搜索组织架构
    [Teardown]    关闭浏览器

删除组织架构
    登录    ${组织机构}
    进入iframe
    删除组织架构
    [Teardown]    关闭浏览器
