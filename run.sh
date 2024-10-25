sleep 40


pip install -r requirements.txt
flask db init
flask db migrate -m "initial migration"
flask db upgrade
gunicorn app:app --bind 0.0.0.0:5000