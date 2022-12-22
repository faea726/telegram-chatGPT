import os

import openai
from dotenv import load_dotenv
from telegram.ext import Filters, MessageHandler, Updater


class TelegramChatGPT:
    def __init__(self):
        load_dotenv()
        try:
            self.OPEN_API_KEY = os.environ["OPEN_API_KEY"].strip()
            self.TELEGRAM_BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"].strip()
            self.USER_ID = int(os.environ["USER_ID"].strip())
        except Exception as err:
            print(err)
            exit()

    def run(self):
        print("Init bot...")
        try:
            openai.api_key = self.OPEN_API_KEY
            updater = Updater(self.TELEGRAM_BOT_TOKEN, use_context=True)
        except Exception as err:
            print(err)
            exit()
        dispatcher = updater.dispatcher
        chat_handler = MessageHandler(Filters.text & Filters.user(user_id=self.USER_ID), self._chat_cmd)
        dispatcher.add_handler(chat_handler)
        updater.start_polling()
        print("Listening...")

    def _chat_cmd(self, update, context):
        message = update.message.text
        print(f"[~] {message}")
        try:
            response = openai.Completion.create(
                engine="text-davinci-002",
                prompt=message,
                max_tokens=1024,
                temperature=0.7,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )
            msg = response.choices[0].text
            update.message.reply_text( msg)
        except Exception:
            update.message.reply_text("Yamete! It's too fast! I can't handle this!")

if __name__ == "__main__":
    TelegramChatGPT().run()
