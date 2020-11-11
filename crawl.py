from bs4 import BeautifulSoup
import requests

def crawling(website_link, link_class):
  
    
    # get content of website and parse it
    website_request = requests.get('https://ktu.edu.in/eu/core/announcements.htm', timeout=5)
    website_content = BeautifulSoup(website_request.content, 'html.parser')
    
    # extract job description
    jobs_link = website_content.find_all(class_ = 'b')
    return jobs_link
