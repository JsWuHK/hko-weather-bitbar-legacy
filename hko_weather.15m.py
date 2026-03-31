#!/Library/Frameworks/Python.framework/Versions/3.13/bin/python3
# -*- coding: utf-8 -*-
# ---------------------------------------------------------
# Project: HK Observatory Menubar Weather for BitBar
# Date: 2026-03-30
# Description: 解決 macOS 10.14 舊系統天氣組件失效問題。
#              使用 Python 3.13 + 繞過過期 SSL 憑證。
# Co-authored by Jackson Wu & Gemini 3 Flash
# ---------------------------------------------------------
import urllib.request
import json
import ssl

# --- 在這裡設定你想固定的地區名稱 ---
# 必須跟天文台使用的名稱完全一樣，例如："尖沙咀", "沙田", "觀塘", "赤鱲角"
MY_REGION = "將軍澳" 

def get_weather():
    url = "https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=rhrread&lang=tc"
    context = ssl._create_unverified_context()

    try:
        with urllib.request.urlopen(url, context=context, timeout=10) as response:
            data = json.loads(response.read().decode('utf-8'))
            
            # 1. 取得所有地區的氣溫列表 (這是一個 List)
            all_regions = data['temperature']['data']
            
            # 2. 預設值（萬一找不到指定地區，就用第一個「天文台」總部）
            target_data = all_regions[0]
            
            # 3. 遍歷 List，尋找匹配的地區
            for region in all_regions:
                if region['place'] == MY_REGION:
                    target_data = region
                    break
            
            # 4. 取得圖示
            icon_id = data.get('icon', [50])[0]
            icon_map = {
                        50: "☀️", 51: "☀️", 52: "🌤️", 53: "⛅", 54: "☁️",
                        60: "☁️", 62: "🌧️", 63: "🌧️", 64: "⛈️", 65: "⛈️",
                        70: "🌤️", 71: "🌤️", 76: "🌧️", 81: "🌦️"
                        }
            weather_emoji = icon_map.get(icon_id, "🌡️")

            # --- 輸出到選單列 ---
            # 顯示格式：[地區] [圖示] [氣溫]°C
            print(f"{target_data['place']} {weather_emoji} {target_data['value']}°C")
            
            print("---")
            print(f"測站地點: {target_data['place']}")
            print(f"相對濕度: {data['humidity']['data'][0]['value']}%")
            
            # 顯示更新時間
            print(f"更新時間: {data['updateTime'][11:16]}")
            
            print("---")
            print("查看全港氣溫...")
            for r in all_regions[:10]: # 顯示前10個參考
                print(f"--{r['place']}: {r['value']}°C")
            print("---")
            print("資料來源: 香港天文台 | href=https://www.hko.gov.hk/")

    except Exception as e:
        print("❌ 讀取失敗")

if __name__ == "__main__":
    get_weather()
