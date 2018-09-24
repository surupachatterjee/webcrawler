ASSIGNMENT 1:
Goal:Implementing your own web crawler.Performing focused crawling

==========================================================================================================================================
TASK DESCRIPTION:

TASK1 : 
BFSCrawler:     
		Web crawler designed to crawl a web starting from the seed URL provided as 'https://en.wikipedia.org/wiki/Solar_eclipse'.
		BFSCrawler.py generates the list of 1000 URL's crawled using the BFS searching technique.
		BFS Crawling Technique : Starting from the seed URL ,the URL's at a shallow depth are crawled first 
		and after all URL at a particular depth are crawled,the crawler moves to the next depth.
		The maximum crawls end with the crawler reaching a depth of 6 or URL's crawled reaches 1000(whichever is reached first).
		The list of 1000 URLs crawled are added to a file "BFSUrls.txt"
		
DFSCrawler:
		Web crawler designed to crawl a web starting from the seed URL provided as 'https://en.wikipedia.org/wiki/Solar_eclipse'.
		DFSCrawler.py generates the list of 1000 URL's crawled using the DFS searching technique.
		DFS Crawling Technique: Starting from the seed URL ,the first child URL is crawled,followed by its child and so on,
		until a depth of 6 or a crawl of 1000 URLs is done(whichever is reached first).The URLs at the deeper depth are
		explored first compared to the URLs at a shallower depth.
		The list of 1000 URLs crawled are added to a file "DFSUrls.txt"
		
BFSFocusedCrawler:
		Web crawler designed to crawl a web starting from the seed URL provided as 'https://en.wikipedia.org/wiki/Solar_eclipse'.
		BFSFocusedCrawler.py generates the list of 1000 URL's crawled using the BFS Focused searching technique.
		BFS Focused searching technique : Starting from the seed URL ,the URLs at a shallower depth that either have a 
		match with keywords provided("moon","lunar") in their hyperlink or within the text of the hyperlink are crawled first
		and after all URL at a particular depth are crawled,the crawler moves to the next depth.
		The maximum crawls end with the crawler reaching a depth of 6 or URL's crawled reaches 1000(whichever is reached first).
		The list of 1000 URLs crawled are added to a file "BFSFocusedUrls.txt"

=============================================================================================================================================
GENERAL SETUP INSTRUCTIONS: (SPECIFIC TO WINDOWS)
	1. Download Python version 3.6 from https://www.python.org/downloads/
	2. Set the environment variable PATH as Directory for python scripts or your home directory for python
	3. Install BeautifulSoup4 using the command 'pip install beautifulsoup4'
	4  Other Libraries to be imported  : 'requests' , 're' ,'urllib.parse','time'

=============================================================================================================================================
	
PROGRAM SPECIFIC INSTRUCTIONS: 
	1.Create a folder where you would keep the .py files
	2.Open Windows PowerShell -> Navigate to the folder with(.py) files -> run command "python <Filename.py>"
	2.running the program  (BFSCrawler.py , DFSCrawler.py ,BFSFocussedCrawler.py ) will generate the text files(BFSUrls.txt , DFSUrls.txt
	  and BFSFocusedUrls.txt)
	
=============================================================================================================================================

RESULTS: 
	1. BFSCrawler.py would generate a directory named 'BFSCrawler' -> which will contain another directory 'RawHTML'(contains
	   the html content in all of the files that have been crawled).Also 'BFSCrawler' -> 'BFSUrls.txt' (contains 1000 URLs that
	   have been crawled)
	 (BFSCrawler -> RawHTML
	       	 -> BFSUrls
	MAXIMUM DEPTH REACHED  - 3
	2. DFSCrawler.py would generate a directory named 'DFSCrawler' -> 'DFSUrls.txt'(contains 1000 URLs that have been crawled)
	MAXIMUM DEPTH REACHED - 6
	3. BFSFocussedCrawler.py would generate a directory named 'BFSFocusedCrawler' -> 'BFSFocusedUrls.txt'
	MAXIMUM DEPTH REACHED - 4
=============================================================================================================================================
CITATIONS:

	1. https://www.crummy.com/software/BeautifulSoup/bs4/doc	
	2. https://www.udemy.com/home/my-courses/learning/
	3. https://www.youtube.com/watch?v=bIA8HEEUxZI
	4. https://www.youtube.com/watch?v=3xQTJi2tqgk
	5. https://www.youtube.com/watch?v=nRW90GASSXE&list=PL6gx4Cwl9DGA8Vys-f48mAH9OKSUyav0q&index=1
	6. https://docs.python.org/3.4/library/re.html#re.search
	7. https://docs.python.org/3/
	8. https://www.tutorialspoint.com//python/index.htm
