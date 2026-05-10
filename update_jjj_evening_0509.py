#!/usr/bin/env python3
"""
招标公告晚间更新脚本 - 京津冀地区 (2026-05-09)
仅保留京津冀地区的造价咨询相关招标公告
"""
import json
import subprocess
from datetime import datetime, timedelta
import os

# 读取现有数据
with open('data/announcements.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 获取当前最大ID
max_id = max([a['id'] for a in data['announcements']]) if data['announcements'] else 0
print(f"当前最大ID: {max_id}, 当前总数: {data['totalCount']}")

# 京津冀地区新增公告数据 (2026年5月9日最新发现)
new_announcements = [
    {
        "id": max_id + 1,
        "title": "2026年~2028年造价咨询服务采购公告",
        "pubDate": "2026-05-09",
        "source": "乙方宝/阳光招采",
        "link": "http://www.yfbzb.com/inviteBid/detail/20260509_595512991.html",
        "keywords": ["全过程造价", "造价咨询", "跟踪审计", "成本管理"],
        "collectedAt": "2026-05-09",
        "slot": "晚间",
        "budget": "协议期内",
        "region": "北京",
        "description": "地区：北京；采购内容：2026-2028年造价咨询服务；服务范围：方案成本测算、预结算编制与审核、工程量清单及标底编制、清标、进度款审核、动态成本监控等全过程造价咨询服务"
    },
    {
        "id": max_id + 2,
        "title": "南开大学国家基础研究创新提升工程建设项目（化学）全过程造价咨询服务公开招标公告",
        "pubDate": "2026-05-07",
        "source": "中国政府采购网天津分网",
        "link": "https://m.bidcenter.com.cn/news-1-417646829.html",
        "keywords": ["全过程造价", "造价咨询", "南开大学"],
        "collectedAt": "2026-05-09",
        "slot": "晚间",
        "budget": "100万元（最高限价80万元）",
        "region": "天津",
        "description": "地区：天津南开区；采购单位：南开大学；预算100万元，最高限价80万元；开标时间2026年6月2日"
    },
    {
        "id": max_id + 3,
        "title": "南开大学国家基础研究创新提升工程建设项目（生物学）全过程造价咨询服务公开招标公告",
        "pubDate": "2026-05-07",
        "source": "中国政府采购网天津分网",
        "link": "https://m.bidcenter.com.cn/news-1-417624207.html",
        "keywords": ["全过程造价", "造价咨询", "南开大学"],
        "collectedAt": "2026-05-09",
        "slot": "晚间",
        "budget": "100万元（最高限价75万元）",
        "region": "天津",
        "description": "地区：天津南开区；采购单位：南开大学；预算100万元，最高限价75万元；开标时间2026年6月1日"
    },
    {
        "id": max_id + 4,
        "title": "河北承德医院2026-2027年造价咨询机构框架协议采购项目征集公告",
        "pubDate": "2026-05-08",
        "source": "采招网",
        "link": "https://m.bidcenter.com.cn/news-1-417875000.html",
        "keywords": ["造价咨询", "框架协议"],
        "collectedAt": "2026-05-09",
        "slot": "晚间",
        "budget": "框架协议2年",
        "region": "河北承德",
        "description": "地区：河北承德双桥区；采购单位：河北承德医院；合同期限2年；入围数量按有效响应供应商80%计算"
    },
    {
        "id": max_id + 5,
        "title": "2026年北京普通公路健康工程造价咨询第1标段",
        "pubDate": "2026-04-20",
        "source": "北京市交通委员会",
        "link": "https://jtw.beijing.gov.cn/xxgk/ztbxx/202604/t20260420_4597184.html",
        "keywords": ["造价咨询", "公路工程", "结算审核"],
        "collectedAt": "2026-05-09",
        "slot": "晚间",
        "budget": "79万元",
        "region": "北京",
        "description": "地区：北京；服务区域：通州/怀柔/密云/平谷/房山/全市高速；服务内容：工程量复核、定额审核、决结算审核等；截止时间2026年5月11日"
    },
    {
        "id": max_id + 6,
        "title": "2026年北京普通公路健康工程造价咨询第2标段",
        "pubDate": "2026-04-20",
        "source": "北京市交通委员会",
        "link": "https://jtw.beijing.gov.cn/xxgk/ztbxx/202604/t20260420_4597184.html",
        "keywords": ["造价咨询", "公路工程", "结算审核"],
        "collectedAt": "2026-05-09",
        "slot": "晚间",
        "budget": "83万元",
        "region": "北京",
        "description": "地区：北京；服务区域：顺义/大兴/门头沟/昌平/延庆；服务内容：工程量复核、定额审核、决结算审核等；截止时间2026年5月11日"
    },
    {
        "id": max_id + 7,
        "title": "天津市滨海新区土地发展中心造价咨询服务更正公告",
        "pubDate": "2026-05-08",
        "source": "中国政府采购网天津分网",
        "link": "http://www.ccgp.gov.cn/cggg/dfgg/gzgg/202605/t20260508_26530532.htm",
        "keywords": ["造价咨询"],
        "collectedAt": "2026-05-09",
        "slot": "晚间",
        "budget": "90万元（6个包，每包15万元）",
        "region": "天津滨海新区",
        "description": "地区：天津滨海新区；采购单位：天津市滨海新区土地发展中心；更正内容：服务人员资质要求等；开标时间2026年5月20日"
    },
    {
        "id": max_id + 8,
        "title": "北京协和医院国家医学中心(雄安院区)一期建设项目施工总承包资格预审公告",
        "pubDate": "2026-05-06",
        "source": "雄安新区公共资源交易平台",
        "link": "http://m.toutiao.com/group/7636736382639096363/",
        "keywords": ["施工总承包", "医院建设", "雄安新区"],
        "collectedAt": "2026-05-09",
        "slot": "晚间",
        "budget": "约36亿元",
        "region": "雄安新区",
        "description": "地区：雄安新区起步区第五组团；建筑面积365743㎡；工期42个月；含临床转化综合楼、科研楼、多粒子诊疗中心等"
    },
    {
        "id": max_id + 9,
        "title": "廊坊经济技术开发区东部片区基础设施及配套工程(一期)全过程造价咨询",
        "pubDate": "2026-04-28",
        "source": "河北省公共资源交易平台",
        "link": "https://szj.hebei.gov.cn/hbggfwpt/jydt/003001/003001001/003001001001/20260428/bf208ea1-44ae-4f6b-a109-0dd90621e392.html",
        "keywords": ["全过程造价", "造价咨询", "市政基础设施"],
        "collectedAt": "2026-05-09",
        "slot": "晚间",
        "budget": "157.642万元",
        "region": "河北廊坊",
        "description": "地区：河北廊坊；采购单位：廊坊经济技术开发区住房和城乡建设局；服务范围：道路、桥梁、给排水、热力、电力等全过程造价咨询；开标时间2026年5月21日"
    },
    {
        "id": max_id + 10,
        "title": "石景山区黄庄村棚户区改造项目(方案设计、初步设计、施工图设计)招标公告",
        "pubDate": "2026-05-07",
        "source": "北京造价信息网",
        "link": "https://bj.bidcenter.com.cn/zhaobiao/zbkeyw-24187-0-1-100.html",
        "keywords": ["设计招标", "棚户区改造", "造价"],
        "collectedAt": "2026-05-09",
        "slot": "晚间",
        "budget": "未知",
        "region": "北京石景山",
        "description": "地区：北京石景山区；项目名称：黄庄村43号棚户区改造项目SS00-1622-002、SS00-2501-002地块"
    }
]

print(f"准备新增 {len(new_announcements)} 条公告")

# 合并新数据
data['announcements'].extend(new_announcements)

# 更新统计
data['totalCount'] = len(data['announcements'])
data['lastUpdate'] = datetime.now().strftime('%Y-%m-%d %H:%M')

# 按日期排序
data['announcements'].sort(key=lambda x: (x['pubDate'], x['id']), reverse=True)

# 保存JSON
with open('data/announcements.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"JSON已更新，总数: {data['totalCount']}")
print("更新完成!")
