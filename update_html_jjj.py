import json

# 读取更新后的数据
with open('data/announcements.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 生成内嵌数据脚本
embedded_data = json.dumps(data, ensure_ascii=False)

# 读取原始index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# 找到并替换 EMBEDDED_DATA 部分
import re
pattern = r'const EMBEDDED_DATA = \[.*?\];'
if re.search(pattern, html_content, re.DOTALL):
    new_content = re.sub(pattern, f'const EMBEDDED_DATA = {embedded_data};', html_content, flags=re.DOTALL)
else:
    # 如果格式不同，尝试其他模式
    pattern2 = r'var announcements = \[.*?\];'
    if re.search(pattern2, html_content, re.DOTALL):
        new_content = re.sub(pattern2, f'var announcements = {embedded_data};', html_content, flags=re.DOTALL)
    else:
        # 尝试查找 JSON 数据块
        pattern3 = r'<!-- DATA_START -->.*?<!-- DATA_END -->'
        if re.search(pattern3, html_content, re.DOTALL):
            new_content = re.sub(pattern3, f'<!-- DATA_START -->\nconst DATA = {embedded_data};\n<!-- DATA_END -->', html_content, flags=re.DOTALL)
        else:
            print("未找到可替换的数据区域，请检查HTML结构")
            exit(1)

# 保存更新后的HTML
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"HTML已更新，共 {data['totalCount']} 条公告")
print(f"更新时间: {data['lastUpdate']}")
