import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urlparse
from urllib.parse import urljoin
import time
import datetime
from generate_files import *


seed_url = 'https://en.wikipedia.org/wiki/Solar_eclipse'
pattern = re.compile('^/wiki/')
crawled_links = []
link_details = []
base_url = 'https://en.wikipedia.org'
maxno_of_urls_crawl =1000
max_depth = 6
keywords = ['moon','lunar']

def parse_webpage(url,cur_depth,max_depth,max_url_count):
    read_content = requests.get(url)
    content = BeautifulSoup(read_content.content, "html.parser")
    links = content.find("div", {"id": "bodyContent"}).find_all('a', href=pattern)
    child_url_depth = cur_depth + 1
    if cur_depth < max_depth:
        for link in links:
            cl = (str(link.get("href")))
            if ":" not in cl:
                if '#' in cl:
                    cl = cl[: cl.index('#')]
                cl_url = urljoin(base_url, cl)
                #print("cl_url " + cl_url)
                #print(cl_url == link[0] for link in link_details)
                if not any(cl_url == link[0] for link in link_details):
                    link_details.append([cl_url,child_url_depth])
                    match_pattern(cl_url, link,max_url_count)

def match_pattern(url,link,max_url_count):
    text = str(link.text.encode("utf-8"))
    for k in keywords:
        if re.search(r'.*{0}.*'.format(k), url, re.IGNORECASE) or re.search(r'.*{0}.*'.format(k), text,re.IGNORECASE):
            if url not in crawled_links and len(crawled_links) < max_url_count :
                crawled_links.append(url)
            break


def bfs_crawl(url,max_depth,max_url_count,politeness_factor):
    link_details.append([url, 1])
    count = 0
    for link in link_details:
        count = + 1
        print("Grabbing url " + str(count) + " @" + str(time.time()) + " " + " @Depth: " + str(link[1]) + " on " + link[
            0])
        parse_webpage(link[0], link[1], max_depth,max_url_count)
        time.sleep(politeness_factor)
        politeness_factor = +count
        if len(crawled_links) >= max_url_count:
            break
    print(len(crawled_links))
    #print(len(link_details))
    print(crawled_links)

def start():
    max_depth_reached = 0
    project_dir_name = "BFSFocusedCrawler/"
    urls_file =project_dir_name+ "BFSFocusedUrls.txt"
    bfs_crawl(seed_url, max_depth, maxno_of_urls_crawl, 1)
    delete_directory(project_dir_name)
    create_project_dir(project_dir_name)
    create_file(urls_file)
    append_to_file(urls_file,str(crawled_links).replace("', '",'\n').replace("['",'').replace("']",''))

    print("Maximum Depth reached " + str(link_details[-1][1]))


start()


