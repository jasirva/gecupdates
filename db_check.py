import os
import psycopg2
import sqlite3 as lite

def check_result_send_mess():
    '''
    This function looks up the values stored in the SQL database
    and compares them to the crawled jobs and sends out any jobs
    not in the db to the telegram bot
    Args: None
    Returns: None
    '''
    
    # try to create SQL database and table to store jobs in, else send error message to bot
    try:
       DATABASE_URL = os.environ['DATABASE_URL']
       conn = psycopg2.connect(DATABASE_URL, sslmode='require')
       jobs_db = conn.cursor()
       jobs_db.execute('CREATE TABLE IF NOT EXISTS jobs (id SERIAL, job TEXT NOT NULL)')
    except:
       send_message(chat_id, 'The database could not be accessed')
        
    # crawl the jobs from website
    jobs_link_pm = crawling('https://ktu.edu.in/eu/core/announcements.htm','b')
    
    # check if there were new jobs added
    for item in jobs_link_pm:
        job_exists = jobs_db.execute('SELECT job FROM jobs WHERE job = %s', [item.text])
        
        if len(jobs_db.fetchall()) != 1:
            mess_content = item.text + item['href']
            send_message(chat_id, mess_content)
            jobs_db.execute('INSERT INTO jobs (job) VALUES (%s);', [item.text])
            conn.commit()
        else:
            continue
            
    # end SQL connection
    jobs_db.close()
