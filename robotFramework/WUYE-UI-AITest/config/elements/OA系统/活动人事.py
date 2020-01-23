# Can be used in the test data like ${MyObject()} or ${MyObject(1)}
class MyObject:
    def __init__(self, index=''):
        self.index = index
    def __str__(self):
        return '<MyObject%s>' % self.index
		
'''
活动管理

'''
###活动列表####
新建活动="//button[@class='ant-btn ant-btn-primary']"
编辑活动="//div[@class='ant-table-fixed-right']//tbody/tr[1]/td//a[2]"
查看活动="//div[@class='ant-table-fixed-right']//tbody/tr[1]/td//a[1]"
发布活动="//div[@class='ant-table-fixed-right']//tbody/tr[1]/td//a[4]"
删除活动="//div[@class='ant-table-fixed-right']//tbody/tr[1]/td//a[3]"
下线活动="//div[@class='ant-table-fixed-right']//tbody/tr[1]/td//a[2]"
搜索活动框="//input[@placeholder='搜索...']"
搜索活动按钮="//div[@style='float: right;']/span/span"
活动类别="//div[@id='category']//div[@class='ant-select-selection__rendered']"
活动类别数据="//div[@style='position: absolute; top: 0px; left: 0px; width: 100%;'][1]//ul[@role='listbox']/li[1]"
活动类别添加="//li[text()='+ 添加']"
活动类别名称="//input[@id='category']"
活动类别保存="//body/div[4]//div[@class='ant-modal-content']/div[3]//button[2]"
发送范围="//div[@id='regions']//div[@class='ant-select-selection__rendered']"
发送范围数据选择="//div[@style='position: absolute; top: 0px; left: 0px; width: 100%;'][2]//ul[@role='listbox']/li[2]"
活动主题="id=title"
活动简介="id=introInfo"
活动地址="id=address"
活动内容="//div[@contenteditable='true']"
活动时间="id=campaignRangeTime"
活动报名时间="id=registrationRangeTime"
开始时间="//div[@class='ant-calendar-date-panel']/div[1]//tbody/tr[1]/td[1]"
结束时间="//div[@class='ant-calendar-date-panel']/div[1]//tbody/tr[last()]/td[last()]"
活动保存="//div[@class='ant-modal-content']/div[3]//button[2]"
查看页面取消="xpath=//button/span[text()='取 消']"
###报名结果##
导出Excel="//button/span[text()='导出Excel']"
确认删除按钮="//div[@class='ant-popover-buttons']/button[2]"
'''
人事管理
'''
###考勤管理###


###排班设置###
排班新建="//div[@class='ant-tabs ant-tabs-top ant-tabs-line']//div[@role='tabpanel'and @aria-hidden='false']//button"
分组新建="//div[@class='ant-tabs ant-tabs-top ant-tabs-line']//div[@role='tabpanel'and @aria-hidden='false']//button/span[text()='新 建']/.."
班次名称="id=className"
编辑班次="//tbody/tr/td[5]//a[1]"
日历管理="//div[@role='tab'and text()='日历管理']"
周期管理="//div[@role='tab'and text()='周期管理']"
排班分组="//div[@role='tab'and text()='排班分组']"
日历名称="id=name"
编辑日历="//div[@class='ant-col ant-col-8'][1]//ul[@class='ant-card-actions']/li[1]/span"
周期名称="id=cycleName"
第一天="//div[@id='flight1']"
第二天="//div[@id='flight2']"
每天的值="//li[text()='假']"
第二天的值="//div[@style='position: absolute; top: 0px; left: 0px; width: 100%;'][2]//ul[@role='listbox']/li[1]"
班组名称="id=groupName"
排班周期="//div[@id='cycle']"  
排班周期的值="//div[@style='position: absolute; top: 0px; left: 0px; width: 100%;'][1]//ul[@role='listbox']/li[1]"      
排班日历="//div[@id='calendar']"
排班日历的值="//div[@style='position: absolute; top: 0px; left: 0px; width: 100%;'][2]//ul[@role='listbox']/li[1]" 
班组员工="//span[@class='ant-form-item-children']/span/span/span"
班组员工数据="//ul[@class='ant-select-tree']/li[1]/span[2]"
预设班次="//tbody//td[@newgroup='[object Object]'][2]"
排班分组编辑="//tbody/tr[1]/td[6]//a[1]"
排班分组查看="//tbody/tr[1]/td[1]//a"
自动排班="//button/span[text()='自动排班']"

'''
考勤管理
'''
考勤新建="//div/span[1]/button"
职员姓名="id=name"
职员性别="//div[@id='sex']/label[1]/span[@class='ant-radio']"
职员导出="//button/span[text()='导 出']"
职员搜索框="//input[@placeholder='搜索...']"
职员搜索按钮="//span[@class='ant-input-suffix']/i"
职员查看="//div[@class='ant-table-fixed-right']//tbody/tr[1]/td[1]/span/a"
职员查看页面返回="//button/span[text()='返 回']"
职员添加="//div[@class='ant-table-fixed-right']//tbody/tr[1]/td[1]/span/span/a"
考勤类型="id=Type"
出差="//li[text()='出差']"
小时="id=hours"
职员查看页面删除="//tbody/tr[1]/td[10]/span/a"
职员查看页面编辑="//tbody/tr[1]/td[10]/span/span/a"
考勤管理高级搜索="//a[@class='seniorSearchBtn']"
职员名称="id=staffName"
高级搜索按钮="//div[@class='ant-card-body']//button[2]"


