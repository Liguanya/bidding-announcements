#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
招标公告推送平台 - 自动化更新脚本
用于每日定时更新网页数据
"""

import os
import sys
import json
import re
from datetime import datetime
from pathlib import Path

# ============================================
# 路径配置
# ============================================
SCRIPT_DIR = Path(__file__).parent.resolve()
PROJECT_ROOT = Path.cwd().resolve()
SOURCE_DIR = PROJECT_ROOT / "造价咨询" / "招标公告监控"
OUTPUT_DIR = SCRIPT_DIR.parent / "data"
OUTPUT_FILE = OUTPUT_DIR / "announcements.json"


def detect_keywords(title):
    """检测标题中的关键词"""
    keywords = []
    keyword_map = {
        '造价': ['造价'],
        '造价咨询': ['造价咨询'],
        '全过程咨询': ['全过程咨询', '全过程造价'],
        '招标代理': ['招标代理'],
        '项目管理': ['项目管理']
    }
    
    for keyword, patterns in keyword_map.items():
        if any(p in title for p in patterns):
            keywords.append(keyword)
    
    if not keywords:
        keywords.append('其他')
    
    return keywords


def format_display_date(date_key):
    """格式化日期显示"""
    if len(date_key) == 8:
        return f"{date_key[:4]}-{date_key[4:6]}-{date_key[6:8]}"
    return date_key


def extract_links(text):
    """从文本中提取链接"""
    links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', text)
    return {title: url for title, url in links}


def parse_detail_report(md_content, date_key, filename):
    """解析详细的监控报告文件（晚间.md等）"""
    announcements = []
    links = extract_links(md_content)
    
    # 匹配表格格式: | 1 | 标题 | 时间 | 关键词 | [查看](url) |
    table_pattern = r'\|\s*\d+\s*\|\s*([^\|]{10,100})\s*\|\s*(\d{4}-\d{2}-\d{2})\s*\|\s*([^\|]+?)\s*\|\s*\[查看\]\(([^)]+)\)'
    matches = re.findall(table_pattern, md_content)
    
    for title, pub_date, keyword_info, url in matches:
        title = title.strip()
        
        # 过滤无效标题
        if len(title) < 5 or any(skip in title for skip in ['暂无', '无相关', '---']):
            continue
        
        # 提取关键词
        keywords = detect_keywords(title)
        
        # 检测来源
        source = "中国政府采购网"
        if '天津市政府采购网' in md_content[:1000] or '天津' in md_content[:500]:
            # 检查上下文判断是哪个来源
            section_start = max(0, md_content.find(title) - 500)
            section = md_content[section_start:md_content.find(title)]
            if '天津市政府采购网' in section or '天津' in section:
                source = "天津市政府采购网"
        
        # 提取金额（从关键词信息）
        budget = None
        budget_match = re.search(r'(\d+(?:\.\d+)?)\s*(?:万|元)', keyword_info)
        if budget_match:
            budget = budget_match.group(1)
            unit = '万元' if '万' in keyword_info[budget_match.start():budget_match.end()+2] else '元'
            budget = f"{budget}{unit}"
        
        # 提取代理机构
        agency = None
        agency_match = re.search(r'代理[：:]\s*([^\s，。,]+)', keyword_info)
        if agency_match:
            agency = agency_match.group(1).strip()
        
        announcement = {
            'id': 0,  # 稍后填充
            'title': title,
            'date': pub_date,
            'dateKey': date_key,
            'source': source,
            'keywords': keywords,
            'url': url,
            'budget': budget,
            'unit': None,
            'agency': agency,
            'content': None,
            'publishTime': pub_date
        }
        
        announcements.append(announcement)
    
    # 匹配汇总格式: | 项目名 | 单位 | 金额 | [查看](url) |
    summary_pattern = r'\|\s*([^\|]{10,80})\s*\|[^\|]*\|[^\|]*\|\s*\[查看\]\(([^)]+)\)'
    summary_matches = re.findall(summary_pattern, md_content)
    
    for title, url in summary_matches:
        title = title.strip()
        if len(title) < 10 or any(skip in title for skip in ['项目名称', '---', '暂无']):
            continue
        
        # 检查是否已存在
        if any(a['title'] == title for a in announcements):
            continue
        
        announcement = {
            'id': 0,
            'title': title,
            'date': format_display_date(date_key),
            'dateKey': date_key,
            'source': "天津市政府采购网" if '天津' in md_content[:500] else "中国政府采购网",
            'keywords': detect_keywords(title),
            'url': url,
            'budget': None,
            'unit': None,
            'agency': None,
            'content': None,
            'publishTime': None
        }
        
        announcements.append(announcement)
    
    return announcements


def parse_simple_summary(md_content, date_key):
    """解析简单汇总格式"""
    announcements = []
    
    # 匹配表格格式
    patterns = [
        # 带链接的表格
        r'\|\s*([^\|]{10,80})\s*\|[^\|]*\|[^\|]*\|\s*\[查看\]\(([^)]+)\)',
        # 另一种格式
        r'\|\s*([^\|]{10,60})\s*\|\s*([^\|]+?)\s*\|\s*([^\|]+?)\s*\|\s*\[查看\]\(([^)]+)\)',
    ]
    
    for pattern in patterns:
        matches = re.findall(pattern, md_content)
        for match in matches:
            if len(match) >= 2:
                title = match[0].strip() if isinstance(match[0], str) else match[0]
                url = match[-1] if isinstance(match[-1], str) else match[1]
                
                if len(title) < 10 or any(skip in title for skip in ['项目名称', '---', '暂无', '无']):
                    continue
                
                # 检查是否已存在
                if any(a['title'] == title for a in announcements):
                    continue
                
                source = "中国政府采购网"
                if '天津' in md_content[:500]:
                    source = "天津市政府采购网"
                
                announcement = {
                    'id': 0,
                    'title': title,
                    'date': format_display_date(date_key),
                    'dateKey': date_key,
                    'source': source,
                    'keywords': detect_keywords(title),
                    'url': url,
                    'budget': None,
                    'unit': None,
                    'agency': None,
                    'content': None,
                    'publishTime': None
                }
                
                announcements.append(announcement)
    
    return announcements


def process_all_data():
    """处理所有日期目录的数据"""
    all_announcements = []
    seen_titles = set()
    
    if not SOURCE_DIR.exists():
        print(f"❌ 数据源目录不存在: {SOURCE_DIR}")
        return []
    
    # 获取所有日期目录
    date_dirs = [d for d in SOURCE_DIR.iterdir() if d.is_dir() and re.match(r'\d{8}', d.name)]
    date_dirs.sort(key=lambda x: x.name, reverse=True)
    
    print(f"\n📁 找到 {len(date_dirs)} 个日期目录")
    
    for date_dir in date_dirs:
        date_key = date_dir.name
        
        # 按优先级处理文件
        files_to_try = [
            ("晚间.md", lambda c, dk, f: parse_detail_report(c, dk, f)),
            ("下午.md", lambda c, dk, f: parse_detail_report(c, dk, f)),
            ("早间.md", lambda c, dk, f: parse_detail_report(c, dk, f)),
            ("每日汇总.md", lambda c, dk, f: parse_simple_summary(c, dk)),
        ]
        
        found_count = 0
        for filename, parser_func in files_to_try:
            file_path = date_dir / filename
            if file_path.exists():
                try:
                    content = file_path.read_text(encoding='utf-8')
                    announcements = parser_func(content, date_key, str(file_path))
                    
                    for ann in announcements:
                        if ann['title'] not in seen_titles:
                            seen_titles.add(ann['title'])
                            ann['id'] = len(all_announcements) + 1
                            all_announcements.append(ann)
                            found_count += 1
                            
                except Exception as e:
                    print(f"   ⚠️ {date_key}/{filename}: 解析失败 - {e}")
        
        if found_count > 0:
            print(f"   {date_key}: 提取 {found_count} 条公告")
    
    # 重新排序
    all_announcements.sort(key=lambda x: (x['dateKey'], -x['id']), reverse=True)
    
    # 重新编号
    for i, ann in enumerate(all_announcements):
        ann['id'] = i + 1
    
    return all_announcements


def update_data():
    """更新数据"""
    print("=" * 50)
    print("📢 招标公告推送平台 - 数据更新")
    print("=" * 50)
    print(f"⏰ 执行时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    # 处理数据
    announcements = process_all_data()
    
    # 确保输出目录存在
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    # 构建输出数据
    output_data = {
        "updateTime": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "totalCount": len(announcements),
        "announcements": announcements
    }
    
    # 写入JSON
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)
    
    print()
    print(f"✅ 数据更新完成!")
    print(f"   - 总公告数: {len(announcements)}")
    print(f"   - 输出文件: {OUTPUT_FILE}")
    
    # 统计
    if announcements:
        sources = {}
        keywords_count = {}
        for ann in announcements:
            sources[ann['source']] = sources.get(ann['source'], 0) + 1
            for kw in ann['keywords']:
                keywords_count[kw] = keywords_count.get(kw, 0) + 1
        
        print(f"\n📊 数据统计:")
        for src, cnt in sources.items():
            print(f"   - {src}: {cnt}条")
        print(f"   关键词分布:")
        for kw, cnt in keywords_count.items():
            print(f"     • {kw}: {cnt}条")
    
    return len(announcements)


if __name__ == "__main__":
    update_data()
