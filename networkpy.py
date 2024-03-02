from socket import *
import time

def scan_port(port):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((target, port))
    if result == 0:
        print(f"Port {port} is open")
    sock.close()

target = input("Enter the host to be scanned: ")
t_IP = gethostbyname(target)
print(f"Starting scan on host: {t_IP}")
start_time = time.time()

for port in range(1, 1025):
    scan_port(port)

print(f"Scan completed in {time.time() - start_time} seconds")