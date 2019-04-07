import telepot
class TelegramAPI(object):
    def __init__(self,token = "894536994:AAE87i36ZAi45quKlr9p55Fp-XGyC4PfTxw",group_chat = "-391286369"):
        self.token = token
        self.bot = telepot.Bot(token)
        self.group_chat = group_chat
    def sendTelegramMessage(self, message):
        try:
            self.bot.sendMessage(self.group_chat,message)
            return "Telegram API successfully sent"
        except:
            return "Telegram API failed to send message"
if __name__ == "__main__":
    TeleBot = TelegramAPI()
    msg = "Bye World"
    print(TeleBot.sendTelegramMessage(msg))
