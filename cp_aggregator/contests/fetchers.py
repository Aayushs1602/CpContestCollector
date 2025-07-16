import requests
from datetime import datetime, timezone
from .models import Contest

def fetch_codeforces_contests():
    url = "https://codeforces.com/api/contest.list"
    response = requests.get(url)
    data = response.json()

    if data["status"] != "OK":
        print("Failed to fetch from Codeforces")
        return

    contests = data["result"]
    for c in contests:
        if c["phase"] != "BEFORE":
            continue  # Only future contests

        contest_id = str(c["id"])
        title = c["name"]
        start_time = datetime.fromtimestamp(c["startTimeSeconds"], tz=timezone.utc)
        duration = int(c["durationSeconds"] / 60)
        url = f"https://codeforces.com/contests/{contest_id}"

        # Check if it already exists
        if Contest.objects.filter(platform="codeforces", contest_id=contest_id).exists():
            continue

        Contest.objects.create(
            platform="codeforces",
            contest_id=contest_id,
            title=title,
            start_time=start_time,
            duration=duration,
            url=url
        )
        print(f"Added: {title}")
