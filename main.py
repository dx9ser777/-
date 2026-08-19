import os
import telebot

# Берем токен из переменной окружения или вставляем напрямую
TOKEN = os.getenv("BOT_TOKEN", "8343818784:AAG_8HL6W5ON83EPWvvEtUP-API1VScgPVw")
bot = telebot.TeleBot(TOKEN)

# Обработка заявок на вступление в канал
@bot.chat_join_request_handler()
funcdef(request):
    try:
        bot.approve_chat_join_request(request.chat.id, request.from_user.id)
        print(f"Заявка одобрена для: {request.from_user.first_name}")
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    print("Бот запущен и слушает заявки...")
    bot.infinity_polling()
    
