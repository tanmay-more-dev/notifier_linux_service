import os
import time
from datetime import datetime
import sys
sys.path.append('/home/user1/.local/lib/python3.11/site-packages/plyer')
from plyer import notification

os.environ['DBUS_SESSION_BUS_ADDRESS'] = f'unix:path=/run/user/{os.getuid()}/bus'

TITLE = "Albert"

def notify(msg, title=TITLE, timeout=15):
    notification.notify(title=title, message=msg, timeout=timeout)

ALERTS = {
    "startup": "Hi! I will remind you of some important daily tasks.",
    "default": "Don't forget to drink water. Keep yourself hydrated!",
    17: "It's a Tea Time. Take a break and enjoy a cup of tea.",
    13: "It's a Lunch Time. I'm gonna have some pan cakes. And you?",
    0: "It's too late. You should sleep now.",
    20: "It's dinner time. What are you having today?",
}

notify(title=f"{TITLE} Activated", msg=ALERTS.get("startup"), timeout=10)
time.sleep((60 - datetime.now().minute) * 60)

while True:
    hrs_now = datetime.now().hour
    if ALERTS.get(hrs_now):
        notify(msg=ALERTS.get(hrs_now))
    else:
        notify(msg=ALERTS.get("default"))
    time.sleep(60 * 60)
