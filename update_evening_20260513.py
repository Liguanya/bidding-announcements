#!/usr/bin/env python3
"""
招标公告晚间更新脚本 - 京津冀地区 (2026年5月13日)
仅保留京津冀地区的造价咨询相关招标公告
更新时间：2026年5月13日 18:30
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
        "title": "2026年雄安新区房屋建筑和市政基础设施工程勘察设计质量抽查技术服务项目",
        "pubDate": "2026-05-11",
        "source": "中国政府采购网",
        "link": "http://www.ccgp.gov.cn/cggg/dfgg/zbgg/202605/t20260511_26543872.htm",
        "keywords": ["勘察设计质量抽查", "技术服务", "房屋建筑", "市政基础设施", "工程咨询"],
        "collectedAt": "2026-05-13",
        "slot": "晚间",
        "budget": "149.6万元",
        "region": "雄安新区",
        "description": "地区：雄安新区；采购单位：河北雄安新区建设和交通管理局；项目编号：GXTC-A1-261330016；服务内容：雄安新区房屋建筑和市政基础设施工程勘察设计质量抽查技术服务；分为4个标包，中标单位包括河北博瓴工程咨询、河北朗坤工程咨询等；发布时间：2026年5月11日"
    },
    {
        "id": max_id + 2,
        "title": "子牙新河献县段治理工程全过程造价咨询竞争性磋商",
        "pubDate": "2026-05-11",
        "source": "中国政府采购网",
        "link": "https://www.ccgp-hebei.gov.cn/BidWinAnncFiles/3e66a839-3ff2-4716-9bfb-0d462a95fdd7.pdf",
        "keywords": ["全过程造价咨询", "水利工程", "河道治理", "献县", "沧州"],
        "collectedAt": "2026-05-13",
        "slot": "晚间",
        "budget": "未公开",
        "region": "河北沧州",
        "description": "地区：河北沧州献县；服务内容：子牙新河献县段治理工程全过程造价咨询；采购方式：竞争性磋商；发布时间：2026年5月11日"
    },
    {
        "id": max_id + 3,
        "title": "天津市滨海新区土地发展中心造价咨询服务更正公告",
        "pubDate": "2026-05-08",
        "source": "中国政府采购网",
        "link": "http://www.ccgp.gov.cn/cggg/dfgg/gzgg/202605/t20260508_26530532.htm",
        "keywords": ["造价咨询服务", "更正公告", "土地发展"],
        "collectedAt": "2026-05-13",
        "slot": "晚间",
        "budget": "未公开",
        "region": "天津滨海新区",
        "description": "地区：天津滨海新区；采购单位：天津市滨海新区土地发展中心；项目编号：TJJH-2026-FW032；服务内容：造价咨询服务；首次公告日期：2026年4月29日；更正内容：招标文件技术要求调整；投标截止时间：2026年5月20日10点"
    },
    {
        "id": max_id + 4,
        "title": "天津市北辰区财政局2026年度财政投资项目评审项目合同公告",
        "pubDate": "2026-05-12",
        "source": "机电产品招标投标电子交易平台",
        "link": "https://www.chinabidding.com/bidDetail/262928338-BidResult.html",
        "keywords": ["财政投资评审", "造价咨询", "合同公告"],
        "collectedAt": "2026-05-13",
        "slot": "晚间",
        "budget": "120万元",
        "region": "天津北辰区",
        "description": "地区：天津北辰区；采购单位：天津市北辰区财政局机关；项目编号：XYCG-2026-019；中标单位：天津兴业工程咨询有限公司；合同金额：120万元；服务期限：2026年5月8日至2027年5月7日；服务内容：2026年度财政投资项目评审"
    },
    {
        "id": max_id + 5,
        "title": "公共服务平台(二期)监理服务",
        "pubDate": "2026-05-09",
        "source": "北京市公共资源交易服务平台",
        "link": "https://ggzyfw.beijing.gov.cn/jyxxcggg/20260509/5524321.html",
        "keywords": ["监理服务", "项目管理", "全过程咨询"],
        "collectedAt": "2026-05-13",
        "slot": "晚间",
        "budget": "12万元",
        "region": "北京",
        "description": "地区：北京；采购单位：北京市科学技术委员会、中关村科技园区管理委员会综合事务中心；项目编号：1100002****200165591-XM001；服务内容：公共服务平台(二期)项目启动、执行、验收等全过程的项目管理，质量控制、进度控制、投资控制、变更控制、合同管理、文档管理、安全管理及组织协调等；服务期限：自签订合同之日起一年；开标时间：2026年6月1日09:30"
    },
    {
        "id": max_id + 6,
        "title": "公共服务平台(二期)测评服务",
        "pubDate": "2026-05-09",
        "source": "北京市公共资源交易服务平台",
        "link": "https://ggzyfw.beijing.gov.cn/jyxxcggg/20260509/5524321.html",
        "keywords": ["测评服务", "软件测试", "性能测试"],
        "collectedAt": "2026-05-13",
        "slot": "晚间",
        "budget": "32.6万元",
        "region": "北京",
        "description": "地区：北京；采购单位：北京市科学技术委员会、中关村科技园区管理委员会综合事务中心；项目编号：1100002****200165591-XM001；服务内容：公共服务平台(二期)项目的应用软件系统进行验收测评，包括功能测试、性能测试、可靠性、易用性、安全性测试等；服务期限：自签订合同之日起一年；开标时间：2026年6月1日09:30；专门面向中小企业采购"
    },
    {
        "id": max_id + 7,
        "title": "雄安高新区产业研究院项目(一期)勘察设计(二次)招标公告",
        "pubDate": "2026-05-09",
        "source": "雄安新区公共资源交易中心",
        "link": "https://ggzyfw.beijing.gov.cn/xtggxazbgg/20260509/5524422.html",
        "keywords": ["勘察设计", "产业研究院", "全过程咨询", "BIM"],
        "collectedAt": "2026-05-13",
        "slot": "晚间",
        "budget": "1094.40161万元",
        "region": "雄安新区",
        "description": "地区：雄安新区昝岗组团；采购单位：雄安高新科创发展有限公司；项目业主：雄安高新科创发展有限公司；招标代理：天津市泛亚工程咨询有限公司；服务内容：包括勘察服务（初勘、详勘、补勘、基坑支护设计、基坑监测设计等）和设计服务（方案设计、初步设计、施工图设计、幕墙、泛光照明、高低压变配电、燃气、热力、海绵城市、智慧城市及建筑智能化、绿建设计及咨询、人防、BIM专项等）；最高投标限价：1094.40161万元；项目总投资约8.3亿；总建筑面积约85600平方米"
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
