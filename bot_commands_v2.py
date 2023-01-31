from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
import datetime
import random


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'''Команды бота:
/hello - давай поздароваемся :)
/time - узнать точное Московское время
/date - узнать сегодняшюю дату
/ny - узнать сколько осталось дней до Нового года!
/sum x y - посчитать сумму двух чисел
/english - узнать новое английское слово
''')


async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Hello, {update.effective_user.first_name}!')


async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Точное время - {datetime.datetime.now().time().replace(microsecond=0)}')


async def date_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    date = datetime.date.today()
    await update.message.reply_text(f'Сегодня - {date.day}.{date.month}.{date.year}')


async def ny_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    ny_2024 = datetime.date(2024, 1, 1)
    current_day = datetime.date.today()
    await update.message.reply_text(f'До Нового 2024 года осталось {(current_day - ny_2024).days} дней(я)')


async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'sum {x} + {y} = {x + y}')


async def eng_learn_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    with open('Eng.txt', 'r', encoding = 'utf8') as data:
        line = data.readlines()
        word = line[random.randrange(0, 30601, 2)]         
        await update.message.reply_text(f'Новое слово для тебя:\n{word}')