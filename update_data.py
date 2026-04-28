import json
import re

# 读取现有数据
with open('data/announcements.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 当前最大ID
max_id = max(item['id'] for item in data['announcements'])
print(f"当前最大ID: {max_id}, 当前总数: {data['totalCount']}")

# 新增公告数据（从搜索结果提取）
new_announcements = [
    {
        "id": max_id + 1,
        "title": "湖南省交通运输厅2026年造价审查及咨询服务专项重新立项招标公告",
        "pubDate": "2026-04-22",
        "source": "湖南省公共资源交易服务平台",
        "link": "https://www.chinamae.com/purchases/2c7d4df03bec8089c6f579928d1bbe4e.html",
        "keywords": ["造价咨询"],
        "collectedAt": "2026-04-28",
        "slot": "上午",
        "budget": "45万元",
        "description": "地区：湖南长沙；采购单位：湖南省交通运输厅交通建设造价管理站；采购方式：公开招标；最高限价45万元；服务期1年；标的：信息化及公路工程项目造价审查及咨询服务；投标截止：2026-05-15 10:00"
    },
    {
        "id": max_id + 2,
        "title": "如皋市交通运输局2026-2027年度造价咨询服务（预算编制、结算审计）竞争性磋商公告",
        "pubDate": "2026-04-02",
        "source": "江苏省政府采购网",
        "link": "http://jsggzy.jszwfw.gov.cn/jyxx/003004/003004002/20260402/b0bc7c1fd5f34477b849d39e289345be.html",
        "keywords": ["造价咨询"],
        "collectedAt": "2026-04-28",
        "slot": "上午",
        "budget": "320万元",
        "description": "地区：江苏如皋；采购单位：如皋市交通运输局；采购方式：竞争性磋商；预算金额320万元（分4个采购包，每包80万元）；采购包1-2为预算编制，采购包3-4为结算审计；服务期限：自合同签订之日起两年"
    },
    {
        "id": max_id + 3,
        "title": "北京市通州区台湖镇选聘2026年度造价咨询公司公开招标公告",
        "pubDate": "2026-03-24",
        "source": "中国政府采购网",
        "link": "http://www.ccgp.gov.cn/cggg/dfgg/gkzb/202603/t20260324_26307237.htm",
        "keywords": ["造价咨询"],
        "collectedAt": "2026-04-28",
        "slot": "上午",
        "budget": "419万元",
        "description": "地区：北京通州；采购单位：北京市通州区台湖镇人民政府；预算金额419万元（分5个包，每包83.8万元）；采购内容：房屋建筑类、市政工程类、拆改移工程类、环境整治类、园林绿化类造价咨询；服务期：签订合同之日起一年；投标截止：2026-04-15 09:00"
    },
    {
        "id": max_id + 4,
        "title": "连州市财政性资金投资建设工程造价咨询服务采购项目招标公告",
        "pubDate": "2026-03-16",
        "source": "广东省政府采购网",
        "link": "http://www.ccgp.gov.cn/cggg/dfgg/gkzb/202603/t20260316_26275733.htm",
        "keywords": ["造价咨询"],
        "collectedAt": "2026-04-28",
        "slot": "上午",
        "budget": "1000万元",
        "description": "地区：广东连州；采购单位：连州市财政局投资审核中心；预算金额1000万元（分3个采购包，每包400/300/300万元）；服务期：两年；采购内容：财政性资金投资建设工程造价咨询服务；投标截止：2026-04-08 09:00"
    },
    {
        "id": max_id + 5,
        "title": "成都市锦江区发展和改革局2026-2029政府投资项目工程咨询及造价咨询服务采购项目招标公告",
        "pubDate": "2026-03-26",
        "source": "中国政府采购网",
        "link": "http://www.ccgp.gov.cn/cggg/dfgg/gkzb/202603/t20260326_26318667.htm",
        "keywords": ["造价咨询", "全过程咨询", "项目管理"],
        "collectedAt": "2026-04-28",
        "slot": "上午",
        "budget": "400万元",
        "description": "地区：四川成都；采购单位：成都市锦江区发展和改革局；预算金额400万元（分两包：工程咨询160万/年+工程造价240万/年）；服务期：3年，合同一年一签；允许联合体投标；需在全国投资项目在线审批监管平台备案；投标截止：2026-04-20 09:30"
    },
    {
        "id": max_id + 6,
        "title": "襄阳市全过程工程咨询服务项目竞争性磋商公告",
        "pubDate": "2026-03-09",
        "source": "湖北省政府采购网",
        "link": "https://m.sohu.com/a/994187449_122434053/",
        "keywords": ["全过程咨询", "项目管理"],
        "collectedAt": "2026-04-28",
        "slot": "上午",
        "budget": "10.37万元",
        "description": "地区：湖北襄阳；采购单位：襄阳市某单位；采购方式：竞争性磋商；预算金额10.37万元；专门面向中小微企业；需具备工程监理综合资质或房屋建筑工程乙级及以上资质；项目总负责人须具有一级造价工程师证书"
    },
    {
        "id": max_id + 7,
        "title": "浙江省水利水电技术咨询中心全过程工程咨询项目协作技术服务公开招标公告",
        "pubDate": "2026-02-12",
        "source": "中国政府采购网",
        "link": "http://www.ccgp.gov.cn/cggg/dfgg/gkzb/202602/t20260212_26176805.htm",
        "keywords": ["全过程咨询", "项目管理"],
        "collectedAt": "2026-04-28",
        "slot": "上午",
        "budget": "1900万元",
        "description": "地区：浙江杭州；采购单位：浙江省水利水电技术咨询中心；预算金额1900万元；最高限价1883.4万元；采购方式：公开招标；服务内容：全过程工程咨询项目协作技术服务；接受联合体投标；投标截止：2026-03-04 09:30"
    }
]

# 检查是否已存在相同标题的公告
existing_titles = {item['title'] for item in data['announcements']}
added_count = 0
for new_item in new_announcements:
    if new_item['title'] not in existing_titles:
        data['announcements'].insert(0, new_item)
        added_count += 1
        print(f"新增: {new_item['title'][:40]}...")

# 更新元数据
data['lastUpdate'] = "2026-04-28 09:00"
data['totalCount'] = len(data['announcements'])

print(f"\n本次新增: {added_count}条")
print(f"更新后总数: {data['totalCount']}")

# 保存JSON
with open('data/announcements.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# 生成内嵌数据脚本
embedded_data = json.dumps(data, ensure_ascii=False)
html_content = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>📢 招标公告推送平台</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); min-height: 100vh; padding: 20px; }}
        .container {{ max-width: 1400px; margin: 0 auto; }}
        .header {{ background: white; border-radius: 16px; padding: 30px; margin-bottom: 24px; box-shadow: 0 10px 40px rgba(0,0,0,0.1); }}
        .header h1 {{ color: #333; font-size: 28px; margin-bottom: 8px; }}
        .header-subtitle {{ color: #666; font-size: 14px; margin-bottom: 16px; }}
        .stats {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; margin-top: 20px; }}
        .stat-card {{ background: linear-gradient(135deg, #667eea, #764ba2); color: white; padding: 20px; border-radius: 12px; text-align: center; }}
        .stat-card.green {{ background: linear-gradient(135deg, #43a047, #2e7d32); }}
        .stat-card.orange {{ background: linear-gradient(135deg, #ff9800, #f57c00); }}
        .stat-value {{ font-size: 2rem; font-weight: bold; }}
        .filters {{ background: white; border-radius: 16px; padding: 24px; margin-bottom: 24px; box-shadow: 0 4px 20px rgba(0,0,0,0.08); }}
        .filter-row {{ display: flex; gap: 16px; flex-wrap: wrap; align-items: center; }}
        .filter-group {{ display: flex; align-items: center; gap: 8px; }}
        .filter-group label {{ color: #666; font-size: 14px; }}
        .filter-group select {{ padding: 10px 16px; border: 2px solid #e0e0e0; border-radius: 8px; font-size: 14px; min-width: 140px; }}
        .search-box {{ flex: 1; min-width: 200px; }}
        .search-box input {{ width: 100%; padding: 10px 16px; border: 2px solid #e0e0e0; border-radius: 8px; font-size: 14px; }}
        .announcement-list {{ background: white; border-radius: 16px; padding: 24px; box-shadow: 0 4px 20px rgba(0,0,0,0.08); }}
        .announcement-item {{ border: 1px solid #e8e8e8; border-radius: 12px; padding: 20px; margin-bottom: 16px; cursor: pointer; transition: all 0.3s; }}
        .announcement-item:hover {{ border-color: #667eea; box-shadow: 0 4px 20px rgba(102,126,234,0.15); transform: translateX(4px); }}
        .item-title {{ color: #333; font-size: 16px; font-weight: 600; margin-bottom: 8px; }}
        .item-meta {{ display: flex; gap: 12px; flex-wrap: wrap; margin-bottom: 8px; }}
        .meta-tag {{ padding: 4px 12px; border-radius: 20px; font-size: 12px; background: #f0f0f0; color: #666; }}
        .meta-tag.source {{ background: #e3f2fd; color: #1565c0; }}
        .meta-tag.keyword {{ background: #fff3e0; color: #e65100; }}
        .item-date {{ color: #999; font-size: 13px; }}
        .pagination {{ display: flex; justify-content: center; gap: 8px; margin-top: 24px; }}
        .pagination button {{ padding: 8px 16px; border: 1px solid #e0e0e0; background: white; border-radius: 8px; cursor: pointer; }}
        .pagination button.active {{ background: #667eea; color: white; border-color: #667eea; }}
        .modal-overlay {{ position: fixed; top: 0; left: 0; right: 0; bottom: 0; background: rgba(0,0,0,0.5); display: none; justify-content: center; align-items: center; z-index: 1000; }}
        .modal-overlay.active {{ display: flex; }}
        .modal {{ background: white; border-radius: 16px; padding: 30px; max-width: 600px; width: 90%; max-height: 80vh; overflow-y: auto; }}
        .modal-header {{ display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 20px; }}
        .modal-title {{ font-size: 18px; color: #333; flex: 1; }}
        .modal-close {{ background: none; border: none; font-size: 24px; cursor: pointer; color: #999; }}
        .detail-section {{ margin-bottom: 16px; }}
        .detail-section h4 {{ color: #666; font-size: 14px; margin-bottom: 8px; }}
        .detail-content {{ color: #333; font-size: 14px; }}
        .detail-link {{ color: #1e88e5; text-decoration: none; word-break: break-all; }}
        .toast {{ position: fixed; bottom: 20px; left: 50%; transform: translateX(-50%); background: #333; color: white; padding: 12px 24px; border-radius: 8px; display: none; z-index: 2000; }}
        .toast.show {{ display: block; }}
        @media (max-width: 768px) {{ .stats {{ grid-template-columns: repeat(2, 1fr); }} .filter-row {{ flex-direction: column; }} }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>📢 招标公告推送平台</h1>
            <p class="header-subtitle">实时推送政府采购招标公告，助您把握商机 | 最后更新: {data['lastUpdate']}</p>
            <div class="stats">
                <div class="stat-card"><div class="stat-label">总公告数</div><div class="stat-value" id="totalCount">-</div></div>
                <div class="stat-card green"><div class="stat-label">今日新增</div><div class="stat-value" id="todayCount">-</div></div>
                <div class="stat-card orange"><div class="stat-label">天津地区</div><div class="stat-value" id="tjCount">-</div></div>
                <div class="stat-card"><div class="stat-label">全国公告</div><div class="stat-value" id="nationCount">-</div></div>
            </div>
        </div>
        <div class="filters">
            <div class="filter-row">
                <div class="filter-group"><label>日期</label><select id="filterDate"><option value="">全部日期</option></select></div>
                <div class="filter-group"><label>关键词</label><select id="filterKeyword"><option value="">全部关键词</option><option value="造价">造价</option><option value="全过程咨询">全过程咨询</option><option value="招标代理">招标代理</option><option value="项目管理">项目管理</option></select></div>
                <div class="filter-group"><label>来源</label><select id="filterSource"><option value="">全部来源</option><option value="中国政府采购网">中国政府采购网</option><option value="天津">天津</option></select></div>
                <div class="search-box"><input type="text" id="searchInput" placeholder="🔍 搜索公告标题..."></div>
                <button onclick="resetFilters()" style="padding:10px 20px;border:1px solid #e0e0e0;border-radius:8px;background:white;cursor:pointer;">🔄 重置</button>
            </div>
        </div>
        <div class="announcement-list">
            <h3 style="margin-bottom:20px;">📋 公告列表 <span id="resultCount"></span></h3>
            <div id="announcementList"></div>
            <div class="pagination" id="pagination"></div>
        </div>
    </div>
    <div class="modal-overlay" id="modalOverlay" onclick="closeModal()">
        <div class="modal" onclick="event.stopPropagation()">
            <div class="modal-header"><h2 class="modal-title" id="modalTitle"></h2><button class="modal-close" onclick="closeModal()">×</button></div>
            <div class="modal-body" id="modalBody"></div>
        </div>
    </div>
    <div class="toast" id="toast"></div>
    <script>
        const EMBEDDED_DATA = {embedded_data};
        let allAnnouncements = [], filteredAnnouncements = [], currentPage = 1, pageSize = 15;
        const FAVORITES_KEY = 'bidding_favorites';
        function getFavorites() {{ return JSON.parse(localStorage.getItem(FAVORITES_KEY) || '[]'); }}
        document.addEventListener('DOMContentLoaded', function() {{ loadData(); setupFilters(); document.getElementById('searchInput').addEventListener('input', handleSearch); }});
        function loadData() {{
            try {{
                const data = EMBEDDED_DATA;
                allAnnouncements = (data.announcements || []).map(item => ({{...item, dateKey: item.dateKey || (item.pubDate ? item.pubDate.replace(/-/g, '') : '')}}));
                filteredAnnouncements = [...allAnnouncements];
                updateStats(); initFilterOptions(); renderAnnouncements();
            }} catch (error) {{ console.error('加载数据失败:', error); document.getElementById('announcementList').innerHTML = '<p style="text-align:center;color:#999;">数据加载失败</p>'; }}
        }}
        function updateStats() {{
            document.getElementById('totalCount').textContent = allAnnouncements.length;
            const today = new Date().toISOString().split('T')[0].replace(/-/g, '');
            document.getElementById('todayCount').textContent = allAnnouncements.filter(a => a.dateKey === today || a.collectedAt === today || (a.collectedAt && a.collectedAt.replace(/-/g, '') === today)).length;
            document.getElementById('tjCount').textContent = allAnnouncements.filter(a => (a.description && a.description.includes('天津')) || (a.title && a.title.includes('天津'))).length;
            document.getElementById('nationCount').textContent = allAnnouncements.length;
        }}
        function initFilterOptions() {{
            const dates = [...new Set(allAnnouncements.map(a => a.pubDate).filter(Boolean))].sort().reverse();
            const dateSelect = document.getElementById('filterDate');
            dates.forEach(d => {{ const opt = document.createElement('option'); opt.value = d; opt.textContent = d; dateSelect.appendChild(opt); }});
            document.getElementById('filterDate').addEventListener('change', applyFilters);
            document.getElementById('filterKeyword').addEventListener('change', applyFilters);
            document.getElementById('filterSource').addEventListener('change', applyFilters);
        }}
        function applyFilters() {{
            const date = document.getElementById('filterDate').value;
            const keyword = document.getElementById('filterKeyword').value;
            const source = document.getElementById('filterSource').value;
            const search = document.getElementById('searchInput').value.toLowerCase();
            filteredAnnouncements = allAnnouncements.filter(a => {{
                if (date && a.pubDate !== date) return false;
                if (keyword && !(a.keywords && a.keywords.some(k => k.includes(keyword)))) return false;
                if (source === '天津' && !(a.description && a.description.includes('天津'))) return false;
                if (source && source !== '天津' && a.source !== source) return false;
                if (search && !(a.title && a.title.toLowerCase().includes(search))) return false;
                return true;
            }});
            currentPage = 1; renderAnnouncements();
        }}
        function handleSearch() {{ applyFilters(); }}
        function resetFilters() {{ document.getElementById('filterDate').value = ''; document.getElementById('filterKeyword').value = ''; document.getElementById('filterSource').value = ''; document.getElementById('searchInput').value = ''; applyFilters(); }}
        function renderAnnouncements() {{
            const start = (currentPage - 1) * pageSize, end = start + pageSize;
            const items = filteredAnnouncements.slice(start, end);
            const container = document.getElementById('announcementList');
            if (items.length === 0) {{ container.innerHTML = '<p style="text-align:center;color:#999;padding:40px;">暂无公告</p>'; document.getElementById('pagination').innerHTML = ''; document.getElementById('resultCount').textContent = ''; return; }}
            container.innerHTML = items.map(item => `
                <div class="announcement-item" onclick='showDetail({JSON.stringify(item)})'>
                    <div class="item-title">{{{{item.title}}}}</div>
                    <div class="item-meta">
                        <span class="meta-tag source">{{{{item.source || ''}}}}</span>
                        {{{{item.budget ? '<span class="meta-tag" style="background:#e8f5e9;color:#2e7d32;">💰 ' + item.budget + '</span>' : ''}}}}
                        {{item.keywords && item.keywords.map(k => '<span class="meta-tag keyword">' + k + '</span>').join('')}}
                    </div>
                    <div class="item-date">📅 {{item.pubDate || ''}} | 🕐 {{item.collectedAt || ''}} {{item.slot || ''}}</div>
                </div>
            `).join('');
            document.getElementById('resultCount').textContent = `(共${filteredAnnouncements.length}条)`;
            renderPagination();
        }}
        function renderPagination() {{
            const totalPages = Math.ceil(filteredAnnouncements.length / pageSize);
            const pagination = document.getElementById('pagination');
            if (totalPages <= 1) {{ pagination.innerHTML = ''; return; }}
            let html = `<button onclick="changePage(1)" ${currentPage === 1 ? 'disabled' : ''}>«</button>`;
            for (let i = Math.max(1, currentPage - 2); i <= Math.min(totalPages, currentPage + 2); i++) {{ html += `<button onclick="changePage(${i})" class="${i === currentPage ? 'active' : ''}">${i}</button>`; }}
            html += `<button onclick="changePage(${totalPages})" ${currentPage === totalPages ? 'disabled' : ''}>»</button>`;
            pagination.innerHTML = html;
        }}
        function changePage(page) {{ currentPage = page; renderAnnouncements(); window.scrollTo({top: 0, behavior: 'smooth'}); }}
        function showDetail(item) {{
            document.getElementById('modalTitle').textContent = item.title;
            document.getElementById('modalBody').innerHTML = `
                <div class="detail-section"><h4>📰 来源</h4><div class="detail-content">{{item.source || '未知'}}</div></div>
                <div class="detail-section"><h4>📅 发布日期</h4><div class="detail-content">{{item.pubDate || ''}}</div></div>
                {{item.budget ? '<div class="detail-section"><h4>💰 预算金额</h4><div class="detail-content">' + item.budget + '</div></div>' : ''}}
                <div class="detail-section"><h4>🏷️ 关键词</h4><div class="detail-content">{{(item.keywords || []).join(' | ')}}</div></div>
                <div class="detail-section"><h4>📋 详情描述</h4><div class="detail-content">{{item.description || '暂无描述'}}</div></div>
                <div class="detail-section"><h4>🔗 原文链接</h4><div class="detail-content"><a class="detail-link" href="{{item.link}}" target="_blank">{{item.link || '无'}}</a></div></div>
            `;
            document.getElementById('modalOverlay').classList.add('active');
        }}
        function closeModal() {{ document.getElementById('modalOverlay').classList.remove('active'); }}
        document.addEventListener('keydown', e => {{ if (e.key === 'Escape') closeModal(); }});
    </script>
</body>
</html>'''

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"\n✅ 已更新 index.html")
print(f"✅ 数据更新完成！")
