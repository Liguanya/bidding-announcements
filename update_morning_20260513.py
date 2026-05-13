#!/usr/bin/env python3
"""
招标公告早间更新脚本 - 京津冀地区 (2026年5月13日)
仅保留京津冀地区的造价咨询相关招标公告
更新时间：2026年5月13日 08:50
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
        "title": "河北省公安厅交通管理局审计业务费采购（B包：造价咨询服务）",
        "pubDate": "2026-05-08",
        "source": "中国政府采购网河北分网",
        "link": "http://www.ccgp.gov.cn/cggg/dfgg/jzxcs/202605/t20260508_26531757.htm",
        "keywords": ["造价咨询", "审计业务", "竞争性磋商", "河北省"],
        "collectedAt": "2026-05-13",
        "slot": "早间",
        "budget": "最高限价为《河北省工程造价咨询服务收费管理暂行办法》收费标准的80%",
        "region": "河北省石家庄市",
        "description": "地区：河北省石家庄市；采购单位：河北省公安厅交通管理局本级；项目编号：BWZB2026-04N36；服务内容：本项目分2个标包，B包为造价咨询服务，最高限价为《河北省工程造价咨询服务收费管理暂行办法》（冀建市研[2017]2号）文件收费标准的80%；开标时间：2026年5月21日；专门面向中小企业采购"
    },
    {
        "id": max_id + 2,
        "title": "邱县2026年小麦病虫害防控药品采购项目（二次）",
        "pubDate": "2026-05-09",
        "source": "中国政府采购网河北分网",
        "link": "http://www.ccgp.gov.cn/cggg/dfgg/gkzb/202605/t20260509_26534330.htm",
        "keywords": ["造价咨询公司", "代理机构", "河北天诺", "政府采购"],
        "collectedAt": "2026-05-13",
        "slot": "早间",
        "budget": "134.642957万元",
        "region": "河北省邯郸市邱县",
        "description": "地区：河北省邯郸市邱县；采购单位：邱县农业农村局；项目编号：HBTNCG-20260414；代理机构：河北天诺工程造价咨询有限公司；采购内容：联苯·噻虫胺、吡唑醚菌酯、氨基酸水溶肥、芸苔素等；开标时间：2026年6月1日；采用双盲评审"
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
