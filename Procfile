release: python manage.py migrate && python manage.py collectstatic --noinput
web: gunicorn LMS.wsgi:application --port $PORT --bind 0.0.0.0 -v2


