#!/usr/bin/env python3
"""
修复数据并更新公告
"""
import json
from datetime import datetime

# 读取现有数据
data_path = '/app/data/所有对话/主对话/bidding-announcements/data/announcements.json'
with open(data_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f"修复前 - totalCount: {data['totalCount']}, 实际长度: {len(data['announcements'])}")

# 获取当前最大ID
max_id = max([a['id'] for a in data['announcements']]) if data['announcements'] else 0
print(f"当前最大ID: {max_id}")

# 京津冀地区新增公告数据
new_announcements = [
    {
        "id": max_id + 1,
        "title": "2026年度工程造价编制及审核服务项目招标公告",
        "pubDate": "2026-05-08",
        "source": "采招网",
        "link": "https://m.bidcenter.com.cn/news-1-417853104.html",
        "keywords": ["造价编制", "造价审核", "工程量清单", "招标控制价", "军队工程"],
        "collectedAt": "2026-05-11",
        "slot": "下午",
        "budget": "186.5万元",
        "region": "北京房山区",
        "description": "地区：北京房山区；服务范围：工程造价编制（包1）+工程造价审核（包2）；服务周期3年（1+1+1模式）；采用折扣率报价；开标时间：2026年5月27日"
    },
    {
        "id": max_id + 2,
        "title": "南开大学国家基础研究创新提升工程建设项目（化学）全过程造价咨询服务",
        "pubDate": "2026-05-07",
        "source": "采招网",
        "link": "https://m.bidcenter.com.cn/news-1-417646829.html",
        "keywords": ["全过程造价咨询", "高校建设", "化学实验室", "造价管理"],
        "collectedAt": "2026-05-11",
        "slot": "下午",
        "budget": "100万元（最高限价80万元）",
        "region": "天津南开区",
        "description": "地区：天津南开区；采购单位：南开大学；项目编号：NK2026F038；服务内容：招标及合同签订阶段、施工阶段、竣工结算阶段全过程工程造价咨询及管理；开标时间：2026年6月2日；专门面向中小企业采购"
    },
    {
        "id": max_id + 3,
        "title": "唐山市曹妃甸区农村公路改造提升项目造价咨询服务公开招标",
        "pubDate": "2026-05-08",
        "source": "河北省公共资源交易服务平台",
        "link": "http://ggzyjy.xzspj.tangshan.gov.cn/",
        "keywords": ["造价咨询", "农村公路", "交通建设", "清单编制", "控制价编制"],
        "collectedAt": "2026-05-11",
        "slot": "下午",
        "budget": "未公开",
        "region": "河北唐山曹妃甸区",
        "description": "地区：河北唐山曹妃甸区；采购单位：唐山市曹妃甸区住房和城乡建设局；服务内容：国家综合货运枢纽补链强链2025年农村公路改造提升项目造价咨询；采用双盲评审；开标时间：2026年5月21日"
    },
    {
        "id": max_id + 4,
        "title": "北京市退休职工活动站2026年度造价咨询单位选取",
        "pubDate": "2026-05-08",
        "source": "北京造价信息网",
        "link": "https://www.bidizhaobiao.com/tag_2_46/",
        "keywords": ["造价咨询", "年度框架", "政府投资"],
        "collectedAt": "2026-05-11",
        "slot": "下午",
        "budget": "未公开",
        "region": "北京",
        "description": "地区：北京；采购单位：北京市退休职工活动站；服务内容：2026年度造价咨询单位选取；发布时间：2026年5月8日"
    },
    {
        "id": max_id + 5,
        "title": "密云水库2026年造价咨询服务",
        "pubDate": "2026-05-07",
        "source": "北京造价信息网",
        "link": "https://www.bidizhaobiao.com/tag_2_46/",
        "keywords": ["造价咨询", "水利工程", "水库建设"],
        "collectedAt": "2026-05-11",
        "slot": "下午",
        "budget": "未公开",
        "region": "北京密云区",
        "description": "地区：北京密云区；服务内容：密云水库2026年造价咨询服务；发布时间：2026年5月7日"
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

print(f"修复后 - totalCount: {data['totalCount']}, 实际长度: {len(data['announcements'])}")
print(f"JSON已更新，总数: {data['totalCount']}")
print("更新完成!")
