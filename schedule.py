import schedule

# bot and chat ids
bot = <your bot API>
chat_id = <your chat id>

# schedule crawler
schedule.every().day.at("08:00").do(check_result_send_mess)

# run script infinitely
while True:
    schedule.run_pending()
