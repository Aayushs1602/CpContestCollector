# # contests/tasks.py

# from celery import shared_task
# from .fetchers import fetch_codeforces_contests

# @shared_task
# def fetch_codeforces():
#     print("Fetching Codeforces contests...")
#     fetch_codeforces_contests()

# testing
import logging
from celery import shared_task

logger = logging.getLogger(__name__)

@shared_task
def fetch_codeforces():
    logger.info("🔥 Periodic fetch task triggered.")
    print("🔥 Periodic fetch task triggered (print).")
