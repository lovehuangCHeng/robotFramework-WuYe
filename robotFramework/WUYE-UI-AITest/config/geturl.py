# Can be used in the test data like ${MyObject()} or ${MyObject(1)}
basicURL='http://10.10.120.171:8081'
loginURL='/Login'
首页=basicURL+'/#/home'
##基础信息
#房产管理
物业资源管理=basicURL+'/#/PropertyManage/BasicResources'
房产资源平面图=basicURL+'/#/resourcePlanManage'
房产状态统计=basicURL+'/#/Nova.Pms.PropertyManagementSystem/ResourcesSummaryReport/Index'
绑定房产管理员=basicURL+'/#/basicResourceManager'
#客户管理
客户档案=basicURL+'/#/GTLJ/BasicInformation/Customer'
业主委员会=basicURL+'/#/ownersCommitteeManagement/committeeMemberList'
#仪表管理
仪表类型=basicURL+'/#/BasicInformationManage/MeterManage/MeterType'
房间仪表管理=basicURL+'/#/Nova.Pms.PropertyManagementSystem/HouseMeter/Index'
公摊仪表管理=basicURL+'/#/Nova.Pms.PropertyManagementSystem/PublicMeter/Index'

##客户服务
#房屋交付管理
交房登记=basicURL+'/#/Nova.Pms.PropertyManagementSystem/HandOverHouse/Index'
接房登记=basicURL+'/#/Nova.Pms.PropertyManagementSystem/ReceiveHouse/Index'
入住登记=basicURL+'/#/Nova.Pms.PropertyManagementSystem/CustomerCheckIn/Index'
装修登记=basicURL+'/#/Nova.Pms.CustomerService/Decorate/Index'
#报事报修
提醒设置=basicURL+'/#/Nova.Pms.CustomerService/DispatchPrioritySetting/Index'
工单类型管理=basicURL+'/#/Nova.Pms.CustomerService/DispatchType/Index'
工单紧急程度=basicURL+'/#/Nova.Pms.CustomerService/DispatchPriority/Index'
报修管理=basicURL+'/#/Nova.Pms.CustomerService/RepairService/Index'
派工管理=basicURL+'/#/Nova.Pms.CustomerService/Dispatch/Index'
投诉建议=basicURL+'/#/Nova.Pms.CustomerService/ComplaintHandle/Index'
客户回访=basicURL+'/#/Nova.Pms.CustomerService/CustomerReturnVisit/Index'
及时率报表=basicURL+'/#/Nova.Pms.CustomerService/CustomerServiceReportManage/Report'
汇总统计=basicURL+'/#/customerServiceReport'
#短信平台
短信模板=basicURL+'/#/Nova.Pms.SMS/ShortMessageTemplate/Index'
发送欠费消息=basicURL+'/#/Nova.Pms.SMS/ArrearsShortMessage/Index'
发送公告消息=basicURL+'/#/Nova.Pms.SMS/Announcement/Index'
短信服务商设置=basicURL+'/#/Nova.Pms.SMS/MessageAccount/Index'


##消息提醒
消息提醒设置=basicURL+'/#/oaSystem/messageAlertSetting/messageReceptionList'
站内消息=basicURL+'/#/oaSystem/messageAlertSetting/allmessagemanagelist'
接受岗位设置=basicURL+'/#/oaSystem/messageAlertSetting/postManageList'
接受用户组设置=basicURL+'/#/oaSystem/messageAlertSetting/userGroupManageList'


##物业管理
#保安消防
安防事件记录=basicURL+'/#/securityFireManage/securityEventsList'
来人来访=basicURL+'/#/securityFireManage/visitorRegistrationList'
物品出入登记=basicURL+'/#/securityFireManage/articleRegistrationList'
安防设施管理=basicURL+'/#/securityFireManage/securityEquipMentList'
值班方案=basicURL+'/#/securityFireManage/securityDutyPlanList'
保安岗位管理=basicURL+'/#/securityFireManage/securityPositionList'
保安排班表=basicURL+'/#/securityFireManage/securityScheduleList'
#保洁管理
保洁区域=basicURL+'/#/cleaningManage/cleaningAreaList'
保洁记录=basicURL+'/#/cleaningManage/cleaningRecordList'
保洁检查=basicURL+'/#/cleaningManage/cleaningInspectList'
保洁工具检查=basicURL+'/#/cleaningManage/cleaningToolList'
#设备管理
设备档案=basicURL+'/#/Nova.Pms.DeviceManagement/Device/Index'
保养计划=basicURL+'/#/Nova.Pms.DeviceManagement/DeviceMaintenancePlan/Index'
设备运维=basicURL+'/#/Nova.Pms.DeviceManagement/DeviceMaintenanceOperation/Index'
设备保养记录=basicURL+'/#/Nova.Pms.DeviceManagement/DeviceMaintenance/Index'
#物料管理
供应商=basicURL+'/#/Nova.Pms.MaterialManagement/Supplier/Index'
物料清单=basicURL+'/#/Nova.Pms.MaterialManagement/Material/Index'
采购入库=basicURL+'/#/Nova.Pms.MaterialManagement/Inventory/Index'
领用出库=basicURL+'/#/Nova.Pms.MaterialManagement/StockOut/Index'
维修领料=basicURL+'/#/Nova.Pms.MaterialManagement/RepairMaterial/Index'
库存查询=basicURL+'/#/inventoryQueryList'
#绿化管理
绿化区域=basicURL+'/#/greeningManage/greeningAreaList'
绿化植被登记=basicURL+'/#/greeningManage/greeningPlantList'
绿化事件记录=basicURL+'/#/greeningManage/greeningMaintenanceList'
绿化检查工作=basicURL+'/#/greeningManage/greeningInspectionList'
#固定资产管理
固定资产=basicURL+'/#/fixedAssetsManagement/fixedAssetsList'
#巡更管理
巡更点=basicURL+'/#/PropertyManage/PatrolManage/PatrolPoint'
巡更路线=basicURL+'/#/PropertyManage/PatrolManage/PatrolRoute'
巡更计划=basicURL+'/#/PropertyManage/PatrolManage/PatrolPlan'
巡更任务=basicURL+'/#/PropertyManage/PatrolManage/PatrolTask'
问题列表=basicURL+'/#/PropertyManage/PatrolManage/PatrolProblem'
#保洁巡查
保洁巡查计划=basicURL+'/#/PropertyManage/PatrolManage/CleaningInspection/CleaningInspectionPlan'
保洁巡查任务=basicURL+'/#/PropertyManage/PatrolManage/CleaningInspection/CleaningInspectionTask'
保洁巡查问题列表=basicURL+'/#/PropertyManage/PatrolManage/CleaningInspection/CleaningInspectionProblem'

##系统管理
#系统设置
图标版权设置=basicURL+'/#/Nova.Pms.SystemManagement/CustomLogo/Index'
系统参数设置=basicURL+'/#/Nova.Pms.PropertyManagementSystem/DecimalDigitSetting/Index'
支付方式配置=basicURL+'/#/paymentMethodSetting'
系统初始化=basicURL+'/#/systemInit'
打印设置=basicURL+'/#/Nova.Pms.PropertyManagementSystem/PrintTemplate/Index'
数据备份=basicURL+'/#/Nova.Pms.SystemManagement/DatabaseBackup/Index'
操作日志=basicURL+'/#/operationLogManageList'
轮播图设置=basicURL+'/#/SystemManage/SystemSetting/Swiper'
#组织架构
组织机构=basicURL+'/#/GTLJ/SystemManage/Organization'
权限管理=basicURL+'/#/GTLJ/SystemManage/AuthorityManage'
用户管理=basicURL+'/#/GTLJ/SystemManage/UserManage'
#财务对接配置
基本设置=basicURL+'/#/financeSetting'
科目配置=basicURL+'/#/financeItemSetting'
生成凭证=basicURL+'/#/voucherList'


##OA系统
#办公管理
公告管理=basicURL+'/#/oaSystem/officeManage/noticeManagement/noticeList'
待办事项=basicURL+'/#/oaSystem/officeManage/todoList'
文档类别管理=basicURL+'/#/oaSystem/officeManage/documentCategoryList'
会议类别管理=basicURL+'/#/oaSystem/officeManage/meetingCategoryList'
计划类别管理=basicURL+'/#/oaSystem/officeManage/planTypeCategoryList'
文档资料管理=basicURL+'/#/oaSystem/officeManage/documentList'
会议记录=basicURL+'/#/oaSystem/officeManage/meetingList'
工作计划=basicURL+'/#/oaSystem/officeManage/workingPlanList'
#审批管理
定义审批类型=basicURL+'/#/oaSystem/approvalManage/approvalTypeList'
发起审批申请=basicURL+'/#/oaSystem/approvalManage/initiatedList'
待我审批=basicURL+'/#/oaSystem/approvalManage/pendingApprovalList'
我已审批的=basicURL+'/#/oaSystem/approvalManage/approvedList'
抄送我的=basicURL+'/#/oaSystem/approvalManage/sendApprovalList'
#活动管理
活动列表=basicURL+'/#/oaSystem/groupCampaign/groupCampaignList'
报名结果=basicURL+'/#/oaSystem/groupCampaign/groupCampaignResult'
#人事管理
考勤管理=basicURL+'/#/oaSystem/hrManage/workAttendanceList'
我的排班=basicURL+'/#/oaSystem/hrManage/WorkShiftMyShift'
排班计划=basicURL+'/#/oaSystem/hrManage/WorkShiftPlan'
排班设置=basicURL+'/#/oaSystem/hrManage/WorkShiftSetting'


##出入管理
#停车场
停车场管理=basicURL+'/#/IntelligentDeviceManage/ParkingManage'
停车场设备=basicURL+'/#/IntelligentDeviceManage/DeviceManage'
业主车辆登记=basicURL+'/#/IntelligentDeviceManage/VehicleManage'
车辆入场记录=basicURL+'/#/IntelligentDeviceManage/ParkingRecordsManage/ParkingInRecord'
车辆出场记录=basicURL+'/#/IntelligentDeviceManage/ParkingRecordsManage/ParkingOutRecord'
#非机动车
RFID设备=basicURL+'/#/RFIDManage/RFIDDevice'
卡类型=basicURL+'/#/RFIDManage/RFID-CardType'
非机动车发卡=basicURL+'/#/RFIDManage/RFIDCard'
非机动车出入记录=basicURL+'/#/RFIDManage/RFIDInOutLog'
#门禁管理
门禁设备=basicURL+'/#/DoorAccessManage/Access-PointDevice'
门禁点=basicURL+'/#/DoorAccessManage/AccessPoint'
员工发卡=basicURL+'/#/IntelligentDeviceManage/DoorAccessManage/StaffCard'
人脸录入=basicURL+'/#/IntelligentDeviceManage/DoorAccessManage/FaceEntry'
门禁权限查询=basicURL+'/#/IntelligentDeviceManage/DoorAccessManage/AuthorityQuery'
权限下发记录=basicURL+'/#/IntelligentDeviceManage/DoorAccessManage/PermissionIssuingRecord'
人员进出记录=basicURL+'/#/IntelligentDeviceManage/DoorAccessManage/PersonnelEntryRecord'
#车位租赁
租赁办理=basicURL+'/#/IntelligentDeviceManage/CarParkingRent'
车位状态查询=basicURL+'/#/Nova.Pms.ParkingManagement/CarParkingPlaceReport/Index'
车位租赁状态图=basicURL+'/#/parkingPlaceManageList'
车位租赁配置=basicURL+'/#/Nova.Pms.ParkingManagement/ParkingWarningSetting/Index'


##财务管理
#收支管理
收支科目=basicURL+'/#/incomeExpenseManage/incomeExpenseAccountList'
收入登记=basicURL+'/#/incomeExpenseManage/incomeManageList'
支出登记=basicURL+'/#/incomeExpenseManage/expenseManageList'
收支综合统计=basicURL+'/#/incomeExpenseManage/totalManageList'
#费用报表
银行托收明细=basicURL+'/#/Nova.Pms.BankAutoPayment/BankAutoPayReport/Index'
已收费用日报=basicURL+'/#/Nova.Pms.PropertyManagementSystem/DayPaymentHistoryReport/Index'
综合报表=basicURL+'/#/Nova.Pms.PropertyManagementSystem/ComprehensiveFinancialReport/Index'
现金收款明细=basicURL+'/#/Nova.Pms.PropertyManagementSystem/CashPayDetailReport/Index'
预存转实收明细=basicURL+'/#/Nova.Pms.PropertyManagementSystem/AdvancePayDetailReport/Index'
应收实收预存一览=basicURL+'/#/Nova.Pms.PropertyManagementSystem/ChargeRateSummaryReport/Index'
预存款收支明细=basicURL+'/#/Nova.Pms.PropertyManagementSystem/AdvancePaymentIncomeAndPaidReport/Index'
住户缴费日期报表=basicURL+'/#/householdPaymnet'
微信支付明细=basicURL+'/#/Nova.Pms.PropertyManagementSystem/WeChatPayDetailReport/Index'
微信支付提现对账=basicURL+'/#/wechatWithdrawAccountList'
报表统计=basicURL+'/#/reportStatistics'
保证金收退明细=basicURL+'/#/depositChargeDetailReport'
合同费用汇总表=basicURL+'/#/FinancialManage/ExpenseReports/ContractSummaryReport'
往年收欠率表=basicURL+'/#/FinancialManage/ExpenseReports/PastYearsRateReport'
综合收费率报表=basicURL+'/#/FinancialManage/ExpenseReports/ComprehensiveRateReport'
#月报表
应收月度统计=basicURL+'/#/Nova.Pms.PropertyManagementSystem/ReceivableMonthReport/Index'
欠费月度统计=basicURL+'/#/Nova.Pms.PropertyManagementSystem/OwningMonthReport/Index'
已收费用月统计=basicURL+'/#/Nova.Pms.PropertyManagementSystem/MonthPaymentHistoryReport/Index'
收入月度分摊=basicURL+'/#/Nova.Pms.PropertyManagementSystem/ChargeMonthReport/Index'
#年报表
应收年度统计=basicURL+'/#/Nova.Pms.PropertyManagementSystem/ReceivableYearReport/Index'	
欠费年度统计=basicURL+'/#/Nova.Pms.PropertyManagementSystem/OwningYearReport/Index'
已收费用年度统计=basicURL+'/#/Nova.Pms.PropertyManagementSystem/ChargeYearReport/Index'
收费率年度统计=basicURL+'/#/Nova.Pms.PropertyManagementSystem/ChargeYearRateReport/Index'
#费用减免统计
费用减免明细=basicURL+'/#/Nova.Pms.PropertyManagementSystem/FeeDiscountReport/Index'
费用减免汇总=basicURL+'/#/Nova.Pms.PropertyManagementSystem/FeeDiscountReport/Summary'
#欠费报表
欠费按时长分阶统计=basicURL+'/#/FinanceManage/OweReport/OweTimes'
欠费按金额分阶统计=basicURL+'/#/FinanceManage/OweReport/OweAmount'


##租赁管理
#租赁合同
合同列表=basicURL+'/#/Nova.Pms.Contract/Contract/Index'
生成合同费用=basicURL+'/#/Nova.Pms.Contract/GenerateContractBill/Index'
合同收费=basicURL+'/#/Nova.Pms.Contract/ContractCharge/Index'
合同催费=basicURL+'/#/Nova.Pms.Contract/ContractFeeNotice/Index'
合同到期预警=basicURL+'/#/contractExpiredWarningManage'
合同费用报表=basicURL+'/#/contractFeeReportManage'
应收摊销表=basicURL+'/#/amortizeContractManage'
租控图=basicURL+'/#/rentManage'
空置资源查询=basicURL+'/#/vacantResourceManage'
租赁资源统计表=basicURL+'/#/rentResourceStat'
合同模板管理=basicURL+'/#/contractTemplate'
#招商管理
招商客户=basicURL+'/#/investmentManagement/customerManagement'
销售漏斗分析=basicURL+'/#/investmentManagement/investmentAnalysis'
招商来源分析=basicURL+'/#/investmentManagement/investmentSourceAnalysis'
招商流失分析=basicURL+'/#/investmentManagement/investmentLostAnalysis'
#代收货款
销售单管理=basicURL+'/#/paymentCollection/salesOrderManageList'
返款管理=basicURL+'/#/paymentCollection/rebateManageList'
#委托经营
委托合同=basicURL+'/#/delegateContractManage/delegateContractList'
返租台账=basicURL+'/#/delegateContractManage/delegateContractReport'


##收费管理
#收费参数设置
收费项目定义=basicURL+'/#/chargeItemTypeManage'
收费标准设置=basicURL+'/#/ChargeManage/ChargeParamSetting/ChargeStandardSetting/ChargeItemSetting'
绑定收费标准=basicURL+'/#/Nova.Pms.PropertyManagementSystem/HouseChargeSetting/Index'
自动生成账单=basicURL+'/#/Nova.Pms.PropertyManagementSystem/AutoGenerateBillSetting/Index'
#票据管理
票据本管理=basicURL+'/#/ChargeManage/TicketManage/TicketBookManage'
损毁票据登记=basicURL+'/#/ChargeManage/TicketManage/InvalidTicket'
#退款管理
新建退款=basicURL+'/#/Nova.Pms.PropertyManagementSystem/Deposit/Index'
退款历史记录=basicURL+'/#/Nova.Pms.PropertyManagementSystem/Refund/Index'
#抄表管理
房间仪表抄表=basicURL+'/#/Nova.Pms.PropertyManagementSystem/HouseMeterReading/Index'
公摊仪表抄表=basicURL+'/#/Nova.Pms.PropertyManagementSystem/PublicMeterData/Index'
#应收管理
未出账单=basicURL+'/#/Nova.Pms.PropertyManagementSystem/GenerateBill/Index'
已出账单=basicURL+'/#/Nova.Pms.PropertyManagementSystem/ReceivableListDetailReport/Index'
减免活动=basicURL+'/#/ChargeManage/ARManage/DiscountRules'
指定金额减免=basicURL+'/#/ChargeManage/ARManage/DiscountAmount'
固定金额分摊=basicURL+'/#/Nova.Pms.PropertyManagementSystem/CostAllocation/Index'
#银行托收
银行=basicURL+'/#/Nova.Pms.BankAutoPayment/Bank/Index'
客户银行账号=basicURL+'/#/Nova.Pms.BankAutoPayment/CustomerBankAccount/Index'
银行托收模板=basicURL+'/#/Nova.Pms.BankAutoPayment/BankDisketteTemplate/Index'
报盘=basicURL+'/#/Nova.Pms.BankAutoPayment/BankDisketteExport/Index'
回盘=basicURL+'/#/Nova.Pms.BankAutoPayment/BankDisketteImport/Index'
#前台收费
日常收费=basicURL+'/#/Nova.Pms.PropertyManagementSystem/ChargeFeesWizard/Index'
预存款=basicURL+'/#/Nova.Pms.PropertyManagementSystem/CustomerAccount/Index'
经营性收费=basicURL+'/#/Nova.Pms.PropertyManagementSystem/TemporaryCharge/Index'
打印催费单=basicURL+'/#/Nova.Pms.ReportManagement/PrintFeeNotice/Index'
收费历史记录=basicURL+'/#/Nova.Pms.PropertyManagementSystem/PaymentHistory/Index'
客户零头账户=basicURL+'/#/Nova.Pms.PropertyManagementSystem/CustomerSmallChangeAccount/Index'
交款申请=basicURL+'/#/Nova.Pms.PropertyManagementSystem/AccountStatement/Index'