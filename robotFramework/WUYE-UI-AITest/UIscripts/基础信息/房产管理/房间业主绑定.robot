*** Settings ***
Resource          报表管理方法.robot
Resource          ../../通用方法.robot

*** Test Cases ***
房间业主列表查询
    登录    ${房间绑定业主状态统计表}
    房间业主列表查询
    [Teardown]    关闭浏览器
	
房间业主列表导出Excel重置
    登录    ${房间绑定业主状态统计表}
    房间业主列表导出Excel重置
    [Teardown]    关闭浏览器
	
房间业主列表_查询明细
    登录    ${房间绑定业主状态统计表}
    房间业主列表_查询明细
    [Teardown]    关闭浏览器
	
房间业主列表_明细导出
    登录    ${房间绑定业主状态统计表}
    房间业主列表_明细导出
    [Teardown]    关闭浏览器