#!/usr/bin/env python3
import os
from datetime import date
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

def generate_report(filename, title, additional_info):
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(filename)
    report_title = Paragraph(title, styles['h1'])
    report_info = Paragraph(additional_info, styles['BodyText'])
    empty_line = Spacer(1, 20)
    report.build([report_title, empty_line, report_info, empty_line])

report_name = 'processed.pdf'
title = 'Processed Update on {}'.format(date.today)

desc_dir = '/supplier-data/descriptions/'
os.chdir(desc_dir)
additional_info = ''
for text in os.listdir(desc_dir):
    additional_info += '{}\n{}\n'.format(*text.read().rstrip().split()[:2])

generate_report(report_name, title, additional_info)