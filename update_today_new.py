import json
from datetime import datetime

# 读取现有数据
with open('data/announcements.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 今天的新增招标公告
new_announcements = [
    {
        "id": 999,
        "title": "成都市锦江区2026-2029政府投资项目工程咨询及造价咨询服务采购项目",
        "pubDate": "2026-03-26",
        "source": "中国政府采购网",
        "link": "http://www.ccgp.gov.cn/cggg/dfgg/gkzb/202603/t20260326_26318667.htm",
        "keywords": ["造价咨询", "工程咨询", "全过程咨询"],
        "collectedAt": "2026-04-30",
        "slot": "晚间",
        "budget": "400万元",
        "description": "地区：四川成都；采购单位：成都市锦江区发展和改革局；采购包1（工程咨询类）：160万元/年；采购包2（工程造价类）：240万元/年；服务期3年"
    },
    {
        "id": 998,
        "title": "北京市通州区台湖镇选聘2026年度造价咨询公司公开招标公告",
        "pubDate": "2026-03-24",
        "source": "中国政府采购网",
        "link": "http://www.ccgp.gov.cn/cggg/dfgg/gkzb/202603/t20260324_26307237.htm",
        "keywords": ["造价咨询"],
        "collectedAt": "2026-04-30",
        "slot": "晚间",
        "budget": "419万元",
        "description": "地区：北京通州；采购单位：台湖镇人民政府；采购5个包，每包83.8万元，包括房屋建筑类、市政工程类、拆改移工程类、环境整治类、园林绿化类"
    },
    {
        "id": 997,
        "title": "江苏省如皋市2026-2027年度造价咨询（预算编制、结算审计）服务项目",
        "pubDate": "2026-04-02",
        "source": "江苏省政府采购网",
        "link": "http://jsggzy.jszwfw.gov.cn/jyxx/003004/003004002/20260402/b0bc7c1fd5f34477b849d39e289345be.html",
        "keywords": ["造价咨询", "预算编制", "结算审计"],
        "collectedAt": "2026-04-30",
        "slot": "晚间",
        "budget": "320万元",
        "description": "地区：江苏如皋；采购单位：如皋市交通运输局；采购4个包，每包80万元；包括预算编制和结算审计服务；服务期2年"
    },
    {
        "id": 996,
        "title": "菏泽市总工会2026年度项目招标代理及全过程咨询服务机构遴选公告",
        "pubDate": "2026-04-07",
        "source": "菏泽市总工会",
        "link": "https://www.hzghw.org.cn/gsggs/40544.jhtml",
        "keywords": ["招标代理", "全过程咨询", "造价咨询", "项目管理"],
        "collectedAt": "2026-04-30",
        "slot": "晚间",
        "budget": "待定",
        "description": "地区：山东菏泽；采购单位：菏泽市总工会；服务内容：招标代理服务+全过程造价控制、工程监理、项目管理等全过程咨询服务；服务期1年"
    },
    {
        "id": 995,
        "title": "湖南省交通运输厅2026年造价审查及咨询服务专项重新立项项目公开招标",
        "pubDate": "2026-04-22",
        "source": "中国政府采购网/湖南省政府采购网",
        "link": "https://m.bidcenter.com.cn/news-1-415475825.html",
        "keywords": ["造价咨询", "造价审查"],
        "collectedAt": "2026-04-30",
        "slot": "晚间",
        "budget": "45万元",
        "description": "地区：湖南长沙；采购单位：湖南省交通运输厅交通建设造价管理站；采购内容：造价审查及咨询服务专项；服务期1年"
    },
    {
        "id": 994,
        "title": "运营项目2026~2027年度全过程工程咨询服务公开招标公告",
        "pubDate": "2026-04-29",
        "source": "陕西采购与招标网",
        "link": "https://m.bidcenter.com.cn/news-1-416819253.html",
        "keywords": ["全过程工程咨询", "项目管理", "工程监理", "造价咨询"],
        "collectedAt": "2026-04-30",
        "slot": "晚间",
        "budget": "待定",
        "description": "地区：陕西西安；采购单位：陕西省保障房事务中心；服务内容：维修、提升改造、设备采购及安装等全过程工程咨询服务；服务期：2026~2027年度"
    },
    {
        "id": 993,
        "title": "某部全过程工程咨询单位选取更正公告",
        "pubDate": "2026-04-30",
        "source": "军队采购网",
        "link": "https://m.bidcenter.com.cn/news-6-417013755.html",
        "keywords": ["全过程工程咨询", "工程监理", "工程设计"],
        "collectedAt": "2026-04-30",
        "slot": "晚间",
        "budget": "待定",
        "description": "地区：湖北；采购单位：某部；更正内容：调整特定资格要求，工程勘察资质不再作为必要条件；投标截止：2026年5月4日"
    },
    {
        "id": 992,
        "title": "连州市财政性资金投资建设工程造价咨询服务采购项目",
        "pubDate": "2026-03-16",
        "source": "中国政府采购网/广东省政府采购网",
        "link": "http://www.ccgp.gov.cn/cggg/dfgg/gkzb/202603/t20260316_26275733.htm",
        "keywords": ["造价咨询", "预算编制", "结算审计"],
        "collectedAt": "2026-04-30",
        "slot": "晚间",
        "budget": "1000万元",
        "description": "地区：广东连州；采购单位：连州市财政局投资审核中心；采购3个包，每包约300-400万元；服务期2年；包括预算编制和结算审计服务"
    },
    {
        "id": 991,
        "title": "国家粮食和物资储备局新疆局XX项目全过程造价咨询征集公告",
        "pubDate": "2026-03-31",
        "source": "中国政府采购网",
        "link": "http://www.ccgp.gov.cn/cggg/zygg/qtgg/202603/t20260331_26340019.htm",
        "keywords": ["全过程造价咨询", "造价咨询"],
        "collectedAt": "2026-04-30",
        "slot": "晚间",
        "budget": "待定",
        "description": "地区：新疆喀什；采购单位：国家粮食和物资储备局新疆局；服务内容：编制工程量清单、招标控制价，协助合同谈判与签订，清标，审核工程计量与支付，处理工程变更、索赔和签证，审核竣工结算"
    },
    {
        "id": 990,
        "title": "云栖未来产业智造基地项目全过程咨询项目",
        "pubDate": "2026-04-28",
        "source": "全国公共资源交易平台",
        "link": "https://www.qianlima.com/gjxx/507411/index_2703_0.html",
        "keywords": ["全过程咨询", "项目管理", "造价咨询"],
        "collectedAt": "2026-04-30",
        "slot": "晚间",
        "budget": "待定",
        "description": "地区：浙江杭州；项目名称：云栖未来产业智造基地项目（转塘单元XH100503-09、10地块）全过程咨询项目"
    },
    {
        "id": 989,
        "title": "霞浦县和美海岛环境整治提升项目全过程咨询（房建市政部分）重新招标",
        "pubDate": "2026-04-28",
        "source": "全国公共资源交易平台",
        "link": "https://www.qianlima.com/gjxx/507411/index_2703_0.html",
        "keywords": ["全过程咨询", "项目管理", "造价咨询"],
        "collectedAt": "2026-04-30",
        "slot": "晚间",
        "budget": "待定",
        "description": "地区：福建霞浦；项目名称：霞浦县和美海岛环境整治提升项目全过程咨询（房建市政部分）重新招标"
    }
]

# 更新数据
current_max_id = max(a['id'] for a in data['announcements'])
new_id = current_max_id + 1

for new_item in new_announcements:
    new_item['id'] = new_id
    data['announcements'].insert(0, new_item)  # 添加到开头
    new_id += 1

# 更新元数据
data['lastUpdate'] = datetime.now().strftime('%Y-%m-%d %H:%M')
data['totalCount'] = len(data['announcements'])

# 保存
with open('data/announcements.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Added {len(new_announcements)} new announcements")
print(f"Total count now: {data['totalCount']}")
print(f"Last update: {data['lastUpdate']}")
