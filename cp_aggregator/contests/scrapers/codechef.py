import requests
from datetime import datetime

def scrape_codechef_contests():
    url = "https://www.codechef.com/api/list/contests/all"
    
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
        ),
        "Accept": "application/json, text/plain, */*",
        "Referer": "https://www.codechef.com/contests",
        "Origin": "https://www.codechef.com",
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
    except Exception as e:
        return f"Error fetching/parsing CodeChef contests: {e}"

    contests = []

    for row in data.get("future_contests", []):
        try:
            title = row.get("contest_name", "").strip()
            contest_code = row.get("contest_code", "").strip()
            start_str = row.get("contest_start_date_iso")
            end_str = row.get("contest_end_date_iso")

            if not (title and contest_code and start_str and end_str):
                continue

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
        except Exception as inner_e:
            continue  # skip malformed contest entries

    return contests
