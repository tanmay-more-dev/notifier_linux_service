import os
import time
from datetime import datetime
import sys
sys.path.append('/home/user1/.local/lib/python3.11/site-packages/plyer')
from plyer import notification

user_id = os.getuid()
dbus_session_bus_address = f'unix:path=/run/user/{user_id}/bus'
os.environ['DBUS_SESSION_BUS_ADDRESS'] = dbus_session_bus_address

TITLE = "Albert"
APP_ICON = "/custom_notifier/media/img/alert.png"

notification.notify(
    title=f"{TITLE} Activated (Custom Reminder)",
    message="Hi! I will remind you of some important daily tasks.",
    timeout=15, app_icon=APP_ICON)
time.sleep((60 - datetime.now().minute) * 60)

while True:
    current_hour = datetime.now().hour

    if current_hour == 17:
        notification.notify(
            title=TITLE,
            message="It's a Tea Time. Take a break and enjoy a cup of tea.",
            timeout=20, app_icon=APP_ICON)
    elif current_hour == 13:
        notification.notify(
            title=TITLE,
            message='''It's a Lunch Time. I'm gonna have some
            pan cakes. And you?''',
            timeout=20, app_icon=APP_ICON)
    elif current_hour == 0:
        notification.notify(
            title=TITLE,
            message="It's too late. You should sleep now.",
            timeout=20, app_icon=APP_ICON)
    elif current_hour == 20:
        notification.notify(
            title=TITLE,
            message="It's dinner time. What are you having today?",
            timeout=20, app_icon=APP_ICON)
    else:
        notification.notify(
            title=TITLE,
            message="Don't forget to drink water. Keep yourself hydrated!",
            timeout=20, app_icon=APP_ICON)

    time.sleep(60 * 60)
