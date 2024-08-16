run-dev-bot:
	poetry run python bot.py

create-service:
	sudo cp telegabot.service /etc/systemd/system/telegabot.service

run-service:
	sudo systemctl daemon-reload
	sudo systemctl enable telegabot.service
	sudo systemctl start telegabot.service

check-service:
	sudo systemctl status telegabot.service

stop-service:
	sudo systemctl stop telegabot.service
	sudo systemctl disable telegabot.service

remove-service:
	sudo rm -rf /etc/systemd/system/telegabot.service
