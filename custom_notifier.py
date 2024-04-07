import time
from datetime import datetime
import sys
sys.path.append('/home/user1/.local/lib/python3.11/site-packages/plyer')
from plyer import notification
import os

user_id = os.getuid()
dbus_session_bus_address = f'unix:path=/run/user/{user_id}/bus'
os.environ['DBUS_SESSION_BUS_ADDRESS'] = dbus_session_bus_address

notification.notify(title="Custom Notifier Activated", timeout=10, app_icon="/alert.png")
time.sleep((60 - datetime.now().minute) * 60)

while True:
    current_hour = datetime.now().hour

    if current_hour == 17:
        notification.notify(title="Tea Time",
                            message="Take a break and enjoy a cup of tea.",
                            timeout=10, app_icon="/alert.png")
    elif current_hour == 13:
        notification.notify(
            title="Lunch Time",
            message="It's time to have lunch. Take a break and refuel.",
            timeout=10, app_icon="/alert.png")
    else:
        notification.notify(
            title="Stay Hydrated",
            message="Don't forget to drink water. Keep yourself hydrated!",
            timeout=10, app_icon="/alert.png")

    time.sleep(60 * 60)
