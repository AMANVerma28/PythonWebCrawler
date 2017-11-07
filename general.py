import os

#Each crawled website is a seperate project (folder)
def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating project' + directory)
        os.makedirs(directory)

#Create queue and crawled files (if not created)
def create_data_files(project_name, base_url):
    queue = project_name + '/queue.txt'
    crawled = project_name + '/crawled.txt'
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')

#Create a new file
def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()

#Add data onto existing file
def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')

#Delete content of an existing file
def delete_file_content(path):
    with open(path, 'w'):
        pass

#Read a file and convert it to set
def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n',''))
    return results

#Iterate through set, each item in the set is a line in file
def set_to_file(links, file_name):
    delete_file_content(file_name)
    for link in sorted(links):
        append_to_file(file_name, link)
