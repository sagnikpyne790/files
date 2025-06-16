import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_socket.bind(("0.0.0.0", 9998))

print("[*] UDP Server is listening...")

try:

while True:

try:

data, addr = server_socket.recvfrom(1024)

try:

decoded_data = data.decode('utf-8')

except UnicodeDecodeEггог:

decoded_data = f"[Non-UTF-8 data received: (data)]"

print(f"Received from {addr): (decoded_data}")

except Keyboard Interrupt:

print("\n[*] Server shutting down...")

break

except Exception as e:

print(f"[!] An error occurred: {e}")

finally:

server_socket.close()

print("[*] Socket closed.")