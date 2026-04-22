#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
招标公告数据转换脚本
将 Markdown 格式的监控数据转换为 JSON 格式，供网页读取
"""

import os
import json
import re
from datetime import datetime
from pathlib import Path

# 配置路径 - 使用绝对路径确保脚本可正常运行
import os
_current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOURCE_DIR = Path(os.path.join(_current_dir, "造价咨询", "招标公告监控"))
OUTPUT_FILE = Path(os.path.join(_current_dir, "data", "announcements.json"))


def parse_date_from_filename(filename):
    """从文件名提取日期"""
    match = re.search(r'(\d{8})', filename)
    if match:
        date_str = match.group(1)
        return date_str
    return datetime.now().strftime("%Y%m%d")


def parse_table_row(row):
    """解析表格行"""
    cells = re.findall(r'\|([^|]+)\|', row)
    if cells:
        return [cell.strip() for cell in cells if cell.strip()]
    return None


def extract_links(text):
    """从文本中提取链接"""
    links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', text)
    return {title: url for title, url in links}


def parse_markdown_to_announcements(md_content, date_key, source="未知"):
    """解析 Markdown 内容为公告列表"""
    announcements = []
    
    # 提取链接
    links = extract_links(md_content)
    
    # 分割内容块
    blocks = re.split(r'\n---\n', md_content)
    
    for block in blocks:
        lines = block.strip().split('\n')
        
        # 跳过标题块
        if not lines or lines[0].startswith('#'):
            continue
        
        # 查找项目名称行（通常是加粗或表格中的第一个单元格）
        project_patterns = [
            r'\|\s*\*\*(.+?)\s*\*\*',  # **项目名称**
            r'\|\s*([^\|]+?)\s*\|',      # | 项目名称 |
            r'\d+\.\s*\*\*(.+?)\*\*',    # 1. **项目名称**
            r'\*\*(.+?)\*\*',             # **项目名称**
        ]
        
        for i, line in enumerate(lines):
            for pattern in project_patterns:
                match = re.search(pattern, line)
                if match:
                    title = match.group(1).strip()
                    # 过滤掉标题行
                    if len(title) > 5 and not any(skip in title for skip in ['项目名称', '采购单位', '预算', '代理机构', '开标时间']):
                        announcement = {
                            'id': len(announcements) + 1,
                            'title': title,
                            'date': format_display_date(date_key),
                            'dateKey': date_key,
                            'source': source,
                            'keywords': detect_keywords(title),
                            'url': None
                        }
                        
                        # 尝试在同一块内容中查找更多信息
                        block_text = '\n'.join(lines)
                        
                        # 查找链接
                        for check_title, url in links.items():
                            if any(word in check_title for word in title[:10].split()):
                                announcement['url'] = url
                                break
                        
                        # 查找金额
                        budget_match = re.search(r'(\d+(?:\.\d+)?)\s*(?:万|元)', block_text)
                        if budget_match:
                            amount = float(budget_match.group(1))
                            unit = '万元' if '万' in budget_match.group(0) else '元'
                            announcement['budget'] = f"{amount}{unit}"
                        
                        # 查找采购单位
                        unit_match = re.search(r'采购单位[：:]\s*([^\n|]+)', block_text)
                        if unit_match:
                            announcement['unit'] = unit_match.group(1).strip()
                        
                        # 查找代理机构
                        agency_match = re.search(r'代理机构[：:]\s*([^\n|]+)', block_text)
                        if agency_match:
                            announcement['agency'] = agency_match.group(1).strip()
                        
                        # 提取摘要
                        if len(lines) > i + 1:
                            summary_lines = []
                            for j in range(i + 1, min(i + 4, len(lines))):
                                clean_line = re.sub(r'\|', '', lines[j]).strip()
                                clean_line = re.sub(r'\*\*|\*|`', '', clean_line)
                                if clean_line and not clean_line.startswith('http'):
                                    summary_lines.append(clean_line)
                            if summary_lines:
                                announcement['summary'] = ' | '.join(summary_lines[:2])
                        
                        announcements.append(announcement)
                        break
    
    return announcements


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


def parse_simple_announcement(md_content, date_key, filename):
    """解析简单格式的公告（从汇总文件提取）"""
    announcements = []
    
    # 尝试匹配各种公告格式
    patterns = [
        # 表格行格式
        r'\|\s*([^\|]{10,60})\s*\|[^\|]*\|[^\|]*\|\s*\[查看\]\(([^)]+)\)',
        # 带链接的格式
        r'\|\s*([^\|]{10,60})\s*\|\s*([^\|]+?)\s*\|\s*([^\|]+?)\s*\|\s*\[查看\]\(([^)]+)\)',
    ]
    
    for pattern in patterns:
        matches = re.findall(pattern, md_content)
        for match in matches:
            if len(match) >= 2:
                title = match[0].strip()
                url = match[-1]  # 最后一个是URL
                
                # 过滤无效标题
                if len(title) < 10 or any(skip in title for skip in ['项目名称', '---', '暂无']):
                    continue
                
                # 确定来源
                source = "中国政府采购网"
                if '天津' in md_content and '天津市政府采购' in md_content:
                    source = "天津市政府采购网"
                
                announcement = {
                    'id': len(announcements) + 1,
                    'title': title,
                    'date': format_display_date(date_key),
                    'dateKey': date_key,
                    'source': source,
                    'keywords': detect_keywords(title),
                    'url': url,
                    'publishTime': None
                }
                
                # 尝试提取更多信息
                if len(match) >= 3:
                    # 可能是金额或单位
                    for item in match[1:-1]:
                        if '万元' in item or '元' in item:
                            announcement['budget'] = item.strip()
                        elif '大学' in item or '医院' in item or '局' in item or '公司' in item:
                            announcement['unit'] = item.strip()
                        elif '代理' in item:
                            announcement['agency'] = item.strip()
                
                announcements.append(announcement)
    
    return announcements


def process_directory():
    """处理整个目录"""
    all_announcements = []
    seen_titles = set()
    
    if not SOURCE_DIR.exists():
        print(f"❌ 源目录不存在: {SOURCE_DIR}")
        return None
    
    # 获取所有日期目录
    date_dirs = [d for d in SOURCE_DIR.iterdir() if d.is_dir() and re.match(r'\d{8}', d.name)]
    date_dirs.sort(key=lambda x: x.name, reverse=True)
    
    for date_dir in date_dirs:
        date_key = date_dir.name
        
        # 优先处理汇总文件
        summary_file = date_dir / "每日汇总.md"
        if summary_file.exists():
            content = summary_file.read_text(encoding='utf-8')
            announcements = parse_simple_announcement(content, date_key, str(summary_file))
            
            for ann in announcements:
                # 去重
                if ann['title'] not in seen_titles:
                    seen_titles.add(ann['title'])
                    ann['id'] = len(all_announcements) + 1
                    all_announcements.append(ann)
    
    # 按日期和相关性排序
    all_announcements.sort(key=lambda x: (x['dateKey'], x['title']), reverse=True)
    
    return all_announcements


def main():
    """主函数"""
    print("🚀 开始转换招标公告数据...")
    
    # 确保输出目录存在
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    
    # 处理数据
    announcements = process_directory()
    
    if not announcements:
        print("⚠️ 未找到任何公告数据")
        # 创建空数据结构
        announcements = []
    
    # 构建输出数据
    output_data = {
        "updateTime": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "totalCount": len(announcements),
        "announcements": announcements
    }
    
    # 写入JSON文件
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)
    
    print(f"✅ 转换完成！")
    print(f"   - 总公告数: {len(announcements)}")
    print(f"   - 输出文件: {OUTPUT_FILE}")
    
    # 打印统计
    if announcements:
        sources = {}
        keywords_count = {}
        for ann in announcements:
            sources[ann['source']] = sources.get(ann['source'], 0) + 1
            for kw in ann['keywords']:
                keywords_count[kw] = keywords_count.get(kw, 0) + 1
        
        print(f"\n📊 数据统计:")
        print(f"   来源分布: {sources}")
        print(f"   关键词分布: {keywords_count}")


if __name__ == "__main__":
    main()
