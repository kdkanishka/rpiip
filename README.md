# rpiip
Reports linux network interface information of a RPi to a targeted email address via SMTP on startup.

Inorder to execute the script on RPi startup, Add below entry to /etc/rc.local
```
# Send Rpi network information as an email
/home/pi/Projects/rpiip/raspberryip.py &
```


