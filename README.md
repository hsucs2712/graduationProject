# 🎓 畢業專題：智慧飼料車與即時影像辨識系統

這是一個整合了 **Django 網頁伺服器**、**OpenCV 即時影像辨識** 與 **硬體控制（飼料車）** 的專題作品，目標是提升畜牧業自動化與效率。

---

## 📸 專案功能簡介

- ✅ 使用攝影機即時辨識動物行為與位置
- ✅ 自動控制飼料車進行移動與投餵
- ✅ 網頁前端即時觀看畫面、控制與資料查看
- ✅ Django 後端伺服器整合影像流與控制邏輯
- ✅ 使用 PySerial 串接 C++ 控制模組，實現物聯網應用

---

## 🖥️ 專案結構說明

```
graduationProject/
├── chicken/               # 飼料車控制程式（C++）
├── django_videostream/    # Django 網頁與辨識功能
│   ├── detection.py       # OpenCV 即時影像辨識程式
│   └── manage.py          # Django 管理腳本
├── 專題簡報.pdf
├── 技術報告.pdf
├── 成品影片.mp4
└── README.md              # 說明文件
```

---

## 🔧 使用技術

| 技術領域   | 使用內容                      |
|------------|-------------------------------|
| Python     | 影像處理、Web伺服器             |
| Django     | 架設網頁介面與 API            |
| OpenCV     | 即時影像辨識處理               |
| C++        | 控制飼料車（Arduino 等設備）  |
| PySerial   | 串口通訊實作硬體控制           |
| HTML/JS    | 前端畫面顯示與控制             |

---

## 🚀 執行方式

### 1️⃣ 啟動 Django 網頁伺服器

請先確認已安裝以下 Python 套件：

```bash
pip install django==3.2.7 opencv-python==4.6.0 pyserial==3.5 requests==2.28.1
```

然後啟動伺服器：

```bash
cd django_videostream
python manage.py runserver
```

### 2️⃣ 啟動影像辨識功能

開啟第二個終端機並執行：

```bash
python detection.py
```

### 3️⃣ 硬體控制設定

進入 `chicken/` 資料夾修改 `ser1`、`ser2` 通訊埠（COM port）為你當前設備的設定值。

---

## 🙋‍♂️ 作者資訊

- 作者：徐千善 (hsucs2712)
- 學校：朝洋科技大學
- GitHub：https://github.com/hsucs2712

---

## 💬 備註

本專案為畢業專題作品，包含多項技術整合，若有任何問題或合作意願，歡迎聯繫！
