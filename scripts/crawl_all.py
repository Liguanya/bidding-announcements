#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
京津冀招标公告综合抓取脚本 v1.0
抓取天津市政府采购中心、河北省政府采购网等网站的公告
"""

import requests
from bs4 import BeautifulSoup
import json
import re
from datetime import datetime, timedelta
import time
import random
import os

# ========== 配置 ==========
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}

# 京津冀关键词
JJJ_KEYWORDS = ['北京', '天津', '河北', '石家庄', '唐山', '保定', '廊坊', '秦皇岛', 
                '邯郸', '邢台', '张家口', '承德', '沧州', '衡水', '雄安']

# 行业关键词
INDUSTRY_KEYWORDS = ['造价', '造价咨询', '全过程咨询', '全过程造价', '全过程工程', 
                     '招标代理', '项目管理', '工程监理', '结算审计', '预算编制',
                     '协审', '评审', '绩效评价', '投资评审', '跟踪审计', '工程咨询']

# 2026年法定节假日
HOLIDAYS_2026 = [
    datetime(2026, 1, 1),  # 元旦
    datetime(2026, 2, 15), datetime(2026, 2, 16), datetime(2026, 2, 17),
    datetime(2026, 2, 18), datetime(2026, 2, 19), datetime(2026, 2, 20), datetime(2026, 2, 21),
    datetime(2026, 4, 4), datetime(2026, 4, 5), datetime(2026, 4, 6),
    datetime(2026, 5, 1), datetime(2026, 5, 2), datetime(2026, 5, 3),
    datetime(2026, 5, 4), datetime(2026, 5, 5),
    datetime(2026, 6, 19), datetime(2026, 6, 20), datetime(2026, 6, 21),
    datetime(2026, 9, 25), datetime(2026, 9, 26), datetime(2026, 9, 27),
    datetime(2026, 10, 1), datetime(2026, 10, 2), datetime(2026, 10, 3),
    datetime(2026, 10, 4), datetime(2026, 10, 5), datetime(2026, 10, 6), datetime(2026, 10, 7),
]

# ========== 工具函数 ==========
def is_workday(date_obj):
    """判断是否为工作日"""
    if date_obj.weekday() >= 5:
        return False
    check_date = date_obj.date() if hasattr(date_obj, 'date') else date_obj
    holiday_dates = [h.date() if hasattr(h, 'date') else h for h in HOLIDAYS_2026]
    if check_date in holiday_dates:
        return False
    return True

def is_within_working_days(date_str, n=5):
    """判断日期是否在N个工作日内"""
    if not date_str:
        return False
    try:
        pub_date = datetime.strptime(date_str.strip()[:10], '%Y-%m-%d')
        today = datetime.now()
        
        count = 0
        days_ago = 0
        while count < n:
            days_ago += 1
            check_date = today - timedelta(days=days_ago)
            if is_workday(check_date):
                count += 1
        
        start_date = today - timedelta(days=days_ago)
        return start_date <= pub_date <= today
    except:
        return False

def is_jjj_related(text):
    """判断是否与京津冀相关"""
    text = text or ''
    return any(kw in text for kw in JJJ_KEYWORDS)

def is_industry_related(text):
    """判断是否与造价咨询行业相关"""
    text = text or ''
    return any(kw in text for kw in INDUSTRY_KEYWORDS)

def normalize_url(href, base_url=''):
    """标准化URL"""
    if href.startswith('http'):
        return href
    elif href.startswith('//'):
        return 'https:' + href
    elif href.startswith('/'):
        return base_url + href
    else:
        return base_url + '/' + href

def extract_date_from_text(text):
    """从文本中提取日期"""
    patterns = [
        r'(\d{4}-\d{1,2}-\d{1,2})',
        r'(\d{4}/\d{1,2}/\d{1,2})',
        r'(\d{4}\.\d{1,2}\.\d{1,2})',
    ]
    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            return match.group(1).replace('/', '.').replace('-', '-')
    return None

# ========== 抓取函数 ==========

def crawl_tianjin_gpc():
    """抓取天津市政府采购中心"""
    print("\n[1/2] 天津市政府采购中心...")
    announcements = []
    
    keywords = ['造价', '全过程', '协审', '评审']
    
    for kw in keywords:
        url = f"http://tjgpc.zwfwb.tj.gov.cn/webInfo/getSearchWebInfoList1.do?keyWord={kw}&page=1"
        try:
            resp = requests.get(url, headers=HEADERS, timeout=30)
            soup = BeautifulSoup(resp.text, 'html.parser')
            links = soup.find_all('a', href=re.compile(r'documentView'))
            
            for link in links:
                title = link.get_text(strip=True)
                href = link.get('href', '')
                
                if len(title) > 15 and is_industry_related(title):
                    # 提取日期（从标题或父元素）
                    date_text = ''
                    parent = link.find_parent(['td', 'li', 'div'])
                    if parent:
                        date_match = re.search(r'(\d{4}-\d{2}-\d{2})', parent.get_text())
                        if date_match:
                            date_text = date_match.group(1)
                    
                    if not date_text:
                        date_text = datetime.now().strftime('%Y-%m-%d')
                    
                    announcements.append({
                        'title': title,
                        'pubDate': date_text,
                        'source': '天津市政府采购中心',
                        'link': normalize_url(href, 'http://www.ccgp-tianjin.gov.cn'),
                        'keywords': [kw for kw in INDUSTRY_KEYWORDS if kw in title],
                    })
            
            time.sleep(random.uniform(0.3, 0.5))
        except Exception as e:
            print(f"  关键词'{kw}'抓取失败: {e}")
    
    # 去重
    seen = set()
    unique = []
    for ann in announcements:
        if ann['title'] not in seen:
            seen.add(ann['title'])
            unique.append(ann)
    
    print(f"  获取到 {len(unique)} 条公告")
    return unique

def crawl_hebei():
    """抓取河北省政府采购网"""
    print("\n[2/2] 河北省政府采购网...")
    announcements = []
    
    pages = [
        ("http://www.ccgp-hebei.gov.cn/zjk/zjk_kfq/", "张家口"),
    ]
    
    for url, region in pages:
        try:
            resp = requests.get(url, headers=HEADERS, timeout=30)
            resp.encoding = 'utf-8'
            soup = BeautifulSoup(resp.text, 'html.parser')
            
            links = soup.find_all('a', href=True)
            for a in links:
                title = a.get_text(strip=True)
                href = a.get('href', '')
                
                if len(title) > 20 and is_industry_related(title):
                    announcements.append({
                        'title': title,
                        'pubDate': datetime.now().strftime('%Y-%m-%d'),
                        'source': f'河北省政府采购网-{region}',
                        'link': normalize_url(href, 'http://www.ccgp-hebei.gov.cn'),
                        'keywords': [kw for kw in INDUSTRY_KEYWORDS if kw in title],
                    })
            
            time.sleep(random.uniform(0.3, 0.5))
        except Exception as e:
            print(f"  {region}抓取失败: {e}")
    
    print(f"  获取到 {len(announcements)} 条公告")
    return announcements

# ========== 主函数 ==========
def main():
    """主函数"""
    print("=" * 60)
    print("京津冀招标公告综合抓取程序")
    print("=" * 60)
    
    all_announcements = []
    
    # 抓取各网站
    tianjin_anns = crawl_tianjin_gpc()
    all_announcements.extend(tianjin_anns)
    
    hebei_anns = crawl_hebei()
    all_announcements.extend(hebei_anns)
    
    # 去重
    seen = set()
    unique_anns = []
    for ann in all_announcements:
        if ann['title'] not in seen:
            seen.add(ann['title'])
            unique_anns.append(ann)
    
    # 过滤5个工作日内的公告
    valid_anns = [a for a in unique_anns if is_within_working_days(a.get('pubDate', ''), 5)]
    
    print(f"\n" + "=" * 60)
    print(f"抓取完成!")
    print(f"  总计: {len(unique_anns)} 条")
    print(f"  5个工作日内: {len(valid_anns)} 条")
    print("=" * 60)
    
    # 更新数据文件
    update_data_files(valid_anns)
    
    return valid_anns

def update_data_files(announcements):
    """更新数据文件"""
    # 切换到项目目录
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.dirname(script_dir)
    os.chdir(project_dir)
    
    # 生成ID
    new_id = 1
    try:
        with open('data/announcements.json', 'r', encoding='utf-8') as f:
            existing_data = json.load(f)
            existing_ids = [a.get('id', 0) for a in existing_data.get('announcements', [])]
            new_id = max(existing_ids) + 1 if existing_ids else 1
    except:
        existing_data = {'totalCount': 0, 'announcements': []}
    
    # 合并现有数据和新数据
    existing_titles = {a.get('title', '') for a in existing_data.get('announcements', [])}
    
    for ann in announcements:
        if ann['title'] not in existing_titles:
            ann['id'] = new_id
            ann['collectedAt'] = datetime.now().strftime('%Y-%m-%d')
            ann['description'] = f"地区：{ann['source']}；{ann['title']}"
            existing_data['announcements'].insert(0, ann)
            new_id += 1
    
    # 更新统计
    existing_data['totalCount'] = len(existing_data['announcements'])
    existing_data['lastUpdate'] = datetime.now().strftime('%Y-%m-%d %H:%M')
    
    # 保存JSON
    with open('data/announcements.json', 'w', encoding='utf-8') as f:
        json.dump(existing_data, f, ensure_ascii=False, indent=2)
    
    print(f"\n✅ 数据已更新: {len(announcements)} 条新公告")

if __name__ == '__main__':
    main()
