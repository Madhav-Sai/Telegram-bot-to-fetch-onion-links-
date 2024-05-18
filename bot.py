import requests
import re
import random
import telebot

BOT_TOKEN = 'TELEGRAM-API-TOKEN-HERE'# TOKEN
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Hello! Use /darkweb to search for information on the dark web.")

@bot.message_handler(commands=['darkweb', 'getonions'])
def send_welcome(message):
    bot.reply_to(message, "[+] Getting Links")
    data = message.text
    newdata = data.replace('/darkweb ', '')
    bot.reply_to(message, scrape(newdata))
    bot.reply_to(message, "You need TOR to access .onion links")

def scrape(newdata):
    yourquery = newdata

    if " " in yourquery:
        yourquery = yourquery.replace(" ", "+")
    url = "https://ahmia.fi/search/?q={}".format(yourquery)
    request = requests.get(url)
    content = request.text

    regexquery = r"\w+\.onion"

    minedata = re.findall(regexquery, content)

    n = random.randint(1, 9999)
    filename = "sites{}.txt".format(str(n))
    print("Saving to ....", filename)

    minedata = list(dict.fromkeys(minedata))

    with open(filename, "w+") as _:
        print("")
    for k in minedata:
        with open(filename, "a") as newfile:
            k = k + "\n"
            newfile.write(k)
    print("All the files written to text file : ", filename)

    with open(filename) as input_file:
        head = [next(input_file) for _ in range(11)]
        contents = '\n'.join(map(str, head))

    return contents

bot.infinity_polling()
