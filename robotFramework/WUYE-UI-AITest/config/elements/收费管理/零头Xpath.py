#客户零头明细
业主姓名="//input[@id='filterCustomer']"
开始日期="//input[@placeholder='收费起始日期']"
开始日期输入="//input[@placeholder='收费起始日期' and @class='ant-calendar-input ']"
结束日期="//input[@placeholder='收费结束日期']"
结束日期输入="//input[@placeholder='收费结束日期' and @class='ant-calendar-input ']"
搜索账户="//button/span[text()='查 询']/.."
概览数据存在断言="//tbody/tr[1]/td[1]"
明细数据存在断言="//table//tr[1]/td[6]"
收起明细按钮="//tbody/tr[1]/td[1]/div"
展开明细按钮="//tbody/tr[1]/td[1]/div"
重置搜索="//button/span[text()='重 置']/.."
导出Excel="//button/span[text()='导出EXCEL']/.."