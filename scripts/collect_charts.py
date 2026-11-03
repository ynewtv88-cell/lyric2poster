import os
import requests
import json
from datetime import datetime

# 간단한 Last.fm 차트 수집 기본 뼈대 코드
api_key = os.environ.get("LASTFM_API_KEY")
print("Last.fm API Key check:", "Loaded successfully!" if api_key else "Key not found!")

# 폴더 생성
os.makedirs("data/charts", exist_ok=True)

# 더미/기본 차트 JSON 파일 생성 (테스트용)
sample_data = {
    "date": datetime.now().strftime("%Y-%m-%d"),
    "tracks": [
        {"rank": 1, "title": "Example Song 1", "artist": "Example Artist 1"},
        {"rank": 2, "title": "Example Song 2", "artist": "Example Artist 2"}
    ]
}

with open("data/charts/global.json", "w", encoding="utf-8") as f:
    json.dump(sample_data, f, ensure_ascii=False, indent=4)

print("Chart collection test completed successfully!")
