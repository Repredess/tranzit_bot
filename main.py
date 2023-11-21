import telebot

import CONFIG


def main():
    tranzit_bot = telebot.TeleBot(CONFIG.BOT_API)

    @tranzit_bot.message_handler(message.text == 'start')
    def start(message):
        tranzit_bot.send_message(message.chat.id, f'Hello, <b><i>{message.from_user.first_name}</i></b>',
                                 parse_mode='html')

    tranzit_bot.infinity_polling()


if __name__ == '__main__':
    main()
