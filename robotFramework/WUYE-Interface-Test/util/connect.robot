*** Settings ***
Library           RequestsLibrary
Library           Mylibrary
Library           DatabaseLibrary
Variables         ../config/header.py
Variables         ../config/PC端接口.py


*** Keywords ***
login_pc
	${cookies}    Getlogin Cookie    ${login}    ${userName}    ${passWord}    ${from_header}
    [Return]    ${cookies}
	
login_app
	${apptoken}    get apptoken    ${applogin}    ${userName}    ${passWord}    ${app_login_header}
    [Return]    ${apptoken}
	
sqlselect
	[Arguments]    ${sqlselect}
    Connect To Database Using Custom Params    pyodbc    ${connectDataBase}
    ${var}    Query    ${sqlselect}
    Set Global Variable    ${var}
    Disconnect From Database
    [Return]    ${var}
	
sqledit
	[Arguments]    ${sqlselect}
    Connect To Database Using Custom Params    pyodbc    ${connectDataBase}
    Execute Sql String    ${sqlselect}
    Disconnect From Database


