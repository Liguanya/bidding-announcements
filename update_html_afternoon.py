import json
import re

# 读取JSON数据
with open('data/announcements.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 读取index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# 提取最新20条公告用于显示
latest_announcements = data['announcements'][:20]

# 生成新的HTML数据行
html_rows = ""
for ann in latest_announcements:
    keywords_str = ', '.join(f'"{k}"' for k in ann.get('keywords', []))
    budget = ann.get('budget', '未知')
    description = ann.get('description', '')
    html_rows += f'''            <tr>
                <td>{ann['id']}</td>
                <td><a href="{ann['link']}" target="_blank">{ann['title']}</a></td>
                <td>{ann['pubDate']}</td>
                <td>{ann['source']}</td>
                <td>{ann['keywords']}</td>
                <td>{budget}</td>
                <td>{description[:80]}...</td>
            </tr>
'''

# 替换数据行
pattern = r'(<tbody id="announcementsBody">)[\s\S]*?(</tbody>)'
new_html = re.sub(pattern, rf'\1\n{html_rows}\2', html_content)

# 更新统计信息
new_html = re.sub(r'更新日期：\d{4}-\d{2}-\d{2} \d{2}:\d{2}', '更新日期：2026-05-05 13:57', new_html)
new_html = re.sub(r'公告总数：\d+', f'公告总数：{data["totalCount"]}', new_html)

# 保存
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("index.html更新完成!")
print(f"显示公告数量: {len(latest_announcements)}")
print(f"总公告数: {data['totalCount']}")
