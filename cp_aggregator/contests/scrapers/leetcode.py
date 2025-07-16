import requests
from datetime import datetime

def scrape_leetcode_contests():
    url = "https://leetcode.com/graphql"
    payload = {
        "query": """
        query {
          allContests {
            title
            titleSlug
            startTime
            duration
          }
        }
        """
    }

    headers = {
        "Content-Type": "application/json",
        "Referer": "https://leetcode.com/contest/",
        "Origin": "https://leetcode.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    res = requests.post(url, json=payload, headers=headers)
    
    try:
        data = res.json()
    except Exception:
        print("[error] Failed to parse JSON")
        print(res.text)
        return []

    if "data" not in data or "allContests" not in data["data"]:
        print("[error] Unexpected response:")
        print(data)
        return []

    contests = []
    now_ts = datetime.utcnow().timestamp()

    for contest in data["data"]["allContests"]:
        start_ts = contest.get("startTime", 0)
        if start_ts < now_ts:
            continue  # skip past contests

        title = contest["title"]
        slug = contest["titleSlug"]
        start_time = datetime.utcfromtimestamp(start_ts)
        duration = int(contest["duration"]) // 60

        contests.append({
            "title": title,
            "platform": "LeetCode",
            "contest_id": slug,
            "start_time": start_time,
            "duration": duration,
            "url": f"https://leetcode.com/contest/{slug}"
        })

    return contests
