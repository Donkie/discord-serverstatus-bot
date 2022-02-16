
# Discord Server Status Bot
A discord bot which displays Source and Minecraft server statuses as its custom status

## Docker setup

Example docker-compose:

```yml
version: "3.8"
services:
  mc1:
    image: image/path
    environment:
      - BOT_TOKEN=OTA2yaddayadda
      - BOT_SERVER_TYPE=minecraft
      - BOT_SERVER_IP=123.123.123.123
      - BOT_SERVER_PORT=25565
```

BOT_SERVER_TYPE can be either `minecraft` or `source`. `source` supports any A2S compatible server.

## Bot setup
Create a new Discord application and then a bot, see https://discordpy.readthedocs.io/en/stable/discord.html
* The name of the application doesn't matter. The name and avatar of the bot will be what is displayed in Discord.
* The bot doesn't really need any permissions at all in your server.
