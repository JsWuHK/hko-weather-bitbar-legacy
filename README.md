# HKO Weather for BitBar (Legacy macOS Fix)
<img width="563" height="335" alt="HKO script for BitBar" src="https://github.com/user-attachments/assets/e2dfb71f-e5ea-446e-934c-bdebb65c8b50" />

A lightweight Python script for **BitBar** to restore real-time weather info in the macOS menu bar.

解決舊版 Mac 天氣組件失效的 Python 腳本。

### Why this project?
In older versions of macOS (e.g., 10.14 Mojave), the built-in **Dashboard Weather Widget** and system weather services have permanently stopped working. This script provides a modern, reliable alternative using the official Hong Kong Observatory (HKO) API.

### Key Features
- **Legacy System Support**: Bypasses SSL verification to work on older macOS versions where root certificates have expired.
- **Manual Station Setting**: No auto-location tracking (privacy/saving resources); users can manually set their preferred district.
- **Rich Display**: Shows emojis, temperature, humidity, and update time.
- **Auto-Refresh**: The `.15m` filename tells BitBar to update every 15 minutes.

### Prerequisites
1. **BitBar (v1.9.1)**: [Download from GitHub](https://github.com/matryer/bitbar/releases/tag/v1.9.1)
2. **Python 3.13**: Stable on legacy systems. (Avoid Python 3.14+ on 10.14 due to `hashlib` errors).

### Installation & Setup
1. **Download**: Save `hko_weather.15m.py` to your BitBar plugins folder.
2. **Set Python Path**: Open the file and check the **first line** (`#!...`).
   - Ensure it points to your Python 3.13 location.
   - *Tip: Type `which python3` in Terminal to find your path.*
3. **Set your Location**: Modify the `MY_REGION` variable (e.g., `"將軍澳"` 或 `"尖沙咀"`).
4. **Grant Execution Permission**: Open Terminal, `cd` to your plugin folder, and run:
   `chmod +x hko_weather.15m.py`
5. **Refresh**: Select "Refresh" from the BitBar menu.

---

# 香港天文台 BitBar 天氣插件 (舊版 macOS 修復版)

這是一個專為 **BitBar** 設計的 Python 腳本，用於恢復 macOS 選單列的即時天氣顯示。

### 開發原因
在較舊的 macOS（如 10.14 Mojave）中，內建的 **Dashboard 天氣 Widget** 及系統天氣功能已完全失效。本腳本透過香港天文台官方 API，為舊機用戶提供一個穩定且現代的替代方案。

### 核心功能
- **舊系統支援**：繞過 SSL 驗證，解決舊版 macOS 因根憑證過期導致無法抓取數據的問題。
- **手動地區設定**：本版本**不具備自動定位功能**（節省資源並保護隱私），用戶可根據需求自行修改觀測站。
- **豐富資訊**：支援天氣圖示 (Emoji)、氣溫、相對濕度及更新時間。
- **自動更新**：檔名中的 `.15m` 會引導 BitBar 每 15 分鐘自動抓取一次最新數據。

### 準備工作
1. **BitBar (v1.9.1)**：建議 10.14 用戶使用此版本。[從 GitHub 下載](https://github.com/matryer/bitbar/releases/tag/v1.9.1)。
2. **Python 3.13**：經測試在舊系統上最為穩定（請避開 3.14+ 以免出現 `hashlib` 錯誤）。

### 安裝與設定
1. **下載檔案**：將 `hko_weather.15m.py` 放入 BitBar 插件資料夾。
2. **設定 Python 路徑**：打開檔案並檢查**第一行** (`#!...`)。
   - 確保該路徑指向您電腦中 Python 3.13 的安裝位置。
   - *提示：在終端機輸入 `which python3` 即可找出您的正確路徑。*
3. **修改地區**：自行修改 `MY_REGION` 變數（例如：`"將軍澳"` 或 `"尖沙咀"`）。
4. **賦予執行權限**：開啟終端機 (Terminal)，`cd` 進入該資料夾後執行：
   `chmod +x hko_weather.15m.py`
5. **重新整理**：在 BitBar 選單點擊「Refresh」。

---

**Author**: Jackson Wu  
**Co-authored by**: Gemini 3 Flash (An AI collaboration experiment)

*Generated in March 2026 - Keeping legacy Macs alive with code.*
