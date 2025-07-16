import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta, timezone


def scrape_atcoder_contests():
    url = "https://atcoder.jp/contests/"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")

    contests = []

    # Upcoming contests table is the 2nd one
    table = soup.find_all("table")[1]
    for row in table.find("tbody").find_all("tr"):
        cols = row.find_all("td")
        start_str = cols[0].text.strip()
        title = cols[1].text.strip()
        link = "https://atcoder.jp" + cols[1].find("a")["href"]
        contest_slug = cols[1].find("a")["href"].strip("/").split("/")[-1]

        # Parse JST time and convert to UTC
        jst = datetime.strptime(start_str, "%Y-%m-%d %H:%M:%S%z")
        start_time = jst.astimezone(tz=timezone.utc).replace(tzinfo=None)  # convert to UTC

        contests.append({
            "title": title,
            "platform": "AtCoder",
            "start_time": start_time,
            "contest_id": contest_slug,
            "duration": 100,  # fixed or parse from another page if needed
            "url": link
        })

    return contests
