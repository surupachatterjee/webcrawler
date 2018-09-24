import os


def create_project_dir(directory):
    if not os.path.exists(directory):
        #print('Creating the directory' + directory)
        os.makedirs(directory)

def create_file(filename):
    if not os.path.isfile(filename):
        with open(filename,'w') as f:
            f.write('')
            f.close()


def append_to_file(filename,data):
    with open(filename,'a') as f:
       # f.write(str(data.encode('UTF-8')))
        f.write(data)
        f.close()

def delete_file(filename):
    if os.path.isfile(filename):
        os.remove(filename)

def delete_directory(directory_name):
    if os.path.exists(directory_name):
        for entry in os.scandir(directory_name):
            if os.path.isfile(entry):
                delete_file(entry)
            else:
                delete_directory(entry)
        os.rmdir(directory_name)


#delete_directory("BFSCrawler")
#create_project_dir("BFSCrawler")
#create_file("BFSCrawler/queue1.txt")
#delete_file("Test/Test1/queue1")
#create_project_dir("Test")
#create_file("Test/queue")
#create_file("stack")
#append_to_file("BFSCrawler/queue1.txt","This is the first line")

