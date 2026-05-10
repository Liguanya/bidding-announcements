#!/usr/bin/env python3
"""
招标公告晚间更新脚本 - 京津冀地区 (2026年5月10日)
仅保留京津冀地区的造价咨询相关招标公告
更新时间：2026年5月10日 18:20
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

# 京津冀地区新增公告数据 (2026年5月7日-10日最新发现)
new_announcements = [
    {
        "id": max_id + 1,
        "title": "东尖塔村棚户区改造二期项目全过程造价咨询招标公告",
        "pubDate": "2026-05-08",
        "source": "河北招标网",
        "link": "https://hbs.bidcenter.com.cn/zhaobiao/zbkeyw-24187-0-0-0.html",
        "keywords": ["全过程造价咨询", "棚户区改造", "廊坊"],
        "collectedAt": "2026-05-10",
        "slot": "晚间",
        "budget": "未公开",
        "region": "河北廊坊市",
        "description": "地区：河北廊坊市；项目名称：东尖塔村棚户区改造二期项目；服务内容：全过程造价咨询；发布时间：2026年5月8日"
    },
    {
        "id": max_id + 2,
        "title": "招标代理及造价咨询服务商采购项目招标公告",
        "pubDate": "2026-05-08",
        "source": "河北招标网",
        "link": "https://hbs.bidcenter.com.cn/zhaobiao/zbkeyw-24187-0-0-0.html",
        "keywords": ["招标代理", "造价咨询", "服务商采购", "石家庄"],
        "collectedAt": "2026-05-10",
        "slot": "晚间",
        "budget": "未公开",
        "region": "河北石家庄藁城区",
        "description": "地区：河北石家庄藁城区；招标编号：CTZX-202605010；招标人：河北国津天创污水处理有限责任公司；采购内容：招标代理及造价咨询服务商；发布时间：2026年5月8日"
    },
    {
        "id": max_id + 3,
        "title": "宽城满族自治县生活污水处理厂改扩建项目招标代理服务造价咨询服务采购",
        "pubDate": "2026-05-07",
        "source": "河北招标网",
        "link": "https://hbs.bidcenter.com.cn/zhaobiao/zbkeyw-24187-0-0-0.html",
        "keywords": ["招标代理服务", "造价咨询服务", "污水处理厂", "宽城"],
        "collectedAt": "2026-05-10",
        "slot": "晚间",
        "budget": "未公开",
        "region": "河北承德宽城满族自治县",
        "description": "地区：河北承德宽城满族自治县滨河街286号；项目编号：DL2026023；项目名称：宽城满族自治县生活污水处理厂改扩建项目；采购内容：招标代理服务、造价咨询服务；响应文件递交截止：2026年5月18日09:30；发布时间：2026年5月7日"
    },
    {
        "id": max_id + 4,
        "title": "晟泰澜樾项目造价咨询服务项目竞争性磋商公告",
        "pubDate": "2026-05-07",
        "source": "河北招标网",
        "link": "https://hbs.bidcenter.com.cn/zhaobiao/zbkeyw-24187-0-0-0.html",
        "keywords": ["造价咨询服务", "竞争性磋商", "房地产项目"],
        "collectedAt": "2026-05-10",
        "slot": "晚间",
        "budget": "未公开",
        "region": "河北省",
        "description": "地区：河北省；项目名称：晟泰澜樾项目；采购内容：造价咨询服务；采购方式：竞争性磋商；发布时间：2026年5月7日"
    },
    {
        "id": max_id + 5,
        "title": "高铁片区南地下智慧车库项目结算审核造价咨询机构比选公告",
        "pubDate": "2026-05-07",
        "source": "河北招标网",
        "link": "https://hbs.bidcenter.com.cn/zhaobiao/zbkeyw-24187-0-0-0.html",
        "keywords": ["结算审核", "造价咨询", "智慧车库", "高铁片区"],
        "collectedAt": "2026-05-10",
        "slot": "晚间",
        "budget": "未公开",
        "region": "河北省",
        "description": "地区：河北省；项目规模：总建筑面积14803.84平方米，地上64平方米，地下14739.84平方米，人防面积4646.53平方米，总停车位391辆(含充电桩停车位124辆)；采购内容：结算审核造价咨询服务；发布时间：2026年5月7日"
    },
    {
        "id": max_id + 6,
        "title": "蠡县留史镇坑塘治理工程结算审核造价咨询服务项目竞争性磋商公告",
        "pubDate": "2026-05-07",
        "source": "中国政府采购网",
        "link": "http://www.ccgp.gov.cn/cggg/dfgg/gkzb/202605/t20260507_26520000.htm",
        "keywords": ["结算审核", "造价咨询服务", "坑塘治理", "蠡县"],
        "collectedAt": "2026-05-10",
        "slot": "晚间",
        "budget": "未公开",
        "region": "河北保定蠡县",
        "description": "地区：河北保定蠡县建设路22号；采购项目编号：HCGCC202604002；采购人：蠡县留史镇人民政府；采购内容：坑塘治理工程结算审核造价咨询服务；采购方式：竞争性磋商；发布时间：2026年5月7日"
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
