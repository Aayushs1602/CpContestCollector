from django.core.management.base import BaseCommand
from contests.scrapers.codeforces import scrape_codeforces_contests

class Command(BaseCommand):
    help = "Fetch upcoming Codeforces contests"

    def handle(self, *args, **kwargs):
        scrape_codeforces_contests()
        self.stdout.write(self.style.SUCCESS("✅ Codeforces contests fetched successfully."))
