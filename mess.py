from pymessenger.bot import Bot

PAGE_ACCESS_TOKEN = '<PAGE_ACCESS_TOKEN>'
bot = Bot(PAGE_ACCESS_TOKEN)

bot.send_text_message(recipient_id=103972447927048, message='asd')
