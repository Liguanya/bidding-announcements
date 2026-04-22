#!/bin/bash
# ============================================
# 招标公告推送平台 - 定时任务安装脚本
# ============================================
# 安装方法：bash install_cron.sh
# ============================================

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
UPDATE_SCRIPT="$SCRIPT_DIR/update_data.py"
LOG_DIR="$PROJECT_ROOT/logs"
LOG_FILE="$LOG_DIR/update.log"
CRON_CMD="0 9,14,18 * * * cd $PROJECT_ROOT && python3 $UPDATE_SCRIPT >> $LOG_FILE 2>&1"

echo "=========================================="
echo "📢 招标公告推送平台 - 定时任务安装"
echo "=========================================="
echo ""

# 创建日志目录
mkdir -p "$LOG_DIR"

# 检查是否已有定时任务
if crontab -l 2>/dev/null | grep -q "update_data.py"; then
    echo "⚠️  已存在定时任务，正在移除旧任务..."
    crontab -l 2>/dev/null | grep -v "update_data.py" | crontab -
fi

# 添加新定时任务
echo "📝 添加定时任务..."
echo "$CRON_CMD" | crontab -

echo ""
echo "✅ 定时任务安装完成！"
echo ""
echo "📋 当前定时任务："
echo "   • 每天 09:00 自动更新"
echo "   • 每天 14:00 自动更新"
echo "   • 每天 18:00 自动更新"
echo ""
echo "📁 日志文件: $LOG_FILE"
echo ""
echo "🔧 常用命令："
echo "   查看定时任务: crontab -l"
echo "   编辑定时任务: crontab -e"
echo "   删除定时任务: crontab -r"
echo "   查看日志: tail -f $LOG_FILE"
echo "   手动执行: python3 $UPDATE_SCRIPT"
echo ""
