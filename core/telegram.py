import urllib.request
import urllib.parse
from django.conf import settings


def send_telegram(message):
    """Contact xabarini bir yoki bir nechta Telegram chatga yuboradi."""
    token = settings.TELEGRAM_BOT_TOKEN
    chat_ids = settings.TELEGRAM_CHAT_ID
    if not token or not chat_ids:
        return False
    sent = False
    for chat_id in str(chat_ids).split(','):
        chat_id = chat_id.strip()
        if not chat_id:
            continue
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        data = urllib.parse.urlencode({
            'chat_id': chat_id,
            'text': message,
            'parse_mode': 'HTML',
        }).encode()
        try:
            urllib.request.urlopen(urllib.request.Request(url, data=data), timeout=5)
            sent = True
        except Exception:
            pass
    return sent
