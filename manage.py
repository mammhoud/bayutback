#!/usr/bin/env python

def init_django():
    import django
    from django.conf import settings
    from pathlib import Path
    BASE_DIR = Path(__file__).resolve().parent
    import os
    if settings.configured:
        return

    settings.configure(
        INSTALLED_APPS=[
            'db',
        ],
        DATABASES={
            'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db' / 'db.sqlite3',
                }
        }
    )
    django.setup()
    print("Database created: ", BASE_DIR / 'db' / 'db.sqlite3')


if __name__ == "__main__":
    from django.core.management import execute_from_command_line

    init_django()
    execute_from_command_line()