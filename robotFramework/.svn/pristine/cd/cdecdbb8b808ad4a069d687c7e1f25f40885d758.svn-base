*** Settings ***
Library           RequestsLibrary
Library           DatabaseLibrary
Library           String
Library           Mylibrary
Variables         ../config/header.py
Variables         ../config/PC端接口.py

*** Test Cases ***
02
    ${cookie}    Getlogin Cookie    ${baseURL}    ${userName}    ${passWord}    ${from_header}
    log    ${cookie}

03_gettoken
    ${cookies}    Getlogin Cookie    ${login}    ${userName}    ${passWord}    ${from_header}
    log    ${cookies}
    Create Session    login    ${baseURL}    cookies=${cookies}
    log    ${from_header}
    ${res}    Get Request    login    ${souyemeaue}
    log    ${res}
