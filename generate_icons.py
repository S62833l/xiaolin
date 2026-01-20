from PIL import Image, ImageDraw, ImageFont
import os

def create_modern_icon(size, output_path, text="霖霖宝宝"):
    img = Image.new('RGBA', (size, size), (255, 182, 193, 255))
    draw = ImageDraw.Draw(img)
    
    font_path = "C:/Windows/Fonts/msyh.ttc"
    font_size = int(size * 0.2)
    
    try:
        font = ImageFont.truetype(font_path, font_size)
    except:
        font = ImageFont.load_default()
    
    chars = list(text)
    n_chars = len(chars)
    n_cols = 2
    n_rows = (n_chars + n_cols - 1) // n_cols
    
    cell_width = size * 0.35
    cell_height = size * 0.22
    start_x = (size - cell_width * n_cols) / 2 + cell_width * 0.1
    start_y = (size - cell_height * n_rows) / 2 + cell_height * 0.1
    
    for i, char in enumerate(chars):
        row = i // n_cols
        col = i % n_cols
        x = start_x + col * cell_width
        y = start_y + row * cell_height
        
        bbox = draw.textbbox((0, 0), char, font=font)
        char_width = bbox[2] - bbox[0]
        char_height = bbox[3] - bbox[1]
        
        x = x + (cell_width - char_width) / 2
        y = y + (cell_height - char_height) / 2
        
        draw.text((x, y), char, fill=(255, 255, 255, 255), font=font)
    
    img.save(output_path)
    print(f"✓ 创建图标: {output_path} ({size}x{size})")

sizes = [192, 512]

for size in sizes:
    output_path = f"icon-{size}.png"
    create_modern_icon(size, output_path)

print("\n✅ 现代化图标生成完成！")
