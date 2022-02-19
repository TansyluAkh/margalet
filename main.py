import os

import telebot,config, database
from flask import Flask, request

bot = telebot.TeleBot(config.usr, threaded=False)
initmarkup =  config.array(change='')[0]
server = Flask(__name__)


@bot.message_handler(commands=['start'])
def start(m):
    open = False
    gamekey = [config.b1, config.b2, config.b3, config.b4, config.b5, config.b6]
    btns = [config.b1, config.b2, config.b3, config.b4, config.b5, config.b6]
    letters = ["⬜", "⬜","⬜","⬜","⬜","✅" ]
    r1, r2, r3, r4, r5 = letters, letters, letters, letters, letters
    pos = 0
    database.new_user(m.chat.id, letters, open, pos, r1, r2, r3, r4, r5)
    bot.send_message(m.chat.id, 'Нажмите на серую ячейку, чтобы ввести букву', reply_markup=initmarkup)

def convert(txt):
    if len(txt) >1:
        i, x = int(txt[0]), int(txt[1])
        return(6*(i-1) +(x-1))
    else:
        return(int(txt)-1)



@bot.message_handler(content_types=['text'])
def save(m):
    return m


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        info = database.get_user(call.message.chat.id)
        print(info)
        print(call.data, call.message.chat.id,' call.data')
        if call.data.isdigit():
            if int(call.data) in [2, 3, 4, 5,  22, 23, 24, 25, 32, 33, 34, 35,42, 43, 44, 45, 52, 53, 54, 55,1,21, 31, 41, 51]:
                if info.open == False:
                    info.pos = convert(call.data)
                    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id,
                                                  reply_markup=info.alifba())
                    info.open = True
                info.pos = convert(call.data)

            elif call.data in ['16', '26', '36', '46', '56']:
                res, correct = [], {}
                flag = True
                for l in range(5):
                    if info.letters[l].lower() == info.today[l]:
                       res.append(info.letters[l]+'🟩')
                       correct[str(l)] = info.letters[l]
                    else:
                        flag = False
                        if info.letters[l].lower() in info.today:
                            res.append(info.letters[l]+'🟨')
                        else:
                            res.append(info.letters[l]+'⬛')
                if flag:
                    bot.send_message(call.message.chat.id, 'Вы отгадали слово дня: '+'\n'+info.today)
                else:
                    info.open = False
                    info.pos = convert(str(int(call.data[0])+1)+'1')
                    print(info.pos, 'POS')
                    reset = info.showres(int(call.data[0]), res, correct)
                    info.gamekey = reset[1]
                    info.letters = reset[2]
                    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id,
                                                  reply_markup=reset[0])
                    print(info.letters)
        if call.data in info.alifbas:
            newkey = info.array(info.pos, call.data, info.pos+1)
            info.gamekey = newkey[1]
            info.pos = newkey[2]
            ind = info.pos - (info.pos // 6) * 6
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=info.alifba())

        return


@server.route('/' + config.usr, methods=['POST'])
def getMessage():
    print(request)
    update = telebot.types.Update.de_json(request.data.decode('utf-8'))
    bot.process_new_updates([update])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://kelimelle.herokuapp.com/' + config.usr)
    return "!", 200


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))