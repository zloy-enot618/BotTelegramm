import telebot
from telebot.types import ReactionTypeEmoji
import random
from bot_logic import gen_pass, gen_emoji, coin_flip
    # Замени 'TOKEN' на токен твоего бота
    # Этот токен ты получаешь от BotFather, чтобы бот мог работать
bot = telebot.TeleBot("********************************************")
    
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь!")
    
@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")
    
@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")
    
@bot.message_handler(commands=['genpas'])
def generpas(message):
    generpas = gen_pass(10)
    bot.reply_to(message, generpas)

@bot.message_handler(commands=['genemoji'])
def gen_emoj(message):
    emodji = gen_emoji()
    bot.reply_to(message, f"Вот твой эмоджи: {emodji}")

@bot.message_handler(commands=['coinflip'])
def moneta(message):
    flip = coin_flip()
    bot.reply_to(message, f"Выпало: {flip}")

# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
#     bot.reply_to(message, message.text)

@bot.message_handler(func=lambda message: True)
def send_reaction(message):
    emo = ["\U0001F525", "\U0001F917", "\U0001F60E"]  # or use ["🔥", "🤗", "😎"]
    bot.set_message_reaction(message.chat.id, message.id, [ReactionTypeEmoji(random.choice(emo))], is_big=False)
bot.polling()
