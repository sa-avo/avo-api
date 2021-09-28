import requests
import json
import generic_functions

url = 'http://localhost:5000/results'
server_url = 'http://localhost:5000/'

def interface():

    while True:

        check_server = generic_functions.check_server_status(server_url)
        server_status = check_server

        if server_status is True:

            generic_functions.print_function("Welcome to the simple Api Interface", 0.1)
            generic_functions.print_function("Some options ... ", 0.1)
            generic_functions.print_function("1 - Use Pipple Algorithm to predict ", 0.1)
            generic_functions.print_function("2 - Exit Interface ", 0.1)

            choice = input("Please select 1 or 2 ")

            if choice == "1":

                value1 = input("Insert values SepalLength ")
                value2 = input("Insert values SepalWidth ")
                value3 = input("Insert values PetalLength ")
                value4 = input("Insert values PetalWidth ")

                r = requests.post(url, json={'SepalLength': float(value1), 'SepalWidth': float(value2),
                                             'PetalLength': float(value3), 'PetalWidth': float(value4)})

                mr = r.json()
                print(mr)

                with open('responsedata.json') as res:
                    res_data = json.load(res)
                    print(res_data['FlowerIrisResponseData'][mr])

            elif choice == "2" or server_status is False:
                print("Exiting interface, cheers!")
                break
        else:
            print("fix server issues before restarting ..")
            break


if __name__ == "__main__":
    interface()



