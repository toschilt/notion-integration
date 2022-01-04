#TODO Change the secrets local, it's better in a separated file.

import secrets
from bot_modules.config import sid

if __name__ == '__main__':
    sid.run(secrets.DiscordKEY)