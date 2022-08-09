#!/usr/bin/env python3
import socket
import psutil, shutil
from emails import generate_email, send_email

cpu_usage = psutil.cpu_percent(1)
du = shutil.disk_usage('/')
disk_usage = du.free / du.total * 100
free_memory = psutil.virtual_memory().available
localhost_check = socket.gethostbyname('localhost') == '127.0.0.1'

if  cpu_usage > 80:
    subject = 'Error - CPU usage is over 80%'
elif disk_usage < 20:
    subject = 'Error - Available disk space is less than 20%'
elif free_memory < 500 * 1024 * 1024:
    subject = 'Error - Available memory is less than 500MB'
elif not localhost_check:
    subject = 'Error - localhost cannot be resolved to 127.0.0.1'

if subject != '':
    sender = 'automation@example.com'
    recipient = 'username@example.com'
    body = 'Please check your system and resolve the issue as soon as possible.'
    ap = '/supplier-data/descriptions/processed.pdf'
    message = generate_email(sender, recipient, subject, body, ap)
    send_email(message)