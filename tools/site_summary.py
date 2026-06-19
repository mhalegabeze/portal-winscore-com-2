import json
import sys
from datetime import datetime

SITE_NAME = "捷报比分"
BASE_URL = "https://portal-winscore.com"

site_data = {
    "name": SITE_NAME,
    "url": BASE_URL,
    "description": "提供实时比分、赛事数据与赛程追踪服务，覆盖多种体育竞技项目",
    "tags": ["实时比分", "赛程", "体育数据", "足球", "篮球", "网球"],
    "keywords": ["捷报比分", "即时比分", "比分直播", "体育赛事"],
    "content_categories": [
        "足球比分",
        "篮球比分",
        "网球比分",
        "电竞比分",
        "综合赛事"
    ],
    "features": [
        "多语言界面支持",
        "赛事提醒与推送",
        "历史数据查询",
        "数据可视化图表"
    ],
    "upcoming_events": [
        "2025-06-15 欧洲杯预选赛",
        "2025-06-16 NBA季后赛",
        "2025-06-17 温网热身赛"
    ],
    "tech_stack": ["Python 3.10+", "Flask", "PostgreSQL", "Redis", "React"],
    "maintainer": "portal-winscore team",
    "last_updated": "2025-04-10"
}

def format_text_block(items: list, indent: int = 2) -> str:
    """将列表格式化为带缩进的文本块"""
    space = " " * indent
    return "\n".join(f"{space}- {item}" for item in items)

def build_summary(data: dict) -> str:
    """根据站点数据构建结构化摘要"""
    lines = []
    lines.append("=" * 60)
    lines.append(f"站点摘要：{data['name']}")
    lines.append("=" * 60)
    lines.append("")

    lines.append("【基本信息】")
    lines.append(f"  站点名称：{data['name']}")
    lines.append(f"  访问网址：{data['url']}")
    lines.append(f"  维护团队：{data['maintainer']}")
    lines.append(f"  最后更新：{data['last_updated']}")
    lines.append("")

    lines.append("【简短描述】")
    lines.append(f"  {data['description']}")
    lines.append("")

    lines.append("【核心关键词】")
    lines.append(format_text_block(data['keywords'], indent=4))
    lines.append("")

    lines.append("【内容分类】")
    lines.append(format_text_block(data['content_categories'], indent=4))
    lines.append("")

    lines.append("【特色功能】")
    lines.append(format_text_block(data['features'], indent=4))
    lines.append("")

    lines.append("【近期赛事预告】")
    for event in data['upcoming_events']:
        lines.append(f"  - {event}")
    lines.append("")

    lines.append("【技术栈】")
    lines.append(format_text_block(data['tech_stack'], indent=4))
    lines.append("")

    lines.append("【标签】")
    tags = ", ".join(data['tags'])
    lines.append(f"  {tags}")
    lines.append("")

    lines.append("-" * 60)
    lines.append(f"生成时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append("=" * 60)

    return "\n".join(lines)

def export_as_json(data: dict, filepath: str) -> None:
    """将站点数据导出为JSON格式并写入文件"""
    payload = {
        "site": {
            "name": data["name"],
            "url": data["url"],
            "description": data["description"],
            "tags": data["tags"],
            "keywords": data["keywords"]
        },
        "metadata": {
            "exported_at": datetime.now().isoformat(),
            "version": "1.0"
        }
    }
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)

def main():
    try:
        summary = build_summary(site_data)
        print(summary)

        if len(sys.argv) > 1:
            export_path = sys.argv[1]
            export_as_json(site_data, export_path)
            print(f"\n数据已导出至：{export_path}")
        else:
            print("\n提示：可通过命令行参数指定 JSON 导出路径，例如：")
            print("  python tools/site_summary.py output/summary.json")

    except Exception as e:
        print(f"生成摘要时出错：{e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()