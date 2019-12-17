*** Settings ***
Library           Selenium2Library    timeout=15
Resource          ../../通用方法.robot
Resource          用户管理-resource.robot
Variables         ../../../config/geturl.py

*** Test Cases ***
新建用户
    登录    ${用户管理}
    进入iframe
    新建用户
    [Teardown]    关闭浏览器

搜索用户
    登录    ${用户管理}
    进入iframe
    搜索用户
    [Teardown]    关闭浏览器

编辑用户
    登录    ${用户管理}
    进入iframe
    编辑用户
    [Teardown]    关闭浏览器

禁用用户
    登录    ${用户管理}
    进入iframe
    禁用用户
    [Teardown]    关闭浏览器

启用用户
    登录    ${用户管理}
    进入iframe
    启用用户
    [Teardown]    关闭浏览器

显示禁用用户
    登录    ${用户管理}
    进入iframe
    显示禁用用户
    [Teardown]    关闭浏览器

显示启用用户
    登录    ${用户管理}
    进入iframe
    显示启用用户
    [Teardown]    关闭浏览器

下载用户导入模板
    登录    ${用户管理}
    进入iframe
    下载用户导入模板
    [Teardown]    关闭浏览器

高级搜索用户
    登录    ${用户管理}
    进入iframe
    高级搜索用户
    [Teardown]    关闭浏览器

组织机构添加职员
    登录    ${用户管理}
    进入iframe
    组织机构添加职员
    [Teardown]    关闭浏览器

组织机构移除职员
    登录    ${用户管理}
    进入iframe
    组织机构移除职员
    [Teardown]    关闭浏览器

岗位添加职员
    登录    ${用户管理}
    进入iframe
    岗位添加职员
    [Teardown]    关闭浏览器

岗位移除职员
    登录    ${用户管理}
    进入iframe
    岗位移除职员
    [Teardown]    关闭浏览器

删除用户
    登录    ${用户管理}
    进入iframe
    删除用户
    [Teardown]    关闭浏览器
