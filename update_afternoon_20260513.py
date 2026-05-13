#!/usr/bin/env python3
"""
招标公告下午更新脚本 - 京津冀地区 (2026年5月13日)
仅保留京津冀地区的造价咨询相关招标公告
更新时间：2026年5月13日 13:50
"""
import json
from datetime import datetime
import os

# 读取现有数据
data_path = '/app/data/所有对话/主对话/bidding-announcements/data/announcements.json'
with open(data_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# 获取当前最大ID
max_id = max([a['id'] for a in data['announcements']]) if data['announcements'] else 0
print(f"当前最大ID: {max_id}, 当前总数: {data['totalCount']}")

# 京津冀地区新增公告数据 (2026年5月13日最新发现)
new_announcements = [
    {
        "id": max_id + 1,
        "title": "南开大学国家基础研究创新提升工程建设项目（化学）全过程造价咨询服务公开招标",
        "pubDate": "2026-05-07",
        "source": "中国政府采购网",
        "link": "http://www.ccgp.gov.cn/cggg/zygg/gkzb/202605/t20260507_26520324.htm",
        "keywords": ["全过程造价咨询", "高校建设", "基础研究", "南开大学", "天津"],
        "collectedAt": "2026-05-13",
        "slot": "下午",
        "budget": "100万元（最高限价80万元）",
        "region": "天津",
        "description": "地区：天津；采购单位：南开大学；项目编号：NK2026F038；服务内容：招标及合同签订阶段、施工阶段、竣工结算阶段全过程工程造价咨询、造价管理及控制、文件资料分发、相关人员沟通协调、结算送审资料审核汇总及造价资料整理归档；最高限价80万元；开标时间：2026年6月2日；专门面向中小企业采购"
    },
    {
        "id": max_id + 2,
        "title": "大兴区瀛海镇京台西区级统筹地块九年一贯制学校建设项目工程造价咨询单位公开招标",
        "pubDate": "2026-04-22",
        "source": "北京市政府采购网",
        "link": "http://www.ccgp-beijing.gov.cn/xxgg/qjxxgg/qjzbgg/2026/4/df141b0b9fbd41f1a251ff4688071485.htm",
        "keywords": ["工程造价咨询", "学校建设", "工程量清单", "招标控制价", "大兴区"],
        "collectedAt": "2026-05-13",
        "slot": "下午",
        "budget": "114.6万元",
        "region": "北京大兴区",
        "description": "地区：北京大兴区；采购单位：北京市大兴区瀛海镇人民政府；项目编号：11011526210200032762-XM001；服务内容：编制建设项目工程量清单及最高投标限价；开标时间：2026年5月13日；专门面向小微企业采购；项目负责人需具有一级注册造价工程师执业资格"
    },
    {
        "id": max_id + 3,
        "title": "2026年北京市普通公路健康工程造价咨询第1标段（二次）招标",
        "pubDate": "2026-04-20",
        "source": "北京市交通委员会",
        "link": "https://jtw.beijing.gov.cn/xxgk/ztbxx/202604/P020260420648265052375.pdf",
        "keywords": ["公路工程造价咨询", "健康工程", "结算审核", "二次招标", "北京市"],
        "collectedAt": "2026-05-13",
        "slot": "下午",
        "budget": "162万元（第1标段79万元，第2标段83万元）",
        "region": "北京",
        "description": "地区：北京；采购单位：北京市公路事业发展中心；服务内容：通州区、怀柔区、密云区、平谷区、房山区及全市高速公路普通公路健康工程造价咨询审查；包括工程量复核、定额选用审核、人材机单价审核、项目决(结)算审核等；服务期限至2026年12月31日；第一次招标流标，现二次招标；专门面向中小企业采购"
    },
    {
        "id": max_id + 4,
        "title": "房山区财政局项目评审服务（工程造价咨询类）公开招标",
        "pubDate": "2026-04-10",
        "source": "中国政府采购网",
        "link": "http://www.ccgp.gov.cn/cggg/dfgg/gkzb/202604/t20260410_26386816.htm",
        "keywords": ["项目评审", "工程造价咨询", "预算评审", "结算评审", "房山区"],
        "collectedAt": "2026-05-13",
        "slot": "下午",
        "budget": "2520万元（分7包，每包360万元）",
        "region": "北京房山区",
        "description": "地区：北京房山区；采购单位：北京市房山区财政局本级；项目编号：11011126210200029556-XM001；服务内容：新建、修缮基础设施等工程类项目预（结）算评审，分析必要性、可行性、完整性，评审预算合规性、合理性、经济性及定额测算；分7个包，服务期限3年；开标时间：2026年5月7日"
    },
    {
        "id": max_id + 5,
        "title": "子牙新河献县段治理工程全过程造价咨询竞争性磋商",
        "pubDate": "2026-05-11",
        "source": "河北省政府采购网",
        "link": "https://www.ccgp-hebei.gov.cn/BidWinAnncFiles/3e66a839-3ff2-4716-9bfb-0d462a95fdd7.pdf",
        "keywords": ["全过程造价咨询", "水利工程", "河道治理", "献县", "沧州"],
        "collectedAt": "2026-05-13",
        "slot": "下午",
        "budget": "130万元",
        "region": "河北沧州献县",
        "description": "地区：河北沧州献县；采购单位：献县水务局、献县建投工程项目管理有限公司；项目编号：zyxh/xxdzlgc/zjzx-2024-01；服务内容：施工图预算审核、工程量清单审核、招标控制价编制及审核、工程计量及进度款支付审核、材料设备选型询价认价、设计变更预算审核、各阶段结算审核、项目建设后成本评价、配合竣工决算审计等；专门面向小微企业采购；项目负责人需具有一级注册造价师(水利工程)职业资格"
    }
]

print(f"准备新增 {len(new_announcements)} 条公告")

# 合并新数据
data['announcements'].extend(new_announcements)

# 更新统计
data['totalCount'] = len(data['announcements'])
data['lastUpdate'] = datetime.now().strftime('%Y-%m-%d %H:%M')

# 按日期排序（最新的在前）
data['announcements'].sort(key=lambda x: (x['pubDate'], x['id']), reverse=True)

# 保存JSON
with open(data_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"JSON已更新，总数: {data['totalCount']}")
print("更新完成!")
