import telebot
from telebot import types
import time

# --- البيانات الأساسية ---
# التوكن والآيدي الخاصين بك
API_TOKEN = '8330900850:AAFklWqUev9H4PmOUdX9zZUr_5FxW7pjxk8'
ID_ALMODIR = 7165280345 

bot = telebot.TeleBot(API_TOKEN)

# بيانات الخدمات
services_data = {
    "ببجي عالمي 🔫": "60 شدة بـ ...\n325 شدة بـ ...",
    "فري فاير 🔥": "100 جوهرة بـ ...",
    "سهرة شات ✨": "الباقات المتوفرة...",
    "سوجو 💎": "شحن سوجو...",
    "سول شيل 🌀": "شحن سول شيل..."
}

@bot.message_handler(commands=['start'])
def start_menu(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn1 = types.KeyboardButton("🎮 قسم الألعاب")
    btn2 = types.KeyboardButton("📱 تطبيقات الدردشة")
    btn3 = types.KeyboardButton("💰 شحن رصيد")
    
    if message.chat.id == ID_ALMODIR:
        btn_admin = types.KeyboardButton("⚙️ لوحة تحكم المدير")
        markup.add(btn1, btn2, btn3, btn_admin)
    else:
        markup.add(btn1, btn2, btn3)
        
    bot.send_message(message.chat.id, "أهلاً بك في متجر محمد ستور 🛒\nالبوت يعمل الآن من السيرفر بنجاح ✅", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_all(message):
    cid = message.chat.id
    txt = message.text
    
    if txt == "⚙️ لوحة تحكم المدير" and cid == ID_ALMODIR:
        bot.send_message(cid, "أهلاً يا مدير، البوت شغال ومستقر 100%")
    elif txt == "🎮 قسم الألعاب":
        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        markup.add("ببجي عالمي 🔫", "فري فاير 🔥", "🏠 القائمة الرئيسية")
        bot.send_message(cid, "اختر اللعبة:", reply_markup=markup)
    elif txt == "📱 تطبيقات الدردشة":
        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        markup.add("سهرة شات ✨", "سوجو 💎", "سول شيل 🌀", "🏠 القائمة الرئيسية")
        bot.send_message(cid, "اختر التطبيق:", reply_markup=markup)
    elif txt == "🏠 القائمة الرئيسية":
        start_menu(message)
    elif txt in services_data:
        bot.send_message(cid, f"💎 باقات {txt}:\n\n{services_data[txt]}")

# وظيفة تشغيل البوت مع إعادة المحاولة التلقائية
def run_bot():
    try:
        print("🚀 البوت انطلق...")
        bot.infinity_polling(timeout=10, long_polling_timeout=5)
    except Exception as e:
        print(f"خطأ: {e}. إعادة تشغيل خلال 5 ثواني...")
        time.sleep(5)
        run_bot()

if __name__ == "__main__":
    run_bot()
  
