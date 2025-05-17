from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
PAYER_TOKEN = "1877036958:TEST:633b01e07ed390023c478bc06324abc099aa0c5f"



async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


async def message(update: Update, context: ContextTypes.DEFAULT_TYPE ) :
    PRICES = [{
        "label": "Medicated Soap",
        "amount": 2000,
        "sale_amount": 1500
    }]
    CURRENCY = "NGN"
    pay_load = "unique_string"
    title = "Dettol Medicated Soap"
    description="This is a good soap for the body"
    context.bot.sendInvoice(update.message.chat_id, title, description, payload=pay_load, provider_token=PAYER_TOKEN, currency=CURRENCY, prices=PRICES )


app = ApplicationBuilder().token("YOUR TOKEN HERE").build()

app.add_handler(CommandHandler("start", hello))

app.run_polling()