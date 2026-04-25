import json
import os
from datetime import datetime

# 读取现有数据
with open('/app/data/所有对话/主对话/bidding-announcements/data/announcements.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 新增的招标公告
new_announcements = [
    {
        "id": 113,
        "title": "新县财政局预算评审中心工程造价咨询框架协议采购项目",
        "pubDate": "2026-04-22",
        "source": "河南省政府采购网",
        "link": "https://zfcg.henan.gov.cn/henan/content?channelCode=D920502&infoId=1947104",
        "keywords": ["造价咨询"],
        "collectedAt": "2026-04-25",
        "slot": "早间",
        "budget": "100万元",
        "description": "地区：河南信阳新县；采购方式：公开招标；预算金额100万元；选聘15家工程造价咨询公司；框架协议期限3年；投标截止：2026-05-13 09:00"
    },
    {
        "id": 114,
        "title": "2026年耕地种植用途管控一张图项目和粮油及重要经济作物病虫害绿色防控新技术、新产品研发项目招标代理机构比选公告",
        "pubDate": "2026-04-23",
        "source": "贵州省农业农村厅",
        "link": "http://m.toutiao.com/group/7631847098018759209/",
        "keywords": ["招标代理"],
        "collectedAt": "2026-04-25",
        "slot": "早间",
        "description": "地区：贵州；采购单位：贵州省农业农村厅；比选1家招标代理机构；服务范围：招标采购代理相关业务；响应文件截止：2026-04-28 15:00"
    },
    {
        "id": 115,
        "title": "北京市住房和城乡建设委员会综合事务中心2026年相关政府采购项目采购代理服务比选",
        "pubDate": "2026-04-01",
        "source": "北京市住建委",
        "link": "https://zjw.beijing.gov.cn/bjjs/xxgk/zwdt/743966866/index.shtml",
        "keywords": ["招标代理"],
        "collectedAt": "2026-04-25",
        "slot": "早间",
        "description": "地区：北京；采购单位：北京市住建委综合事务中心；采购代理服务比选；响应文件截止：2026-04-13 17:30；比选时间：2026-04-17 09:30"
    },
    {
        "id": 116,
        "title": "宁夏固原经济开发区管理委员会关于开展申报国家级零碳园区咨询服务采购项目",
        "pubDate": "2026-04-18",
        "source": "宁夏回族自治区政府采购网",
        "link": "http://m.toutiao.com/group/7630040099287237156/",
        "keywords": ["咨询服务"],
        "collectedAt": "2026-04-25",
        "slot": "早间",
        "budget": "90万元",
        "description": "地区：宁夏固原；预算金额90万元；专门面向中小企业；申报国家级零碳园区咨询服务；投标截止：2026-05-08 09:00"
    },
    {
        "id": 117,
        "title": "连州市财政性资金投资建设工程造价咨询服务采购项目",
        "pubDate": "2026-03-16",
        "source": "中国政府采购网",
        "link": "http://www.ccgp.gov.cn/cggg/dfgg/gkzb/202603/t20260316_26275733.htm",
        "keywords": ["造价咨询"],
        "collectedAt": "2026-04-25",
        "slot": "早间",
        "budget": "1000万元",
        "description": "地区：广东清远连州；采购单位：连州市财政局投资审核中心；预算金额1000万元（分3个采购包：400万+300万+300万）；服务期2年；开标时间：2026-04-08"
    },
    {
        "id": 118,
        "title": "2026年-2029年江门市本级财政投资建设工程造价评审服务项目",
        "pubDate": "2026-03-05",
        "source": "中国政府采购网",
        "link": "http://www.ccgp.gov.cn/cggg/dfgg/gkzb/202603/t20260305_26235418.htm",
        "keywords": ["造价咨询"],
        "collectedAt": "2026-04-25",
        "slot": "早间",
        "budget": "1560万元",
        "description": "地区：广东江门；采购单位：江门市财政投资评审中心；预算金额1560万元（分10个采购包）；内容包括基建项目工程造价预、结算评审及工程造价管理规范编制等咨询业务"
    },
    {
        "id": 119,
        "title": "全过程工程咨询项目协作技术服务公开招标公告",
        "pubDate": "2026-02-12",
        "source": "中国政府采购网",
        "link": "http://www.ccgp.gov.cn/cggg/dfgg/gkzb/202602/t20260212_26176805.htm",
        "keywords": ["全过程咨询"],
        "collectedAt": "2026-04-25",
        "slot": "早间",
        "budget": "1900万元",
        "description": "地区：浙江；采购单位：浙江省水利水电技术咨询中心；预算金额1900万元；最高限价1883.4万元；接受联合体投标；开标时间：2026-03-04"
    },
    {
        "id": 120,
        "title": "2026年造价审查及咨询服务专项项目公开招标公告",
        "pubDate": "2026-03-27",
        "source": "采招网",
        "link": "https://m.bidcenter.com.cn/news-1-410928764.html",
        "keywords": ["造价咨询"],
        "collectedAt": "2026-04-25",
        "slot": "早间",
        "budget": "480万元",
        "description": "地区：湖南；采购单位：湖南省交通运输厅交通建设造价管理站；预算金额480万元；服务期1年；投标截止：2026-04-09 09:00"
    }
]

# 获取当前最大的ID
max_id = max(a['id'] for a in data['announcements'])

# 更新lastUpdate和totalCount
data['lastUpdate'] = datetime.now().strftime('%Y-%m-%d %H:%M')
data['totalCount'] = len(data['announcements']) + len(new_announcements)

# 添加新公告到列表开头
data['announcements'] = new_announcements + data['announcements']

# 写入更新后的JSON
with open('/app/data/所有对话/主对话/bidding-announcements/data/announcements.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"已添加 {len(new_announcements)} 条新公告")
print(f"总公告数: {data['totalCount']}")
print(f"最后更新时间: {data['lastUpdate']}")
