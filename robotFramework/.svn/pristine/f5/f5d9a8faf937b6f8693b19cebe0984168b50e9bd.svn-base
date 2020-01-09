*** Settings ***
Resource          ../../通用方法.robot
Variables         ../../../config/sql.py
Resource          客户管理中方法封装.robot

*** Test Cases ***
返回管理区数据
    数据库查询操作    ${guanliqu}
    ${GLQ}    Set Variable    ${var[0][0]}
    log    ${GLQ}

新建客户
    登录    ${客户档案}
    iframr 切换
    新建客户数据    逐日者奥利娅    1254689
    sleep    2
    [Teardown]    关闭浏览器

编辑客户
    登录    ${客户档案}
    iframr 切换
    编辑客户档案
    sleep    2
    [Teardown]    关闭浏览器

查询客户
    登录    ${客户档案}
    iframr 切换
    查询客户数据    逐日者
    sleep    2
    [Teardown]    关闭浏览器

高级查询客户
    登录    ${客户档案}
    iframr 切换
    客户数据高级搜索    逐日者奥利娅
    sleep    2
    [Teardown]    关闭浏览器

合并同名客户
    登录    ${客户档案}
    iframr 切换
    合并重名客户
    sleep    2
    [Teardown]    关闭浏览器

删除客户
    登录    ${客户档案}
    iframr 切换
    查询客户数据    逐日者奥利娅
    删除新建客户
    sleep    2
    [Teardown]    关闭浏览器

导出Excel
    登录    ${客户档案}
    iframr 切换
    Click Element    ${客户档案导出Excel}
    sleep    2
    [Teardown]    关闭浏览器
