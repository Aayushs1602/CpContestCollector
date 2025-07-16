from django.core.management.base import BaseCommand
from contests.models import Contest
from contests.scrapers.codechef import scrape_codechef_contests

class Command(BaseCommand):
    help = 'Fetch CodeChef contests and save to DB'

    def handle(self, *args, **kwargs):
        contests = scrape_codechef_contests()
        for data in contests:
            obj, created = Contest.objects.get_or_create(
                platform="CodeChef",
                contest_id=data["contest_id"],
                defaults={
                    "title": data["title"],
                    "start_time": data["start_time"],
                    "duration": data["duration"],
                    "url": data["url"]
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Added: {data['title']}"))
            else:
                self.stdout.write(f"Already exists: {data['title']}")
