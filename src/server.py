import socket
from os import path
import sys

# To keep track of the request count from the client
requests_count = 0

# The file name of customer data
file_name = "files/data.txt"

# Checking if file exists or not
if not path.exists(file_name):
    sys.exit("data.txt file doesn't exit")

# Reading data from the file
file = open(file_name, 'r')

# To store the data from the file
dictionary = {}
data = file.readlines()

for line in data:
    record = line.split("|")
    list_attributes = ["Not Provided", "Not Provided", "Not Provided"]
    count = 0
    name_found = False
    for element in record:

        element = element.replace("\n", "")
        element = element.strip()

        if element == "":
            # print("count : " + str(count))
            # print(record)
            # print("element : " + str(element))

            if count == 0:
                break

        else:
            if count == 0:
                name = element
                name_found = True
            elif count == 1:
                list_attributes[0] = element
            elif count == 2:
                list_attributes[1] = element
            else:
                list_attributes[2] = element

        count = count + 1
    if name_found:
        dictionary[name] = list_attributes

# print(dictionary)

# creating socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# defining host and port
host = 'localhost'
port = 10000

# bind to the port
server_socket.bind((host, port))

print("Python DB is running")


def format_record(record):
    result = ""
    count = 1
    for elements in record:

        if count == 1:
            result = result + "age : " + elements + "\n"
        elif count == 2:
            result = result + "address : " + elements + "\n"
        else:
            result = result + "phone number : " + elements
            count = 1
        count = count + 1
    return result


def add_customer(line):
    record = line.split("|")
    list_attributes = ["Not Provided", "Not Provided", "Not Provided"]
    count = 0
    name_found = False
    for element in record:

        element = element.replace("\n", "")
        element = element.strip()

        if element == "":
            # print("count : " + str(count))
            # print(record)
            # print("element : " + str(element))

            if count == 0:
                return "Customer can't be added"
                # break

        else:
            if count == 0:
                name = element
                if dictionary.get(name) is not None:
                    return "Customer already exists"
                name_found = True
            elif count == 1:
                list_attributes[0] = element
            elif count == 2:
                list_attributes[1] = element
            else:
                list_attributes[2] = element

        count = count + 1
    if name_found:
        dictionary[name] = list_attributes

    return "Customer has been added successfully"


while True:
    # Listening for connection on established socket
    print("listening....")
    server_socket.listen()
    requests_count = requests_count + 1
    client_socket, address = server_socket.accept()

    # Displaying the client address
    # print("Got a connection from %s" % str(address))
    client_data = client_socket.recv(2048)

    # Displaying the data sent by the client
    message = client_data.decode('ascii')
    # print(message)

    service = int(message[0:1])

    if service == 1:
        name = message[2:]
        record = dictionary.get(name)
        # print(record)
        if record is not None:
            result = "name : " + name + "\n" + format_record(record)
            # print(result)
            client_socket.send(result.encode('ascii'))
        else:
            client_socket.send("customer not found".encode('ascii'))

    if service == 2:
        line = message[2:]
        result = add_customer(line)
        # print(dictionary)
        client_socket.send(result.encode('ascii'))

    if service == 3:
        name = message[2:]
        record = dictionary.get(name)
        # print(record)
        if record is not None:
            del dictionary[name]
            result = name + " has been deleted successfully"
        else:
            result = name + " not found"
        client_socket.send(result.encode('ascii'))

    if service == 4:
        record = message[2:]
        record = record.split("|")
        name, age = record
        # print(name)
        # print(age)

        record = dictionary.get(name)
        if record is None:
            result = name + " not found"
        else:
            if age == "":
                age = "Not Provided"
            record[0] = age
            dictionary[name] = record
            result = "Customer age has been updated successfully"

        client_socket.send(result.encode('ascii'))

    if service == 5:
        record = message[2:]
        record = record.split("|")
        name, address = record
        # print(name)
        # print(address)

        record = dictionary.get(name)
        if record is None:
            result = name + " not found"
        else:
            if address == "":
                address = "Not Provided"
            record[1] = address
            dictionary[name] = record
            result = "Customer address has been updated successfully"

        client_socket.send(result.encode('ascii'))

    if service == 6:
        record = message[2:]
        record = record.split("|")
        name, phone_number = record
        # print(name)
        # print(phone_number)

        record = dictionary.get(name)
        if record is None:
            result = name + " not found"
        else:
            if phone_number == "":
                phone_number = "Not Provided"
            record[2] = phone_number
            dictionary[name] = record
            result = "Customer phone number has been updated successfully"

        client_socket.send(result.encode('ascii'))

    else:
        result = ""
        for keys in dictionary:
            temp = "name - " + keys + "\n"
            # print(temp)
            temp = temp + format_record(dictionary.get(keys))
            result = result + temp + "\n" + "\n"
        client_socket.send(result.encode('ascii'))

    print("Request - " + str(requests_count) + " served")

    client_socket.close()
