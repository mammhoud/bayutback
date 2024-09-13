
from datetime import datetime, timedelta
import time

def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, '%d/%m/%Y')
        return True
    except ValueError:
        # If parsing fails, return False
        return False

def change_date_format(date_str):
    try:
        if '\n' in date_str:
            date_str = date_str.replace('\n', '')
            date_str = datetime.strptime(date_str, '%d %b %Y')
            date_str = date_str.strftime('%d/%m/%Y')
            return date_str

        if 'Sept' in date_str:
            date_str = date_str.replace('Sept', 'Sep')
            date_str = datetime.strptime(date_str, '%d %b %Y')
            date_str = date_str.strftime('%d/%m/%Y')
            return date_str

        else:
            date_str = datetime.strptime(date_str, '%d %b %Y')
            date_str = date_str.strftime('%d/%m/%Y')
            return date_str
    except ValueError:
        # If parsing fails, return False
        return False
    

    