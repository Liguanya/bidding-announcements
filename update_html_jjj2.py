import json

# 读取更新后的数据
with open('data/announcements.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 生成内嵌数据
embedded_data = json.dumps(data, ensure_ascii=False)

# 读取原始index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# 查找并替换 EMBEDDED_DATA
import re

# 找到 EMBEDDED_DATA 的起始和结束位置
pattern = r'const EMBEDDED_DATA = \{[^}]*\};'
match = re.search(pattern, html_content, re.DOTALL)
if match:
    # 提取完整的 JSON 对象（包括嵌套的大括号）
    start = match.start()
    # 找到匹配的结束大括号
    brace_count = 0
    in_json = False
    end = start
    for i, c in enumerate(html_content[start:]):
        if c == '{':
            brace_count += 1
            in_json = True
        elif c == '}':
            brace_count -= 1
            if in_json and brace_count == 0:
                end = start + i + 1
                break
    
    old_data = html_content[start:end]
    new_data = f'const EMBEDDED_DATA = {embedded_data};'
    html_content = html_content.replace(old_data, new_data)
    print("EMBEDDED_DATA 已更新")
else:
    print("未找到 EMBEDDED_DATA")

# 查找并替换 ANNOUNCEMENTS_DATA
pattern2 = r'const ANNOUNCEMENTS_DATA = \{[^}]*\};'
match2 = re.search(pattern2, html_content, re.DOTALL)
if match2:
    start = match2.start()
    brace_count = 0
    in_json = False
    end = start
    for i, c in enumerate(html_content[start:]):
        if c == '{':
            brace_count += 1
            in_json = True
        elif c == '}':
            brace_count -= 1
            if in_json and brace_count == 0:
                end = start + i + 1
                break
    
    old_data = html_content[start:end]
    new_data = f'const ANNOUNCEMENTS_DATA = {embedded_data};'
    html_content = html_content.replace(old_data, new_data)
    print("ANNOUNCEMENTS_DATA 已更新")
else:
    print("未找到 ANNOUNCEMENTS_DATA")

# 保存更新后的HTML
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"\nHTML已更新，共 {data['totalCount']} 条公告")
print(f"更新时间: {data['lastUpdate']}")
