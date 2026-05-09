#!/usr/bin/env python3
"""
招标公告下午更新脚本 - 2026年5月9日
抓取京津冀地区最新招标公告
"""

import json
from datetime import datetime

# 读取现有数据
with open('data/announcements.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 获取当前最大ID
max_id = max([a['id'] for a in data['announcements']]) if data['announcements'] else 0

# 5月9日下午新增的公告数据
new_announcements = [
    {
        "id": max_id + 1,
        "title": "北京邮电大学沙河校区研究生宿舍变配电及外电源工程采购项目中标公告",
        "pubDate": "2026-05-08",
        "source": "中国政府采购网",
        "link": "http://www.ccgp.gov.cn/cggg/zygg/zbgg/",
        "keywords": ["招标代理", "变配电", "工程造价"],
        "collectedAt": "2026-05-09",
        "slot": "下午",
        "budget": "未知",
        "description": "地区：北京；采购单位：北京邮电大学沙河校区；项目名称：研究生宿舍变配电及外电源工程"
    },
    {
        "id": max_id + 2,
        "title": "北京师范大学电感耦合等离子体光谱仪、全自动气体吸附分析仪采购项目中标公告",
        "pubDate": "2026-05-08",
        "source": "中国政府采购网",
        "link": "http://www.ccgp.gov.cn/cggg/zygg/zbgg/",
        "keywords": ["招标代理", "设备采购"],
        "collectedAt": "2026-05-09",
        "slot": "下午",
        "budget": "未知",
        "description": "地区：北京；采购单位：北京师范大学；采购内容：电感耦合等离子体光谱仪、全自动气体吸附分析仪"
    },
    {
        "id": max_id + 3,
        "title": "天津大学石化中心全自动原位在线检测高压反应系统采购项目中标公告",
        "pubDate": "2026-05-08",
        "source": "中国政府采购网",
        "link": "http://www.ccgp.gov.cn/cggg/zygg/zbgg/",
        "keywords": ["招标代理", "设备采购"],
        "collectedAt": "2026-05-09",
        "slot": "下午",
        "budget": "未知",
        "description": "地区：天津；采购单位：天津大学石化中心；采购内容：全自动原位在线检测高压反应系统"
    },
    {
        "id": max_id + 4,
        "title": "2026年石家庄海关技术中心试剂耗材采购中标公告",
        "pubDate": "2026-05-08",
        "source": "中国政府采购网",
        "link": "http://www.ccgp.gov.cn/cggg/zygg/zbgg/",
        "keywords": ["招标代理", "试剂耗材"],
        "collectedAt": "2026-05-09",
        "slot": "下午",
        "budget": "未知",
        "description": "地区：河北石家庄；采购单位：石家庄海关技术中心；采购内容：试剂耗材采购"
    },
    {
        "id": max_id + 5,
        "title": "天津港保税区建设服务中心政府投资项目工程造价咨询服务项目",
        "pubDate": "2026-05-08",
        "source": "中国政府采购网",
        "link": "http://www.ccgp.gov.cn/cggg/dfgg/gkzb/",
        "keywords": ["造价咨询", "招标代理", "全过程咨询"],
        "collectedAt": "2026-05-09",
        "slot": "下午",
        "budget": "134.1265万元",
        "description": "地区：天津滨海新区；采购单位：天津港保税区建设服务中心；服务内容：预算编制、变更结算审核"
    },
    {
        "id": max_id + 6,
        "title": "首都机场线更新改造类工程造价结算服务",
        "pubDate": "2026-05-08",
        "source": "北京工程造价招标信息网",
        "link": "https://m.yfbzb.com/zbzt/36/2/",
        "keywords": ["造价咨询", "项目管理", "全过程咨询"],
        "collectedAt": "2026-05-09",
        "slot": "下午",
        "budget": "未知",
        "description": "地区：北京；采购单位：北京市；项目名称：首都机场线更新改造类工程造价结算服务"
    },
    {
        "id": max_id + 7,
        "title": "北京航空航天大学电源可靠性设计分析与评估验证平台定制开发项目",
        "pubDate": "2026-05-08",
        "source": "中国政府采购网",
        "link": "http://www.ccgp.gov.cn/cggg/zygg/zbgg/",
        "keywords": ["招标代理", "软件开发", "项目管理"],
        "collectedAt": "2026-05-09",
        "slot": "下午",
        "budget": "未知",
        "description": "地区：北京；采购单位：北京航空航天大学；采购内容：电源可靠性设计分析与评估验证平台"
    },
    {
        "id": max_id + 8,
        "title": "中国环境监测总站国家地表水环境质量监测运行维护项目公开招标公告",
        "pubDate": "2026-05-07",
        "source": "中国政府采购网",
        "link": "http://www.ccgp.gov.cn/cggg/zygg/",
        "keywords": ["招标代理", "环境监测", "项目管理"],
        "collectedAt": "2026-05-09",
        "slot": "下午",
        "budget": "未知",
        "description": "地区：北京；采购单位：中国环境监测总站；采购内容：国家地表水环境质量监测运行维护"
    },
    {
        "id": max_id + 9,
        "title": "中国信息通信研究院信息通信产品中试验证平台项目公开招标公告",
        "pubDate": "2026-05-07",
        "source": "中国政府采购网",
        "link": "http://www.ccgp.gov.cn/cggg/zygg/",
        "keywords": ["招标代理", "信息化", "项目管理"],
        "collectedAt": "2026-05-09",
        "slot": "下午",
        "budget": "未知",
        "description": "地区：北京；采购单位：中国信息通信研究院；采购内容：信息通信产品中试验证平台项目"
    },
    {
        "id": max_id + 10,
        "title": "天津出入境边防检查总站考勤系统建设项目竞争性磋商公告",
        "pubDate": "2026-05-01",
        "source": "中国政府采购网",
        "link": "http://www.ccgp.gov.cn/cggg/zygg/",
        "keywords": ["招标代理", "项目管理", "考勤系统"],
        "collectedAt": "2026-05-09",
        "slot": "下午",
        "budget": "未知",
        "description": "地区：天津；采购单位：中华人民共和国天津出入境边防检查总站；采购内容：考勤系统建设"
    },
]

# 将新公告添加到列表开头
data['announcements'] = new_announcements + data['announcements']

# 更新元数据
data['lastUpdate'] = datetime.now().strftime('%Y-%m-%d %H:%M')
data['totalCount'] = len(data['announcements'])

# 保存更新后的数据
with open('data/announcements.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✅ 数据更新完成！")
print(f"   - 新增公告: {len(new_announcements)} 条")
print(f"   - 总计公告: {data['totalCount']} 条")
print(f"   - 最后更新: {data['lastUpdate']}")
