from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .message_compiler import send_report

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(send_report, 'interval', minutes=5)
    scheduler.start()