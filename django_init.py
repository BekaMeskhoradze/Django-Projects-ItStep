import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')
django.setup()


#exec(open('django_init.py').read())