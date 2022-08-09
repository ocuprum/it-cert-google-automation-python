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

