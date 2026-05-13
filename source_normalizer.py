#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Source字段规范化模块 - 确保所有公告的source字段严格符合白名单

使用方法:
    from source_normalizer import normalize_source, normalize_all_sources, ALLOWED_SOURCES
    
    # 规范化单个source
    clean_source = normalize_source("河北省政府采购网-张家口")  # 返回 "中国政府采购网"
    
    # 规范化所有公告数据
    normalize_all_sources(announcements_list)
"""

import json

# 来源白名单 - 严格限定为这4个
ALLOWED_SOURCES = [
    "天津市公共资源交易平台",
    "中国招标投标公共服务平台",
    "中国政府采购网",
    "天津市政府采购网"
]

def normalize_source(source):
    """
    将任意source字符串规范化为白名单中的值
    
    Args:
        source: 原始source字符串
        
    Returns:
        规范化后的source字符串（属于白名单）
    """
    if not source:
        return "中国政府采购网"  # 默认值
    
    # 如果已经在白名单中，直接返回
    if source in ALLOWED_SOURCES:
        return source
    
    source_lower = source.lower()
    
    # 匹配天津市政府采购网
    if "天津" in source and "政府采购" in source_lower:
        return "天津市政府采购网"
    
    # 匹配天津市公共资源交易平台
    if "天津" in source and ("公共资源" in source_lower or "交易" in source_lower):
        return "天津市公共资源交易平台"
    
    # 匹配中国招标投标公共服务平台
    if "招标投标" in source and "服务平台" in source:
        return "中国招标投标公共服务平台"
    
    # 默认归类为中国政府采购网
    return "中国政府采购网"

def normalize_all_sources(announcements):
    """
    规范化所有公告的source字段（原地修改）
    
    Args:
        announcements: 公告列表（每个公告是一个dict，包含source字段）
        
    Returns:
        修改的数量统计
    """
    normalized_count = 0
    invalid_sources = set()
    
    for item in announcements:
        original_source = item.get('source', '')
        new_source = normalize_source(original_source)
        
        if original_source != new_source:
            normalized_count += 1
            invalid_sources.add(original_source)
            item['source'] = new_source
    
    if normalized_count > 0:
        print(f"[source规范化] 已修改 {normalized_count} 条记录")
        print(f"[source规范化] 发现的非法source: {invalid_sources}")
    else:
        print(f"[source规范化] 所有记录均符合白名单要求")
    
    return normalized_count

def validate_sources(announcements):
    """
    验证所有公告的source字段是否都在白名单中
    
    Args:
        announcements: 公告列表
        
    Returns:
        (是否全部合法, 非法source集合)
    """
    invalid_sources = set()
    
    for item in announcements:
        source = item.get('source', '')
        if source not in ALLOWED_SOURCES:
            invalid_sources.add(source)
    
    if invalid_sources:
        print(f"[验证失败] 发现非法source: {invalid_sources}")
        return False, invalid_sources
    else:
        print(f"[验证通过] 所有source字段均符合白名单要求")
        return True, set()

if __name__ == "__main__":
    # 测试
    test_cases = [
        "河北省政府采购网-张家口",
        "中国政府采购网河北分网",
        "天津市政府采购网",
        "北京市公共资源交易服务平台",
        "采招网",
        "",
        None,
        "乙方宝官网",
    ]
    
    print("测试source规范化:")
    for test in test_cases:
        result = normalize_source(test)
        print(f"  '{test}' -> '{result}'")
    
    print(f"\n白名单: {ALLOWED_SOURCES}")
