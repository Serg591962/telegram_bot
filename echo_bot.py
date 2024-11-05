from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext

# Вставьте ваш API-токен
TOKEN = '7640982348:AAFPuxfOqdAP3KuIQS9UVs4cPXUAGXoA2BY'

# Функция для обработки входящих сообщений
def echo(update: Update, context: CallbackContext) -> None:
    # Бот отвечает тем же текстом, который получил от пользователя
    update.message.reply_text(update.message.text)

def main():
    # Создаем Updater и передаем API-токен
    updater = Updater(TOKEN)

    # Получаем диспетчер для регистрации обработчиков
    dispatcher = updater.dispatcher

    # Обработчик для текстовых сообщений (эхо-ответ)
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Запуск бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()


