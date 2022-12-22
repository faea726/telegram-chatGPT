# Telegram ChatGPT

It's a telegram bot (for personal only). Help you interact with
[chatGPT](https://chat.openai.com/) without open web browser.

## Usage

Setup with [PIP](https://pypi.org/project/pip/)

```bash
pip install -r requirements.txt
```

Copy `.env-example` into new file named `.env`.

Add your [OpenAPI API key](https://beta.openai.com/account/api-keys),
[Telegram Bot Token](https://t.me/BotFather), and your
[Telegram ID](https://telegram.org/faq#q-what-is-a-user-id).

```
# File .env
OPEN_API_KEY = <YOUR_OPENAPI_KEY>
TELEGRAM_BOT_TOKEN = <YOUR_BOT_TOKEN>
USER_ID = <YOUR_USER_ID>
```

Run

```bash
python main.py
```

## License

[MIT](https://choosealicense.com/licenses/mit/)
