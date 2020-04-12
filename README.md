# Discord Bot written in Python
A discord bot written in python used within a linux environment (game server control, server control)

Based on the excellent guide at https://realpython.com/how-to-make-a-discord-bot-python/

## Environment
* Python 3.6+
* .env file with DISCORD_TOKEN="xyxyxy"
* Ubuntu 18.04+ as OS (or any Linux distro)

```bash
DISCORD_TOKEN="xyxyxy
```

## Configuration and setup
Install dependencies with pip. On ubuntu do:

```bash
sudo apt install python3-pip
pip3 install -r requirements.txt
```

Use different prefixes if you run multiple bots in one guild/server. Register the bot's separately and use their tokens. 

In order to start the bot while the system starts, copy as sudo the systemd file discordbot.service into
/etc/systemd/system and reboot (or systemctl start discordbot). Adjust the ExecStart and User.