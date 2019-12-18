*** Settings ***
Resource          活动方法.robot
Resource          ../../通用方法.robot

*** Test Cases ***
新建活动类别
    登录    ${活动列表}
    活动类别新建    野营活动
    [Teardown]    关闭浏览器
新建活动
    登录    ${活动列表}
    活动新建    
    [Teardown]    关闭浏览器

活动编辑
    登录    ${活动列表}
    活动编辑    
    [Teardown]    关闭浏览器

活动查看
    登录    ${活动列表}
    活动查看    
    [Teardown]    关闭浏览器
	
活动发布
    登录    ${活动列表}
    活动发布    
    [Teardown]    关闭浏览器
	
活动下线
    登录    ${活动列表}
    活动下线    
    [Teardown]    关闭浏览器
	
活动删除
    登录    ${活动列表}
    活动删除    
    [Teardown]    关闭浏览器
	
