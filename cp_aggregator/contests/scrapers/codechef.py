import requests
from datetime import datetime
import re

def parse_duration(start, end):
    start_dt = datetime.strptime(start, "%d %b %Y %H:%M:%S")
    end_dt = datetime.strptime(end, "%d %b %Y %H:%M:%S")
    return int((end_dt - start_dt).total_seconds() // 60)

def scrape_codechef_contests():
    url = "https://www.codechef.com/api/list/contests/all"
    res = requests.get(url)
    data = res.json()

    contests = []

    for row in data.get("future_contests", []):
        title = row["contest_name"]
        contest_code = row["contest_code"]
        start_str = row["contest_start_date_iso"]
        end_str = row["contest_end_date_iso"]

        start_time = datetime.fromisoformat(start_str)
        end_time = datetime.fromisoformat(end_str)
        duration = int((end_time - start_time).total_seconds() // 60)

        contests.append({
            "title": title,
            "platform": "CodeChef",
            "contest_id": contest_code,
            "start_time": start_time,
            "duration": duration,
            "url": f"https://www.codechef.com/{contest_code}"
        })

    return contests
