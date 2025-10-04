import telebot
import schedule
import json
import datetime
import time 

# Token dari BotFather
TOKEN = "8391829918:AAF-ToRPCPeYmuPoC5NVEs2eI8cSvJifOUc"
bot = telebot.TeleBot(TOKEN)
CHAT_ID = "@satuharisatuhaditss"

with open("listHadits.json","r", encoding="utf-8") as f:
        hadist_list = json.load(f)

def kirim_hadits():
    start_date = datetime.date(2025, 10, 2)
    today = datetime.date.today()  
    day_index = (today - start_date).days % len(hadist_list)
    h = hadist_list[day_index]

    pesan = f"""
    Hadits Hari ke-{day_index+1}

{h['arab']}

**🌍Artinya:**
"{h['arti']}"
({h['periwayat']})

**📝Hikmah yang bisa kita ambil :**
{h['hikmah']}

**✅Maka dari itu kita bisa melakukan:**
{h['implementasi']}
"""
    bot.send_message(CHAT_ID, pesan, parse_mode="Markdown")
    print("Pesan Terkirim")

# Atur jadwal → setiap hari jam 09:00
schedule.every().day.at("21:57").do(kirim_hadits)
print("⏳ Bot berjalan... menunggu jadwal")

while True:
    schedule.run_pending()
    time.sleep(1)
