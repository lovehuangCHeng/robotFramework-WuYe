'''
通用的按钮
'''
搜索框="//input[@placeholder='搜索...']"
搜索按钮="//span[@class='ant-input-suffix']/i"
保存="//div[@class='ant-modal-footer']//button[2]"
确认删除="//div[@class='ant-popover-buttons']/button[2]"
新建="//button/span[text()='新 建']/.."
导出="//button/span[text()='导 出']/.."
批量删除="//button/span[text()='批量删除']/.."
查看="//div[@class='ant-table-fixed-right']//tr[1]//a[text()='查看']"
编辑="//div[@class='ant-table-fixed-right']//tr[1]//a[text()='编辑']"
删除="//div[@class='ant-table-fixed-right']//tr[1]//a[text()='删除']"
列表第一个复选框="//tbody/tr/td[1]/span/label/span"
高级展开="//a[@class='seniorSearchBtn']"
高级收起="//a[@class='seniorSearchBtn']"
高级搜索="//button/span[text()='搜 索']/.."

#断言
编辑成功="//span[text()='编辑成功']"
新建成功="//span[text()='新建成功']"
删除成功="//span[text()='删除成功']"
'''
	保洁管理
'''
###保洁区域###
保洁区域_区域名称="id=areaName"
保洁区域_管理区="id=regionId"
保洁区域_管理区数据="//ul[@role='listbox']/li[1]"
保洁区域_区域代码="id=areaCode"
保洁区域_地址="id=place"
保洁区域_工作要求="id=requirement"
保洁区域_是否外包="id=isOutsourced"
保洁区域_是否外包_是="//ul[@role='listbox']/li[text()='是']"
保洁区域_备注="id=remark"
保洁区域_责任人="id=staffId"
保洁区域_选择责任人="//li[text()='testing']"
#断言
保洁区域_列表_区域名称="//tbody/tr/td[4]"

 ###保洁记录###
保洁记录_管理区="id=regionId"
保洁记录_管理区数据="//ul[@role='listbox']/li[1]"
保洁记录_保洁区域="id=cleaningAreaId"
保洁记录_保洁区域数据="//div[@style='position: absolute; top: 0px; left: 0px; width: 100%;'][2]//ul/li[1]"
保洁记录_项目名称="id=name"
保洁记录_项目类型="id=type"
保洁记录_项目类型数据="//li[text()='日常保洁']"
保洁记录_完成时间="id=completeDate"
保洁记录_完成时间_今天="//a[text()='今天']"
保洁记录_责任人="id=staffId"
保洁记录_责任人_数据="//li[text()='testing']"
保洁记录_状态="id=state"
保洁记录_状态_数据="//li[text()='计划中']"
保洁记录_具体内容="id=content"
保洁记录_备注="id=remark"
#断言
项目名称="//tbody/tr/td[3]"

###保洁检查###
保洁检查_管理区="id=regionId"
保洁检查_管理区数据="//ul[@role='listbox']/li[1]"
保洁检查_保洁区域="id=cleaningAreaId"
保洁检查_保洁区域数据="//div[@style='position: absolute; top: 0px; left: 0px; width: 100%;'][2]//ul/li[1]"
保洁检查_负责人="id=leadId"
保洁检查_负责人_数据="//li[text()='testing']"
保洁检查_检查人="id=rummagerId"
保洁检查_检查人_数据="//div[@style='position: absolute; top: 0px; left: 0px; width: 100%;'][4]//ul/li[1]"
保洁检查_检查时间="id=inspectDate"
保洁检查_检查时间_今天="//a[text()='今天']"
保洁检查_检查情况="id=content"
保洁检查_检查结果="id=result"
保洁检查_检查结果_数据="//li[text()='合格']"
保洁检查_备注="id=remark"
保洁检查_高级搜索_保洁区域="id=cleaningAreaName"
#断言
保洁检查_检查情况_断言="//tbody/tr/td[7]"

###保洁工具管理###
保洁工具管理_管理区="id=regionId"
保洁工具管理_管理区数据="//ul[@role='listbox']/li[1]"
保洁工具管理_工具名称="id=name"
保洁工具管理_项目类型="id=type"
保洁工具管理_项目类型数据="//li[text()='保洁工具']"
保洁工具管理_入库时间="id=registerDate"
保洁工具管理_入库时间_今天="//a[text()='今天']"
保洁工具管理_工具说明="id=remark"
保洁工具管理_总数量="id=count"
保洁工具管理_领用人="id=staffId"
保洁工具管理_领用人数据="//li[text()='testing']"
保洁工具管理_领用数量="id=count"
保洁工具_编辑="//tr[1]//a[text()='编辑']"
保洁工具_查看="//tr[1]//a[text()='查看']"
保洁工具_删除="//tr[1]//a[text()='删除']"
保洁工具_领用="//tr[1]//a[text()='领用']"
保洁工具_归还="//tr[1]//a[text()='归还']"
保洁工具_返回="//button/span[text()='返 回']/.."
保洁工具_查看页面关闭="//i[@class='anticon anticon-close']"
#断言
添加保洁工具成功="//span[text()='添加保洁工具成功']"
工具名称="//tbody/tr/td[3]"
登记领用成功="//span[text()='领用登记成功']"
归还登记成功="//span[text()='归还登记成功']"

'''
	保安消防
'''
###安防事件记录###
安防事件_管理区="id=regionId"
安防事件_管理区数据="//ul[@role='listbox']/li[1]"
安防事件_事件名称="id=name"
安防事件_类型="id=type"
安防事件_类型数据="//li[text()='突发事件']"
安防事件_责任人="id=responsibilityPersonId"
安防事件_处理人="id=handlePersonId"
安防事件_发生时间="id=occurrenceDateTime"
安防事件_发生时间_此刻="//a[text()='此刻']"
安防事件_发生地点="id=occurrencePlace"
安防事件_具体内容="id=content"
###来人来访###
来人来访_管理区="id=regionId"
来人来访_管理区数据="//ul[@role='listbox']/li[1]"
来访人姓名="id=name"
来访人姓名="id=idCardNo"
联系电话="id=phone"
被访人="id=respondents"
来访时间="id=visitDate"
###物品出入登记###
###安防设施管理###
###值班方案###
###保安岗位管理###
###保安排班表###
