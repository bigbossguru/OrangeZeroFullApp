#!/bin/bash

# Path to the root directory
pwd

# Create and Run all UNIX services

# Backend run gunicorn socket and service
cd ./backend
echo "Backend run gunicorn socket and service"
pwd
poetry install --sync --no-root
make create-gunicorn-socket
make create-gunicorn-service
make run-gunicorn-server
make restart-gunicorn

cd ..
echo

# Configuration Nginx
cd ./nginx
echo "Configuration Nginx service"
pwd
make config-nginx-proxy
make restart-nginx

cd ..
echo

# Configuration Ngrok
cd ./ngrok
echo "Configuration Ngrok service"
pwd
make create-service
make config-ngrok
make run-service
make restart-service

cd ..
echo

# Create Telegram Bot
cd ./telegram_bot
echo "Create Telegram Bot service"
pwd
poetry install --sync --no-root
make create-service
make run-service
make restart-service

cd ..
echo
pwd
echo "Finished"