from django.core.management.base import BaseCommand
from contests.scrapers.codeforces import scrape_codeforces_contests
from contests.scrapers.atcoder import scrape_atcoder_contests
from contests.scrapers.codechef import scrape_codechef_contests
from contests.scrapers.leetcode import scrape_leetcode_contests
from contests.models import Contest

class Command(BaseCommand):
    help = "Fetch contests from all platforms"

    def handle(self, *args, **kwargs):
        all_scrapers = [
            scrape_codeforces_contests,
            scrape_atcoder_contests,
            scrape_codechef_contests,
            scrape_leetcode_contests
        ]

        added = 0
        for scraper in all_scrapers:
            contests = scraper()
            for c in contests:
                obj, created = Contest.objects.get_or_create(
                    contest_id=c["contest_id"],
                    platform=c["platform"],
                    defaults={
                        "title": c["title"],
                        "start_time": c["start_time"],
                        "duration": c["duration"],
                        "url": c["url"]
                    }
                )
                if created:
                    added += 1
        self.stdout.write(self.style.SUCCESS(f"✅ Total new contests added: {added}"))
