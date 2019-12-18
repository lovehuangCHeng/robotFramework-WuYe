*** Settings ***
Resource          人事管理方法.robot
Resource          ../../通用方法.robot

*** Test Cases ***
考勤管理新建
    登录    ${考勤管理}
    考勤管理新建    test003
    [Teardown]    关闭浏览器
	
考勤管理添加
    登录    ${考勤管理}
    考勤管理添加    test003		2
    [Teardown]    关闭浏览器
	
考勤查看编辑
    登录    ${考勤管理}
    考勤查看编辑    test003
    [Teardown]    关闭浏览器
	
考勤查看删除
    登录    ${考勤管理}
    考勤查看删除    test003
    [Teardown]    关闭浏览器
	
考勤管理高级搜索查询
    登录    ${考勤管理}
    考勤管理高级搜索查询    test003
    [Teardown]    关闭浏览器
	
考勤查看导出
    登录    ${考勤管理}
    考勤查看导出    test003
    [Teardown]    关闭浏览器