import json
import re

# 读取数据
with open('data/announcements.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 读取index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# 生成新的内嵌数据脚本
announcements_json = json.dumps(data, ensure_ascii=False, indent=2)

# 替换内嵌数据
pattern = r'<script>\s*const ANNOUNCEMENTS_DATA\s*=\s*\{[^}]*"announcements":\s*\[[\s\S]*?\]\s*[^}]*\}\s*</script>'
replacement = f'<script>\\nconst ANNOUNCEMENTS_DATA = {announcements_json};\\n</script>'

# 检查是否有内嵌数据
if 'const ANNOUNCEMENTS_DATA' in html_content:
    # 使用正则替换
    html_content = re.sub(
        r'<script>\s*const ANNOUNCEMENTS_DATA\s*=\s*\{[\s\S]*?\}?\s*</script>',
        replacement,
        html_content
    )
else:
    # 如果没有内嵌数据，插入到</body>前
    html_content = html_content.replace('</body>', f'{replacement}\\n</body>')

# 保存
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Updated index.html with new data")
print(f"Announcements in data file: {len(data['announcements'])}")
