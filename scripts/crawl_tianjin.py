#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
天津市政府采购网公告抓取脚本 v2.0
支持从天津市政府采购中心网站抓取公告，自动过滤京津冀地区5个工作日内的相关公告

使用方法:
    python crawl_tianjin.py

输出:
    - data/tianjin_announcements.json: 抓取的原始数据
    - 更新 data/announcements.json: 合并后的公告数据
"""

import requests
from bs4 import BeautifulSoup
import json
import re
import time
import random
import os
import sys
from datetime import datetime, timedelta

# 京津冀关键词
JJJ_KEYWORDS = ['北京', '天津', '河北', '石家庄', '唐山', '保定', '廊坊', '秦皇岛', 
                '邯郸', '邢台', '张家口', '承德', '沧州', '衡水', '雄安', '雄安新区']

# 行业关键词
INDUSTRY_KEYWORDS = ['造价', '造价咨询', '全过程咨询', '全过程造价', '招标代理', 
                     '项目管理', '工程监理', '全过程工程', '结算审计', '预算编制',
                     '协审', '评审']

# 请求头
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Referer': 'http://tjgpc.zwfwb.tj.gov.cn/web_index1.do',
}

def is_jjj_related(text):
    """判断是否与京津冀相关"""
    text = text or ''
    return any(kw in text for kw in JJJ_KEYWORDS)

def is_industry_related(text):
    """判断是否与造价咨询行业相关"""
    text = text or ''
    return any(kw in text for kw in INDUSTRY_KEYWORDS)

# 2026年法定节假日
HOLIDAYS_2026 = [
    # 元旦
    datetime(2026, 1, 1),
    # 春节
    datetime(2026, 2, 15), datetime(2026, 2, 16), datetime(2026, 2, 17),
    datetime(2026, 2, 18), datetime(2026, 2, 19), datetime(2026, 2, 20), datetime(2026, 2, 21),
    # 清明节
    datetime(2026, 4, 4), datetime(2026, 4, 5), datetime(2026, 4, 6),
    # 劳动节
    datetime(2026, 5, 1), datetime(2026, 5, 2), datetime(2026, 5, 3),
    datetime(2026, 5, 4), datetime(2026, 5, 5),
    # 端午节（假设）
    datetime(2026, 6, 19), datetime(2026, 6, 20), datetime(2026, 6, 21),
    # 中秋节（假设）
    datetime(2026, 9, 25), datetime(2026, 9, 26), datetime(2026, 9, 27),
    # 国庆节（假设）
    datetime(2026, 10, 1), datetime(2026, 10, 2), datetime(2026, 10, 3),
    datetime(2026, 10, 4), datetime(2026, 10, 5), datetime(2026, 10, 6), datetime(2026, 10, 7),
]

def is_workday(date_obj):
    """判断是否为工作日（排除周末和法定节假日）"""
    if date_obj.weekday() >= 5:
        return False
    # 统一用 date() 比较，避免时间部分不一致导致节假日判断失败
    check_date = date_obj.date() if hasattr(date_obj, 'date') else date_obj
    holiday_dates = [h.date() if hasattr(h, 'date') else h for h in HOLIDAYS_2026]
    if check_date in holiday_dates:
        return False
    return True

def is_within_working_days(date_str, n=5):
    """判断日期是否在N个工作日内（正确考虑法定节假日）"""
    if not date_str:
        return False
    try:
        pub_date = datetime.strptime(date_str.strip()[:10], '%Y-%m-%d')
        today = datetime.now()
        
        # 计算N个工作日前的日期（排除节假日）
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

def get_announcements(keyword, max_pages=10):
    """从天津市政府采购中心获取公告"""
    announcements = []
    
    for page in range(1, max_pages + 1):
        url = f"http://tjgpc.zwfwb.tj.gov.cn/webInfo/getSearchWebInfoList1.do?keyWord={keyword}&page={page}"
        
        try:
            response = requests.get(url, headers=HEADERS, timeout=30)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # 提取文档链接
            doc_links = soup.find_all('a', href=re.compile(r'documentView'))
            
            if not doc_links:
                break
            
            for link in doc_links:
                href = link.get('href', '')
                title = link.get_text(strip=True)
                
                # 跳过分类标签
                if title.startswith('[') and ']' in title[:10]:
                    continue
                if not title or len(title) < 15:
                    continue
                
                # 提取ID
                match = re.search(r'id=(\d+)', href)
                doc_id = match.group(1) if match else ''
                
                # 获取日期
                parent = link.find_parent('li') or link.find_parent('tr') or link.parent
                parent_text = parent.get_text() if parent else ''
                date_match = re.search(r'(\d{4}-\d{2}-\d{2})', parent_text)
                date_str = date_match.group(1) if date_match else ''
                
                announcements.append({
                    'title': title,
                    'pubDate': date_str,
                    'link': f"http://www.ccgp-tianjin.gov.cn/portal/documentView.do?method=view&id={doc_id}" if doc_id else href,
                    'source': '天津市政府采购中心',
                    'category': keyword,
                    'description': '',
                    'budget': '',
                })
            
            time.sleep(random.uniform(0.3, 0.8))
            
        except Exception as e:
            print(f"  抓取「{keyword}」第{page}页失败: {e}")
            break
    
    return announcements

def get_announcement_detail(url):
    """获取公告详情"""
    try:
        response = requests.get(url, headers=HEADERS, timeout=30)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 获取文本内容
        text = soup.get_text()
        
        # 提取预算金额
        budget_match = re.search(r'(预算金额|最高限价|项目预算)[:：]\s*(\d+\.?\d*)\s*万元', text)
        budget = budget_match.group(2) + '万元' if budget_match else ''
        
        # 提取详情描述（项目需求、采购内容等）
        lines = [l.strip() for l in text.split('\n') if l.strip()]
        
        # 查找关键词附近的描述
        description = ''
        for i, line in enumerate(lines):
            if any(kw in line for kw in INDUSTRY_KEYWORDS):
                start = max(0, i-1)
                end = min(len(lines), i+5)
                description = ' '.join(lines[start:end])
                break
        
        if not description:
            description = ' '.join(lines[5:15]) if len(lines) > 15 else ''
        
        return {
            'description': description[:500],
            'budget': budget,
        }
    except:
        return {'description': '', 'budget': ''}

def filter_announcements(announcements):
    """过滤京津冀相关且5个工作日内的公告"""
    filtered = []
    
    for item in announcements:
        title = item.get('title', '')
        full_text = title
        
        # 天津本身就是京津冀地区，所以天津的公告也保留
        if not is_jjj_related(full_text) and '天津' not in full_text:
            continue
        
        # 判断是否与行业相关
        if not is_industry_related(full_text):
            continue
        
        # 判断是否在5个工作日内
        if item.get('pubDate') and not is_within_working_days(item['pubDate'], 5):
            continue
        
        # 添加关键词标签
        keywords = [kw for kw in INDUSTRY_KEYWORDS if kw in title]
        item['keywords'] = keywords
        
        filtered.append(item)
    
    return filtered

def save_results(announcements, output_file='data/tianjin_announcements.json'):
    """保存结果到JSON文件"""
    os.makedirs(os.path.dirname(output_file) if os.path.dirname(output_file) else '.', exist_ok=True)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(announcements, f, ensure_ascii=False, indent=2)
    
    return len(announcements)

def merge_to_main_data(new_announcements, main_file='data/announcements.json'):
    """合并到主数据文件"""
    # 读取现有数据
    existing_data = {'lastUpdate': '', 'totalCount': 0, 'announcements': []}
    if os.path.exists(main_file):
        try:
            with open(main_file, 'r', encoding='utf-8') as f:
                existing_data = json.load(f)
        except:
            pass
    
    # 去重合并
    existing_links = {item['link'] for item in existing_data['announcements']}
    existing_titles = {item['title'] for item in existing_data['announcements']}
    
    new_count = 0
    for item in new_announcements:
        if item['link'] not in existing_links and item['title'] not in existing_titles:
            item['id'] = len(existing_data['announcements']) + 1
            item['collectedAt'] = datetime.now().strftime('%Y-%m-%d')
            existing_data['announcements'].insert(0, item)
            new_count += 1
    
    # 更新元数据
    existing_data['lastUpdate'] = datetime.now().strftime('%Y-%m-%d %H:%M')
    existing_data['totalCount'] = len(existing_data['announcements'])
    
    # 保存
    with open(main_file, 'w', encoding='utf-8') as f:
        json.dump(existing_data, f, ensure_ascii=False, indent=2)
    
    return new_count, existing_data['totalCount']

def main():
    """主函数"""
    print("=" * 60)
    print("天津市政府采购网公告抓取程序")
    print("=" * 60)
    
    # 搜索关键词
    keywords = ['造价', '全过程', '项目管理', '监理', '招标代理', '协审']
    
    all_announcements = []
    
    for kw in keywords:
        print(f"\n搜索关键词: {kw}")
        results = get_announcements(kw, max_pages=5)
        print(f"  获取到 {len(results)} 条公告")
        all_announcements.extend(results)
        
        # 避免请求过快
        time.sleep(random.uniform(0.5, 1))
    
    # 去重
    seen = set()
    unique = []
    for item in all_announcements:
        key = item['link']
        if key not in seen:
            seen.add(key)
            unique.append(item)
    
    print(f"\n去重后共 {len(unique)} 条公告")
    
    # 过滤
    filtered = filter_announcements(unique)
    print(f"京津冀相关且5个工作日内: {len(filtered)} 条")
    
    # 获取详情
    print("\n获取公告详情...")
    for item in filtered[:10]:  # 限制获取数量避免超时
        detail = get_announcement_detail(item['link'])
        item['description'] = detail['description']
        item['budget'] = detail['budget']
        time.sleep(0.3)
    
    # 保存原始数据
    save_count = save_results(filtered)
    print(f"已保存 {save_count} 条到 data/tianjin_announcements.json")
    
    # 合并到主数据
    new_count, total_count = merge_to_main_data(filtered)
    print(f"新增 {new_count} 条，总数 {total_count} 条")
    
    # 显示结果
    if filtered:
        print("\n" + "-" * 40)
        print("最新公告:")
        for item in filtered[:5]:
            print(f"  [{item['pubDate']}] {item['title'][:45]}...")
            if item.get('budget'):
                print(f"    预算: {item['budget']}")
    
    print("\n" + "=" * 60)
    print("抓取完成!")
    print("=" * 60)
    
    return filtered

if __name__ == '__main__':
    results = main()
    sys.exit(0 if results else 1)
