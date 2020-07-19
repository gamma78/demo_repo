from telegram.ext import Updater,CommandHandler,MessageHandler,Filters
from telegram import bot,chatmember,user,chat

token='1335423594:AAFzt0lVelW75xHaa9az8BAxJe4OPztsNCQ'
up = Updater(token,use_context=True)
dispatcher = up.dispatcher

def echo(update,context):
    context.bot.send_message(chat_id=update.message.chat_id, text=update.message.text,
                                 reply_to_message_id=update.message.message_id)



def isLink(update , context):
    if update.message.text[:8] == 'https://' or update.message.text[:8] == 'http://':
            context.bot.delete_message(chat_id=update.message.chat_id,message_id=update.message.message_id)

def sendStickers(update,context):
    context.bot.send_sticker(chat_id=update.message.chat_id, sticker=update.effective_message.sticker.file_id)


def setTitle(update,context):
    context.bot.send_message(chat_id=update.message.chat_id,text='/setTitle <your name>',reply_to_message_id=update.message.message_id)
    context.bot.setChatTitle(chat_id=update.message.chat_id, title=context.args[0])




#def for is it link or not
dispatcher.add_handler(MessageHandler(Filters.text,echo))
#echo bot for set forward message to you
dispatcher.add_handler(MessageHandler(filters=Filters.sticker,callback=sendStickers))
#def for send sticker as same as you :l
dispatcher.add_handler(MessageHandler(filters=Filters.text,callback=isLink))

#bot command for set chat title
dispatcher.add_handler(CommandHandler('setTitle',setTitle,
                                      pass_args=True,
                                      pass_user_data=True))


up.start_polling()
up.idle()
