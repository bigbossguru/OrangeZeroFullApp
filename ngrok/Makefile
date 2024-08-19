create-service:
	sudo cp ngroktunnel.service /etc/systemd/system/ngroktunnel.service

run-service:
	sudo systemctl daemon-reload
	sudo systemctl enable ngroktunnel.service
	sudo systemctl start ngroktunnel.service

check-service:
	sudo systemctl status ngroktunnel.service

restart-service:
	sudo systemctl restart ngroktunnel.service

stop-service:
	sudo systemctl stop ngroktunnel.service
	sudo systemctl disable ngroktunnel.service

remove-service:
	sudo rm -rf /etc/systemd/system/ngroktunnel.service

config-ngrok:
	sudo rm -rf /home/boss/.config/ngrok/ngrok.yml
	sudo cp ngrok.yml /home/boss/.config/ngrok/ngrok.yml
