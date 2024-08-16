config-nginx-proxy:
	sudo rm -rf /etc/nginx/sites-available/proxy_server
	sudo rm -rf /etc/nginx/sites-enabled/proxy_server
	sudo cp proxy_server /etc/nginx/sites-available/proxy_server
	sudo ln -s /etc/nginx/sites-available/proxy_server /etc/nginx/sites-enabled/
	sudo usermod -a -G boss www-data

restart-nginx:
	sudo systemctl restart nginx

check-nginx-status:
	sudo systemctl status nginx