import argparse

from telethon.sync import TelegramClient


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='Telethon Authentication',
        description='Initializing telegram session'
    )
    parser.add_argument('--id', help='API Id of your telegram application', type=int, required=True)
    parser.add_argument('--hash', help='API Hash of your telegram application', type=str, required=True)
    args = parser.parse_args()
    client = TelegramClient('session', args.id, args.hash)
    client.start()
    exit(0)
