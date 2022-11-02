#! /bin/bash

if [ "$1" = "run_django" ]; then
  python manage.py migrate
  python manage.py collectstatic --no-input
  exec gunicorn backend.wsgi:application -b 0.0.0.0:8000 --reload
fi

if [ "$1" = "run_celery" ]; then
  python manage.py migrate
  exec celery -A backend worker -l info
fi

exec "$@"