import django
from django.core.management import call_command

django.setup()

if __name__ == '__main__':
    call_command('seed')
