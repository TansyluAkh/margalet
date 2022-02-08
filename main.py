import telebot, db as dbcreator, config
bot = telebot.TeleBot('5280120471:AAGBHIfqpnPjhl79GUv19v272s1_MGHBho0', threaded=False)
initmarkup =  config.array(change='')[0]
def convert(txt):
    if len(txt) >1:
        i, x = int(txt[0]), int(txt[1])
        return(4*(i-1) +x)
    else:
        return(int(txt)-1)
@bot.message_handler(commands=['start'])
def start(m):
    name = m.from_user.first_name
    bot.send_message(m.chat.id, 'kelimelle', reply_markup = initmarkup)
    bot.send_message(m.chat.id, 'Enter the letters')
    config.gamekey = config.btns

@bot.message_handler(content_types=['text'])
def save(m):
    config.word = m.text
    return
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        print(call.message)
        print(call.data, call.message.chat.id,' call.data')
        if call.data.isdigit():
            if int(call.data) in [1, 2, 3, 4, 5, 21, 22, 23, 24, 25, 31, 32, 33, 34, 35,41, 42, 43, 44, 45, 51, 52, 53, 54, 55,]:
                config.pos = convert(call.data)
                bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=config.alifba())
                print('o')
            elif int(call.data) in [16, 26, 36, 46, 56]:
                btn = (int(call.data[0])-1)*6
                print(config.word)
                arr = [i for i in config.word]
                newkey = config.array(btn, arr, call.data)
                bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup = newkey)
                print('k')
        else:
            if call.data in config.alifbas:
                newkey = config.array(config.pos, call.data, 'f')
                config.gamekey = newkey[1]
                bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=config.alifba())


        return


if __name__ == '__main__':
    bot.polling(none_stop=True)
