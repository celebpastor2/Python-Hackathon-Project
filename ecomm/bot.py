from telegram import Bot, LabeledPrice, Update
from telegram.ext import Updater, CommandHandler, MessageHandler
from products.models import Product

BOT_TOKEN = ""
PAYMENT_PROVIDER_TOKEN="1877036958:TEST:633b01e07ed390023c478bc06324abc099aa0c5f"

bot= Bot(token=BOT_TOKEN)


title = "Premium Product"
description="Access Premium Services"
payload="transactionID"
currency="USD"
prices = [LabeledPrice(label=title, amount=500)]
user_chat_id = ""


bot.send_invoice(chat_id=user_chat_id,title=title, description=description,payload=payload,provider_token=PAYMENT_PROVIDER_TOKEN, currency=currency,prices=prices, start_parameter="Buy Now")

def start(update, context):
    args = context.args

    if args and args[0].startwith("pay_") :
        product_id = args[0][:4]
        product = Product.objects.get(id=product_id)

        if product : 
            title = product.product_name
            description = product.product_desription
            payload = product.uid
            currency="USD"
            prices = [LabeledPrice(label=title, amount=product.price)]
            chat_id = update.message.chat_id
            bot.send_invoice(chat_id=chat_id,title=title, description=description,payload=payload,provider_token=PAYMENT_PROVIDER_TOKEN, currency=currency,prices=prices, start_parameter="Buy Now")


#https://t.me/henrylebokubot?start=agrs

updater = Updater(bot=bot)
updater.dispatcher.add_handler(
    CommandHandler("start", start)
)

