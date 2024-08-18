create-superuser:
	poetry run python manage.py createsuperuser --username admin --email a@a.com

run-dev-server:
	poetry run python manage.py migrate --noinput
	poetry run python manage.py makemigrations --dry-run --noinput
	poetry run python manage.py runserver 0.0.0.0:8000

create-gunicorn-socket:
	sudo rm -rf /etc/systemd/system/gunicorn.socket
	sudo cp services/gunicorn.socket /etc/systemd/system/gunicorn.socket

create-gunicorn-service:
	sudo rm -rf /etc/systemd/system/gunicorn.service
	sudo cp services/gunicorn.service /etc/systemd/system/gunicorn.service

run-gunicorn-server:
	sudo systemctl daemon-reload
	sudo systemctl start gunicorn.socket
	sudo systemctl enable gunicorn.socket
	# curl --unix-socket /run/gunicorn.sock localhost

restart-gunicorn:
	sudo systemctl restart gunicorn.socket

stop-gunicorn-server:
	sudo systemctl stop gunicorn.socket
	sudo systemctl disable gunicorn.socket

check-gunicorn-status:
	sudo systemctl status gunicorn.socket
	file /run/gunicorn.sock
	sudo journalctl -u gunicorn.socket
	sudo systemctl status gunicorn 
