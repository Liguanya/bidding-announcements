#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成完整的招标公告HTML页面"""

import json
from datetime import datetime

# 读取数据
with open('data/announcements.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

announcements = data.get('announcements', [])
last_update = data.get('lastUpdate', datetime.now().strftime('%Y-%m-%d %H:%M'))

# 生成HTML内容
html_content = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>📢 京津冀招标公告追踪平台</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { 
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Microsoft YaHei", sans-serif; 
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
            min-height: 100vh; 
            padding: 20px; 
        }
        .container { max-width: 1400px; margin: 0 auto; }
        
        /* 头部样式 */
        .header { 
            background: white; 
            border-radius: 16px; 
            padding: 30px; 
            margin-bottom: 24px; 
            box-shadow: 0 10px 40px rgba(0,0,0,0.1); 
        }
        .header h1 { color: #333; font-size: 28px; margin-bottom: 8px; }
        .header-subtitle { color: #666; font-size: 14px; margin-bottom: 16px; }
        
        /* 统计卡片 */
        .stats { display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; margin-top: 20px; }
        .stat-card { 
            background: linear-gradient(135deg, #667eea, #764ba2); 
            color: white; 
            padding: 20px; 
            border-radius: 12px; 
            text-align: center; 
        }
        .stat-card.green { background: linear-gradient(135deg, #43a047, #2e7d32); }
        .stat-card.orange { background: linear-gradient(135deg, #ff9800, #f57c00); }
        .stat-card.red { background: linear-gradient(135deg, #e53935, #c62828); }
        .stat-label { font-size: 14px; margin-bottom: 8px; opacity: 0.9; }
        .stat-value { font-size: 2rem; font-weight: bold; }
        
        /* 筛选区域 */
        .filters { 
            background: white; 
            border-radius: 16px; 
            padding: 24px; 
            margin-bottom: 24px; 
            box-shadow: 0 4px 20px rgba(0,0,0,0.08); 
        }
        .filter-row { display: flex; gap: 16px; flex-wrap: wrap; align-items: center; }
        .filter-group { display: flex; align-items: center; gap: 8px; }
        .filter-group label { color: #666; font-size: 14px; font-weight: 500; }
        .filter-group select { 
            padding: 10px 16px; 
            border: 2px solid #e0e0e0; 
            border-radius: 8px; 
            font-size: 14px; 
            min-width: 140px; 
            cursor: pointer;
            transition: border-color 0.3s;
        }
        .filter-group select:focus { outline: none; border-color: #667eea; }
        .search-box { flex: 1; min-width: 200px; }
        .search-box input { 
            width: 100%; 
            padding: 10px 16px; 
            border: 2px solid #e0e0e0; 
            border-radius: 8px; 
            font-size: 14px; 
        }
        .search-box input:focus { outline: none; border-color: #667eea; }
        .btn { 
            padding: 10px 20px; 
            border: 1px solid #e0e0e0; 
            border-radius: 8px; 
            background: white; 
            cursor: pointer; 
            font-size: 14px;
            transition: all 0.3s;
        }
        .btn:hover { background: #f5f5f5; }
        .btn-primary { background: #667eea; color: white; border-color: #667eea; }
        .btn-primary:hover { background: #5a6fd6; }
        
        /* 公告列表 */
        .announcement-list { 
            background: white; 
            border-radius: 16px; 
            padding: 24px; 
            box-shadow: 0 4px 20px rgba(0,0,0,0.08); 
        }
        .list-header { 
            display: flex; 
            justify-content: space-between; 
            align-items: center; 
            margin-bottom: 20px; 
        }
        .list-title { font-size: 18px; color: #333; font-weight: 600; }
        .result-count { color: #666; font-size: 14px; }
        
        /* 公告项 */
        .announcement-item { 
            border: 1px solid #e8e8e8; 
            border-radius: 12px; 
            padding: 20px; 
            margin-bottom: 16px; 
            cursor: pointer; 
            transition: all 0.3s; 
        }
        .announcement-item:hover { 
            border-color: #667eea; 
            box-shadow: 0 4px 20px rgba(102,126,234,0.15); 
            transform: translateX(4px); 
        }
        .item-header { display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 12px; }
        .item-title { color: #333; font-size: 16px; font-weight: 600; flex: 1; margin-right: 16px; }
        .item-date { color: #999; font-size: 13px; white-space: nowrap; }
        .item-meta { display: flex; gap: 12px; flex-wrap: wrap; margin-bottom: 8px; }
        .meta-tag { padding: 4px 12px; border-radius: 20px; font-size: 12px; background: #f0f0f0; color: #666; }
        .meta-tag.source { background: #e3f2fd; color: #1565c0; }
        .meta-tag.keyword { background: #fff3e0; color: #e65100; }
        .meta-tag.region { background: #e8f5e9; color: #2e7d32; }
        .item-description { color: #666; font-size: 14px; line-height: 1.6; margin-top: 8px; }
        .item-link { color: #1e88e5; text-decoration: none; font-size: 14px; }
        .item-link:hover { text-decoration: underline; }
        
        /* 分页 */
        .pagination { display: flex; justify-content: center; gap: 8px; margin-top: 24px; }
        .pagination button { 
            padding: 8px 16px; 
            border: 1px solid #e0e0e0; 
            background: white; 
            border-radius: 8px; 
            cursor: pointer; 
            transition: all 0.3s;
        }
        .pagination button:hover { background: #f5f5f5; }
        .pagination button.active { background: #667eea; color: white; border-color: #667eea; }
        .pagination button:disabled { opacity: 0.5; cursor: not-allowed; }
        
        /* 模态框 */
        .modal-overlay { 
            position: fixed; 
            top: 0; left: 0; right: 0; bottom: 0; 
            background: rgba(0,0,0,0.5); 
            display: none; 
            justify-content: center; 
            align-items: center; 
            z-index: 1000; 
        }
        .modal-overlay.active { display: flex; }
        .modal { 
            background: white; 
            border-radius: 16px; 
            padding: 30px; 
            max-width: 700px; 
            width: 90%; 
            max-height: 85vh; 
            overflow-y: auto; 
        }
        .modal-header { display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 20px; }
        .modal-title { font-size: 18px; color: #333; flex: 1; padding-right: 16px; }
        .modal-close { background: none; border: none; font-size: 28px; cursor: pointer; color: #999; line-height: 1; }
        .modal-close:hover { color: #333; }
        .detail-section { margin-bottom: 16px; }
        .detail-section h4 { color: #666; font-size: 14px; margin-bottom: 8px; font-weight: 500; }
        .detail-content { color: #333; font-size: 14px; line-height: 1.6; }
        .detail-link { color: #1e88e5; text-decoration: none; word-break: break-all; }
        .detail-link:hover { text-decoration: underline; }
        
        /* Toast */
        .toast { 
            position: fixed; 
            bottom: 20px; 
            left: 50%; 
            transform: translateX(-50%); 
            background: #333; 
            color: white; 
            padding: 12px 24px; 
            border-radius: 8px; 
            display: none; 
            z-index: 2000; 
            animation: slideUp 0.3s ease;
        }
        .toast.show { display: block; }
        @keyframes slideUp {
            from { opacity: 0; transform: translateX(-50%) translateY(20px); }
            to { opacity: 1; transform: translateX(-50%) translateY(0); }
        }
        
        /* 空状态 */
        .empty-state { 
            text-align: center; 
            padding: 60px 20px; 
            color: #999; 
        }
        .empty-state .icon { font-size: 48px; margin-bottom: 16px; }
        
        /* 响应式 */
        @media (max-width: 768px) {
            .stats { grid-template-columns: repeat(2, 1fr); }
            .filter-row { flex-direction: column; }
            .filter-group { width: 100%; }
            .filter-group select { flex: 1; }
            .search-box { width: 100%; }
            .list-header { flex-direction: column; gap: 12px; align-items: flex-start; }
        }
    </style>
</head>
<body>
    <div class="container">
        <!-- 头部 -->
        <div class="header">
            <h1>📢 京津冀招标公告追踪平台</h1>
            <p class="header-subtitle">实时推送政府采购招标公告，助您把握商机 | 最后更新: ''' + last_update + '''</p>
            <div class="stats">
                <div class="stat-card">
                    <div class="stat-label">总公告数</div>
                    <div class="stat-value" id="totalCount">-</div>
                </div>
                <div class="stat-card green">
                    <div class="stat-label">今日新增</div>
                    <div class="stat-value" id="todayCount">-</div>
                </div>
                <div class="stat-card orange">
                    <div class="stat-label">天津地区</div>
                    <div class="stat-value" id="tjCount">-</div>
                </div>
                <div class="stat-card red">
                    <div class="stat-label">河北地区</div>
                    <div class="stat-value" id="hbCount">-</div>
                </div>
            </div>
        </div>
        
        <!-- 筛选区域 -->
        <div class="filters">
            <div class="filter-row">
                <div class="filter-group">
                    <label>日期</label>
                    <select id="filterDate">
                        <option value="">全部日期</option>
                    </select>
                </div>
                <div class="filter-group">
                    <label>关键词</label>
                    <select id="filterKeyword">
                        <option value="">全部关键词</option>
                        <option value="造价">造价</option>
                        <option value="全过程咨询">全过程咨询</option>
                        <option value="招标代理">招标代理</option>
                        <option value="项目管理">项目管理</option>
                        <option value="监理">监理</option>
                    </select>
                </div>
                <div class="filter-group">
                    <label>来源</label>
                    <select id="filterSource">
                        <option value="">全部来源</option>
                        <option value="中国政府采购网">中国政府采购网</option>
                        <option value="天津">天津</option>
                        <option value="河北">河北</option>
                        <option value="北京">北京</option>
                    </select>
                </div>
                <div class="filter-group">
                    <label>地区</label>
                    <select id="filterRegion">
                        <option value="">全部地区</option>
                        <option value="天津">天津</option>
                        <option value="河北">河北</option>
                        <option value="北京">北京</option>
                    </select>
                </div>
                <div class="search-box">
                    <input type="text" id="searchInput" placeholder="🔍 搜索公告标题...">
                </div>
                <button class="btn" onclick="resetFilters()">🔄 重置</button>
                <button class="btn btn-primary" onclick="exportData()">📥 导出</button>
            </div>
        </div>
        
        <!-- 公告列表 -->
        <div class="announcement-list">
            <div class="list-header">
                <h3 class="list-title">📋 公告列表</h3>
                <span class="result-count" id="resultCount"></span>
            </div>
            <div id="announcementList"></div>
            <div class="pagination" id="pagination"></div>
        </div>
    </div>
    
    <!-- 模态框 -->
    <div class="modal-overlay" id="modalOverlay" onclick="closeModal()">
        <div class="modal" onclick="event.stopPropagation()">
            <div class="modal-header">
                <h2 class="modal-title" id="modalTitle"></h2>
                <button class="modal-close" onclick="closeModal()">×</button>
            </div>
            <div id="modalBody"></div>
        </div>
    </div>
    
    <!-- Toast -->
    <div class="toast" id="toast"></div>
    
    <script>
        // 嵌入式数据
        const EMBEDDED_DATA = ''' + json.dumps(data, ensure_ascii=False) + ''';
        
        // 全局变量
        let filteredData = [];
        let currentPage = 1;
        const pageSize = 20;
        
        // 初始化
        document.addEventListener('DOMContentLoaded', function() {
            initStats();
            initFilters();
            initSearch();
            renderList();
        });
        
        // 初始化统计数据
        function initStats() {
            const announcements = EMBEDDED_DATA.announcements;
            const today = new Date().toISOString().split('T')[0];
            
            // 总数
            document.getElementById('totalCount').textContent = announcements.length;
            
            // 今日新增
            const todayCount = announcements.filter(a => a.pubDate === today || a.collectedAt === today).length;
            document.getElementById('todayCount').textContent = todayCount;
            
            // 天津地区
            const tjCount = announcements.filter(a => 
                (a.description && a.description.includes('天津')) || 
                (a.source && a.source.includes('天津')) ||
                (a.title && a.title.includes('天津'))
            ).length;
            document.getElementById('tjCount').textContent = tjCount;
            
            // 河北地区
            const hbCount = announcements.filter(a => 
                (a.description && (a.description.includes('河北') || a.description.includes('石家庄') || a.description.includes('保定') || a.description.includes('秦皇岛'))) ||
                (a.source && a.source.includes('河北'))
            ).length;
            document.getElementById('hbCount').textContent = hbCount;
        }
        
        // 初始化筛选器
        function initFilters() {
            // 日期筛选
            const dates = [...new Set(EMBEDDED_DATA.announcements.map(a => a.pubDate))].sort().reverse();
            const dateSelect = document.getElementById('filterDate');
            dates.forEach(date => {
                const option = document.createElement('option');
                option.value = date;
                option.textContent = date;
                dateSelect.appendChild(option);
            });
            
            // 添加事件监听
            ['filterDate', 'filterKeyword', 'filterSource', 'filterRegion'].forEach(id => {
                document.getElementById(id).addEventListener('change', filterData);
            });
        }
        
        // 初始化搜索
        function initSearch() {
            document.getElementById('searchInput').addEventListener('input', debounce(filterData, 300));
        }
        
        // 防抖
        function debounce(func, wait) {
            let timeout;
            return function executedFunction(...args) {
                const later = () => {
                    clearTimeout(timeout);
                    func(...args);
                };
                clearTimeout(timeout);
                timeout = setTimeout(later, wait);
            };
        }
        
        // 筛选数据
        function filterData() {
            const date = document.getElementById('filterDate').value;
            const keyword = document.getElementById('filterKeyword').value;
            const source = document.getElementById('filterSource').value;
            const region = document.getElementById('filterRegion').value;
            const search = document.getElementById('searchInput').value.toLowerCase();
            
            filteredData = EMBEDDED_DATA.announcements.filter(item => {
                // 日期筛选
                if (date && item.pubDate !== date) return false;
                
                // 关键词筛选
                if (keyword && !item.keywords.some(k => k.includes(keyword) || keyword.includes(k))) return false;
                
                // 来源筛选
                if (source && !item.source.includes(source)) return false;
                
                // 地区筛选
                if (region) {
                    const desc = (item.description || '') + (item.title || '');
                    if (!desc.includes(region)) return false;
                }
                
                // 搜索筛选
                if (search && !item.title.toLowerCase().includes(search)) return false;
                
                return true;
            });
            
            currentPage = 1;
            renderList();
        }
        
        // 渲染列表
        function renderList() {
            const listContainer = document.getElementById('announcementList');
            const start = (currentPage - 1) * pageSize;
            const end = start + pageSize;
            const pageData = filteredData.slice(start, end);
            
            // 更新结果数量
            document.getElementById('resultCount').textContent = '共 ' + filteredData.length + ' 条公告';
            
            if (pageData.length === 0) {
                listContainer.innerHTML = '<div class="empty-state"><div class="icon">📭</div><p>暂无公告</p></div>';
                document.getElementById('pagination').innerHTML = '';
                return;
            }
            
            listContainer.innerHTML = pageData.map((item, index) => {
                const keywordsHtml = item.keywords ? item.keywords.map(k => '<span class="meta-tag keyword">' + k + '</span>').join('') : '';
                const sourceHtml = item.source ? '<span class="meta-tag source">' + item.source + '</span>' : '';
                const regionMatch = item.description ? item.description.match(/地区：([^；]+)/) : null;
                const regionHtml = regionMatch ? '<span class="meta-tag region">' + regionMatch[1] + '</span>' : '';
                
                return '<div class="announcement-item" onclick="showDetail(' + (start + index) + ')">' +
                    '<div class="item-header">' +
                        '<div class="item-title">' + item.title + '</div>' +
                        '<div class="item-date">' + item.pubDate + '</div>' +
                    '</div>' +
                    '<div class="item-meta">' + sourceHtml + keywordsHtml + regionHtml + '</div>' +
                '</div>';
            }).join('');
            
            renderPagination();
        }
        
        // 渲染分页
        function renderPagination() {
            const totalPages = Math.ceil(filteredData.length / pageSize);
            const pagination = document.getElementById('pagination');
            
            if (totalPages <= 1) {
                pagination.innerHTML = '';
                return;
            }
            
            let html = '';
            
            // 上一页
            html += '<button ' + (currentPage === 1 ? 'disabled' : '') + ' onclick="goToPage(' + (currentPage - 1) + ')">上一页</button>';
            
            // 页码
            const maxVisible = 5;
            let startPage = Math.max(1, currentPage - Math.floor(maxVisible / 2));
            let endPage = Math.min(totalPages, startPage + maxVisible - 1);
            
            if (endPage - startPage < maxVisible - 1) {
                startPage = Math.max(1, endPage - maxVisible + 1);
            }
            
            if (startPage > 1) {
                html += '<button onclick="goToPage(1)">1</button>';
                if (startPage > 2) html += '<button disabled>...</button>';
            }
            
            for (let i = startPage; i <= endPage; i++) {
                html += '<button class="' + (i === currentPage ? 'active' : '') + '" onclick="goToPage(' + i + ')">' + i + '</button>';
            }
            
            if (endPage < totalPages) {
                if (endPage < totalPages - 1) html += '<button disabled>...</button>';
                html += '<button onclick="goToPage(' + totalPages + ')">' + totalPages + '</button>';
            }
            
            // 下一页
            html += '<button ' + (currentPage === totalPages ? 'disabled' : '') + ' onclick="goToPage(' + (currentPage + 1) + ')">下一页</button>';
            
            pagination.innerHTML = html;
        }
        
        // 跳转页面
        function goToPage(page) {
            currentPage = page;
            renderList();
            window.scrollTo({ top: 0, behavior: 'smooth' });
        }
        
        // 显示详情
        function showDetail(index) {
            const item = filteredData[index];
            if (!item) return;
            
            document.getElementById('modalTitle').textContent = item.title;
            
            let body = '';
            
            if (item.pubDate) {
                body += '<div class="detail-section"><h4>发布日期</h4><div class="detail-content">' + item.pubDate + '</div></div>';
            }
            
            if (item.source) {
                body += '<div class="detail-section"><h4>来源</h4><div class="detail-content">' + item.source + '</div></div>';
            }
            
            if (item.keywords && item.keywords.length > 0) {
                body += '<div class="detail-section"><h4>关键词</h4><div class="detail-content">' + item.keywords.join('、') + '</div></div>';
            }
            
            if (item.description) {
                body += '<div class="detail-section"><h4>详情描述</h4><div class="detail-content">' + item.description + '</div></div>';
            }
            
            if (item.budget && item.budget !== '未知') {
                body += '<div class="detail-section"><h4>预算金额</h4><div class="detail-content">' + item.budget + '</div></div>';
            }
            
            if (item.link && item.link.startsWith('http')) {
                body += '<div class="detail-section"><h4>原文链接</h4><div class="detail-content"><a href="' + item.link + '" target="_blank" class="detail-link">' + item.link + '</a></div></div>';
            }
            
            document.getElementById('modalBody').innerHTML = body;
            document.getElementById('modalOverlay').classList.add('active');
        }
        
        // 关闭模态框
        function closeModal() {
            document.getElementById('modalOverlay').classList.remove('active');
        }
        
        // ESC关闭模态框
        document.addEventListener('keydown', function(e) {
            if (e.key === 'Escape') closeModal();
        });
        
        // 重置筛选
        function resetFilters() {
            document.getElementById('filterDate').value = '';
            document.getElementById('filterKeyword').value = '';
            document.getElementById('filterSource').value = '';
            document.getElementById('filterRegion').value = '';
            document.getElementById('searchInput').value = '';
            filteredData = [...EMBEDDED_DATA.announcements];
            currentPage = 1;
            renderList();
            showToast('筛选已重置');
        }
        
        // 导出数据
        function exportData() {
            const exportData = filteredData.map((item, index) => ({
                '序号': index + 1,
                '发布日期': item.pubDate || '',
                '标题': item.title || '',
                '来源': item.source || '',
                '关键词': item.keywords ? item.keywords.join(', ') : '',
                '详情': item.description || '',
                '链接': item.link || ''
            }));
            
            // 转换为CSV
            const headers = Object.keys(exportData[0]);
            const csvContent = [
                headers.join(','),
                ...exportData.map(row => headers.map(h => '"' + (row[h] || '').replace(/"/g, '""') + '"').join(','))
            ].join('\\n');
            
            // 下载
            const blob = new Blob(['\\uFEFF' + csvContent], { type: 'text/csv;charset=utf-8;' });
            const link = document.createElement('a');
            link.href = URL.createObjectURL(blob);
            link.download = '招标公告_' + new Date().toISOString().split('T')[0] + '.csv';
            link.click();
            
            showToast('数据已导出');
        }
        
        // 显示提示
        function showToast(message) {
            const toast = document.getElementById('toast');
            toast.textContent = message;
            toast.classList.add('show');
            setTimeout(function() {
                toast.classList.remove('show');
            }, 2000);
        }
    </script>
</body>
</html>
'''

# 保存文件
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"✅ HTML文件已生成，共 {len(announcements)} 条公告")
