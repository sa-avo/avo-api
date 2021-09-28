import time
import requests

def print_function(string, print_rate):

    for i in string:
        time.sleep(print_rate)
        print(i, end='')
    print('\n')

def check_server_status(url):

    print_function("Check server", 0.05)

    server_status = False

    try:
        page = requests.get(url)
        if page.status_code == 200:
            time.sleep(1.0)
            print("Server returns OK Code, Up and Running ...")
            time.sleep(1.0)
            server_status = True
    except:
        print("Server Problems: Either start server or check network settings")
        server_status = False

    return server_status

