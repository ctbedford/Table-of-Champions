web: cd backend && gunicorn backend.wsgi --log-file -
release: cd backend && python manage.py migrate
worker: cd frontend && npm start
