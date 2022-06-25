echo "Installing dependencies"
# poetry install
venv=`poetry show -v 2> /dev/null | head -n1 | cut -d ' ' -f 3`
echo "venv path: $venv"
script_folder="`echo ~`/bin"
script="$script_folder/status.sh"
echo "script path: $script"
cwd=`pwd`
echo "cwd: $cwd"
echo "Making directory $script_folder"
mkdir -p $script_folder

echo "Run these commands\n-----------------\n"

echo "echo '
#!/bin/bash
cd $cwd/.. && $venv/bin/python discord_status_changer/status_changer.py
' > $script"

echo "chmod +x $script"
echo "
echo '
[Unit]
Description=Change Discord status

[Service]
User=`whoami`
Type=simple
ExecStart=$script
Restart=always

[Install]
WantedBy=default.target
' > /etc/systemd/system/status.service
"

echo "
systemctl enable status.service
systemctl start status.service
systemctl status status.service
"