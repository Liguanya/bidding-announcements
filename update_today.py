import json

# 读取现有数据
with open('data/announcements.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 今天下午新增的公告（从搜索结果中提取）
new_announcements = [
    {
        "id": 178,
        "title": "贵州省农业农村厅2026年耕地种植用途管控及病虫害防控项目招标代理机构比选公告",
        "pubDate": "2026-04-23",
        "source": "贵州省农业农村厅",
        "link": "http://m.toutiao.com/group/7631847996581216808/",
        "keywords": ["招标代理"],
        "collectedAt": "2026-04-29",
        "slot": "下午",
        "budget": "未知",
        "description": "地区：贵州贵阳；采购单位：贵州省农业农村厅；比选1家招标代理机构；服务范围：2026年耕地种植用途管控“一张图”项目和粮油及重要经济作物病虫害绿色防控新技术、新产品研发项目的政府采购代理业务；报名截止：2026-04-27 17:00；响应文件截止：2026-04-28 15:00"
    },
    {
        "id": 179,
        "title": "宁波某单位2026-2028年招标代理机构入围遴选项目公开招标公告",
        "pubDate": "2026-04-08",
        "source": "国信招投标公共服务平台",
        "link": "https://www.gxzbcg.com.cn/dlcgxx/219047.html",
        "keywords": ["招标代理"],
        "collectedAt": "2026-04-29",
        "slot": "下午",
        "budget": "未知",
        "description": "地区：浙江宁波；采购单位：宁波市某单位；入围家数：5家；服务期限：自合同签订生效之日起至2028年12月31日止；采购需求：政府采购、工程建设、服务外包项目代理；投标截止：2026-04-29 09:30"
    },
    {
        "id": 180,
        "title": "湖南省交通运输厅2026年造价审查及咨询服务专项重新立项招标公告",
        "pubDate": "2026-04-22",
        "source": "湖南省交通运输厅",
        "link": "https://www.chinamae.com/purchases/2c7d4df03bec8089c6f579928d1bbe4e.html",
        "keywords": ["造价咨询"],
        "collectedAt": "2026-04-29",
        "slot": "下午",
        "budget": "未知",
        "description": "地区：湖南长沙；采购单位：湖南省交通运输厅交通建设造价管理站；采购内容：2026年造价审查及咨询服务专项；服务范围包括交通建设项目工程造价审查、造价咨询及相关技术服务"
    },
    {
        "id": 181,
        "title": "某单位食堂食材采购项目公开招标公告",
        "pubDate": "2026-04-21",
        "source": "江苏省港口集团",
        "link": "http://m.toutiao.com/group/7631377121515930164/",
        "keywords": ["招标代理"],
        "collectedAt": "2026-04-29",
        "slot": "下午",
        "budget": "400万元",
        "description": "地区：江苏扬州；采购单位：南京港股份有限公司；招标代理：南京晔恒工程项目管理有限公司；两年采购总预算400万元（含税）；主要采购米、面、油、肉类、鱼类、蔬菜、冻品等；投标截止：2026-05-06 14:00"
    }
]

# 插入新公告到列表开头
for ann in new_announcements:
    # 检查是否已存在
    exists = any(a['id'] == ann['id'] for a in data['announcements'])
    if not exists:
        data['announcements'].insert(0, ann)

# 更新统计信息
data['lastUpdate'] = '2026-04-29 14:00'
data['totalCount'] = len(data['announcements'])

# 保存更新后的JSON
with open('data/announcements.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✅ JSON已更新")
print(f"   - 新增公告: {len(new_announcements)} 条")
print(f"   - 总计公告: {data['totalCount']} 条")
print(f"   - 更新时间: {data['lastUpdate']}")
