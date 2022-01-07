#TODO Change the secrets local, it's better in a separated file.

import secrets
import bot_modules.config

if __name__ == '__main__':
    bot_modules.config.sid.run(secrets.DiscordKEY)