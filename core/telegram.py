import urllib.request
import urllib.parse
from django.conf import settings


def send_telegram(message):
    """Contact xabarini Telegram botga yuboradi. Token/chat_id bo'lmasa jim o'tadi."""
    token = settings.TELEGRAM_BOT_TOKEN
    chat_id = settings.TELEGRAM_CHAT_ID
    if not token or not chat_id:
        return False
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = urllib.parse.urlencode({
        'chat_id': chat_id,
        'text': message,
        'parse_mode': 'HTML',
    }).encode()
    try:
        urllib.request.urlopen(urllib.request.Request(url, data=data), timeout=5)
        return True
    except Exception:
        return False
