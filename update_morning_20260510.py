#!/usr/bin/env python3
"""
招标公告早间更新脚本 - 京津冀地区 (2026年5月10日)
仅保留京津冀地区的造价咨询相关招标公告
更新时间：2026年5月10日 08:46
"""
import json
from datetime import datetime, timedelta
import os

# 读取现有数据
data_path = '/app/data/所有对话/主对话/bidding-announcements/data/announcements.json'
with open(data_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# 获取当前最大ID
max_id = max([a['id'] for a in data['announcements']]) if data['announcements'] else 0
print(f"当前最大ID: {max_id}, 当前总数: {data['totalCount']}")

# 京津冀地区新增公告数据 (2026年5月8日-10日最新发现)
new_announcements = [
    {
        "id": max_id + 1,
        "title": "2026年度工程造价编制及审核服务项目招标公告",
        "pubDate": "2026-05-08",
        "source": "采招网",
        "link": "https://m.bidcenter.com.cn/news-1-417853104.html",
        "keywords": ["工程造价编制", "审核服务", "年度框架", "3年服务期"],
        "collectedAt": "2026-05-10",
        "slot": "早间",
        "budget": "3年框架协议，按实际委托项目计算",
        "region": "北京房山区",
        "description": "地区：北京房山区；采购内容：包1-年度工程造价编制服务（工程量清单及招标控制价编制），包2-年度工程造价审核服务；服务周期：合同签订之日起3年，采取\"1+1+1\"模式逐年签订；截止时间：2026年5月15日"
    },
    {
        "id": max_id + 2,
        "title": "北京市退休职工活动站2026年度造价咨询单位选取",
        "pubDate": "2026-05-08",
        "source": "招标网",
        "link": "https://rl.zhaobiao.cn/bidding_v_36c2ce020e6def5d8ef17fc7e2d467ba.html",
        "keywords": ["造价咨询", "清单编制", "限价编制", "预结算评审"],
        "collectedAt": "2026-05-10",
        "slot": "早间",
        "budget": "按实际委托项目计算，参照京标价协(2022)71号",
        "region": "北京",
        "description": "地区：北京市；项目内容：工程量清单编制、最高投标限价编制及预（结）算评审工作；报名截止：2026年5月18日；报价网址：http://zjfw.beijing.gov.cn"
    },
    {
        "id": max_id + 3,
        "title": "密云水库2026年造价咨询服务",
        "pubDate": "2026-05-07",
        "source": "北京造价信息网",
        "link": "https://www.bidizhaobiao.com/tag_2_46/",
        "keywords": ["造价咨询", "水利工程", "水库项目"],
        "collectedAt": "2026-05-10",
        "slot": "早间",
        "budget": "未公开",
        "region": "北京密云区",
        "description": "地区：北京密云区；采购内容：密云水库相关工程项目造价咨询服务"
    },
    {
        "id": max_id + 4,
        "title": "月亮河片区景观亮化提升工程（招标及造价咨询）比选公告",
        "pubDate": "2026-05-07",
        "source": "北京造价信息网",
        "link": "https://www.bidizhaobiao.com/tag_2_46/",
        "keywords": ["造价咨询", "景观亮化", "招标代理", "市政工程"],
        "collectedAt": "2026-05-10",
        "slot": "早间",
        "budget": "未公开",
        "region": "北京通州区",
        "description": "地区：北京通州区；项目名称：月亮河片区景观亮化提升工程；服务内容：招标代理及造价咨询服务"
    },
    {
        "id": max_id + 5,
        "title": "顺义区北京会展商务区周边及汽车创新走廊带环境整治提升项目造价咨询",
        "pubDate": "2026-05-07",
        "source": "北京造价信息网",
        "link": "https://www.bidizhaobiao.com/tag_2_46/",
        "keywords": ["造价咨询", "环境整治", "市政工程", "会展商务区"],
        "collectedAt": "2026-05-10",
        "slot": "早间",
        "budget": "未公开",
        "region": "北京顺义区",
        "description": "地区：北京顺义区；项目名称：北京会展商务区周边及汽车创新走廊带环境整治提升项目；服务内容：造价咨询服务"
    },
    {
        "id": max_id + 6,
        "title": "2026年~2028年造价咨询服务采购公告",
        "pubDate": "2026-05-09",
        "source": "乙方宝/阳光招采",
        "link": "http://www.yfbzb.com/inviteBid/detail/20260509_595512991.html",
        "keywords": ["全过程造价", "造价咨询", "跟踪审计", "成本管理", "数据机房"],
        "collectedAt": "2026-05-10",
        "slot": "早间",
        "budget": "协议期内，按实际项目计算",
        "region": "北京丰台区",
        "description": "地区：北京丰台区佑安国际大厦；采购内容：方案成本测算、预结算编制与审核、工程量清单及标底编制、清标、变更签证审核、进度款审核、动态成本监控等全过程造价咨询服务；业绩要求：能源类或数据机房IDC类或地产类至少1项全过程造价咨询业绩"
    },
    {
        "id": max_id + 7,
        "title": "中国铁路北京局集团有限公司邯郸机务段委托第三方工程造价咨询服务项目",
        "pubDate": "2026-05-08",
        "source": "北京招标网",
        "link": "https://bj.bidcenter.com.cn/zhaobiao/zbkeyw-17032-0-1-0.html",
        "keywords": ["工程造价咨询", "铁路工程", "零小工程", "投资控制"],
        "collectedAt": "2026-05-10",
        "slot": "早间",
        "budget": "未公开",
        "region": "河北邯郸",
        "description": "地区：河北邯郸（京津冀区域）；采购单位：中国铁路北京局集团有限公司邯郸机务段；采购内容：零小工程项目工程造价咨询服务；采购方式：竞争性谈判"
    },
    {
        "id": max_id + 8,
        "title": "唐山车务段2026年度零小工程项目造价咨询审核服务采购公告",
        "pubDate": "2026-05-08",
        "source": "北京招标网",
        "link": "https://bj.bidcenter.com.cn/zhaobiao/zbkeyw-17032-0-1-0.html",
        "keywords": ["造价咨询", "审核服务", "铁路工程", "零小工程"],
        "collectedAt": "2026-05-10",
        "slot": "早间",
        "budget": "未公开",
        "region": "河北唐山",
        "description": "地区：河北唐山（京津冀区域）；采购单位：中国铁路北京局集团有限公司唐山车务段；项目编号：2026-BJ-FW-XFZB-TJHB-QF124-2；采购内容：2026年度零小工程项目造价咨询审核服务"
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
