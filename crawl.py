from bs4 import BeautifulSoup
import requests

def crawling(website_link, link_class):
    '''
    Args: website_link = string; link of website to be crawled
          link_class = string; class name for job link on website
    Returns: jobs_link = list; list of jobs 
    '''
    
    # get content of website and parse it
    website_request = requests.get('https://ktu.edu.in/eu/core/announcements.htm', timeout=5)
    website_content = BeautifulSoup(website_request.content, 'html.parser')
    
    # extract job description
    jobs_link = website_content.find_all(class_ = 'b')
    return jobs_link
