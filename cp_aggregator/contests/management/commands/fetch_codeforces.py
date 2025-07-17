from django.core.management.base import BaseCommand
from contests.scrapers.codeforces import fetch_codeforces_contests

class Command(BaseCommand):
    help = "Fetch upcoming Codeforces contests"

    def handle(self, *args, **kwargs):
        fetch_codeforces_contests()
        self.stdout.write(self.style.SUCCESS("✅ Codeforces contests fetched successfully."))
