# Can be used in the test data like ${MyObject()} or ${MyObject(1)}
class MyObject:
    def __init__(self, index=''):
        self.index = index

    def __str__(self):
        return '<MyObject%s>' % self.index

账号输入框="//input[@type='text']"
密码输入框="//input[@type='password']"
##########应收月度统计##########
应收月度统计_资源树搜索框="//input[@id='txtSerachTerm']"
应收月度统计_选择年份下拉框="//select[@id='year']"
应收月度统计_选择年份="//select[@id='year']/option[1]"
应收月度统计_选择月份="//div[@id='monthSelector']//label[1]"#input[1-12]分别对应1-12月
应收月度统计_搜索按钮="//button[@id='btnSearch']"
应收月度统计_一条数据的资源代码="//div[@id='gridReceivableMonthDetail']//tbody/tr[1]/td[1]/a"
应收月度统计_资源详情页面="//h2"
应收月度统计_一条数据的客户="//div[@id='gridReceivableMonthDetail']//tbody/tr[1]/td[3]/a"
应收月度统计_客户详情页面客户名称="//div[@class='ant-card-body']/div[1]/div[1]/span[2]"
应收月度统计_指定收费项目="//input[@class='select2-search__field']"
应收月度统计_选择一个收费项目="//ul[@id='select2-ChargeItemTypeIds-results']/li[1]"
应收月度统计_汇总到楼宇勾选框="//input[@id='BuildingName']"
应收月度统计_所有管理区展开="//tbody/tr/td[1]/span[@class='k-icon k-i-arrow-e']"
应收月度统计_所有楼宇展开="//tbody/tr[1]/td[3]/span[1]"
应收月度统计_汇总到收费项目勾选框="//input[@id='ChargeItemTypeName']"
应收月度统计_所有应收展开="//tbody/tr[1]/th[1]/span[1]"
应收月度统计_期初欠费所有项目展开="//div[@id='pivotgridReceivableMonth']//tbody/tr[3]/th[1]/span[1]"
应收月度统计_本期应收所有项目展开="//div[@id='pivotgridReceivableMonth']//tbody/tr[3]/th[2]/span[1]"
应收月度统计_导出Excel按钮="//button[@id='btnExport']"
##########欠费月度统计##########
欠费月度统计_资源树搜索框="//input[@id='txtSerachTerm']"
欠费月度统计_指定收费项目="//input[@class='select2-search__field']"
欠费月度统计_费用应收日期开始="//input[@id='ShouldChargeStartDate']"
欠费月度统计_费用应收日期结束="//input[@id='ShouldChargeEndDate']"
欠费月度统计_选择一个收费项目="//ul[@id='select2-ChargeItemTypeIds-results']/li[1]"
欠费月度统计_搜索按钮="//button[@id='btnSearch']"
欠费月度统计_汇总导出按钮="//button[@id='btnExport']"
欠费月度统计_汇总Tab="//ul[@id='tabHeader']/li[1]"
欠费月度统计_汇总到楼宇勾选框="//input[@id='BuildingName']"
欠费月度统计_所有管理区展开="//tbody/tr/td[1]/span[@class='k-icon k-i-arrow-e']"
欠费月度统计_所有楼宇展开="//tbody/tr[1]/td[3]/span[1]"
欠费月度统计_所有欠费金额="//tbody/tr[1]/td[1]/a"
欠费月度统计_汇总到收费项目勾选框="//input[@id='ChargeItemTypeName']"
欠费月度统计_所有项目展示="//tbody/tr[1]/th[1]/span[@class='k-icon k-i-arrow-e']"
欠费月度统计_客户资源汇总Tab="//ul[@id='tabHeader']/li[2]"
欠费月度统计_客户资源汇总导出按钮="//button[@id='btnExportCustomerSheetSummary']"
欠费月度统计_客户资源汇总查看房间信息="//tbody/tr[1]/td[2]/a"
欠费月度统计_资源详情页面="//h2"
欠费月度统计_客户资源汇总查看客户信息="//tbody/tr[1]/td[5]/a"
欠费月度统计_客户详情页面客户名称="//div[@class='ant-drawer-body']/div[1]/div[1]/div[1]//div[@class='ant-card-body']/div[1]/div[1]/span[2]"
欠费月度统计_客户资源明细Tab="//ul[@id='tabHeader']/li[3]"
欠费月度统计_导出欠费明细按钮="//button[@id='btnExportCustomerSummary']"
欠费月度统计_导出欠费汇总按钮="//button[@id='btnExportCustomerSummaryWithoutDetails']"
欠费月度统计_客户资源明细查看房间信息="//tbody/tr[1]/td[4]/a"
欠费月度统计_客户资源明细查看客户信息="//tbody/tr[1]/td[7]/a"
欠费月度统计_清单明细Tab="//ul[@id='tabHeader']/li[4]"
欠费月度统计_清单明细导出按钮="//button[@id='btnExportDetail']"
欠费月度统计_清单明细查看房间信息="//tbody/tr[1]/td[2]/a"
欠费月度统计_清单明细查看客户信息="//tbody/tr[1]/td[6]/a"
##########已收费用月统计##########
已收费用月统计_资源树搜索框="//input[@id='txtSerachTerm']"
已收费用月统计_选择年份下拉框="//select[@id='year']"
已收费用月统计_选择年份="//select[@id='year']/option[1]"
已收费用月统计_选择月份="//div[@id='monthSelector']//label[1]"#label[1-12]分别对应1-12月
已收费用月统计_指定收费项目="//input[@class='select2-search__field']"
已收费用月统计_选择一个收费项目="//ul[@id='select2-ChargeItemTypeIds-results']/li[1]"
已收费用月统计_搜索按钮="//button[@id='btnSearch']"
已收费用月统计_收费汇总导出按钮="//button[@id='btnExportSummary']"
已收费用月统计_票据汇总Tab="//ul[@id='tabHeader']/li[2]"
已收费用月统计_票据汇总导出按钮="//button[@id='btnExportTicket']"
已收费用月统计_收费明细Tab="//ul[@id='tabHeader']/li[3]"
已收费用月统计_收费明细导出按钮="//button[@id='btnExportDetail']"
已收费用月统计_收费明细查看房间信息="//tbody/tr[1]/td[1]/a"
已收费用月统计_房间详情页面验证="//h2"
已收费用月统计_收费明细查看客户信息="//tbody/tr[1]/td[3]/a"
已收费用月统计_客户详情页面验证="//div[@class='ant-drawer-body']/div[1]/div[1]/div[1]//div[@class='ant-card-body']/div[1]/div[1]/span[2]"
##########收入月度分摊##########
收入月度分摊_资源树搜索框="//input[@id='txtSerachTerm']"
收入月度分摊_选择年份下拉框="//select[@id='year']"
收入月度分摊_选择年份="//select[@id='year']/option[1]"
收入月度分摊_选择月份="//div[@id='monthSelector']//label[1]"#label[1-12]分别对应1-12月
收入月度分摊_指定收费项目="//input[@class='select2-search__field']"
收入月度分摊_选择一个收费项目="//ul[@id='select2-ChargeItemTypeIds-results']/li[1]"
收入月度分摊_搜索按钮="//button[@id='btnSearch']"
收入月度分摊_导出汇总按钮="//button[@id='btnExport']"
收入月度分摊_导出明细按钮="//button[@id='btnDetailExport']"
收入月度分摊_点击本期收往期非金额="//tbody/tr[1]/td[3]/a[1]"
收入月度分摊_查看资源代码详情="//*[@id='gridChargeMonthDetail']/div[2]/table/tbody/tr[1]/td[1]/a"
收入月度分摊_查看客户详情="//*[@id='gridChargeMonthDetail']/div[2]/table/tbody/tr[1]/td[3]/a"
收入月度分摊_资源详情页面="//h2"
收入月度分摊_客户详情页面客户名称="//div[@class='ant-drawer-body']/div[1]/div[1]/div[1]//div[@class='ant-card-body']/div[1]/div[1]/span[2]"
