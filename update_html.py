#!/usr/bin/env python3
"""
更新index.html中的内嵌数据
"""
import json
import re

# 读取JSON数据
data_path = '/app/data/所有对话/主对话/bidding-announcements/data/announcements.json'
with open(data_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# 将数据转换为JSON字符串
json_str = json.dumps(data, ensure_ascii=False, separators=(',', ':'))

# 读取index.html
html_path = '/app/data/所有对话/主对话/bidding-announcements/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

# 替换内嵌数据
pattern = r'const EMBEDDED_DATA = \{.*?\};'
replacement = f'const EMBEDDED_DATA = {json_str};'

new_html = re.sub(pattern, replacement, html_content, flags=re.DOTALL)

# 写入新的index.html
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(new_html)

print("index.html内嵌数据已更新!")
print(f"数据更新时间: {data['lastUpdate']}")
print(f"公告总数: {data['totalCount']}")
