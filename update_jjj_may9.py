import json
import os
from datetime import datetime, timedelta

# 新增的京津冀地区公告（5月6日-9日发布）
new_announcements = [
    {
        "id": 9999,
        "title": "中国农业大学审计处国家农业科技创新港国际农业与全球发展创新基地项目全过程审计服务采购项目中标公告",
        "pubDate": "2026-05-08",
        "source": "中国政府采购网",
        "link": "http://www.ccgp.gov.cn/cggg/zygg/zbgg/202605/t20260508_26528946.htm",
        "keywords": ["全过程审计", "造价咨询", "审计服务"],
        "collectedAt": "2026-05-09",
        "slot": "上午",
        "budget": "149.6万元",
        "region": "北京",
        "description": "地区：北京；采购单位：中国农业大学；中标金额149.6万元；中标单位：北京和兴工程造价咨询有限公司"
    },
    {
        "id": 9998,
        "title": "2026年度工程造价编制及审核服务项目招标公告",
        "pubDate": "2026-05-08",
        "source": "军队采购网",
        "link": "https://m.bidcenter.com.cn/news-1-417853104.html",
        "keywords": ["造价咨询", "造价编制", "造价审核"],
        "collectedAt": "2026-05-09",
        "slot": "上午",
        "budget": "协议期内",
        "region": "北京",
        "description": "地区：北京；采购单位：某部；服务期限3年；工程造价编制及审核服务"
    },
    {
        "id": 9997,
        "title": "南开大学国家基础研究创新提升工程建设项目（化学）全过程造价咨询服务公开招标公告",
        "pubDate": "2026-05-07",
        "source": "中国政府采购网",
        "link": "https://m.bidcenter.com.cn/news-1-417646829.html",
        "keywords": ["全过程造价", "造价咨询"],
        "collectedAt": "2026-05-09",
        "slot": "上午",
        "budget": "100万元（最高限价80万元）",
        "region": "天津",
        "description": "地区：天津南开区；采购单位：南开大学；预算100万元，最高限价80万元；开标时间2026年6月2日"
    },
    {
        "id": 9996,
        "title": "天津市滨海新区土地发展中心造价咨询服务更正公告",
        "pubDate": "2026-05-08",
        "source": "中国政府采购网天津分网",
        "link": "http://www.ccgp.gov.cn/cggg/dfgg/gzgg/202605/t20260508_26530532.htm",
        "keywords": ["造价咨询"],
        "collectedAt": "2026-05-09",
        "slot": "上午",
        "budget": "90万元（6个包，每包15万元）",
        "region": "天津",
        "description": "地区：天津滨海新区；采购单位：天津市滨海新区土地发展中心；预算90万元；开标时间2026年5月20日"
    },
    {
        "id": 9995,
        "title": "重点城市界面沿线风貌一体化设计公开招标公告",
        "pubDate": "2026-05-08",
        "source": "中国政府采购网河北分网",
        "link": "http://www.ccgp.gov.cn/cggg/dfgg/gkzb/202605/t20260508_26525045.htm",
        "keywords": ["设计", "城市设计"],
        "collectedAt": "2026-05-09",
        "slot": "上午",
        "budget": "160万元",
        "region": "雄安新区",
        "description": "地区：雄安新区；采购单位：河北雄安新区自然资源和规划局；预算160万元；服务期限12个月"
    },
    {
        "id": 9994,
        "title": "东尖塔村棚户区改造二期项目全过程造价咨询招标公告",
        "pubDate": "2026-05-08",
        "source": "河北招标网",
        "link": "https://hbs.bidcenter.com.cn/zhaobiao/zbkeyw-24187-0-0-0.html",
        "keywords": ["全过程造价", "造价咨询", "棚户区改造"],
        "collectedAt": "2026-05-09",
        "slot": "上午",
        "budget": "未知",
        "region": "河北廊坊",
        "description": "地区：河北廊坊；项目名称：东尖塔村棚户区改造二期项目全过程造价咨询"
    },
    {
        "id": 9993,
        "title": "招标代理及造价咨询服务商采购项目招标公告",
        "pubDate": "2026-05-08",
        "source": "河北招标网",
        "link": "https://hbs.bidcenter.com.cn/zhaobiao/zbkeyw-24187-0-0-0.html",
        "keywords": ["招标代理", "造价咨询"],
        "collectedAt": "2026-05-09",
        "slot": "上午",
        "budget": "未知",
        "region": "河北石家庄",
        "description": "地区：河北石家庄藁城区；采购单位：河北国津天创污水处理有限责任公司"
    },
    {
        "id": 9992,
        "title": "中国铁路北京局集团有限公司邯郸机务段委托第三方工程造价咨询服务项目竞争性谈判采购公告",
        "pubDate": "2026-05-08",
        "source": "采招网",
        "link": "https://m.bidcenter.com.cn/news-1-417923815.html",
        "keywords": ["造价咨询", "工程造价", "预算编制", "结算审核"],
        "collectedAt": "2026-05-09",
        "slot": "上午",
        "budget": "未知",
        "region": "河北邯郸",
        "description": "地区：河北邯郸；采购单位：邯郸机务段；服务内容：预算编制、结算审核"
    },
    {
        "id": 9991,
        "title": "中国铁路北京局集团有限公司唐山车务段2026年度零小工程项目造价咨询审核服务采购公告",
        "pubDate": "2026-05-08",
        "source": "河北招标网",
        "link": "https://m.bidizhaobiao.com/tag_17_46/",
        "keywords": ["造价咨询", "造价审核"],
        "collectedAt": "2026-05-09",
        "slot": "上午",
        "budget": "未知",
        "region": "河北唐山",
        "description": "地区：河北唐山；采购单位：中国铁路北京局集团有限公司唐山车务段"
    },
    {
        "id": 9990,
        "title": "邢台市信都区西董村城中村改造项目B区全过程造价跟踪服务项目招标公告",
        "pubDate": "2026-05-08",
        "source": "河北招标网",
        "link": "https://m.bidizhaobiao.com/tag_17_46/",
        "keywords": ["全过程造价", "造价跟踪", "城中村改造"],
        "collectedAt": "2026-05-09",
        "slot": "上午",
        "budget": "未知",
        "region": "河北邢台",
        "description": "地区：河北邢台；项目名称：邢台市信都区西董村城中村改造项目B区全过程造价跟踪服务"
    },
    {
        "id": 9989,
        "title": "河北高速集团电子科技产业园项目定制区一期全过程造价咨询服务招标公告",
        "pubDate": "2026-05-08",
        "source": "河北招标网",
        "link": "https://m.bidizhaobiao.com/tag_17_46/",
        "keywords": ["全过程造价", "造价咨询"],
        "collectedAt": "2026-05-09",
        "slot": "上午",
        "budget": "未知",
        "region": "河北石家庄",
        "description": "地区：河北石家庄；项目名称：河北高速集团电子科技产业园项目定制区一期全过程造价咨询服务"
    },
    {
        "id": 9988,
        "title": "廊坊经济技术开发区东部片区基础设施及配套工程(一期)全过程造价咨询公开招标公告",
        "pubDate": "2026-04-28",
        "source": "中国政府采购网",
        "link": "http://www.ccgp.gov.cn/cggg/dfgg/gkzb/202604/t20260428_26471144.htm",
        "keywords": ["全过程造价", "造价咨询", "基础设施"],
        "collectedAt": "2026-05-09",
        "slot": "上午",
        "budget": "157.642万元",
        "region": "河北廊坊",
        "description": "地区：河北廊坊；采购单位：廊坊经济技术开发区住房和城乡建设局；预算157.642万元；开标时间2026年5月21日"
    },
    {
        "id": 9987,
        "title": "2026年工程造价咨询服务（沧州）",
        "pubDate": "2026-05-07",
        "source": "河北招标网",
        "link": "https://hbs.bidcenter.com.cn/zhaobiao/zbkeyw-24187-0-0-0.html",
        "keywords": ["造价咨询", "工程造价"],
        "collectedAt": "2026-05-09",
        "slot": "上午",
        "budget": "未知",
        "region": "河北沧州",
        "description": "地区：河北沧州；2026年工程造价咨询服务"
    },
    {
        "id": 9986,
        "title": "宽城满族自治县生活污水处理厂改扩建项目招标代理服务造价咨询服务",
        "pubDate": "2026-05-07",
        "source": "河北招标网",
        "link": "https://hbs.bidcenter.com.cn/zhaobiao/zbkeyw-24187-0-0-0.html",
        "keywords": ["招标代理", "造价咨询", "污水处理"],
        "collectedAt": "2026-05-09",
        "slot": "上午",
        "budget": "未知",
        "region": "河北承德",
        "description": "地区：河北承德宽城满族自治县；项目名称：宽城满族自治县生活污水处理厂改扩建项目招标代理服务造价咨询"
    },
    {
        "id": 9985,
        "title": "高铁片区南地下智慧车库项目结算审核造价咨询机构比选公告",
        "pubDate": "2026-05-07",
        "source": "河北招标网",
        "link": "https://hbs.bidcenter.com.cn/zhaobiao/zbkeyw-24187-0-0-0.html",
        "keywords": ["造价咨询", "结算审核"],
        "collectedAt": "2026-05-09",
        "slot": "上午",
        "budget": "未知",
        "region": "河北石家庄",
        "description": "地区：河北石家庄；项目名称：高铁片区南地下智慧车库项目结算审核造价咨询机构比选；建筑面积14803.84平方米"
    },
    {
        "id": 9984,
        "title": "绿能公司2026年度第一批新能源项目全过程造价咨询服务询价通知",
        "pubDate": "2026-05-07",
        "source": "河北招标网",
        "link": "https://hbs.bidcenter.com.cn/zhaobiao/zbkeyw-24187-0-0-0.html",
        "keywords": ["全过程造价", "造价咨询", "新能源"],
        "collectedAt": "2026-05-09",
        "slot": "上午",
        "budget": "未知",
        "region": "河北张家口",
        "description": "地区：河北张家口；项目名称：绿能公司2026年度第一批新能源项目全过程造价咨询服务"
    },
    {
        "id": 9983,
        "title": "蠡县留史镇坑塘治理工程结算审核造价咨询服务项目竞争性磋商公告",
        "pubDate": "2026-05-07",
        "source": "河北招标网",
        "link": "https://hbs.bidcenter.com.cn/zhaobiao/zbkeyw-24187-0-0-0.html",
        "keywords": ["造价咨询", "结算审核", "坑塘治理"],
        "collectedAt": "2026-05-09",
        "slot": "上午",
        "budget": "未知",
        "region": "河北保定",
        "description": "地区：河北保定蠡县；项目名称：蠡县留史镇坑塘治理工程结算审核造价咨询服务"
    },
    {
        "id": 9982,
        "title": "晟泰澜樾项目造价咨询服务项目竞争性磋商公告",
        "pubDate": "2026-05-07",
        "source": "河北招标网",
        "link": "https://hbs.bidcenter.com.cn/zhaobiao/zbkeyw-24187-0-0-0.html",
        "keywords": ["造价咨询"],
        "collectedAt": "2026-05-09",
        "slot": "上午",
        "budget": "未知",
        "region": "河北衡水",
        "description": "地区：河北衡水；项目名称：晟泰澜樾项目造价咨询服务"
    },
    {
        "id": 9981,
        "title": "裕华区品质裕华智慧大脑PPP造价服务项目招标公告",
        "pubDate": "2026-05-06",
        "source": "河北招标网",
        "link": "https://m.bidizhaobiao.com/tag_17_46/",
        "keywords": ["造价服务", "PPP"],
        "collectedAt": "2026-05-09",
        "slot": "上午",
        "budget": "未知",
        "region": "河北石家庄",
        "description": "地区：河北石家庄裕华区；项目名称：裕华区品质裕华智慧大脑PPP造价服务项目"
    },
    {
        "id": 9980,
        "title": "安新县燃气安全设施更新改造项目全过程造价咨询服务采购",
        "pubDate": "2026-05-06",
        "source": "雄安新区政府采购网",
        "link": "https://m.bidcenter.com.cn/news-2-416384917.html",
        "keywords": ["全过程造价", "造价咨询", "燃气安全"],
        "collectedAt": "2026-05-09",
        "slot": "上午",
        "budget": "48万元",
        "region": "雄安新区",
        "description": "地区：雄安新区安新县；采购单位：安新县住房和城乡建设局；预算48万元；预计采购时间2026年5月"
    }
]

# 读取现有JSON文件
file_path = os.path.expanduser('~/bidding-announcements/data/announcements.json')
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# 获取现有最大ID
existing_ids = [ann.get('id', 0) for ann in data.get('announcements', [])]
max_id = max(existing_ids) if existing_ids else 0

# 更新新公告的ID（避免与现有ID冲突）
for ann in new_announcements:
    ann['id'] = max_id + new_announcements.index(ann) + 1

# 将新公告添加到列表开头（最新在前）
existing_announcements = data.get('announcements', [])
all_announcements = new_announcements + existing_announcements

# 过滤出京津冀地区公告
jjj_keywords = ['北京', '天津', '河北', '石家庄', '唐山', '保定', '廊坊', '秦皇岛', 
                '邯郸', '邢台', '张家口', '承德', '沧州', '衡水', '雄安', '雄县', 
                '容城', '安新', '滨海新区', '北京']

jjj_announcements = []
for ann in all_announcements:
    title = ann.get('title', '')
    region = ann.get('region', '')
    desc = ann.get('description', '')
    
    # 检查是否属于京津冀地区
    is_jjj = any(kw in title or kw in region or kw in desc for kw in jjj_keywords)
    if is_jjj:
        # 添加region字段
        if 'region' not in ann:
            ann['region'] = region
        jjj_announcements.append(ann)

# 更新数据
data['announcements'] = jjj_announcements
data['lastUpdate'] = datetime.now().strftime('%Y-%m-%d %H:%M')
data['totalCount'] = len(jjj_announcements)

# 写入更新后的JSON文件
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✅ 更新完成！")
print(f"- 总公告数：{data['totalCount']}")
print(f"- 最后更新时间：{data['lastUpdate']}")
print(f"- 新增公告数：{len(new_announcements)}")
