import os
from PIL import ImageFont

font_paths = [
    "C:/Windows/Fonts/msyh.ttc",      # 微软雅黑
    "C:/Windows/Fonts/simhei.ttf",    # 黑体
    "C:/Windows/Fonts/simkai.ttf",    # 楷体
    "C:/Windows/Fonts/simsun.ttc",    # 宋体
    "C:/Windows/Fonts/pingfang.ttf",  # 苹方
]

available = []
for fp in font_paths:
    if os.path.exists(fp):
        available.append(fp)
        print(f"✓ 找到字体: {fp}")

if not available:
    print("未找到中文字体，尝试查找所有字体...")
    for root, dirs, files in os.walk("C:/Windows/Fonts"):
        for f in files:
            if f.endswith(('.ttf', '.ttc')) and any(kw in f.lower() for kw in ['hei', 'kai', 'ming', 'fang', 'song']):
                print(f"✓ 找到: {os.path.join(root, f)}")
