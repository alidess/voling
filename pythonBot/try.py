# -*- coding: UTF-8 -*-
import requests
import datetime
import time
import random

r = requests


class BotHandler:
    def __init__(self, token):
            self.token = token
            self.api_url = "https://api.telegram.org/bot{}/".format(token)

    # url = "https://api.telegram.org/bot<token>/"

    def get_updates(self, offset=0, timeout=30):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params)
        resp.encoding = "utf-8"
        result_json = resp.json()['result']
        return result_json

    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text, 'parse_mode': 'HTML'}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        return resp

    def get_first_update(self):
        get_result = self.get_updates()

        if len(get_result) > 0:
            last_update = get_result[0]
        else:
            last_update = None

        return last_update


token = '608531605:AAGYRjdlkGB2-zVXfn_wod7GddGlsmsCYfA'
bot = BotHandler(token)


def main():
    new_offset = 0
    print('hi, now launching...')

    def msg_lover(n):
        time.sleep(240)
        fi = open("lovers.txt", "r", encoding="utf-8")
        x = bytes(fi.read(), "utf").decode("utf-8").split("\n")
        fi.close()
        bot.send_message(431779236, random.choice(x))
        bot.send_message(562206666, "Done")
        n += 1
        print(str(n) + "n")
    while True:

        all_updates = bot.get_updates(new_offset)
        print(new_offset)

        if len(all_updates) > 0:
            try:
                for current_update in all_updates:
                    print(current_update)
                    try:
                        first_update_id = current_update['update_id']
                    except:
                        print(False)
                    if 'text' not in current_update['message']:
                        first_chat_text = "al"
                        new_offset = first_update_id + 1
                    else:
                        first_chat_text = current_update['message']['text']
                    first_chat_id = current_update['message']['chat']['id']
                    if 'first_name' in current_update['message']:
                        first_chat_name = current_update['message']['chat']['first_name']
                    elif 'new_chat_member' in current_update['message']:
                        first_chat_name = current_update['message']['new_chat_member']['username']
                    elif 'from' in current_update['message']:
                        first_chat_name = current_update['message']['from']['first_name']
                    else:
                        first_chat_name = "unknown"

                    username = current_update['message']['from']['username']
                    message_sticker = current_update['message']['sticker']

                    if first_chat_text:
                        if first_chat_id == 431779236:
                            bot.send_message(first_chat_id, "شتاقيتي ل علي 😉 ترى هوه هم مشتاقلججج 😍🙈")
                            bot.send_message(562206666, first_chat_text + "\n" + username)
                            new_offset = first_update_id + 1
                        elif first_chat_id == 5622066662: # 2
                            f = open("lovers.txt", "a", encoding="utf-8")
                            word = first_chat_text  # .encode("utf-16le")
                            f.write(str(word) + "\n")
                            f.close()
                            bot.send_message(562206666, "okay")
                            new_offset = first_update_id + 1
                        else:
                            if 'sticker' in current_update['message']:
                                print("yes")
                            bot.send_message(562206666, first_chat_text + "\n@" + username)
                            new_offset = first_update_id + 1

                    elif message_sticker:
                        bot.send_message(562206666, "wow")
                        new_offset = first_update_id + 1
                    else:
                        bot.send_message(first_chat_id, 'How are you doing ' + username)
                        new_offset = first_update_id + 1
            except:
                print(False)
                new_offset = first_update_id + 1
        #msg_lover(new_offset)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
