from pyrogram import Client
from pyrogram.types import ChatJoinRequest

# Твои данные (вставил напрямую для простоты)
API_ID = 35652667
API_HASH = "bb4d2b2700dbe396e57c14042c60db34"
BOT_TOKEN = "8343818784:AAG_8HL6W5ON83EPWvvEtUP-API1VScgPVw"

# Создаем клиента бота
app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_chat_join_request()
async def approve_request(client, chat_join_request: ChatJoinRequest):
    # Автоматически одобряем заявку
    await client.approve_chat_join_request(
        chat_id=chat_join_request.chat.id,
        user_id=chat_join_request.from_user.id
    )
    print(f"Заявка принята от: {chat_join_request.from_user.first_name}")

if __name__ == "__main__":
    print("Бот запущен!")
    app.run()
  
