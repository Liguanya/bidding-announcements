#!/usr/bin/env python3
"""
招标公告下午更新脚本 - 京津冀地区 (2026年5月10日)
仅保留京津冀地区的造价咨询相关招标公告
更新时间：2026年5月10日 13:50
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

# 京津冀地区新增公告数据 (2026年5月9日-10日最新发现)
new_announcements = [
    {
        "id": max_id + 1,
        "title": "廊坊市第二十中学分校项目全过程造价咨询服务公开招标",
        "pubDate": "2026-05-09",
        "source": "河北省公共资源交易服务平台",
        "link": "http://www.hebpr.cn/hbggfwpt/",
        "keywords": ["全过程造价咨询", "学校建设", "教育项目", "廊坊"],
        "collectedAt": "2026-05-10",
        "slot": "下午",
        "budget": "未公开",
        "region": "河北廊坊",
        "description": "地区：河北廊坊；项目名称：廊坊市第二十中学分校项目；服务内容：全过程造价咨询服务；发布时间：2026年5月9日"
    },
    {
        "id": max_id + 2,
        "title": "空天智能产品生产及研发项目全过程咨询管理招标",
        "pubDate": "2026-05-10",
        "source": "河北省公共资源交易服务平台",
        "link": "https://m.bidizhaobiao.com/info-770366260.html",
        "keywords": ["全过程咨询", "造价咨询", "工程监理", "项目管理", "空天智能", "产业园区"],
        "collectedAt": "2026-05-10",
        "slot": "下午",
        "budget": "186.5万元",
        "region": "河北廊坊经济技术开发区",
        "description": "地区：河北廊坊经济技术开发区创业路以东、祥云道以南；项目业主：河北时空星通技术有限公司；总用地面积30013.56平方米（约45.02亩），总建筑面积30571.83平方米；服务内容：全过程咨询（项目管理+全过程造价咨询+工程建设监理）；投标最高限价：186.5万元，其中全过程造价咨询最高限价48.5万元；招标文件获取截止：2026年5月14日；投标截止：2026年5月30日9:30"
    },
    {
        "id": max_id + 3,
        "title": "重点城市界面沿线风貌一体化设计项目招标",
        "pubDate": "2026-05-08",
        "source": "中国政府采购网",
        "link": "http://www.ccgp.gov.cn/cggg/dfgg/gkzb/202605/t20260508_26525045.htm",
        "keywords": ["城市设计", "风貌一体化", "雄安新区", "规划咨询"],
        "collectedAt": "2026-05-10",
        "slot": "下午",
        "budget": "160万元",
        "region": "河北雄安新区",
        "description": "地区：河北雄安新区；采购单位：河北雄安新区自然资源和规划局；项目编号：ZCZX2026015；预算金额：160万元；采购内容：针对启动区东西轴、燕赵大街、渥城路、白洋淀路等重要城市界面，开展风貌一体化设计，深化界面贴线、建筑高度、立面形式等核心要素设计统筹；获取招标文件：2026年5月9日至15日；开标时间：2026年5月29日09:00；合同履行期限：12个月"
    },
    {
        "id": max_id + 4,
        "title": "霸州市财政局投资评审货物和服务类项目预算评审服务机构采购",
        "pubDate": "2026-05-09",
        "source": "河北省公共资源交易服务平台",
        "link": "http://www.hebpr.cn/hbggfwpt/",
        "keywords": ["预算评审", "投资评审", "造价咨询", "财政评审", "服务采购"],
        "collectedAt": "2026-05-10",
        "slot": "下午",
        "budget": "未公开",
        "region": "河北廊坊霸州市",
        "description": "地区：河北廊坊霸州市；采购单位：霸州市财政局；服务内容：货物和服务类项目预算评审服务机构采购；发布时间：2026年5月9日"
    },
    {
        "id": max_id + 5,
        "title": "北京协和医院国家医学中心（雄安院区）一期建设项目施工总承包招标",
        "pubDate": "2026-05-06",
        "source": "中国招标投标公共服务平台",
        "link": "http://m.toutiao.com/group/7636736382639096363/",
        "keywords": ["施工总承包", "医院建设", "国家医学中心", "雄安新区", "造价咨询机会"],
        "collectedAt": "2026-05-10",
        "slot": "下午",
        "budget": "约36亿元",
        "region": "河北雄安新区",
        "description": "地区：雄安新区起步区第五组团E08-03-07地块；项目业主：中国医学科学院北京协和医院；总建筑面积365743㎡，地上254883.91㎡，地下110859.09㎡；估算投资约36亿元；招标范围：图纸范围内所有工程施工内容（不含已完成土护降工程）；资格预审文件获取：2026年5月6日至12日；申请文件递交截止：2026年5月18日09:00"
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
