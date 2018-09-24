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
base_url = 'https://en.wikipedia.org'
maxno_of_urls_crawl =1000
max_depth = 6
dfs_crawl_links = []


def parse_webpage(url,max_depth,max_url_count,politeness_factor):
    print("Grabbing url " + " @" + str(time.time()) + " @Height " + str(max_depth) + " on " + url)
    dfs_crawl_links.append(url)
    read_content = requests.get(url)
    content = BeautifulSoup(read_content.content, "html.parser")
    links = content.find("div", {"id": "bodyContent"}).find_all('a', href=pattern)
    for link in links:
        cl = (str(link.get("href")))
        if ":" not in cl:
            if '#' in cl:
                cl = cl[: cl.index('#')]
            cl_url = urljoin(base_url, cl)
            if cl_url not in dfs_crawl_links and len(dfs_crawl_links) < max_url_count and max_depth >=2:
                time.sleep(politeness_factor)
                parse_webpage(cl_url, max_depth-1, max_url_count,politeness_factor)

def DFS_Crawl(url,max_depth,max_url_count,politeness_factor):
    project_dir_name = "DFSCrawler/"
    urls_file = project_dir_name + "DFSUrls.txt"
    parse_webpage(url,max_depth,max_url_count,politeness_factor)
    #print(len(dfs_crawl_links))
    delete_directory(project_dir_name)
    create_project_dir(project_dir_name)
    create_file(urls_file)
    append_to_file(urls_file, str(dfs_crawl_links).replace("', '", '\n').replace("['", '').replace("']", ''))


DFS_Crawl(seed_url,6,1000,1)