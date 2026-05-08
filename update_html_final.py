import json

# 读取更新后的数据
with open('data/announcements.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 生成内嵌数据
embedded_data = json.dumps(data, ensure_ascii=False)

# 读取原始index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# 查找 EMBEDDED_DATA 的位置
search_str = 'const EMBEDDED_DATA = {'
start_idx = html_content.find(search_str)
if start_idx == -1:
    print("未找到 EMBEDDED_DATA")
    exit(1)

# 找到结束位置 (需要匹配大括号)
brace_start = html_content.find('{', start_idx)
brace_count = 1
end_idx = brace_start + 1
for i in range(brace_start + 1, len(html_content)):
    if html_content[i] == '{':
        brace_count += 1
    elif html_content[i] == '}':
        brace_count -= 1
        if brace_count == 0:
            end_idx = i + 1
            break

# 替换数据
old_data = html_content[start_idx:end_idx]
new_data = f'const EMBEDDED_DATA = {embedded_data}'
html_content = html_content.replace(old_data, new_data)

# 保存更新后的HTML
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"HTML已更新，共 {data['totalCount']} 条公告")
print(f"更新时间: {data['lastUpdate']}")
