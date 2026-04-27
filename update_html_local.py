import json
import re

# 读取JSON数据
with open('data/announcements.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 读取HTML文件
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 将数据转换为JavaScript数组格式
announcements_json = json.dumps(data["announcements"], ensure_ascii=False)

# 更新HTML中的数据
pattern = r'const ANNOUNCEMENTS = \[.*?\];'
replacement = f'const ANNOUNCEMENTS = {announcements_json};'
html = re.sub(pattern, replacement, html, flags=re.DOTALL)

# 更新统计数据
html = re.sub(r'共找到 <strong>(\d+)</strong> 条相关招标公告', f'共找到 <strong>{data["totalCount"]}</strong> 条相关招标公告', html)
html = re.sub(r'最后更新：(\d{4}-\d{2}-\d{2} \d{2}:\d{2})', f'最后更新：{data["lastUpdate"]}', html)

# 写入更新后的HTML
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("HTML文件已更新")
print(f"总公告数: {data['totalCount']}")
print(f"最后更新: {data['lastUpdate']}")
