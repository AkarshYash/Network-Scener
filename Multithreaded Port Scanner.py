import socket
import time
import threading
from colorama import Fore, Style, init

init(autoreset=True)

print(Fore.CYAN + Style.BRIGHT + """
╔═════════════════════════════════════╗
║     ⚡ MULTITHREADED PORT SCANNER   ║
╚═════════════════════════════════════╝
By Akarsh Chaturvedi
""")

target = input(Fore.YELLOW + "[?] Enter Target IP: ")
start_port = int(input(Fore.YELLOW + "[?] Start Port: "))
end_port = int(input(Fore.YELLOW + "[?] End Port: "))

print(Fore.MAGENTA + f"\n[+] Scanning {target} from port {start_port} to {end_port}...\n")
time.sleep(1)

def scan_port(port):
    try:
        s = socket.socket()
        s.settimeout(0.5)
        s.connect((target, port))
        print(Fore.GREEN + f"[+] Port {port} is OPEN")
        s.close()
    except:
        pass

threads = []
for port in range(start_port, end_port + 1):
    t = threading.Thread(target=scan_port, args=(port,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(Fore.CYAN + "\n[✓] Multithreaded scan complete.")
