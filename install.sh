#!/bin/sh
sudo touch /etc/systemd/system/mentalbot.service
echo -e "[Unit]\nDescription=Service to run mentalbot\nAfter=network-online.target\n[Service]\nUser=$USER\nType=simple\nRestart=always\nWorkingDirectory=$PWD\nExecStart=/bin/sh -c '/usr/bin/python3 $PWD/main.py'\n[Install]\nWantedBy=multi-user.target" | sudo tee -a /etc/systemd/system/mentalbot.service > /dev/null
sudo systemctl daemon-reload
sudo systemctl enable mentalbot.service
sudo systemctl start mentalbot.service
echo "mentalbot.service was installed and launched!"