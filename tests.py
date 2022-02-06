#bot.send_message(message.chat.id, 'If you know the id of another user, you can find out information about him\n'
                                  #'with the /getinfo command')


#@bot.message_handler(commands=['getinfo'])
#def getinfo(messasge: types.Message):
    #bot.send_message(messasge.chat.id, 'Enter user id in this format: "123456789"')
    #bot.register_next_step_handler(messasge, next)


#def next(message: types.Message):
    #idd = message.text
    #bot.send_message(message.chat.id, idd)