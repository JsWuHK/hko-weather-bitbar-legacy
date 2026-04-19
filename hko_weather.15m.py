#!/Library/Frameworks/Python.framework/Versions/3.13/bin/python3
# -*- coding: utf-8 -*-
# ---------------------------------------------------------
# Project: HK Observatory Menubar Weather for BitBar
# Date: 2026-04-19
# Description: 解決 macOS 10.14 舊系統天氣組件失效問題。
#              新增：讀取 fnd API，顯示未來三天的結構化天氣預報。
# Co-authored by Jackson Wu & Gemini 3 Flash
# ---------------------------------------------------------
import urllib.request
import json
import ssl

# --- 在這裡設定你想固定的地區名稱 ---
MY_REGION = "將軍澳" 

def get_weather():
    # 兩條 API 路徑：即時天氣 (rhrread) 與 九天天氣預報 (fnd)
    url_now = "https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=rhrread&lang=tc"
    url_fnd = "https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=fnd&lang=tc"
    
    # 建立繞過 SSL 驗證的 context
    context = ssl._create_unverified_context()

    try:
        # 1. 讀取即時天氣資料
        with urllib.request.urlopen(url_now, context=context, timeout=10) as response_now:
            data_now = json.loads(response_now.read().decode('utf-8'))
            
        # 2. 讀取九天天氣預報資料 (fnd)
        with urllib.request.urlopen(url_fnd, context=context, timeout=10) as response_fnd:
            data_fnd = json.loads(response_fnd.read().decode('utf-8'))
            
        # --- 處理即時天氣數據 ---
        all_regions = data_now['temperature']['data']
        target_data = all_regions[0] # 預設值
        
        for region in all_regions:
            if region['place'] == MY_REGION:
                target_data = region
                break
        
        icon_id = data_now.get('icon', [50])[0]
        icon_map = {
                    50: "☀️", 51: "☀️", 52: "🌤️", 53: "⛅", 54: "☁️",
                    60: "☁️", 61: "☁️", 62: "🌧", 63: "🌧", 64: "⛈", 65: "⛈",
                    70: "⭐", 71: "🌙", 72: "🌗", 73: "🌕", 74: "🌗", 75: "🌙️", 76: "☁️️️", 77: "☁️"
                    }
        weather_emoji = icon_map.get(icon_id, "🌡️")

        # --- 輸出到選單列 ---
        # 第一行：Menu Bar 上的即時狀態
        print(f"{target_data['place']} {weather_emoji} {target_data['value']}°C")
        
        print("---")
        print(f"測站地點: {target_data['place']}")
        print(f"相對濕度: {data_now['humidity']['data'][0]['value']}%")
        print(f"更新時間: {data_now['updateTime'][11:16]}")
        
        # --- 處理與顯示未來三天預報 ---
        print("---")
        print("📅 未來三天預報 | color=#888888")
        
        # 從 fnd 數據中提取 weatherForecast 列表，並只取前 3 個元素 ([:3])
        forecasts = data_fnd.get('weatherForecast', [])[:3]
        
        for day in forecasts:
            # 安全地提取數據，避免 API 缺漏報錯
            date_raw = day.get('forecastDate', '')
            week = day.get('week', '')
            desc = day.get('forecastWeather', '無資料')
            
            mintemp = day.get('forecastMintemp', {}).get('value', '--')
            maxtemp = day.get('forecastMaxtemp', {}).get('value', '--')
            minrh = day.get('forecastMinrh', {}).get('value', '--')
            maxrh = day.get('forecastMaxrh', {}).get('value', '--')
            
            # 格式化日期 (把 "20260420" 變成 "04/20")
            fmt_date = f"{date_raw[4:6]}/{date_raw[6:8]}" if len(date_raw) == 8 else date_raw
            
            # 第一行：日期、星期、氣溫區間、濕度區間
            print(f"{fmt_date} ({week})  🌡️ {mintemp}-{maxtemp}°C  💧 {minrh}-{maxrh}% | color=#888888" )
            # 第二行：詳細天氣描述 (設定為字體稍小，讓排版更有層次)
            print(f"   └ {desc} | size=12")
        
        print("---")
        print("資料來源: 香港天文台 | href=https://www.hko.gov.hk/")

    except Exception as e:
        print("❌ 讀取失敗")

if __name__ == "__main__":
    get_weather()
