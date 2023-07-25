from datetime import datetime

from apscheduler.schedulers.background import BackgroundScheduler
from.parse_all import main_funk


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(main_funk, 'interval', minutes=20)
    scheduler.start()
