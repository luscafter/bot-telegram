# coding=utf-8
from telegram.ext import CommandHandler, MessageHandler, Filters, Updater
from config.settings import TOKEN_BOT
from lib.commands import *

def main():
    if bool(TOKEN_BOT) == False:
        print("[!] The bot's token is empty! Path: /src/config/.env", end="")
        exit(1)

    try:
        updater = Updater(token=TOKEN_BOT, use_context=True)
        dispatcher = updater.dispatcher

        dispatcher.add_handler(CommandHandler("help", help))
        dispatcher.add_handler(CommandHandler("cep", cep, pass_args=True))
        dispatcher.add_handler(CommandHandler("cnpj", cnpj, pass_args=True))
        dispatcher.add_handler(CommandHandler("fCNPJ", fCNPJ, pass_args=True))
        dispatcher.add_handler(MessageHandler(Filters.command, unknown))

        print("[+] Waking up the bot")
        updater.start_polling()
        updater.idle()
    except Exception as error:
        print(f"[!] Invalid token! Error: {error}", end="")
        exit(1)

if __name__ == "__main__":
    main()
