import schedule

# bot and chat ids
bot = 1164343404:AAFWtA6VxjsG6OUNLhEnO9GPpvvNLX-k0Rk
chat_id = gecupdatesBot

# schedule crawler
schedule.every().day.at("21:12").do(check_result_send_mess)

# run script infinitely
while True:
    schedule.run_pending()
