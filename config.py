from telebot import types
alifbas = ['А','Ә','Б','В','Г','Д','Е','Ё','Ж','Җ','З','И','Й','К','Л','М','Н','Ң','О','Ө','П','Р','С','Т','У','Ү','Ф','Х','Һ','Ц','Ч','Ш','Щ','Ъ','Ы','Ь','Э','Ю','Я']
b1 = types.InlineKeyboardButton(text="⬜", callback_data="1")
b2 = types.InlineKeyboardButton(text="⬜", callback_data="2")
b3 = types.InlineKeyboardButton(text="⬜", callback_data="3")
b4 = types.InlineKeyboardButton(text="⬜", callback_data="4")
b5 = types.InlineKeyboardButton(text="⬜", callback_data="5")
b6 = types.InlineKeyboardButton(text="✅", callback_data="16")
letters = ["⬜", "⬜","⬜","⬜","⬜","✅" ]
usr = '5280120471:AAGBHIfqpnPjhl79GUv19v272s1_MGHBho0'
today = 'тавыш'
rows = 1
word = ''
open = False
pos = 0
gamekey = ''
btns = [b1, b2, b3, b4, b5, b6,]
def array(change='', txt='', callback=''):
    print('change:', change, 'txt:', txt, 'callb:', callback)
    keyboard = types.InlineKeyboardMarkup(row_width=6)
    if change != '':
        ind = change - (change // 6) * 6
        btns[change] = types.InlineKeyboardButton(text=txt, callback_data=str(callback))
        print(ind)
        if ind!=4:
            if letters[ind+1] == "⬜":
                btns[change+1] = types.InlineKeyboardButton(text='_', callback_data=str(callback+1))
        letters[ind] = txt
    keyboard.row(*btns)
    return(keyboard, btns)


def showres(linenum, res, correct):
    print(linenum, 'line:;')
    keyboard = types.InlineKeyboardMarkup(row_width=6)
    start = (linenum-1)*6
    for i in range(start, start+5):
        print(i)
        btns[i] = types.InlineKeyboardButton(text=res[i-start], callback_data='x')
    if linenum != 5:
        ls = ["⬜", "⬜", "⬜", "⬜", "⬜", "✅"]
        for j in range(5):
            if str(j) in correct.keys():
                ls[j] = correct[str(j)]
                btns.append(types.InlineKeyboardButton(text=correct[str(j)], callback_data=str(linenum+1)+str(j+1)))
            else:
                btns.append(types.InlineKeyboardButton(text="⬜", callback_data=str(linenum + 1) + str(j + 1)))
        btns.append(types.InlineKeyboardButton(text="✅", callback_data=str(linenum+1)+"6"))
    keyboard.add(*btns)
    return(keyboard, btns, ls)

def alifba():
    keyboard1 = types.InlineKeyboardMarkup(row_width=6)
    s = []
    keyboard1.add(*btns)
    for i in alifbas:
        s.append(i)
        s.append(types.InlineKeyboardButton(text=i, callback_data=i))
        if len(s) == 8:
            keyboard1.row(*s)
            s = []
    keyboard1.row(*s)
    return keyboard1

alifba()