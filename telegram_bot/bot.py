from telegram import Bot, LabeledPrice, Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext
from products.models import Product
from accounts.models import Profile


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

def start(update: Update, context: CallbackContext):
    keyboard = [
        InlineKeyboardButton("Confirm Your Account", callback_data="account_set")
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Please visit your profile dashboard Sunrise Mart to collect your Telegram Token and Click on the button below to confirm your account with our telegram bot", reply_markup=reply_markup)

def button(update: Update, context: CallbackContext ) :
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=f"No Enter Your Telegram Token From Sunrise Mart Dashboard in this format /token YOUR_TELEGRAM_TOKEN")


def token_verify(update: Update, context: CallbackContext) :
    args = context.args
    chat_id = update.message.chat_id

    if args:
        telegram_token = ''.join(args)
        user        = Profile.objects.get(telegram_token=telegram_token)

        if user :
            user.chat_id = chat_id
            user.save()
            keyboard = [
                InlineKeyboardButton("Check Account", callback_data="check_account"),
                InlineKeyboardButton("Topup Account", callback_data="topup_account"),
                InlineKeyboardButton("Check Orders", callback_data="check_orders"),
                InlineKeyboardButton("Check Profile", callback_data="check_profile")
            ]

            reply_markup = InlineKeyboardMarkup(keyboard)
            update.message.reply_text("User Succesfully Verified. You can now start making transaction on the web site", reply_markup=reply_markup)
        else :
            update.message.reply_text("User Token Invalid, Please Check and Try again")


#https://t.me/henrylebokubot?start=agrs

def main() :

    updater = Updater(bot=bot)
    updater.dispatcher.add_handler(
        CommandHandler("start", start)
    )
    updater.dispatcher.add_handler(
        CommandHandler("token", token_verify)
    )

