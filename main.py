from config import TOKEN
import telebot


bot = telebot.TeleBot(TOKEN) # создаём экземпляр класса TeleBot c токеном


if __name__ == "__main__": # запуск нашего бота будет происходить только из этого файла
    from functions import bot
    bot.polling(none_stop=True)
