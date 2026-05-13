#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
修复关键词筛选功能：
1. 增加新的关键词选项：可行性研究、项目建议、实施方案、设计
2. 确保筛选逻辑正确
"""

import re

def fix_generate_html():
    """修复generate_html.py中的关键词选项"""
    with open('generate_html.py', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 找到关键词筛选部分并增加新选项
    old_keywords = '''                    <select id="filterKeyword">
                        <option value="">全部关键词</option>
                        <option value="造价">造价</option>
                        <option value="全过程咨询">全过程咨询</option>
                        <option value="招标代理">招标代理</option>
                        <option value="项目管理">项目管理</option>
                        <option value="监理">监理</option>
                    </select>'''
    
    new_keywords = '''                    <select id="filterKeyword">
                        <option value="">全部关键词</option>
                        <option value="造价">造价</option>
                        <option value="全过程咨询">全过程咨询</option>
                        <option value="招标代理">招标代理</option>
                        <option value="项目管理">项目管理</option>
                        <option value="监理">监理</option>
                        <option value="可行性研究">可行性研究</option>
                        <option value="项目建议">项目建议</option>
                        <option value="实施方案">实施方案</option>
                        <option value="设计">设计</option>
                    </select>'''
    
    if old_keywords in content:
        content = content.replace(old_keywords, new_keywords)
        print("✓ 已更新generate_html.py中的关键词选项")
    else:
        print("⚠ 未在generate_html.py找到匹配的关键词部分，尝试其他方式...")
        # 尝试只在监理后面插入新选项
        pattern = r'(<option value="监理">监理</option>)'
        replacement = r'\1\n                        <option value="可行性研究">可行性研究</option>\n                        <option value="项目建议">项目建议</option>\n                        <option value="实施方案">实施方案</option>\n                        <option value="设计">设计</option>'
        content = re.sub(pattern, replacement, content)
        print("✓ 已通过正则方式更新generate_html.py中的关键词选项")
    
    with open('generate_html.py', 'w', encoding='utf-8') as f:
        f.write(content)

def fix_index_html():
    """修复index.html中的关键词选项和筛选逻辑"""
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. 增加新的关键词选项
    old_keywords = '''                    <select id="filterKeyword">
                        <option value="">全部关键词</option>
                        <option value="造价">造价</option>
                        <option value="全过程咨询">全过程咨询</option>
                        <option value="招标代理">招标代理</option>
                        <option value="项目管理">项目管理</option>
                        <option value="监理">监理</option>
                    </select>'''
    
    new_keywords = '''                    <select id="filterKeyword">
                        <option value="">全部关键词</option>
                        <option value="造价">造价</option>
                        <option value="全过程咨询">全过程咨询</option>
                        <option value="招标代理">招标代理</option>
                        <option value="项目管理">项目管理</option>
                        <option value="监理">监理</option>
                        <option value="可行性研究">可行性研究</option>
                        <option value="项目建议">项目建议</option>
                        <option value="实施方案">实施方案</option>
                        <option value="设计">设计</option>
                    </select>'''
    
    if old_keywords in content:
        content = content.replace(old_keywords, new_keywords)
        print("✓ 已更新index.html中的关键词选项")
    else:
        print("⚠ 未在index.html找到完全匹配的关键词部分，尝试正则方式...")
        pattern = r'(<option value="监理">监理</option>)'
        replacement = r'\1\n                        <option value="可行性研究">可行性研究</option>\n                        <option value="项目建议">项目建议</option>\n                        <option value="实施方案">实施方案</option>\n                        <option value="设计">设计</option>'
        content = re.sub(pattern, replacement, content)
        print("✓ 已通过正则方式更新index.html中的关键词选项")
    
    # 2. 改进关键词筛选逻辑：同时匹配标题和描述中的关键词
    # 当前逻辑：if (keyword && !item.keywords.some(k => k.includes(keyword) || keyword.includes(k))) return false;
    # 改进为同时检查标题、描述和keywords数组
    old_filter_logic = '''            // 关键词筛选
                if (keyword && !item.keywords.some(k => k.includes(keyword) || keyword.includes(k))) return false;'''
    
    new_filter_logic = '''            // 关键词筛选：同时检查keywords数组、标题和描述
                if (keyword) {
                    const keywordMatch = item.keywords && item.keywords.some(k => k.includes(keyword) || keyword.includes(k));
                    const titleMatch = item.title && item.title.includes(keyword);
                    const descMatch = item.description && item.description.includes(keyword);
                    if (!keywordMatch && !titleMatch && !descMatch) return false;
                }'''
    
    if old_filter_logic in content:
        content = content.replace(old_filter_logic, new_filter_logic)
        print("✓ 已改进关键词筛选逻辑（同时匹配标题和描述）")
    else:
        print("⚠ 未找到完全匹配的筛选逻辑，尝试正则方式...")
        pattern = r'// 关键词筛选\s+if \(keyword && !item\.keywords\.some\(k => k\.includes\(keyword\) \|\| keyword\.includes\(k\)\)\) return false;'
        replacement = '''// 关键词筛选：同时检查keywords数组、标题和描述
                if (keyword) {
                    const keywordMatch = item.keywords && item.keywords.some(k => k.includes(keyword) || keyword.includes(k));
                    const titleMatch = item.title && item.title.includes(keyword);
                    const descMatch = item.description && item.description.includes(keyword);
                    if (!keywordMatch && !titleMatch && !descMatch) return false;
                }'''
        content = re.sub(pattern, replacement, content)
        print("✓ 已通过正则方式改进关键词筛选逻辑")
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("\n关键词列表更新完成：")
    print("  - 造价")
    print("  - 全过程咨询")
    print("  - 招标代理")
    print("  - 项目管理")
    print("  - 监理")
    print("  - 可行性研究 (新增)")
    print("  - 项目建议 (新增)")
    print("  - 实施方案 (新增)")
    print("  - 设计 (新增)")
    print("\n筛选逻辑改进：关键词筛选同时匹配")
    print("  1. 公告的keywords数组")
    print("  2. 公告标题")
    print("  3. 公告描述")

if __name__ == '__main__':
    print("开始修复关键词筛选功能...\n")
    fix_generate_html()
    print("\n" + "="*50 + "\n")
    fix_index_html()
    print("\n" + "="*50)
    print("修复完成！请提交更改到GitHub。")
