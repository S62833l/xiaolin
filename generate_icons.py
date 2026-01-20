from PIL import Image, ImageDraw, ImageFont
import os

def create_app_icon(size, output_path):
    img = Image.new('RGBA', (size, size), (233, 69, 96, 255))
    draw = ImageDraw.Draw(img)
    
    try:
        font_size = int(size * 0.4)
        font = ImageFont.truetype("arial.ttf", font_size)
    except:
        font = ImageFont.load_default()
    
    text = "US"
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    x = (size - text_width) // 2
    y = (size - text_height) // 2 - int(size * 0.05)
    
    draw.text((x, y), text, fill=(255, 255, 255, 255), font=font)
    
    img.save(output_path)
    print(f"✓ 创建图标: {output_path} ({size}x{size})")

sizes = [192, 512]
for size in sizes:
    output_path = f"icon-{size}.png"
    create_app_icon(size, output_path)

print("\n✅ 图标生成完成！")
