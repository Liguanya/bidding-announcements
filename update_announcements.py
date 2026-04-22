import json
from datetime import datetime

# 读取现有数据
with open('data/announcements.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 获取当前最大ID
max_id = max(a['id'] for a in data['announcements'])
print(f"Current max ID: {max_id}")

# 新增的公告（从今日搜索结果中获取）
new_announcements = [
    {
        "id": max_id + 1,
        "title": "南网储能公司2026-2028年云南、贵州区域抽水蓄能电站施工电源工程监理服务框架采购项目",
        "pubDate": "2026-04-22",
        "source": "南方电网储能股份有限公司",
        "link": "http://m.toutiao.com/group/7631377059104784932/",
        "keywords": ["监理", "项目管理"],
        "collectedAt": "2026-04-22",
        "slot": "晚间"
    },
    {
        "id": max_id + 2,
        "title": "台湖镇选聘2026年度造价咨询公司公开招标公告",
        "pubDate": "2026-04-22",
        "source": "中国政府采购网",
        "link": "http://www.ccgp.gov.cn/cggg/dfgg/gkzb/202603/t20260324_26307237.htm",
        "keywords": ["造价"],
        "collectedAt": "2026-04-22",
        "slot": "晚间"
    },
    {
        "id": max_id + 3,
        "title": "2026-2029政府投资项目工程咨询及造价咨询服务采购项目（成都锦江区）",
        "pubDate": "2026-04-22",
        "source": "中国政府采购网",
        "link": "http://www.ccgp.gov.cn/cggg/dfgg/gkzb/202603/t20260326_26318667.htm",
        "keywords": ["造价", "全过程咨询"],
        "collectedAt": "2026-04-22",
        "slot": "晚间"
    },
    {
        "id": max_id + 4,
        "title": "2616工程造价咨询服务询价公告",
        "pubDate": "2026-04-22",
        "source": "采招网",
        "link": "https://m.bidcenter.com.cn/news-1-414608095.html",
        "keywords": ["造价"],
        "collectedAt": "2026-04-22",
        "slot": "晚间"
    },
    {
        "id": max_id + 5,
        "title": "2026-2027年度造价咨询（预算编制、结算审计）服务项目采购公告（江苏如皋）",
        "pubDate": "2026-04-22",
        "source": "江苏省政府采购网",
        "link": "http://jsggzy.jszwfw.gov.cn/jyxx/003004/003004002/20260402/b0bc7c1fd5f34477b849d39e289345be.html",
        "keywords": ["造价"],
        "collectedAt": "2026-04-22",
        "slot": "晚间"
    },
    {
        "id": max_id + 6,
        "title": "2026年-2029年江门市本级财政投资建设工程造价评审服务项目",
        "pubDate": "2026-04-22",
        "source": "中国政府采购网",
        "link": "http://www.ccgp.gov.cn/cggg/dfgg/gkzb/202603/t20260305_26235418.htm",
        "keywords": ["造价"],
        "collectedAt": "2026-04-22",
        "slot": "晚间"
    },
    {
        "id": max_id + 7,
        "title": "湖南省交通运输厅2026年造价审查及咨询服务专项公开招标",
        "pubDate": "2026-04-22",
        "source": "采招网",
        "link": "https://m.bidcenter.com.cn/news-4-414478102.html",
        "keywords": ["造价"],
        "collectedAt": "2026-04-22",
        "slot": "晚间"
    },
    {
        "id": max_id + 8,
        "title": "全过程工程咨询项目协作技术服务公开招标公告",
        "pubDate": "2026-04-22",
        "source": "中国政府采购网",
        "link": "http://www.ccgp.gov.cn/cggg/dfgg/gkzb/202602/t20260212_26176805.htm",
        "keywords": ["全过程咨询", "项目管理"],
        "collectedAt": "2026-04-22",
        "slot": "晚间"
    }
]

# 将新公告添加到列表开头（最新在前）
data['announcements'] = new_announcements + data['announcements']

# 更新时间戳和总数
data['lastUpdate'] = datetime.now().strftime('%Y-%m-%d %H:%M')
data['totalCount'] = len(data['announcements'])

# 保存更新后的数据
with open('data/announcements.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Updated {len(new_announcements)} new announcements")
print(f"Total count: {data['totalCount']}")
print(f"Last update: {data['lastUpdate']}")
