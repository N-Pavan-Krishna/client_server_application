import socket

# defining host and port
host = 'localhost'
port = 10000

# The program loops over until the user wants to terminate
while True:

    # Displaying the menu of options available to the user
    print("""
        Python DB Menu
        1. Find customer
        2. Add customer
        3. Delete customer
        4. Update customer age
        5. Update customer address
        6. Update customer phone
        7. Print report
        8. Exit
        """)

    # Getting input from the client. Making sure we get only integer value in range (1, 8)
    try:
        select = int(input("Select : "))
        if select < 1 or select > 8:
            print("int violation")
            print("""
                Invalid option.
                Requires integer value in between 1 and 8.
                Try again.
            """)
            continue
    except ValueError:
        print("exception")
        print("""
            Invalid option.
            Requires integer value in between 1 and 8.
            Try again.
            """)
        continue

    # Handling valid options of python DB
    if select == 1:
        name = input("Enter name : ")

        message = str(select) + "|" + name

        # creating socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # establishing a connection
        client_socket.connect((host, port))

        client_socket.sendall(message.encode('ascii'))

        # Receive no more than 2048 bytes
        result = client_socket.recv(2048)
        print(result.decode('ascii'))

    elif select == 2:
        # print("Add customer")
        name = input("Enter name : ")
        while True:
            try:
                age = input("Enter age : ")
                if age == "":
                    break
                age = int(age)
                if age < 1:
                    print("int violation")
                    print("""
                        Invalid option.
                        Requires integer value in between 1 and 8.
                        Try again.
                    """)
                    continue
                break
            except ValueError:
                print("exception")
                print("""
                    Invalid option.
                Requires integer.
                Try again.
                """)
        address = input("Enter address : ")
        phone_number = input("Enter phone number : ")

        message = str(select) + "|" + name + "|" + str(age) + "|" + address + "|" + phone_number

        # creating socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # establishing a connection
        client_socket.connect((host, port))

        client_socket.sendall(message.encode('ascii'))

        # Receive no more than 2048 bytes
        result = client_socket.recv(2048)
        print(result.decode('ascii'))

    elif select == 3:
        name = input("Enter name : ")

        message = str(select) + "|" + name

        # creating socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # establishing a connection
        client_socket.connect((host, port))

        client_socket.sendall(message.encode('ascii'))

        # Receive no more than 2048 bytes
        result = client_socket.recv(2048)
        print(result.decode('ascii'))

    elif select == 4:
        # print("Update customer age")
        name = input("Enter name : ")
        while True:
            try:
                age = input("Enter age : ")
                if age == "":
                    break
                age = int(age)
                if age < 1:
                    print("int violation")
                    print("""
                        Invalid option.
                        Requires integer value in between 1 and 8.
                        Try again.
                    """)
                    continue
                break
            except ValueError:
                print("exception")
                print("""
                    Invalid option.
                Requires integer.
                Try again.
                """)

        message = str(select) + "|" + name + "|" + str(age)

        # creating socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # establishing a connection
        client_socket.connect((host, port))

        client_socket.sendall(message.encode('ascii'))

        # Receive no more than 2048 bytes
        result = client_socket.recv(2048)
        print(result.decode('ascii'))

    elif select == 5:
        # print("Update customer address")
        name = input("Enter name : ")
        address = input("Enter address : ")

        message = str(select) + "|" + name + "|" + address

        # creating socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # establishing a connection
        client_socket.connect((host, port))

        client_socket.sendall(message.encode('ascii'))

        # Receive no more than 2048 bytes
        result = client_socket.recv(2048)
        print(result.decode('ascii'))

    elif select == 6:

        name = input("Enter name : ")
        phone_number = input("Enter phone number : ")

        message = str(select) + "|" + name + "|" + phone_number

        # creating socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # establishing a connection
        client_socket.connect((host, port))

        client_socket.sendall(message.encode('ascii'))

        # Receive no more than 2048 bytes
        result = client_socket.recv(2048)
        print(result.decode('ascii'))

    elif select == 7:
        message = str(select)

        # creating socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # establishing a connection
        client_socket.connect((host, port))

        client_socket.sendall(message.encode('ascii'))

        # Receive no more than 2048 bytes
        result = client_socket.recv(2048)
        print(result.decode('ascii'))

    else:
        print("Good bye")
        break

    client_socket.close()
