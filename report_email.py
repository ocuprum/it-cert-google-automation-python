#!/usr/bin/env python3
import os
from datetime import date 
from reports import generate_report
from emails import generate_email, send_email

report_name = 'processed.pdf'
title = 'Processed Update on {}'.format(date.today)

desc_dir = '/supplier-data/descriptions/'
os.chdir(desc_dir)
additional_info = ''
for text in os.listdir(desc_dir):
    additional_info += '{}\n{}\n'.format(*text.read().rstrip().split()[:2])

generate_report(report_name, title, additional_info)

if __name__ == '__main__':
    sender = 'automation@example.com'
    recipient = 'username@example.com'
    subject = 'Upload Completed - Online Fruit Store'
    body = 'All fruits are uploaded to our website successfully. A detailed list is attached to this email.'
    ap = '/supplier-data/descriptions/processed.pdf'
    message = generate_email(sender, recipient, subject, body, ap)
    send_email(message)
