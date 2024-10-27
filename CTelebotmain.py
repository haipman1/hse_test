import telebot
from telebot import types

import CDatabase
import ebaniy_test

bot = telebot.TeleBot('5389806380:AAEIjAV6ndIqu-ZND2024HmQK67tQP2XIQQ')


def telebotmain():
    def get_text(message):
        name = message.text
        bot.send_message(message.chat.id, name)

    @bot.callback_query_handler(func=lambda call: True)
    def callback_worker(call):
        cd = CDatabase
        if call.data == "btc_add_on_check":
            bot.send_message(call.message.chat.id, 'Select price trigger[BTC]')
            bot.register_next_step_handler(call.message, cd.add_trigger, "BTC", call.message.chat.id)
            ###PROVERKA EBANAYA #4
            data = cd.get_all_user_data(call.message.chat.id)
            if list(data)[0][2] != 0:
                print('Проверил, работает #4')
            else:
                print('Проверил, не работает #4')



        elif call.data == "ltc_add_on_check":
            bot.send_message(call.message.chat.id, 'Select price trigger[LTC]')
            bot.register_next_step_handler(call.message, cd.add_trigger, "LTC", call.message.chat.id)

            ###PROVERKA EBANAYA #5
            data = cd.get_all_user_data(call.message.chat.id)
            if list(data)[0][3] != 0:
                print('Проверил, работает #5')
            else:
                print('Проверил, не работает #5')

        elif call.data == "eth_add_on_check":
            bot.send_message(call.message.chat.id, 'Select price trigger[ETH]')
            bot.register_next_step_handler(call.message, cd.add_trigger, "ETH", call.message.chat.id)

            ###PROVERKA EBANAYA #6
            data = cd.get_all_user_data(call.message.chat.id)
            if list(data)[0][4] != 0:
                print('Проверил, работает #6')
            else:
                print('Проверил, не работает #6')
        elif call.data == "sol_add_on_check":
            bot.send_message(call.message.chat.id, 'Select price trigger[SOL]')
            bot.register_next_step_handler(call.message, cd.add_trigger, "SOL", call.message.chat.id)

            ###PROVERKA EBANAYA #7
            data = cd.get_all_user_data(call.message.chat.id)
            if list(data)[0][5] != 0:
                print('Проверил, работает #7')
            else:
                print('Проверил, не работает #7')
        elif call.data == "trx_add_on_check":
            bot.send_message(call.message.chat.id, 'Select price trigger[TRX]')
            bot.register_next_step_handler(call.message, cd.add_trigger, "TRX", call.message.chat.id)

            ###PROVERKA EBANAYA #8
            data = cd.get_all_user_data(call.message.chat.id)
            if list(data)[0][6] != 0:
                print('Проверил, работает #8')
            else:
                print('Проверил, не работает #8')
        elif call.data == "xrp_add_on_check":
            bot.send_message(call.message.chat.id, 'Select price trigger[XRP]')
            bot.register_next_step_handler(call.message, cd.add_trigger, "XRP", call.message.chat.id)

            ###PROVERKA EBANAYA #9
            data = cd.get_all_user_data(call.message.chat.id)
            if list(data)[0][7] != 0:
                print('Проверил, работает #9')
            else:
                print('Проверил, не работает #9')
        elif call.data == "dot_add_on_check":
            bot.send_message(call.message.chat.id, 'Select price trigger[DOT]')
            bot.register_next_step_handler(call.message, cd.add_trigger, "DOT", call.message.chat.id)

            ###PROVERKA EBANAYA #10
            data = cd.get_all_user_data(call.message.chat.id)
            if list(data)[0][8] != 0:
                print('Проверил, работает #10')
            else:
                print('Проверил, не работает #10')
        elif call.data == "atom_add_on_check":
            bot.send_message(call.message.chat.id, 'Select price trigger[ATOM]')
            bot.register_next_step_handler(call.message, cd.add_trigger, "ATOM", call.message.chat.id)

            ###PROVERKA EBANAYA #11
            data = cd.get_all_user_data(call.message.chat.id)
            if list(data)[0][9] != 0:
                print('Проверил, работает #11')
            else:
                print('Проверил, не работает #11')
        elif call.data == "waves_add_on_check":
            bot.send_message(call.message.chat.id, 'Select price trigger[WAVES]')
            bot.register_next_step_handler(call.message, cd.add_trigger, "WAVES", call.message.chat.id)

            ###PROVERKA EBANAYA #12
            data = cd.get_all_user_data(call.message.chat.id)
            if list(data)[0][10] != 0:
                print('Проверил, работает #12')
            else:
                print('Проверил, не работает #12')

    @bot.message_handler(content_types=['text'])
    def start(message):
        if message.text == '/start':
            isNew = CDatabase.is_new_user(message.from_user.id)
            if isNew:
                #PROVERKA EBANAYA na not exist user
                if ebaniy_test.test_is_new_user(message.from_user.id):
                    print(f'Протестил что нет юзера {message.from_user.id} #00')
                else:
                    print(f'Пиздец ошибка, юзер уже существовал #01')
                # PROVERKA EBANAYA na exist user-----
                bot.send_message(message.from_user.id, "Welcome!")
                CDatabase.reg_new_user(message.from_user.id)
            if not isNew:
                # PROVERKA EBANAYA na exist user
                if ebaniy_test.test_no_user_in_db(message.from_user.id):
                    print(f'Протестил что есть юзер в дб {message.from_user.id} #10')
                else:
                    print(f'Пиздец ошибка, юзер не существовал в дб#11')
                # PROVERKA EBANAYA na exist user-----
                bot.send_message(message.from_user.id, "Hello")




        elif message.text == '/add_trigger' or message.text == '/at':
            crypto_acts = ["BTC", "LTC", "ETH", "SOL", "TRX", "XRP", "DOT", "ATOM", "WAVES"]

            CDatabase.is_new_user_and_reg(message.from_user.id)
            keyboard = types.InlineKeyboardMarkup()
            for i in crypto_acts:
                call_data_text = str.lower(i) + '_add_on_check'
                key_yes = types.InlineKeyboardButton(text=i, callback_data=call_data_text)
                keyboard.add(key_yes)

            bot.send_message(message.from_user.id, "Select trigger", reply_markup=keyboard)
        elif message.text == '/print_all' or message.text == '/pa':
            data = CDatabase.get_all_user_data(message.from_user.id)
            ##PROVERKA EBANAYA #2
            if ebaniy_test.test_get_all_user_data(message.from_user.id) == str(data):
                print(f'Протестил что print_all #20')
            bot.send_message(message.from_user.id, str(data))
        elif message.text == '/reset_all' or message.text == '/ra':
            data1 = CDatabase.get_all_user_data(message.from_user.id)

            CDatabase.reset_all(message.from_user.id)
            data2 = CDatabase.get_all_user_data(message.from_user.id)
            ###PROVERKA EBANAYA #3
            if any(list(data2)[0][x] for x in range(2, 10)) == 0:
                print('Проверил, работает')
        elif message.text[0] == '/':
            print('ep')
            bot.send_message(message.from_user.id, "You can use commands: \n/start\n"
                                                   "/add_trigger\n/print_all\n/reset_all\n")

    bot.polling(none_stop=True, interval=0)