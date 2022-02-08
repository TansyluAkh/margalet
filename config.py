from telebot import types
alifbas = ['А','Ә','Б','В','Г','Д','Е','Ё','Ж','Җ','З','И','Й','К','Л','М','Н','Ң','О','Ө','П','Р','С','Т','У','Ү','Ф','Х','Һ','Ц','Ч','Ш','Щ','Ъ','Ы','Ь','Э','Ю','Я']
b1 = types.InlineKeyboardButton(text="⬜", callback_data="1")
b2 = types.InlineKeyboardButton(text="⬜", callback_data="2")
b3 = types.InlineKeyboardButton(text="⬜", callback_data="3")
b4 = types.InlineKeyboardButton(text="⬜", callback_data="4")
b5 = types.InlineKeyboardButton(text="⬜", callback_data="5")
b6 = types.InlineKeyboardButton(text="enter", callback_data="16")
b21 = types.InlineKeyboardButton(text="⬜", callback_data="21")
b22 = types.InlineKeyboardButton(text="⬜", callback_data="22")
b23 = types.InlineKeyboardButton(text="⬜", callback_data="23")
b24 = types.InlineKeyboardButton(text="⬜", callback_data="24")
b25 = types.InlineKeyboardButton(text="⬜", callback_data="25")
b26 = types.InlineKeyboardButton(text="enter", callback_data="26")
b31 = types.InlineKeyboardButton(text="⬜", callback_data="31")
b32 = types.InlineKeyboardButton(text="⬜", callback_data="32")
b33 = types.InlineKeyboardButton(text="⬜", callback_data="33")
b34 = types.InlineKeyboardButton(text="⬜", callback_data="34")
b35 = types.InlineKeyboardButton(text="⬜", callback_data="35")
b36 = types.InlineKeyboardButton(text="enter", callback_data="36")
b41 = types.InlineKeyboardButton(text="⬜", callback_data="41")
b42 = types.InlineKeyboardButton(text="⬜", callback_data="42")
b43 = types.InlineKeyboardButton(text="⬜", callback_data="43")
b44 = types.InlineKeyboardButton(text="⬜", callback_data="44")
b45 = types.InlineKeyboardButton(text="⬜", callback_data="45")
b46 = types.InlineKeyboardButton(text="enter", callback_data="46")
b51 = types.InlineKeyboardButton(text="⬜", callback_data="51")
b52 = types.InlineKeyboardButton(text="⬜", callback_data="52")
b53 = types.InlineKeyboardButton(text="⬜", callback_data="53")
b54 = types.InlineKeyboardButton(text="⬜", callback_data="54")
b55 = types.InlineKeyboardButton(text="⬜", callback_data="55")
b56 = types.InlineKeyboardButton(text="enter", callback_data="56")
word = ''
pos = 0
gamekey = ''
btns = [b1, b2, b3, b4, b5, b6, b21, b22, b23, b24, b25, b26, b31, b32, b33, b34, b35, b36, b41, b42, b43, b44, b45, b46, b51, b52,
            b53, b54, b55, b56]
def array(change='', txt='', callback=''):
    keyboard = types.InlineKeyboardMarkup(row_width=6)
    if change != '':
        btns[change] = types.InlineKeyboardButton(text=txt, callback_data=callback)
    keyboard.add(*btns)
    return(keyboard, btns)
def alifba():
    keyboard1 = types.InlineKeyboardMarkup(row_width=8)
    s = []
    for i in alifbas:
        s.append(types.InlineKeyboardButton(text=i, callback_data=i))
    keyboard1.add(*gamekey)
    keyboard1.add(*s)
    return keyboard1
