import telebot

TOKEN = "8887157306:AAESFAquUho6VdtxPEEPfXp7o7xFCN7kpOc"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! 👋")

print("Бот запускается...")
bot.infinity_polling()
