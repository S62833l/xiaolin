# 超声词汇加油站 - GitHub Pages 部署指南

## 📋 部署步骤

### 第一步：创建GitHub仓库

1. 访问 https://github.com/new
2. 填写仓库信息：
   - **Repository name**: `xiaolin-ultrasound-vocab`
   - **Description**: 超声词汇加油站 - 661个专业词汇学习应用
   - **Public**: ✅ 公开（免费）
   - **不要勾选** "Add a README file"
3. 点击 **Create repository**

### 第二步：推送代码到GitHub

复制以下命令，在PowerShell中执行：

```bash
cd "e:\Pycharm项目库（在下面建立子目录）\小霖的超声词汇加油站_Web版"
git branch -M main
git remote add origin https://github.com/你的GitHub用户名/xiaolin-ultrasound-vocab.git
git push -u origin main
```

**注意：** 将 `你的GitHub用户名` 替换为你的实际GitHub用户名

### 第三步：配置GitHub Pages

1. 在GitHub仓库页面，点击 **Settings** 标签
2. 左侧菜单找到 **Pages**
3. 在 **Build and deployment** 部分：
   - **Source**: 选择 `Deploy from a branch`
   - **Branch**: 选择 `main` 分支，文件夹选择 `/(root)`
4. 点击 **Save**

### 第四步：等待部署完成

- GitHub会自动部署（约1-3分钟）
- 部署完成后会显示访问链接，格式为：
  ```
  https://你的GitHub用户名.github.io/xiaolin-ultrasound-vocab/
  ```

## 📱 手机安装步骤

1. **用手机浏览器打开上面的链接**
2. **点击"添加到主屏幕"**
   - iOS: Safari → 分享按钮 → 添加到主屏幕
   - Android: Chrome → 菜单 → 添加到主屏幕
3. **完成！** 桌面出现App图标

## ✨ 功能特性

- 🎯 661个超声医学专业词汇
- 🔊 真人发音（TTS）
- 💾 离线可用
- 🎉 通关庆祝动画
- 📊 学习进度追踪
- 🔄 智能记忆算法

## 🔧 更新应用

当需要更新应用时：

```bash
cd "e:\Pycharm项目库（在下面建立子目录）\小霖的超声词汇加油站_Web版"
git add .
git commit -m "更新内容"
git push
```

GitHub会自动更新，用户打开时会自动获取最新版本。

## 📞 常见问题

### Q: 推送时提示身份验证错误？
A: 使用Personal Access Token：
1. GitHub → Settings → Developer settings → Personal access tokens
2. 生成新token，勾选 `repo` 权限
3. 推送时使用token作为密码

### Q: Pages显示404？
A: 等待2-3分钟，GitHub需要时间部署

### Q: 如何修改App图标？
A: 替换 `icon-192.png` 和 `icon-512.png`，然后推送更新

---

🎉 部署完成后，小霖就可以在手机上使用这个专业的超声词汇学习App了！
