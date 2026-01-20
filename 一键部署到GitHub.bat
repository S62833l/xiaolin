@echo off
chcp 65001 >nul
echo.
echo ╔══════════════════════════════════════════════════════════════╗
echo ║        超声词汇加油站 - GitHub Pages 自动部署脚本              ║
echo ╚══════════════════════════════════════════════════════════════╝
echo.

set /p username="请输入你的GitHub用户名: "
echo.

echo 📋 正在准备推送代码到GitHub...
echo.

cd "e:\Pycharm项目库（在下面建立子目录）\小霖的超声词汇加油站_Web版"

echo 🔄 1. 重命名分支为main...
git branch -M main

echo 📤 2. 添加远程仓库...
git remote add origin https://github.com/%username%/xiaolin-ultrasound-vocab.git

echo ⬆️ 3. 推送代码到GitHub...
git push -u origin main

if %errorlevel% equ 0 (
    echo.
    echo ✅ 代码推送成功！
    echo.
    echo 🌐 接下来的步骤：
    echo    1. 访问: https://github.com/%username%/xiaolin-ultrasound-vocab
    echo    2. 点击 Settings → Pages
    echo    3. Source选择 "Deploy from a branch"
    echo    4. Branch选择 "main"，文件夹选择 "/(root)"
    echo    5. 点击 Save
    echo.
    echo 📱 部署完成后，访问链接为:
    echo    https://%username%.github.io/xiaolin-ultrasound-vocab/
    echo.
    echo 🎉 小霖的超声词汇App就上线了！
) else (
    echo.
    echo ❌ 推送失败！请检查：
    echo    1. GitHub用户名是否正确
    echo    2. 是否有该仓库的写入权限
    echo    3. 网络连接是否正常
    echo.
    echo 💡 提示：如果提示身份验证，请使用Personal Access Token
)

echo.
pause