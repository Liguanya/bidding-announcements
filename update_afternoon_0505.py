import json
from datetime import datetime

# 读取现有数据
with open('data/announcements.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 获取当前最大ID
max_id = max(a['id'] for a in data['announcements'])
print(f"当前最大ID: {max_id}")

# 今天下午新增的公告（从搜索结果中提取，2026-05-05下午搜索到的最新公告）
new_announcements = [
    {
        "id": max_id + 1,
        "title": "运营项目2026~2027年度全过程工程咨询服务公开招标公告",
        "pubDate": "2026-04-29",
        "source": "采招网",
        "link": "https://m.bidcenter.com.cn/news-1-416819253.html",
        "keywords": ["全过程咨询", "项目管理", "造价咨询", "招标代理"],
        "collectedAt": "2026-05-05",
        "slot": "下午",
        "budget": "未知",
        "description": "地区：陕西西安；采购单位：社保大厦；服务内容：维修、提升改造、设备采购及安装等相关事项全过程工程咨询服务，包含项目管理、工程监理、全过程造价咨询等服务；投标截止：2026-05-20"
    },
    {
        "id": max_id + 2,
        "title": "马栏河污水片区排水管网系统整治工程——西南路、五一路等28条街道排水管网改造工程招标代理及造价咨询服务",
        "pubDate": "2026-04-29",
        "source": "全国招标信息网",
        "link": "https://m.bidcenter.com.cn/news-2-416827867.html",
        "keywords": ["招标代理", "造价咨询"],
        "collectedAt": "2026-05-05",
        "slot": "下午",
        "budget": "153万元",
        "description": "地区：辽宁大连；采购单位：城市公用事业服务中心；采购需求：招标代理及造价咨询服务，包括工程量清单与招标控制价的编制；工程概算、工程预算、施工阶段全过程工程造价咨询服务；预计采购时间：2026-05"
    },
    {
        "id": max_id + 3,
        "title": "云南省贵金属新材料控股集团股份有限公司造价咨询机构框架协议采购",
        "pubDate": "2026-04-29",
        "source": "中国招标投标公共服务平台",
        "link": "http://m.toutiao.com/group/7634346001196646964/",
        "keywords": ["造价咨询", "全过程咨询"],
        "collectedAt": "2026-05-05",
        "slot": "下午",
        "budget": "0万元（框架协议入围3家）",
        "description": "地区：云南昆明；采购单位：云南省贵金属新材料控股集团股份有限公司；代理公司：云南西南咨询有限公司；服务范围：建设项目、零星修缮服务的造价咨询服务及下属各级全资/控股子公司的建设项目造价咨询服务；入围供应商数量：3家；投标截止：2026-05-21 09:30"
    },
    {
        "id": max_id + 4,
        "title": "兰陵县2026年财政投资工程类项目第一批公开选聘造价咨询中介机构项目",
        "pubDate": "2026-04-24",
        "source": "全国招标信息网",
        "link": "https://m.bidcenter.com.cn/news-1-415773274.html",
        "keywords": ["造价咨询", "全过程咨询", "招标代理"],
        "collectedAt": "2026-05-05",
        "slot": "下午",
        "budget": "约202万元",
        "description": "地区：山东临沂；采购单位：兰陵县财政局；采购需求：2026年财政投资工程类项目造价咨询服务，共22个包，包括水库移民扶持基金、废弃矿山生态修复、公路工程、农田建设、校园改造等多个领域全过程咨询服务；开标时间：2026-05-19 09:00"
    },
    {
        "id": max_id + 5,
        "title": "2026年北京市普通公路健康工程造价咨询",
        "pubDate": "2026-04-20",
        "source": "北京市交通委员会",
        "link": "https://jtw.beijing.gov.cn/xxgk/ztbxx/202604/P020260420648265052375.pdf",
        "keywords": ["造价咨询", "全过程咨询"],
        "collectedAt": "2026-05-05",
        "slot": "下午",
        "budget": "第1标段79万元，第2标段83万元",
        "description": "地区：北京；采购单位：北京市公路事业发展中心；代理公司：北京价源技术有限公司；服务内容：北京市普通公路健康工程造价咨询服务，包括工程量复核、定额选用审核、人材机单价审核、项目决(结)算审核等；服务期：至2026年12月31日；投标截止：2026-05-11"
    },
    {
        "id": max_id + 6,
        "title": "蜀道投资集团有限责任公司2026年度工程造价咨询服务",
        "pubDate": "2026-04-24",
        "source": "四川省交通运输厅",
        "link": "http://m.toutiao.com/group/7633932001196639123/",
        "keywords": ["造价咨询"],
        "collectedAt": "2026-05-05",
        "slot": "下午",
        "budget": "未知",
        "description": "地区：四川；采购单位：蜀道投资集团有限责任公司；代理公司：四川明力律师事务所；采购需求：工程造价咨询服务，包括工程量清单与招标控制价的编制；服务要求：熟悉四川省交通运输工程计价依据；投标截止：2026-05-14 09:00"
    },
    {
        "id": max_id + 7,
        "title": "金寨县交通运输局2026年5月1日-2027年4月30日年度招标代理机构采购",
        "pubDate": "2026-04-16",
        "source": "采招网",
        "link": "https://m.bidcenter.com.cn/news-1-414419128.html",
        "keywords": ["招标代理", "项目管理"],
        "collectedAt": "2026-05-05",
        "slot": "下午",
        "budget": "参照标准100%",
        "description": "地区：安徽六安；采购单位：金寨县交通运输局；代理公司：铜陵pf公管项目交易服务；采购需求：选聘3家代理服务机构承担年度限额以下工程类、采购类项目全过程代理服务及工程量清单、控制价编制等服务；服务期：2026年5月1日-2027年4月30日"
    },
    {
        "id": max_id + 8,
        "title": "安徽国风新材料股份有限公司本部精益管理(二期)咨询项目",
        "pubDate": "2026-04-27",
        "source": "安徽公共资源交易集团",
        "link": "http://m.toutiao.com/group/7633603773826368040/",
        "keywords": ["项目管理", "咨询服务"],
        "collectedAt": "2026-05-05",
        "slot": "下午",
        "budget": "120万元（第二阶段）",
        "description": "地区：安徽合肥；采购单位：安徽国风新材料股份有限公司；代理公司：安徽公共资源交易集团项目管理有限公司；服务内容：对公司品质管理业务进行精益化咨询辅导；服务期：自合同签订后9个月；开标时间：2026-05-18 10:30"
    }
]

# 添加新公告到列表开头
data['announcements'] = new_announcements + data['announcements']
data['lastUpdate'] = "2026-05-05 13:57"
data['totalCount'] = len(data['announcements'])

print(f"更新后总数: {data['totalCount']}")
print(f"新增公告数量: {len(new_announcements)}")

# 保存更新后的数据
with open('data/announcements.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("JSON数据更新完成!")
