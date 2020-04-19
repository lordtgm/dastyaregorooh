import telebot
API_TOKEN = '1166168665:AAF8lL1Da2DUL1EUKItjQU41qsWl_Ku1l7c'
bot = telebot.TeleBot(API_TOKEN)
l=[]
for i in range(20):
    l+=[[i,'']]
chat=None
@bot.message_handler(commands=['activate'])
def activate(message):
    global chat,l
    chat=message.chat.id
    txt=''
    for i in l:
        txt+=i[0]+' '+i[1]+'\n'
    txt=txt[-1]
    print(bot.reply_to(message,txt),1)
bot.polling()
