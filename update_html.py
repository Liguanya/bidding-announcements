import json
import re

# 读取最新的JSON数据
with open('data/announcements.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 读取index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# 找到并替换EMBEDDED_DATA
json_str = json.dumps(data, ensure_ascii=False)
new_embedded = f'const EMBEDDED_DATA = {json_str};'

# 使用正则表达式替换
pattern = r'const EMBEDDED_DATA = \{[^;]+\};'
html_content = re.sub(pattern, new_embedded, html_content, flags=re.DOTALL)

# 保存更新后的html
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("HTML更新成功！")
print(f"总公告数: {data['totalCount']}")
print(f"最后更新: {data['lastUpdate']}")
