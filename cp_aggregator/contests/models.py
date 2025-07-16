from django.db import models

class Contest(models.Model):
    PLATFORM_CHOICES = [
        ('codeforces', 'Codeforces'),
        ('atcoder',    'AtCoder'),
        ('codechef',   'CodeChef'),
        ('leetcode',   'LeetCode'),
    ]

    platform    = models.CharField(max_length=32, choices=PLATFORM_CHOICES)
    contest_id  = models.CharField(max_length=64)    # e.g. Codeforces contest ID
    title       = models.CharField(max_length=200)
    start_time  = models.DateTimeField()
    duration    = models.IntegerField(help_text="Duration in minutes")
    url         = models.URLField()

    class Meta:
        unique_together = ('platform', 'contest_id')

    def __str__(self):
        return f"{self.get_platform_display()} – {self.title}"
