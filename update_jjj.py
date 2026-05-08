import json
from datetime import datetime, timedelta

# 读取现有数据
with open('data/announcements.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 获取当前最大ID
max_id = max([a['id'] for a in data['announcements']]) if data['announcements'] else 0
print(f"当前最大ID: {max_id}, 当前总数: {data['totalCount']}")

# 京津冀地区新增公告数据 (2026年5月6日-8日)
new_announcements = [
    {
        "id": max_id + 1,
        "title": "北京市退休职工活动站2026年度造价咨询单位选取公告",
        "pubDate": "2026-05-08",
        "source": "北京造价信息网",
        "link": "https://www.bidizhaobiao.com/tag_2_46/",
        "keywords": ["造价咨询", "招标"],
        "collectedAt": "2026-05-08",
        "slot": "下午",
        "budget": "未知",
        "description": "地区：北京；采购单位：北京市退休职工活动站；项目名称：2026年度造价咨询单位选取"
    },
    {
        "id": max_id + 2,
        "title": "密云水库2026年造价咨询服务采购公告",
        "pubDate": "2026-05-07",
        "source": "北京造价信息网",
        "link": "https://www.bidizhaobiao.com/tag_2_46/",
        "keywords": ["造价咨询"],
        "collectedAt": "2026-05-08",
        "slot": "下午",
        "budget": "未知",
        "description": "地区：北京密云；采购内容：密云水库2026年造价咨询服务"
    },
    {
        "id": max_id + 3,
        "title": "月亮河片区景观亮化提升工程（招标及造价咨询）比选公告",
        "pubDate": "2026-05-07",
        "source": "北京造价信息网",
        "link": "https://www.bidizhaobiao.com/tag_2_46/",
        "keywords": ["造价咨询", "招标代理"],
        "collectedAt": "2026-05-08",
        "slot": "下午",
        "budget": "未知",
        "description": "地区：北京通州；项目名称：月亮河片区景观亮化提升工程；服务内容：招标代理及造价咨询"
    },
    {
        "id": max_id + 4,
        "title": "2026年通州区铁路沿线绿化提升项目（全过程造价咨询服务）成交结果公告",
        "pubDate": "2026-05-07",
        "source": "北京造价信息网",
        "link": "https://www.bidizhaobiao.com/tag_2_46/",
        "keywords": ["全过程造价", "造价咨询"],
        "collectedAt": "2026-05-08",
        "slot": "下午",
        "budget": "未知",
        "description": "地区：北京通州；项目名称：2026年通州区铁路沿线绿化提升项目；服务内容：全过程造价咨询服务"
    },
    {
        "id": max_id + 5,
        "title": "顺义区北京会展商务区周边及汽车创新走廊带环境整治提升项目造价咨询",
        "pubDate": "2026-05-07",
        "source": "北京造价信息网",
        "link": "https://www.bidizhaobiao.com/tag_2_46/",
        "keywords": ["造价咨询", "项目管理"],
        "collectedAt": "2026-05-08",
        "slot": "下午",
        "budget": "未知",
        "description": "地区：北京顺义；项目名称：北京会展商务区周边及汽车创新走廊带环境整治提升项目；服务内容：造价咨询"
    },
    {
        "id": max_id + 6,
        "title": "北京市平谷区南独乐河镇人民政府2026年造价咨询单位选聘中选公告",
        "pubDate": "2026-05-06",
        "source": "北京造价信息网",
        "link": "https://www.bidizhaobiao.com/tag_2_46/",
        "keywords": ["造价咨询"],
        "collectedAt": "2026-05-08",
        "slot": "下午",
        "budget": "未知",
        "description": "地区：北京平谷；采购单位：北京市平谷区南独乐河镇人民政府；项目名称：2026年招标代理服务单位、造价咨询单位、监理单位选聘项目"
    },
    {
        "id": max_id + 7,
        "title": "园区改造竣工结算造价咨询委托服务采购需求公示",
        "pubDate": "2026-05-06",
        "source": "北京工程造价招标信息网",
        "link": "https://m.yfbzb.com/zbzt/36/2/",
        "keywords": ["造价咨询", "结算审核"],
        "collectedAt": "2026-05-08",
        "slot": "下午",
        "budget": "未知",
        "description": "地区：北京；采购内容：园区改造竣工结算造价咨询委托服务"
    },
    {
        "id": max_id + 8,
        "title": "综能公司项目工程造价咨询结算框架服务采购公告",
        "pubDate": "2026-05-06",
        "source": "北京工程造价招标信息网",
        "link": "https://m.yfbzb.com/zbzt/36/2/",
        "keywords": ["造价咨询", "结算", "框架协议"],
        "collectedAt": "2026-05-08",
        "slot": "下午",
        "budget": "未知",
        "description": "地区：北京平谷；采购内容：综能公司项目工程造价咨询结算框架服务；报价截止：2026-05-09 17:00"
    },
    {
        "id": max_id + 9,
        "title": "首都医科大学附属北京同仁医院亦庄院区过敏性疾病创新药物国家工程研究中心新增10KV外电源建设项目造价咨询单位调研公示",
        "pubDate": "2026-05-01",
        "source": "北京工程造价招标信息网",
        "link": "https://m.yfbzb.com/zbzt/36/2/",
        "keywords": ["造价咨询", "10KV", "医院"],
        "collectedAt": "2026-05-08",
        "slot": "下午",
        "budget": "未知",
        "description": "地区：北京亦庄；采购单位：首都医科大学附属北京同仁医院；项目名称：亦庄院区过敏性疾病创新药物国家工程研究中心新增10KV外电源建设项目"
    },
    {
        "id": max_id + 10,
        "title": "窦店东区再生水厂项目工程（施工过程造价管理）竞争性磋商公告",
        "pubDate": "2026-04-30",
        "source": "北京工程造价招标信息网",
        "link": "https://m.yfbzb.com/zbzt/36/2/",
        "keywords": ["造价咨询", "全过程造价", "水厂"],
        "collectedAt": "2026-05-08",
        "slot": "下午",
        "budget": "未知",
        "description": "地区：北京；项目名称：窦店东区再生水厂项目工程；服务内容：施工过程造价管理"
    },
    {
        "id": max_id + 11,
        "title": "北京交通大学校园基础设施及校舍安全改造（供暖、配电设施改造、供电设备改造更新等）造价咨询项目竞争性磋商公告",
        "pubDate": "2026-04-30",
        "source": "北京工程造价招标信息网",
        "link": "https://m.yfbzb.com/zbzt/36/2/",
        "keywords": ["造价咨询", "校园", "配电"],
        "collectedAt": "2026-05-08",
        "slot": "下午",
        "budget": "未知",
        "description": "地区：北京；采购单位：北京交通大学；项目名称：校园基础设施及校舍安全改造造价咨询；服务内容：供暖、配电设施改造、供电设备改造更新等"
    },
    {
        "id": max_id + 12,
        "title": "北京金隅商业管理有限公司北京嘉品Mall项目品质提升及安全保障综合改造工程全过程造价咨询服务",
        "pubDate": "2026-04-29",
        "source": "北京工程造价招标信息网",
        "link": "https://m.yfbzb.com/zbzt/36/2/",
        "keywords": ["全过程造价", "造价咨询", "商业"],
        "collectedAt": "2026-05-08",
        "slot": "下午",
        "budget": "未知",
        "description": "地区：北京；采购单位：北京金隅商业管理有限公司；项目名称：北京嘉品Mall项目品质提升及安全保障综合改造工程；服务内容：全过程造价咨询服务"
    },
    {
        "id": max_id + 13,
        "title": "北京市延庆区小型水库管理中心2026年度工程建设项目预、结算审核造价咨询比选公告",
        "pubDate": "2026-04-28",
        "source": "北京工程造价招标信息网",
        "link": "https://m.yfbzb.com/zbzt/36/2/",
        "keywords": ["造价咨询", "结算审核", "水库"],
        "collectedAt": "2026-05-08",
        "slot": "下午",
        "budget": "未知",
        "description": "地区：北京延庆；采购单位：北京市延庆区小型水库管理中心；项目名称：2026年度工程建设项目预、结算审核造价咨询"
    },
    {
        "id": max_id + 14,
        "title": "北京市朝阳区芍药居北里电梯更新和无负压供水系统设备改造项目造价咨询服务比选公告",
        "pubDate": "2026-04-27",
        "source": "北京工程造价招标信息网",
        "link": "https://m.yfbzb.com/zbzt/36/2/",
        "keywords": ["造价咨询", "电梯改造", "老旧小区"],
        "collectedAt": "2026-05-08",
        "slot": "下午",
        "budget": "未知",
        "description": "地区：北京朝阳；项目名称：芍药居北里电梯更新和无负压供水系统设备改造项目；服务内容：造价咨询服务"
    },
    {
        "id": max_id + 15,
        "title": "北京万商花园酒店装修改造项目（全过程造价咨询）比选公告",
        "pubDate": "2026-04-27",
        "source": "北京工程造价招标信息网",
        "link": "https://m.yfbzb.com/zbzt/36/2/",
        "keywords": ["全过程造价", "造价咨询", "酒店"],
        "collectedAt": "2026-05-08",
        "slot": "下午",
        "budget": "未知",
        "description": "地区：北京；项目名称：北京万商花园酒店装修改造项目；服务内容：全过程造价咨询"
    },
    {
        "id": max_id + 16,
        "title": "北京市朝阳区大西洋新城38台电梯更新工程造价咨询服务比选公告",
        "pubDate": "2026-04-27",
        "source": "北京工程造价招标信息网",
        "link": "https://m.yfbzb.com/zbzt/36/2/",
        "keywords": ["造价咨询", "电梯改造", "老旧小区"],
        "collectedAt": "2026-05-08",
        "slot": "下午",
        "budget": "未知",
        "description": "地区：北京朝阳；项目名称：大西洋新城38台电梯更新工程；服务内容：造价咨询服务"
    },
    {
        "id": max_id + 17,
        "title": "北京育新物业管理有限公司招标代理及造价咨询服务",
        "pubDate": "2026-04-27",
        "source": "北京工程造价招标信息网",
        "link": "https://m.yfbzb.com/zbzt/36/2/",
        "keywords": ["造价咨询", "招标代理"],
        "collectedAt": "2026-05-08",
        "slot": "下午",
        "budget": "未知",
        "description": "地区：北京；采购单位：北京育新物业管理有限公司；服务内容：招标代理及造价咨询服务"
    },
    {
        "id": max_id + 18,
        "title": "2026-2028年基本建设工程项目造价咨询服务",
        "pubDate": "2026-04-26",
        "source": "北京工程造价招标信息网",
        "link": "https://m.yfbzb.com/zbzt/36/2/",
        "keywords": ["造价咨询", "年度协议", "框架协议"],
        "collectedAt": "2026-05-08",
        "slot": "下午",
        "budget": "未知",
        "description": "地区：北京；服务内容：2026-2028年基本建设工程项目造价咨询服务"
    },
    {
        "id": max_id + 19,
        "title": "首都机场线更新改造类工程造价结算服务",
        "pubDate": "2026-04-25",
        "source": "北京工程造价招标信息网",
        "link": "https://m.yfbzb.com/zbzt/36/2/",
        "keywords": ["造价咨询", "结算审核", "地铁"],
        "collectedAt": "2026-05-08",
        "slot": "下午",
        "budget": "未知",
        "description": "地区：北京；采购单位：京城地铁；项目名称：首都机场线更新改造类工程造价结算服务"
    },
    {
        "id": max_id + 20,
        "title": "河北博物院数智化建设实录与精品图录出版公开招标中标公告",
        "pubDate": "2026-05-06",
        "source": "立达标讯",
        "link": "https://www.arrbid.com/dljg?city=9",
        "keywords": ["招标代理", "项目管理"],
        "collectedAt": "2026-05-08",
        "slot": "下午",
        "budget": "未知",
        "description": "地区：河北石家庄；采购单位：河北博物院；项目名称：数智化建设实录与精品图录出版"
    },
    {
        "id": max_id + 21,
        "title": "秦皇岛市北戴河区园林局2026年北戴河区立体绿化工程成交公告",
        "pubDate": "2026-05-06",
        "source": "立达标讯",
        "link": "https://www.arrbid.com/dljg?city=9",
        "keywords": ["招标代理", "园林绿化"],
        "collectedAt": "2026-05-08",
        "slot": "下午",
        "budget": "未知",
        "description": "地区：河北秦皇岛北戴河；采购单位：秦皇岛市北戴河区园林局；项目名称：2026年北戴河区立体绿化工程"
    },
    {
        "id": max_id + 22,
        "title": "保定高新技术产业开发区公共事业服务中心采购泵站安全生产及日常办公、维护用品项目成交结果公示",
        "pubDate": "2026-05-06",
        "source": "立达标讯",
        "link": "https://www.arrbid.com/dljg?city=9",
        "keywords": ["招标代理", "项目管理"],
        "collectedAt": "2026-05-08",
        "slot": "下午",
        "budget": "未知",
        "description": "地区：河北保定；采购单位：保定高新技术产业开发区公共事业服务中心"
    },
    {
        "id": max_id + 23,
        "title": "河北省中医院国家中医药传承创新中心建设项目电梯工程中标结果公告",
        "pubDate": "2026-05-06",
        "source": "立达标讯",
        "link": "https://www.arrbid.com/dljg?city=9",
        "keywords": ["招标代理", "项目管理"],
        "collectedAt": "2026-05-08",
        "slot": "下午",
        "budget": "未知",
        "description": "地区：河北石家庄；采购单位：河北省中医院；项目名称：国家中医药传承创新中心建设项目电梯工程"
    },
    {
        "id": max_id + 24,
        "title": "海港区水务局2026年海港区城市区河道保洁水草打捞项目竞争性磋商成交公告",
        "pubDate": "2026-05-06",
        "source": "立达标讯",
        "link": "https://www.arrbid.com/dljg?city=9",
        "keywords": ["招标代理", "项目管理"],
        "collectedAt": "2026-05-08",
        "slot": "下午",
        "budget": "未知",
        "description": "地区：河北秦皇岛海港；采购单位：海港区水务局；项目名称：2026年海港区城市区河道保洁水草打捞项目"
    },
    {
        "id": max_id + 25,
        "title": "中华人民共和国石家庄出入境边防检查站食堂主副食材配送服务采购项目中标公告",
        "pubDate": "2026-05-06",
        "source": "立达标讯",
        "link": "https://www.arrbid.com/dljg?city=9",
        "keywords": ["招标代理", "食材配送"],
        "collectedAt": "2026-05-08",
        "slot": "下午",
        "budget": "未知",
        "description": "地区：河北石家庄；采购单位：中华人民共和国石家庄出入境边防检查站"
    }
]

# 检查是否已存在相同标题的公告
existing_titles = {item['title'] for item in data['announcements']}
added_count = 0
for new_item in new_announcements:
    if new_item['title'] not in existing_titles:
        data['announcements'].insert(0, new_item)
        added_count += 1
        print(f"新增: {new_item['title'][:50]}...")

# 更新元数据
data['lastUpdate'] = datetime.now().strftime('%Y-%m-%d %H:%M')
data['totalCount'] = len(data['announcements'])

print(f"\n本次新增: {added_count}条")
print(f"更新后总数: {data['totalCount']}")

# 保存JSON
with open('data/announcements.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("数据已保存到 data/announcements.json")
