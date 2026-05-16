#!/usr/bin/env python3
"""
招标公告下午更新脚本 - 京津冀地区 (2026年5月16日)
仅保留京津冀地区的造价咨询相关招标公告
更新时间：2026年5月16日 13:50
"""
import json
from datetime import datetime
import os

# 读取现有数据
data_path = 'data/announcements.json'
with open(data_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# 获取当前最大ID
max_id = max([a['id'] for a in data['announcements']]) if data['announcements'] else 0
print(f"当前最大ID: {max_id}, 当前总数: {data['totalCount']}")

# 京津冀地区新增公告数据 (2026年5月16日最新发现)
new_announcements = [
    {
        "id": max_id + 1,
        "title": "隆尧县农业农村局关于公开遴选2026年度新型农村集体经济发展项目造价咨询单位的公告",
        "pubDate": "2026-05-15",
        "source": "中国政府采购网",
        "link": "http://www.ccgp.gov.cn/",
        "keywords": ["造价咨询", "农村集体经济", "乡村振兴", "邢台", "遴选"],
        "collectedAt": "2026-05-16",
        "slot": "下午",
        "budget": "未公开",
        "region": "河北邢台",
        "description": "地区：河北邢台隆尧；采购单位：隆尧县农业农村局；服务内容：2026年度新型农村集体经济发展项目造价咨询单位遴选；发布时间：2026年5月15日"
    },
    {
        "id": max_id + 2,
        "title": "华油金地物业公司2026年工程造价咨询委托服务（二次）",
        "pubDate": "2026-05-15",
        "source": "中国招标投标公共服务平台",
        "link": "http://www.cebpubservice.com/",
        "keywords": ["造价咨询", "物业工程", "年度框架", "沧州", "二次招标"],
        "collectedAt": "2026-05-16",
        "slot": "下午",
        "budget": "未公开",
        "region": "河北沧州",
        "description": "地区：河北沧州；采购单位：华油金地物业公司；项目编号：HBYT-Z...；服务内容：2026年工程造价咨询委托服务；发布时间：2026年5月15日"
    },
    {
        "id": max_id + 3,
        "title": "易县县域充换电基础设施补短板试点项目造价咨询服务询比采购公告",
        "pubDate": "2026-05-15",
        "source": "冀中能源集团电子招标投标交易平台",
        "link": "http://www.jznyzb.com/",
        "keywords": ["造价咨询", "充换电设施", "新能源", "保定", "询比采购"],
        "collectedAt": "2026-05-16",
        "slot": "下午",
        "budget": "未公开",
        "region": "河北保定易县",
        "description": "地区：河北保定易县；采购单位：易县发展和改革局；服务内容：县域充换电基础设施补短板试点项目造价咨询服务；发布时间：2026年5月15日"
    },
    {
        "id": max_id + 4,
        "title": "张家口市第二医院医养结合服务能力建设项目造价咨询询比采购公告",
        "pubDate": "2026-05-15",
        "source": "中国华电集团电子商务平台",
        "link": "https://www.chd.com.cn/",
        "keywords": ["造价咨询", "医养结合", "医院建设", "张家口", "询比采购"],
        "collectedAt": "2026-05-16",
        "slot": "下午",
        "budget": "未公开",
        "region": "河北张家口",
        "description": "地区：河北张家口；采购单位：张家口市第二医院；服务内容：医养结合服务能力建设项目造价咨询；发布时间：2026年5月15日"
    },
    {
        "id": max_id + 5,
        "title": "正定新城91号地块造价咨询服务项目磋商公告",
        "pubDate": "2026-05-14",
        "source": "河北省公共资源交易服务平台",
        "link": "http://www.hebpr.gov.cn/",
        "keywords": ["造价咨询", "房地产开发", "地块建设", "石家庄正定", "竞争性磋商"],
        "collectedAt": "2026-05-16",
        "slot": "下午",
        "budget": "未公开",
        "region": "河北石家庄正定",
        "description": "地区：河北石家庄正定；采购单位：正定新区建设投资集团；服务内容：新城91号地块造价咨询服务项目；发布时间：2026年5月14日"
    },
    {
        "id": max_id + 6,
        "title": "[大兴区]大兴区瀛海镇京台西区级统筹地块九年一贯制学校建设项目工程造价咨询单位中标公告",
        "pubDate": "2026-05-14",
        "source": "北京市政府采购网",
        "link": "http://www.ccgp-beijing.gov.cn/",
        "keywords": ["造价咨询", "学校建设", "中标公告", "北京大兴", "工程量清单"],
        "collectedAt": "2026-05-16",
        "slot": "下午",
        "budget": "按收费标准优惠率35%",
        "region": "北京大兴",
        "description": "地区：北京大兴；采购单位：北京市大兴区瀛海镇人民政府；中标单位：北京京咨工程项目管理有限公司；中标优惠率：35%；服务内容：编制工程量清单及最高投标限价；项目负责人需具备注册造价工程师资格；发布时间：2026年5月14日"
    },
    {
        "id": max_id + 7,
        "title": "廊坊开发区广阳园区管网基础设施建设项目(南区)全过程造价咨询服务竞争性磋商公告",
        "pubDate": "2026-05-15",
        "source": "河北省公共资源交易服务平台",
        "link": "http://www.hebpr.gov.cn/",
        "keywords": ["全过程造价咨询", "管网建设", "基础设施", "廊坊", "竞争性磋商"],
        "collectedAt": "2026-05-16",
        "slot": "下午",
        "budget": "未公开",
        "region": "河北廊坊",
        "description": "地区：河北廊坊；采购单位：廊坊经济技术开发区住房和城乡建设局；服务内容：广阳园区管网基础设施建设项目(南区)全过程造价咨询服务；发布时间：2026年5月15日"
    },
    {
        "id": max_id + 8,
        "title": "天津商业大学双碳学科交叉与科技创新中心项目全过程造价审计咨询服务竞争性磋商公告",
        "pubDate": "2026-05-13",
        "source": "天津市政府采购网",
        "link": "http://www.ccgp-tianjin.gov.cn/",
        "keywords": ["全过程造价咨询", "审计咨询", "高校建设", "双碳项目", "天津"],
        "collectedAt": "2026-05-16",
        "slot": "下午",
        "budget": "未公开",
        "region": "天津",
        "description": "地区：天津；采购单位：天津商业大学；项目编号：TGPC-2026-D-0279；服务内容：双碳学科交叉与科技创新中心项目全过程造价审计咨询服务；采购方式：竞争性磋商；发布时间：2026年5月13日"
    }
]

print(f"准备新增 {len(new_announcements)} 条公告")

# 检查重复（根据标题去重）
existing_titles = {a.get('title', '') for a in data['announcements']}
unique_new = [a for a in new_announcements if a['title'] not in existing_titles]
print(f"去重后实际新增 {len(unique_new)} 条公告")

# 合并新数据
data['announcements'].extend(unique_new)

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
