import telebot, db as dbcreator, config
bot = telebot.TeleBot('5280120471:AAGBHIfqpnPjhl79GUv19v272s1_MGHBho0', threaded=False)
initmarkup =  config.array(change='')[0]
def convert(txt):
    if len(txt) >1:
        i, x = int(txt[0]), int(txt[1])
        return(6*(i-1) +(x-1))
    else:
        return(int(txt)-1)
@bot.message_handler(commands=['start'])
def start(m):
    bot.send_message(m.chat.id, 'Нажмите на серую ячейку, чтобы ввести букву', reply_markup = initmarkup)
    config.gamekey = [config.b1, config.b2, config.b3, config.b4, config.b5, config.b6]

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
            if int(call.data) in [2, 3, 4, 5,  22, 23, 24, 25, 32, 33, 34, 35,42, 43, 44, 45, 52, 53, 54, 55,1,21, 31, 41, 51]:
                if config.open == False:
                    config.pos = convert(call.data)
                    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id,
                                                  reply_markup=config.alifba())
                    config.open = True
                config.pos = convert(call.data)

            elif call.data in ['16', '26', '36', '46', '56']:
                res, correct = [], {}
                flag = True
                for l in range(5):
                    if config.letters[l].lower() == config.today[l]:
                       res.append(config.letters[l]+'🟩')
                       correct[str(l)] = config.letters[l]
                    else:
                        flag = False
                        if config.letters[l].lower() in config.today:
                            res.append(config.letters[l]+'🟨')
                        else:
                            res.append(config.letters[l]+'⬛')
                if flag:
                    bot.send_message(call.message.chat.id, 'Вы отгадали слово дня: '+'\n'+config.today)
                else:
                    config.open = False
                    config.pos = convert(str(int(call.data[0])+1)+'1')
                    print(config.pos, 'POS')
                    config.rows += 1
                    reset = config.showres(int(call.data[0]), res, correct)
                    config.gamekey = reset[1]
                    config.letters = reset[2]
                    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id,
                                                  reply_markup=reset[0])
                    print(config.letters)
        if call.data in config.alifbas:
            newkey = config.array(config.pos, call.data, config.pos+1)
            config.gamekey = newkey[1]
            ind = config.pos - (config.pos // 6) * 6
            if ind!=4:
                config.pos += 1
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=config.alifba())

        return


if __name__ == '__main__':
    bot.polling(none_stop=True)