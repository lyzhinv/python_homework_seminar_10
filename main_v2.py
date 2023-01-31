from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands_v2 import *

app = ApplicationBuilder().token("5994530779:AAF1ISLKR1llPXf54B8HLGTSx-kn1u51td4").build()

app.add_handler(CommandHandler("start", start_command))
app.add_handler(CommandHandler("hello", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("date", date_command))
app.add_handler(CommandHandler("ny", ny_command))
app.add_handler(CommandHandler("sum", sum_command))
app.add_handler(CommandHandler("english", eng_learn_command))

print('Bot start')
app.run_polling()