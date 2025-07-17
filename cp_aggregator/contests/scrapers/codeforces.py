import requests
from datetime import datetime, timezone

def scrape_codeforces_contests():
    url = "https://codeforces.com/api/contest.list"
    response = requests.get(url)
    data = response.json()

    if data.get("status") != "OK":
        print("[error] Failed to fetch from Codeforces")
        return []

    contests = []
    now_ts = datetime.utcnow().timestamp()

    for contest in data["result"]:
        if contest["phase"] != "BEFORE":
            continue  # skip past and running contests

        start_ts = contest.get("startTimeSeconds", 0)
        if start_ts < now_ts:
            continue

        contests.append({
            "contest_id": str(contest["id"]),
            "platform": "Codeforces",
            "title": contest["name"],
            "start_time": datetime.fromtimestamp(start_ts, tz=timezone.utc),
            "duration": int(contest["durationSeconds"] / 60),  # in minutes
            "url": f"https://codeforces.com/contests/{contest['id']}"
        })

    return contests
