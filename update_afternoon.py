import json
from datetime import datetime

# 读取现有数据
with open('data/announcements.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 获取当前最大ID
max_id = max([a['id'] for a in data['announcements']]) if data['announcements'] else 0

# 新增的公告数据 (基于中国政府采购网搜索结果)
new_announcements = [
    {
        "id": max_id + 1,
        "title": "天津边检总站考勤系统建设项目竞争性磋商公告",
        "pubDate": "2026-05-01",
        "source": "中国政府采购网",
        "link": "https://www.ccgp.gov.cn/cggg/zygg/index.htm",
        "keywords": ["项目管理", "招标代理"],
        "collectedAt": "2026-05-04",
        "slot": "下午",
        "budget": "未知",
        "description": "地区：天津；采购单位：中华人民共和国天津出入境边防检查总站；项目名称：考勤系统建设项目"
    },
    {
        "id": max_id + 2,
        "title": "新疆出入境边防检查总站信息化项目造价咨询服务采购项目成交结果公告",
        "pubDate": "2026-04-27",
        "source": "中国政府采购网",
        "link": "https://www.ccgp.gov.cn/cggg/zygg/index.htm",
        "keywords": ["造价咨询"],
        "collectedAt": "2026-05-04",
        "slot": "下午",
        "budget": "未知",
        "description": "地区：新疆；采购单位：中华人民共和国新疆出入境边防检查总站；服务内容：信息化项目造价咨询服务"
    },
    {
        "id": max_id + 3,
        "title": "武汉理工大学南湖校区全过程造价咨询技术服务招标公告",
        "pubDate": "2026-04-20",
        "source": "中国政府采购网",
        "link": "http://m.toutiao.com/group/7630577153599455744/",
        "keywords": ["全过程咨询", "造价咨询"],
        "collectedAt": "2026-05-04",
        "slot": "下午",
        "budget": "7.11亿元",
        "description": "地区：湖北武汉；采购单位：武汉理工大学；项目名称：南湖校区建设项目；总投资：71122万元；服务内容：初步设计概算初审、进度款审核、变更预算初审、结算审核"
    },
    {
        "id": max_id + 4,
        "title": "云南省贵金属新材料控股集团股份有限公司造价咨询机构框架协议采购招标公告",
        "pubDate": "2026-04-29",
        "source": "全国招标信息网",
        "link": "https://www.bidnews.cn/caigou/zhaobiao-105689001.html",
        "keywords": ["造价咨询"],
        "collectedAt": "2026-05-04",
        "slot": "下午",
        "budget": "50万元/项",
        "description": "地区：云南昆明；采购单位：云南省贵金属新材料控股集团股份有限公司；招标代理机构：云南西南咨询有限公司；服务内容：建设项目造价咨询；单项服务费用不超过50万元"
    },
    {
        "id": max_id + 5,
        "title": "成都市锦江区2026-2029政府投资项目工程咨询及造价咨询服务采购项目",
        "pubDate": "2026-03-26",
        "source": "中国政府采购网",
        "link": "http://www.ccgp.gov.cn/cggg/dfgg/gkzb/202603/t20260326_26318667.htm",
        "keywords": ["造价咨询", "全过程咨询", "项目管理"],
        "collectedAt": "2026-05-04",
        "slot": "下午",
        "budget": "400万元/年",
        "description": "地区：四川成都；采购单位：成都市锦江区发展和改革局；项目名称：2026-2029政府投资项目工程咨询及造价咨询服务采购项目；预算金额：400万元/年（包1工程咨询160万/年，包2工程造价240万/年）"
    },
    {
        "id": max_id + 6,
        "title": "连州市财政性资金投资建设工程造价咨询服务采购项目",
        "pubDate": "2026-03-16",
        "source": "中国政府采购网",
        "link": "http://www.ccgp.gov.cn/cggg/dfgg/gkzb/202603/t20260316_26275733.htm",
        "keywords": ["造价咨询"],
        "collectedAt": "2026-05-04",
        "slot": "下午",
        "budget": "1000万元",
        "description": "地区：广东连州；采购单位：连州市财政局投资审核中心；项目名称：财政性资金投资建设工程造价咨询服务采购项目；预算金额：1000万元；服务期：两年"
    },
    {
        "id": max_id + 7,
        "title": "河北雄安新区2026年财政投资评审造价咨询服务公开招标",
        "pubDate": "2026-01-21",
        "source": "中国政府采购网",
        "link": "http://www.ccgp.gov.cn/cggg/dfgg/gkzb/202601/t20260121_26097735.htm",
        "keywords": ["造价咨询"],
        "collectedAt": "2026-05-04",
        "slot": "下午",
        "budget": "2041万元",
        "description": "地区：河北雄安；采购单位：雄安新区财政投资评审中心；项目名称：2026年河北雄安新区财政投资评审造价咨询服务；预算金额：2041万元；服务内容：竣工结算评审"
    },
    {
        "id": max_id + 8,
        "title": "江门市2026-2029年本级财政投资建设工程造价评审服务项目",
        "pubDate": "2026-03-05",
        "source": "中国政府采购网",
        "link": "http://www.ccgp.gov.cn/cggg/dfgg/gkzb/202603/t20260305_26235418.htm",
        "keywords": ["造价咨询"],
        "collectedAt": "2026-05-04",
        "slot": "下午",
        "budget": "1560万元",
        "description": "地区：广东江门；采购单位：江门市财政投资评审中心；项目名称：2026-2029年江门市本级财政投资建设工程造价评审服务项目；预算金额：1560万元；分为10个采购包"
    },
    {
        "id": max_id + 9,
        "title": "宁波市海曙区月湖街道住宅小区管网改造提升工程全过程工程咨询",
        "pubDate": "2026-02-11",
        "source": "中国政府采购网",
        "link": "https://zfcg.czj.ningbo.gov.cn/project/zcyNotice_view.aspx?Id=202602111730132021517116842315776",
        "keywords": ["全过程咨询", "项目管理", "造价咨询"],
        "collectedAt": "2026-05-04",
        "slot": "下午",
        "budget": "66.13万元",
        "description": "地区：浙江宁波；采购单位：宁波市海曙区月湖街道办事处；项目名称：住宅小区管网改造提升工程全过程工程咨询；预算金额：66.13万元"
    },
    {
        "id": max_id + 10,
        "title": "杭州市某工程提升改造项目全过程工程咨询承包商征集公告",
        "pubDate": "2026-03-01",
        "source": "中国政府采购网",
        "link": "https://rf.hangzhou.gov.cn/col/col1658924/art/2026/art_b3521f0840584a0dbb4e57e212e125ad.html",
        "keywords": ["全过程咨询", "项目管理", "造价咨询", "招标代理"],
        "collectedAt": "2026-05-04",
        "slot": "下午",
        "budget": "8000万元+",
        "description": "地区：浙江杭州；采购单位：杭州市国防动员和军民融合事务保障中心；项目名称：某工程提升改造项目全过程工程咨询；服务内容：项目管理（含设计咨询）、工程监理、造价咨询、招标代理；总投资：8000万元以上"
    },
    {
        "id": max_id + 11,
        "title": "芜湖市马塘新镇排水管道及环境提升工程全过程咨询",
        "pubDate": "2026-02-11",
        "source": "弋江区人民政府",
        "link": "https://www.yjq.gov.cn/zxxx/gsgg/18526778.html",
        "keywords": ["全过程咨询", "项目管理", "造价咨询"],
        "collectedAt": "2026-05-04",
        "slot": "下午",
        "budget": "45万元",
        "description": "地区：安徽芜湖；采购单位：芜湖市弋江区马塘街道办事处；项目名称：马塘新镇排水管道及环境提升工程全过程咨询；预算金额：45万元；服务内容：工程项目管理、工程监理、造价咨询"
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
