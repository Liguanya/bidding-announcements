import json
from datetime import datetime

# 读取现有数据
with open('data/announcements.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 获取当前最大ID
max_id = max([a['id'] for a in data['announcements']]) if data['announcements'] else 0

# 今天下午(2026-05-07 下午)新增的公告数据
new_announcements = [
    {
        "id": max_id + 1,
        "title": "上海高校招标代理、造价咨询服务入围采购项目",
        "pubDate": "2026-05-06",
        "source": "采招网",
        "link": "https://m.bidcenter.com.cn/news-1-417405595.html",
        "keywords": ["招标代理", "造价咨询"],
        "collectedAt": "2026-05-07",
        "slot": "下午",
        "budget": "三年预计600万元",
        "description": "地区：上海；采购单位：上海高校；招标内容：招标代理、造价咨询服务入围；入围2家供应商；服务期限三年，合同一年一签；投标截止：2026-05-27 10:00"
    },
    {
        "id": max_id + 2,
        "title": "义乌市2026年度招标代理和造价咨询服务采购项目",
        "pubDate": "2026-05-06",
        "source": "采招网",
        "link": "https://m.bidcenter.com.cn/news-1-417366169.html",
        "keywords": ["招标代理", "造价咨询"],
        "collectedAt": "2026-05-07",
        "slot": "下午",
        "budget": "单项不超过5万元",
        "description": "地区：浙江金华义乌；采购单位：义乌市；采购内容：2026年度招标代理（含施工、货物及服务采购等）和造价咨询（含工程量清单、预算、结算审核等）；服务期限1年；投标截止：2026-05-13 13:00"
    },
    {
        "id": max_id + 3,
        "title": "某工程全过程工程咨询（二次）招标公告",
        "pubDate": "2026-05-07",
        "source": "中国招标投标公共服务平台",
        "link": "https://www.ctex.cn/sichuan/search?keyword=%E5%85%A8%E8%BF%81%E7%A8%8B%E5%B7%A5%E7%A8%8B",
        "keywords": ["全过程咨询", "项目管理", "造价咨询", "工程监理"],
        "collectedAt": "2026-05-07",
        "slot": "下午",
        "description": "地区：吉林长春；建设规模：食堂及附属设施，营区内部分用房外窗节能改造；服务范围：项目管理、设计、造价咨询、工程监理；截止时间：2026-05-15"
    },
    {
        "id": max_id + 4,
        "title": "某单位2026年度工程项目全过程咨询服务采购",
        "pubDate": "2026-05-07",
        "source": "武汉市招标网",
        "link": "https://wuhan.hangnian.com/info-69d8a925f1200000f8005592.html",
        "keywords": ["全过程咨询", "项目管理", "造价咨询", "招标代理"],
        "collectedAt": "2026-05-07",
        "slot": "下午",
        "description": "地区：湖北武汉；采购单位：某单位；服务内容：全过程项目管理、投资咨询、工程勘察、工程设计、造价咨询、工程招标代理、工程监理；合同期限1年"
    },
    {
        "id": max_id + 5,
        "title": "巢湖市审计局2026年度政府投资建设工程造价咨询服务（第一批）",
        "pubDate": "2026-05-07",
        "source": "安徽合肥公共资源交易网",
        "link": "https://zfcg.ah.gov.cn/site/detail?articleId=qLcnXsF+inY7J7Bd6aCAvg==",
        "keywords": ["造价咨询", "政府投资", "框架协议"],
        "collectedAt": "2026-05-07",
        "slot": "下午",
        "budget": "180万元（5包各36万元）",
        "description": "地区：安徽合肥巢湖；采购单位：巢湖市审计局；采购内容：工程造价咨询服务；分5个采购包，每包36万；专门面向中小企业；投标截止：2026-05-20 09:00"
    },
    {
        "id": max_id + 6,
        "title": "某单位全过程工程咨询单位选取",
        "pubDate": "2026-05-07",
        "source": "采招网",
        "link": "https://m.bidcenter.com.cn/news-1-416236490.html",
        "keywords": ["全过程咨询", "项目管理", "造价咨询", "工程监理"],
        "collectedAt": "2026-05-07",
        "slot": "下午",
        "description": "地区：湖北武汉；采购单位：某部；服务内容：项目管理、决策咨询、勘察设计、招标代理、工程监理、造价咨询；服务期12个月；选取2家入围单位；投标截止：2026-05-20 09:30"
    },
    {
        "id": max_id + 7,
        "title": "某学校2026-2027年招标代理服务机构入围比选",
        "pubDate": "2026-05-07",
        "source": "中国采购与招标网",
        "link": "https://sc.bidcenter.com.cn/diqucontent-416113394-1.html",
        "keywords": ["招标代理", "入围比选"],
        "collectedAt": "2026-05-07",
        "slot": "下午",
        "description": "地区：四川资阳；采购单位：某学校；采购内容：2026~2027年度招标代理机构入围；入围2家；服务期限1年"
    },
    {
        "id": max_id + 8,
        "title": "国核电力规划设计研究院发电项目常规岛造价咨询辅助服务招标",
        "pubDate": "2026-04-30",
        "source": "采招网",
        "link": "https://m.dljczb.com/wd-336/789/",
        "keywords": ["造价咨询", "电力项目"],
        "collectedAt": "2026-05-07",
        "slot": "下午",
        "description": "采购单位：国核电力规划设计研究院有限公司；服务内容：某电力发电项目常规岛及BOP造价咨询辅助服务"
    },
    {
        "id": max_id + 9,
        "title": "新疆医科大学第一附属医院建设工程造价咨询服务",
        "pubDate": "2026-04-27",
        "source": "新疆政府采购网",
        "link": "http://www.ccgp.gov.cn",
        "keywords": ["造价咨询", "全过程造价", "医院建设"],
        "collectedAt": "2026-05-07",
        "slot": "下午",
        "budget": "75万元/标包",
        "description": "地区：新疆乌鲁木齐；采购单位：新疆医科大学第一附属医院；标包1、2各75万元；服务期3年"
    },
    {
        "id": max_id + 10,
        "title": "云南省贵金属新材料控股集团股份有限公司造价咨询机构框架协议采购",
        "pubDate": "2026-04-29",
        "source": "中国招标投标公共服务平台",
        "link": "http://m.toutiao.com/group/7634346001196646964/",
        "keywords": ["造价咨询", "框架协议"],
        "collectedAt": "2026-05-07",
        "slot": "下午",
        "description": "地区：云南昆明；采购单位：云南省贵金属新材料控股集团股份有限公司；入围3家；投标截止：2026-05-21 09:30"
    }
]

# 将新公告添加到列表开头（最新的在前）
data['announcements'] = new_announcements + data['announcements']

# 更新元数据
data['lastUpdate'] = datetime.now().strftime('%Y-%m-%d %H:%M')
data['totalCount'] = len(data['announcements'])

# 保存更新后的JSON
with open('data/announcements.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"已添加 {len(new_announcements)} 条新公告")
print(f"总公告数: {data['totalCount']}")
print(f"更新时间: {data['lastUpdate']}")
