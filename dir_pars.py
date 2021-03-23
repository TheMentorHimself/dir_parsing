####MADE BY THE MENTOR####
import sys

import requests
from bs4 import BeautifulSoup


def save_file(link_list):

    try:
        with open(soup.title.string, "a") as file:
            for link in link_list:
                if link == None:
                    pass
                else:
                    file.write(link)
                    file.write("\n")
            print("[+]DONE[+]")
    except Exception as error:
        print("An error has occured: ")
        print(error)


def get_index(url):
    try:
        req = requests.get(url)
        if req.status_code == 200:
            return req.content
    except Exception as error:
        print("An error has ocurred: ") 
        print(error)


def parse(source):
    global soup
    soup = BeautifulSoup(source, "html.parser")
    all_link = []
    for link in soup.find_all('a'):
        if link in all_link:
            pass
        else:
            all_link.append(link.get("href"))
            print(link.get("href"))
    
    tmp = input(str("Save in wordlist? S/N\n--> "))
    if tmp.lower() == 's':
        save_file(all_link)
    else:
        exit(0)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("use: python {} [url]".format(sys.argv[0]))
    else:
        main_index = get_index(sys.argv[1])
        if main_index:
            parse(main_index)
        else:
            print("No value has been returned")
