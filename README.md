# NOTIFIER SERVICE FOR LINUX

A custom made notifier service for linux OS(with systemd). It gives you system notification for curcial daily tasks. You can modify the notifications according to your needs(file: custom_notifier.py).

## STEPS TO USE:

1. Clone the repo
2. Install python
3. Install plyer using pip
4. Copy/move custom_notifier.py to the desired path.
5. Edit line no 9 of customnotifier.service:  
    From:  
  		`ExecStart=/usr/bin/python3 /custom_notifier/main.py`  
  	To:  
  		`ExecStart=/usr/bin/python3 <PATH TO custom_notifier.py>`  
6. Copy customnotifier.service to /etc/systemd/system/
7. Reload the system daemon using `systemctl daemon-reload`
8. Start and enable the service  
     `systemctl start customnotifier.service`  
     `systemctl enable customnotifier.service`
