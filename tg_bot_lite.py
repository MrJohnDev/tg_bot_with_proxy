import telebot,sys
bot = telebot.TeleBot('bot token')

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.send_message(message.chat.id,message.text)
	
proxies=[line.rstrip('\n') for line in open('proxies.txt')]
proxy=proxies[0]
while True:
	try:
		telebot.apihelper.proxy = {'https':proxy,'http':proxy}
		bot.polling()
		sys.exit()
	except Exception as e:
		print(e)
		index = proxies.index(proxy)
		proxy = proxies[0] if (index+1>=len(proxies)) else proxies[index+1]