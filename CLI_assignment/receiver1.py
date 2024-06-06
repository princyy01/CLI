import socket

def save_file(file_name, file_content):
    with open(file_name, 'w') as file:
        file.write(file_content)
    print(f"File '{file_name}' has been saved.")

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
ip_address = "127.0.0.1"
port_no = 2525
my_address = (ip_address, port_no)
s.bind(my_address)

print(f"Receiver is listening on {ip_address}:{port_no}")

while True:
    data, addr = s.recvfrom(1024)  
    if data == b'MSG':
        data, addr = s.recvfrom(1024)  
        print(f"Received message: {data.decode('ascii')} from {addr}")
    elif data == b'FILE':
        file_name, addr = s.recvfrom(1024) 
        file_content, addr = s.recvfrom(1024) 
        save_file(file_name.decode('ascii'), file_content.decode('ascii'))
