import json
from datetime import datetime

# 读取现有数据
with open('data/announcements.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 获取现有最大ID
max_id = max(item['id'] for item in data['announcements'])

# 新增的招标公告（从本次搜索结果中获取）
new_announcements = [
    {
        "id": max_id + 1,
        "title": "武汉理工大学南湖校区建设项目全过程造价咨询服务",
        "pubDate": "2026-04-20",
        "source": "中国政府采购网",
        "link": "http://m.toutiao.com/group/7630523698490933794/",
        "keywords": ["造价咨询", "全过程咨询", "项目管理"],
        "collectedAt": "2026-04-26",
        "slot": "早间",
        "budget": "71122万元",
        "description": "地区：湖北武汉；采购单位：武汉理工大学；总投资71122万元；总建筑面积103512平方米；服务内容：初设概算审核、进度款审核、变更预算审核、施工结算审核、清单和控制价编制；服务期：1460日历天（约4年）；投标截止：2026-05-11 09:30"
    },
    {
        "id": max_id + 2,
        "title": "某工程全过程工程咨询（二次）招标公告",
        "pubDate": "2026-04-21",
        "source": "采招网",
        "link": "https://www.qianlima.com/bid-591363094.html",
        "keywords": ["全过程咨询", "造价咨询", "项目管理"],
        "collectedAt": "2026-04-26",
        "slot": "早间",
        "budget": "590万元",
        "description": "地区：某省某市；采购单位：某单位；建设规模：1项；投资额约590万元；服务内容：全过程工程咨询包括项目管理、设计、造价咨询、工程监理；服务期：自签订合同起至工程竣工决算完成止"
    },
    {
        "id": max_id + 3,
        "title": "吉安市本级JA0327全过程咨询服务采购项目",
        "pubDate": "2026-04-08",
        "source": "采招网",
        "link": "https://m.bidcenter.com.cn/news-1-412598627.html",
        "keywords": ["全过程咨询", "项目管理"],
        "collectedAt": "2026-04-26",
        "slot": "早间",
        "description": "地区：江西吉安；采购单位：吉安市本级；采购方式：公开招标；服务内容：工程项目管理服务；合同履行期限：从合同签订之日起至工程审计完成，其中施工工期约18个月；投标截止：2026-04-29 09:00"
    },
    {
        "id": max_id + 4,
        "title": "国网技术学院泰安明堂路校区培训服务用房项目管理服务",
        "pubDate": "2026-04-07",
        "source": "齐鲁壹点",
        "link": "http://m.toutiao.com/group/7625919384862736896/",
        "keywords": ["项目管理", "招标代理"],
        "collectedAt": "2026-04-26",
        "slot": "早间",
        "budget": "120万元",
        "description": "地区：山东泰安；采购单位：山东电力高等专科学校；控制价120万元；服务内容：负责项目前期手续办理、设计管理、项目准备管理、采购管理、项目实施管理、文档管理、竣工及质保期管理、后评价管理等；服务期：从项目前期策划至工程投入使用及保修期管理；投标截止：2026-04-28 09:00"
    },
    {
        "id": max_id + 5,
        "title": "2026年零星工程全过程咨询服务采购招标公告",
        "pubDate": "2026-04-09",
        "source": "采招网",
        "link": "https://m.bidcenter.com.cn/news-1-413093868.html",
        "keywords": ["全过程咨询", "造价咨询", "工程监理"],
        "collectedAt": "2026-04-26",
        "slot": "早间",
        "budget": "约41万元",
        "description": "地区：黑龙江哈尔滨；服务内容：主要包括工程监理和造价咨询（全过程造价咨询）；工作内容包括编制工程量清单、清单预算，施工过程造价管理，工程结算初审；项目预算费率上限3.81%；投标截止：2026-04-21"
    },
    {
        "id": max_id + 6,
        "title": "2026-2027年度造价咨询（预算编制、结算审计）服务项目",
        "pubDate": "2026-04-02",
        "source": "江苏省政府采购网",
        "link": "http://jsggzy.jszwfw.gov.cn/jyxx/003004/003004002/20260402/b0bc7c1fd5f34477b849d39e289345be.html",
        "keywords": ["造价咨询", "预算编制", "结算审计"],
        "collectedAt": "2026-04-26",
        "slot": "早间",
        "budget": "320万元",
        "description": "地区：江苏如皋；采购单位：如皋市交通运输局；预算金额320万元（分4个采购包，每个80万元）；采购包1-2为预算编制，采购包3-4为结算审计；合同履行期限：自合同签订之日起两年；投标截止：2026-04-14 09:00"
    }
]

# 将新公告添加到列表开头（最新的在前面）
data['announcements'] = new_announcements + data['announcements']
data['lastUpdate'] = datetime.now().strftime('%Y-%m-%d %H:%M')
data['totalCount'] = len(data['announcements'])

# 保存更新后的数据
with open('data/announcements.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"已添加 {len(new_announcements)} 条新公告")
print(f"当前总数: {data['totalCount']}")
print(f"更新时间: {data['lastUpdate']}")
