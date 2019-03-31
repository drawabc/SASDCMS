#Testing shitt
from apscheduler.schedulers.blocking import BlockingScheduler
import SocialMedia_API
import sys

sched = BlockingScheduler()
socialMedia = SocialMedia_API.SocialMedia()

@sched.scheduled_job('interval', hours=1)
def send_social_media_messages():
    socialMedia.sendSocialMedia()
    print("Message sent")
    sys.stdout.flush()

sched.start()
