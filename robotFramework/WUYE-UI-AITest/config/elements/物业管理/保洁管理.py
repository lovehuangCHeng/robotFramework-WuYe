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
查看="//a[text()='查看']"
编辑="//a[text()='编辑']"
删除="//a[text()='删除']"
领用="//a[text()='领用']"
归还="//a[text()='归还']"

'''
 保洁区域
'''

保洁区域-高级展开="//a[@class='seniorSearchBtn']"
保洁区域-高级收起=""
保洁区域-区域名称="id=areaName"
保洁区域-管理区="id=regionId"
保洁区域-管理区数据="//ul[@role='listbox']/li[1]"
保洁区域-区域代码="id=areaCode"
保洁区域-地址="id=place"
保洁区域-高级搜索=""
保洁区域-工作要求="id=requirement"
保洁区域-是否外包="id=isOutsourced"
保洁区域-是否外包-是="//ul[@role='listbox']/li[text()='是']"
保洁区域-备注="id=remark"
保洁区域-责任人="id=staffId"
保洁区域-选择责任人="//body/div[4]//ul[@role='listbox']/li[1]"
保洁区域-列表第一个复选框="//tbody/tr/td[1]/span/label/span"


#断言
保洁区域-列表-区域名称="//tbody/tr/td[4]"
'''
 保洁记录
'''



'''
 保洁检查
'''



'''
 保洁工具管理
'''