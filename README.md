# I DESIGNER — Interyer Dizayn Sayti

3D Max interyer dizaynerlar uchun Django asosidagi portfolio sayti.

## Imkoniyatlar
- Hero karusel (admin paneldan rasm qo'shish/o'chirish)
- Portfolio galereya (kategoriya bo'yicha filtr)
- Narxlar va paketlar
- Kontakt forma — har bir murojaat **Telegram botga** yuboriladi
- Admin panel orqali boshqaruv

## O'rnatish
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Sozlash
`.env.example` ni `.env` ga nusxalang va qiymatlarni to'ldiring:
```bash
cp .env.example .env
```

## Ishga tushirish
```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Sayt: http://127.0.0.1:8000
Admin: http://127.0.0.1:8000/admin
