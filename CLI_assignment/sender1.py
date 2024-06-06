import socket
import os

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
TARGET_ip = "127.0.0.1"
port_no = 2525
target_address = (TARGET_ip, port_no)

quit = True
while quit:
    option = input("Enter 'm' to send a message or 'f' to send a file: ").strip().lower()
    if option == 'm':
        message = input("Please enter your message: ")
        s.sendto(b'MSG', target_address)  
        s.sendto(message.encode('ascii'), target_address)
        print("Your message has been sent!")
    elif option == 'f':
        file_path = input("Enter the path of the text file to send: ")
        if os.path.isfile(file_path):
            file_name = os.path.basename(file_path)
            with open(file_path, 'r') as file:
                file_content = file.read()

            s.sendto(b'FILE', target_address)  
            s.sendto(file_name.encode('ascii'), target_address) 
            s.sendto(file_content.encode('ascii'), target_address) 
            print(f"File '{file_name}' has been sent!")
        else:
            print("The file does not exist")
    else:
        print("Please enter 'm' or 'f'.")
    
    user_input = input("Do you want to quit? Press Y/N: ").strip().lower()
    if user_input == 'y':
        quit = False

s.close()
