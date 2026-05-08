import json
from datetime import datetime

# 读取数据
with open('data/announcements.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 生成HTML表格行
def generate_table_rows(announcements):
    rows = []
    for ann in announcements[:100]:  # 限制显示最新100条
        keywords_html = ''.join([f'<span class="keyword">{k}</span>' for k in ann.get('keywords', [])])
        budget = ann.get('budget', '')
        budget_html = f'<span class="budget">{budget}</span>' if budget else ''
        row = f'''                <tr>
                    <td>{ann.get('id', '')}</td>
                    <td>{ann.get('pubDate', '')}</td>
                    <td><a href="{ann.get('link', '')}" target="_blank">{ann.get('title', '')}</a></td>
                    <td>{ann.get('source', '')}</td>
                    <td>{keywords_html}</td>
                    <td>{budget_html}</td>
                    <td>{ann.get('description', '')[:80]}...</td>
                </tr>'''
        rows.append(row)
    return '\n'.join(rows)

# 生成筛选选项
def generate_filter_options(announcements):
    keywords_set = set()
    sources_set = set()
    for ann in announcements:
        keywords_set.update(ann.get('keywords', []))
        sources_set.add(ann.get('source', ''))
    return sorted(keywords_set), sorted(sources_set)

keywords, sources = generate_filter_options(data['announcements'])

# 生成JavaScript数据
js_data = f'''const announcementsData = {json.dumps(data['announcements'][:200], ensure_ascii=False, indent=4)};'''

# HTML模板
html_content = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>招标公告追踪平台</title>
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; margin: 0; padding: 20px; background: #f5f5f5; }}
        .header {{ background: linear-gradient(135deg, #1a73e8, #0d47a1); color: white; padding: 30px; border-radius: 12px; margin-bottom: 20px; }}
        .header h1 {{ margin: 0 0 10px 0; font-size: 28px; }}
        .header .stats {{ display: flex; gap: 30px; font-size: 14px; opacity: 0.9; }}
        .stats-item {{ background: rgba(255,255,255,0.2); padding: 10px 20px; border-radius: 20px; }}
        .filters {{ background: white; padding: 20px; border-radius: 12px; margin-bottom: 20px; display: flex; gap: 15px; flex-wrap: wrap; align-items: center; }}
        .filter-group {{ display: flex; align-items: center; gap: 8px; }}
        .filter-group label {{ font-weight: 500; color: #333; }}
        select, input {{ padding: 8px 12px; border: 1px solid #ddd; border-radius: 6px; font-size: 14px; }}
        input[type="text"] {{ width: 200px; }}
        .btn {{ padding: 8px 16px; background: #1a73e8; color: white; border: none; border-radius: 6px; cursor: pointer; font-size: 14px; }}
        .btn:hover {{ background: #1557b0; }}
        .table-container {{ background: white; border-radius: 12px; overflow: hidden; box-shadow: 0 2px 8px rgba(0,0,0,0.1); }}
        table {{ width: 100%; border-collapse: collapse; }}
        th {{ background: #e8f0fe; color: #1a73e8; padding: 15px 12px; text-align: left; font-weight: 600; position: sticky; top: 0; }}
        td {{ padding: 12px; border-bottom: 1px solid #eee; vertical-align: top; }}
        tr:hover {{ background: #f8f9fa; }}
        a {{ color: #1a73e8; text-decoration: none; }}
        a:hover {{ text-decoration: underline; }}
        .keyword {{ display: inline-block; background: #e8f0fe; color: #1a73e8; padding: 2px 8px; border-radius: 12px; font-size: 12px; margin: 2px; }}
        .budget {{ color: #e65100; font-weight: 500; }}
        .source {{ color: #666; font-size: 12px; }}
        .description {{ font-size: 13px; color: #555; max-width: 300px; }}
        .footer {{ text-align: center; padding: 20px; color: #666; font-size: 13px; }}
        .export-btns {{ display: flex; gap: 10px; }}
        .pagination {{ display: flex; justify-content: center; align-items: center; gap: 10px; margin-top: 20px; }}
        .pagination button {{ padding: 8px 16px; background: #1a73e8; color: white; border: none; border-radius: 6px; cursor: pointer; }}
        .pagination button:disabled {{ background: #ccc; cursor: not-allowed; }}
        .pagination span {{ color: #666; }}
        .highlight {{ background: #fff3cd; }}
    </style>
</head>
<body>
    <div class="header">
        <h1>📢 招标公告追踪平台</h1>
        <div class="stats">
            <span class="stats-item">📊 总计: {data['totalCount']} 条</span>
            <span class="stats-item">🕐 最后更新: {data['lastUpdate']}</span>
        </div>
    </div>
    
    <div class="filters">
        <div class="filter-group">
            <label>关键词:</label>
            <input type="text" id="keywordFilter" placeholder="搜索关键词...">
        </div>
        <div class="filter-group">
            <label>来源:</label>
            <select id="sourceFilter">
                <option value="">全部</option>
                {' '.join([f'<option value="{s}">{s}</option>' for s in sources[:10]])}
            </select>
        </div>
        <div class="filter-group">
            <label>日期:</label>
            <input type="date" id="dateFilter">
        </div>
        <button class="btn" onclick="applyFilters()">🔍 筛选</button>
        <button class="btn" onclick="resetFilters()">🔄 重置</button>
        <div class="export-btns">
            <button class="btn" onclick="exportCSV()">📥 导出CSV</button>
            <button class="btn" onclick="exportJSON()">📥 导出JSON</button>
        </div>
    </div>
    
    <div class="table-container">
        <table>
            <thead>
                <tr>
                    <th style="width:60px">ID</th>
                    <th style="width:100px">日期</th>
                    <th>标题</th>
                    <th style="width:100px">来源</th>
                    <th style="width:150px">关键词</th>
                    <th style="width:120px">预算</th>
                    <th>摘要</th>
                </tr>
            </thead>
            <tbody id="tableBody">
                <!-- 数据行将通过JavaScript动态生成 -->
            </tbody>
        </table>
    </div>
    
    <div class="pagination">
        <button onclick="prevPage()" id="prevBtn">上一页</button>
        <span id="pageInfo">第 1 页，共 1 页</span>
        <button onclick="nextPage()" id="nextBtn">下一页</button>
    </div>
    
    <div class="footer">
        <p>数据来源：中国政府采购网、各地公共资源交易中心、采招网等 | 仅供学习参考</p>
    </div>

    <script>
        {js_data}
        
        let filteredData = [...announcementsData];
        let currentPage = 1;
        const pageSize = 50;
        
        function renderTable() {{
            const start = (currentPage - 1) * pageSize;
            const end = start + pageSize;
            const pageData = filteredData.slice(start, end);
            
            const tbody = document.getElementById('tableBody');
            tbody.innerHTML = pageData.map(ann => {{
                const keywords = ann.keywords ? ann.keywords.map(k => `<span class="keyword">{{k}}</span>`).join('') : '';
                const budget = ann.budget ? `<span class="budget">{{ann.budget}}</span>` : '';
                return `<tr>
                    <td>{{ann.id}}</td>
                    <td>{{ann.pubDate}}</td>
                    <td><a href="{{ann.link}}" target="_blank">{{ann.title}}</a></td>
                    <td class="source">{{ann.source}}</td>
                    <td>{{keywords}}</td>
                    <td>{{budget}}</td>
                    <td class="description">{{ann.description || ''}}</td>
                </tr>`;
            }}).join('');
            
            const totalPages = Math.ceil(filteredData.length / pageSize) || 1;
            document.getElementById('pageInfo').textContent = `第 ${{currentPage}} 页，共 ${{totalPages}} 页 (共 ${{filteredData.length}} 条)`;
            document.getElementById('prevBtn').disabled = currentPage === 1;
            document.getElementById('nextBtn').disabled = currentPage >= totalPages;
        }}
        
        function applyFilters() {{
            const keyword = document.getElementById('keywordFilter').value.toLowerCase();
            const source = document.getElementById('sourceFilter').value;
            const date = document.getElementById('dateFilter').value;
            
            filteredData = announcementsData.filter(ann => {{
                const matchKeyword = !keyword || 
                    (ann.title && ann.title.toLowerCase().includes(keyword)) ||
                    (ann.description && ann.description.toLowerCase().includes(keyword)) ||
                    (ann.keywords && ann.keywords.some(k => k.toLowerCase().includes(keyword)));
                const matchSource = !source || ann.source === source;
                const matchDate = !date || ann.pubDate === date;
                return matchKeyword && matchSource && matchDate;
            }});
            
            currentPage = 1;
            renderTable();
        }}
        
        function resetFilters() {{
            document.getElementById('keywordFilter').value = '';
            document.getElementById('sourceFilter').value = '';
            document.getElementById('dateFilter').value = '';
            filteredData = [...announcementsData];
            currentPage = 1;
            renderTable();
        }}
        
        function prevPage() {{
            if (currentPage > 1) {{
                currentPage--;
                renderTable();
            }}
        }}
        
        function nextPage() {{
            const totalPages = Math.ceil(filteredData.length / pageSize) || 1;
            if (currentPage < totalPages) {{
                currentPage++;
                renderTable();
            }}
        }}
        
        function exportCSV() {{
            const headers = ['ID', '日期', '标题', '来源', '关键词', '预算', '描述', '链接'];
            const rows = filteredData.map(ann => [
                ann.id, ann.pubDate, ann.title, ann.source,
                (ann.keywords || []).join(';'), ann.budget || '', ann.description || '', ann.link
            ]);
            
            let csv = headers.join(',') + '\\n';
            rows.forEach(row => {{
                csv += row.map(cell => `\\"${{String(cell).replace(/\\"/g, '\\"\\"')}}\\"`).join(',') + '\\n';
            }});
            
            const blob = new Blob(['\\ufeff' + csv], {{ type: 'text/csv;charset=utf-8;' }});
            const link = document.createElement('a');
            link.href = URL.createObjectURL(blob);
            link.download = `招标公告_${{new Date().toISOString().slice(0,10)}}.csv`;
            link.click();
        }}
        
        function exportJSON() {{
            const blob = new Blob([JSON.stringify(filteredData, null, 2)], {{ type: 'application/json' }});
            const link = document.createElement('a');
            link.href = URL.createObjectURL(blob);
            link.download = `招标公告_${{new Date().toISOString().slice(0,10)}}.json`;
            link.click();
        }}
        
        // 初始化
        renderTable();
    </script>
</body>
</html>'''

# 保存HTML
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"HTML已更新，包含 {data['totalCount']} 条数据")
