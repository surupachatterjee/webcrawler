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
max_allowed_depth = 6
depth = 1
urls_crawled =0
link_details = list()



def parse_webpage(url,max_depth,max_url_count):
    max_depth_reached = 0
    current_url_depth = 0
    read_content = requests.get(url)
    content = BeautifulSoup(read_content.content, "html.parser")
    links = content.find("div", {"id": "bodyContent"}).find_all('a', href=pattern)
    if len(link_details) == 0:
        link_details.append([url, 1, content.prettify()])
    else:
        for l in link_details:
            if url == l[0]:
                current_url_depth = l[1]
                l[2] = content.prettify()

    child_url_depth = current_url_depth + 1
    if child_url_depth <= max_depth and len(crawled_links) < max_url_count:
        for link in links:
            cl = (str(link.get("href")))
            if ":" not in cl:
                if '#' in cl:
                    cl = cl[: cl.index('#')]
                cl_url = urljoin(base_url, cl)
                if cl_url not in crawled_links:
                    crawled_links.append(cl_url)
                    link_details.append([cl_url, child_url_depth, ''])
                    if len(crawled_links) == max_url_count:
                        break


def BFS_Crawl(url,max_depth,max_url_count,politeness_factor):
    crawled_links.append(url)
    print(len(crawled_links))
    for link in crawled_links:
        time.sleep(politeness_factor)
        parse_webpage(link,max_depth,max_url_count)


def start():
    max_depth_reached = 0
    project_dir_name = "BFSCrawler/"
    raw_file_dir = project_dir_name  +"RawHTML/"
    urls_file =project_dir_name+ "BFSUrls.txt"
    BFS_Crawl(seed_url, max_allowed_depth, maxno_of_urls_crawl, 1)
    delete_directory(project_dir_name)
    create_project_dir(project_dir_name)
    create_file(urls_file)
    append_to_file(urls_file,str(crawled_links).replace("', '",'\n').replace("['",'').replace("']",''))
    create_project_dir(raw_file_dir)


    for link in link_details:
        html_filename =raw_file_dir + link[0].replace(',','_').split("/wiki/")[1] + ".txt"
        create_file(html_filename)
        append_to_file(html_filename,str(link[2].encode('UTF-8')))
        if max_depth_reached < link[1]:
            max_depth_reached = link[1]

    print("Max depth reached" + str(max_depth_reached+1))


start()










