#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
招标公告下午更新脚本 - 2026年5月27日
抓取京津冀地区最新招标公告
"""

import json
from datetime import datetime

# 读取现有数据
with open('data/announcements.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 获取当前最大ID
max_id = max([a.get('id', 0) for a in data['announcements']]) if data['announcements'] else 0
print(f"当前最大ID: {max_id}")

# 现有公告标题（用于去重）
existing_titles = {a.get('title', '') for a in data['announcements']}
print(f"现有公告数量: {len(existing_titles)}")

# 2026年5月27日下午新增的公告数据（5个工作日内：5月20日-5月27日）
new_announcements = [
    {
        "id": max_id + 1,
        "title": "中国中医科学院眼科医院国家中医药传承创新中心建设项目基建工程工程量清单及最高投标限价编制竞争性磋商",
        "pubDate": "2026-05-26",
        "source": "中国政府采购网",
        "link": "http://www.ccgp.gov.cn/cggg/zygg/jzxcs/202605/t20260526_26630379.htm",
        "keywords": ["造价咨询", "清单编制", "最高投标限价", "石景山区"],
        "collectedAt": "2026-05-27",
        "slot": "下午",
        "budget": "8.57万元",
        "region": "北京石景山",
        "description": "地区：北京石景山区；采购单位：中国中医科学院眼科医院；项目编号：B0708-CMC26N7394；预算金额：8.57万元；服务内容：基建工程工程量清单及最高投标限价编制；合同履行期限：30个日历日；采购方式：竞争性磋商；特定资格要求：须为中央政府采购网工程造价咨询服务定点供应商；响应文件开启时间：2026年6月8日14:30"
    },
    {
        "id": max_id + 2,
        "title": "南开大学津南校区学生公寓(二期)项目全过程造价咨询服务中标公告",
        "pubDate": "2026-05-27",
        "source": "中国政府采购网",
        "link": "http://www.ccgp.gov.cn/cggg/zygg/zbgg/202605/t20260527_26643402.htm",
        "keywords": ["全过程造价咨询", "造价咨询", "中标公告", "南开大学"],
        "collectedAt": "2026-05-27",
        "slot": "下午",
        "budget": "84万元",
        "region": "天津",
        "description": "地区：天津市；采购单位：南开大学；项目编号：NK2026F036；中标金额：84万元；中标供应商：北京建智达工程管理股份有限公司；服务内容：全过程造价咨询服务；合同履行期限：自签订造价咨询服务合同之日起至合同约定范围内所有造价咨询报告完成并通过审查合格之日止；发布时间：2026年5月27日"
    },
    {
        "id": max_id + 3,
        "title": "中国科学院遗传与发育生物学研究所实验温室修缮(三期)项目和生物技术育种基地科研综合楼本体修缮项目造价咨询服务采购竞争性磋商",
        "pubDate": "2026-05-21",
        "source": "中国政府采购网",
        "link": "http://www.ccgp.gov.cn/cggg/zygg/jzxcs/202605/t20260521_26608567.htm",
        "keywords": ["造价咨询", "全过程跟踪造价咨询", "朝阳区"],
        "collectedAt": "2026-05-27",
        "slot": "下午",
        "budget": "49万元",
        "region": "北京朝阳",
        "description": "地区：北京朝阳区；采购单位：中国科学院遗传与发育生物学研究所；项目编号：HSZT2026FC/047；预算金额：49万元（实验温室修缮（三期）10万元+生物技术育种基地科研综合楼本体修缮39万元）；服务内容：全过程跟踪造价咨询服务，从编制清单和招标控制价至项目通过院验收为止；合同履行期限：自合同签订之日开始实施至竣工结算审计完成；采购方式：竞争性磋商；响应文件开启时间：2026年6月1日09:30"
    },
    {
        "id": max_id + 4,
        "title": "廊坊经济技术开发区东部片区基础设施及配套工程(一期)全过程造价咨询公开招标中标公告",
        "pubDate": "2026-05-22",
        "source": "中国政府采购网河北分网",
        "link": "http://www.ccgp.gov.cn/cggg/dfgg/zbgg/202605/t20260522_26612120.htm",
        "keywords": ["全过程造价咨询", "造价咨询", "廊坊", "中标公告"],
        "collectedAt": "2026-05-27",
        "slot": "下午",
        "budget": "71万元",
        "region": "河北廊坊",
        "description": "地区：河北廊坊；采购单位：廊坊经济技术开发区住房和城乡建设局本级；项目编号：Z1310002600802001；中标金额：71万元；中标供应商：中大宇辰项目管理有限公司；服务范围：道路及配套设施工程（含交通标线、道路绿化）、桥梁工程、给排水工程、热力工程、电力排管工程、照明工程等全过程造价咨询；合同履行期限：自签订合同之日开始实施至工程完成竣工结算终止；发布时间：2026年5月22日"
    },
]

# 过滤重复公告
added_count = 0
for ann in new_announcements:
    if ann['title'] not in existing_titles:
        data['announcements'].insert(0, ann)
        existing_titles.add(ann['title'])
        added_count += 1
        print(f"✅ 新增: {ann['title'][:50]}...")
    else:
        print(f"⏭️ 跳过（已存在）: {ann['title'][:50]}...")

# 更新元数据
data['lastUpdate'] = datetime.now().strftime('%Y-%m-%d %H:%M')
data['totalCount'] = len(data['announcements'])

# 保存更新后的数据
with open('data/announcements.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"\n✅ 数据更新完成！")
print(f"   - 新增公告: {added_count} 条")
print(f"   - 总计公告: {data['totalCount']} 条")
print(f"   - 最后更新: {data['lastUpdate']}")
