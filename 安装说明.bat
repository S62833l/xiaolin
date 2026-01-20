@echo off
chcp 65001 >nul
echo.
echo ╔══════════════════════════════════════════════════════════════╗
echo ║         超声词汇加油站 - PWA 安装包生成脚本                    ║
echo ╚══════════════════════════════════════════════════════════════╝
echo.

REM 检查Python和Pillow
python -c "from PIL import Image" 2>nul
if errorlevel 1 (
    echo ❌ 需要安装Pillow库
    echo   运行: pip install pillow
    pause
    exit /b 1
)

echo 📱 正在生成App图标...
python generate_icons.py

echo.
echo ✅ PWA文件准备完成！
echo.
echo 📂 文件结构:
echo    ├── 小霖的超声词汇加油站_Web版.html  (主应用)
echo    ├── manifest.json                    (PWA配置)
echo    ├── service-worker.js               (离线支持)
echo    ├── icon-192.png                    (图标)
echo    └── icon-512.png                    (图标)
echo.
echo 🚀 部署方法:
echo    1. 将整个文件夹上传到任意静态网站托管:
echo       - GitHub Pages (免费)
echo       - Vercel (免费)
echo       - 阿里云OSS (免费)
echo       - 腾讯云COS (免费)
echo    2. 使用Python本地测试:
echo       python -m http.server 8000
echo    3. 访问后点击"添加到主屏幕"即可安装
echo.
pause
