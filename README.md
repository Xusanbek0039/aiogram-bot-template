# 🤖 Aiogram Bot Template

![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)
![Aiogram](https://img.shields.io/badge/Aiogram-2.x-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)

Bu loyiha — **Telegram bot** yaratishda foydalanish uchun tayyorlangan `aiogram` framework'iga asoslangan **shablon (template)** hisoblanadi. Strukturasi toza, kengaytiriladigan va yangi botlar yaratishni osonlashtiradi.

---

## 📁 Loyihaning Tuzilishi

```bash
aiogram-bot-template/
│
├── data/               # Konfiguratsiyalar, ma'lumotlar
├── handlers/           # Bot handler'lari (message, callback)
├── keyboards/          # Tugmalar (Inline, Reply)
├── middlewares/        # O‘rta qatlamlar (Logging, Throttling)
├── states/             # FSM holatlari
├── utils/              # Foydali yordamchi funksiyalar
├── main.py             # Asosiy fayl – botni ishga tushiradi
├── config.py           # Configlar (token, db, va h.k.)
├── requirements.txt    # Kerakli kutubxonalar
└── README.md           # Loyihaning tavsifi
```
🚀 Ishga tushirish
Repository'ni klonlang:
```bash
git clone https://github.com/Xusanbek0039/aiogram-bot-template.git
cd aiogram-bot-template
```
Virtual muhit yarating va faollashtiring:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```
Talablar (kutubxonalar)ni o‘rnating:

```bash
pip install -r requirements.txt
```
.env yoki config.py faylida token va sozlamalarni kiriting

Botni ishga tushiring:
```bash
python main.py
```
🛠 Texnologiyalar
Python 3.10+

Aiogram 2.x – Asinxron Telegram bot framework

Logging – Konsolga log chiqarish

FSM (Finite State Machine) – Foydalanuvchi holatlarini boshqarish

Middleware – So‘rovlar orasida maxsus qatlamlar

💡 Foydali
Aiogram rasmiy hujjatlari

BotFather – Telegram bot yaratish

Python Telegram Bot kursi (UZ) – Darslar

👨‍💻 Muallif
Xusanbek
GitHub: @Xusanbek0039

