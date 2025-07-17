from celery import shared_task
from .scrapers.codeforces import scrape_codeforces_contests
from .scrapers.atcoder import scrape_atcoder_contests
from .scrapers.codechef import scrape_codechef_contests
from .scrapers.leetcode import scrape_leetcode_contests
from .models import Contest
from django.utils.timezone import make_aware, is_naive

@shared_task
def fetch_all_contests():
    scrapers = {
        "codeforces": scrape_codeforces_contests,
        "atcoder": scrape_atcoder_contests,
        "codechef": scrape_codechef_contests,
        "leetcode": scrape_leetcode_contests,
    }

    total_added = 0
    result_summary = {}

    for platform, scraper in scrapers.items():
        try:
            contests = scraper()
            added = 0
            for c in contests:
                start_time = c["start_time"]
                if is_naive(start_time):
                    start_time = make_aware(start_time)

                obj, created = Contest.objects.get_or_create(
                    contest_id=c["contest_id"],
                    platform=c["platform"],
                    defaults={
                        "title": c["title"],
                        "start_time": start_time,
                        "duration": c["duration"],
                        "url": c["url"]
                    }
                )
                if created:
                    added += 1
            total_added += added
            result_summary[platform] = added
        except Exception as e:
            result_summary[platform] = f"Error: {str(e)}"

    return {
        "total_added": total_added,
        "per_platform": result_summary
    }
