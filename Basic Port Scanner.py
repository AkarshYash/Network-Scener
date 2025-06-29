import socket
import time
from colorama import Fore, Style, init

init(autoreset=True)

print(Fore.CYAN + Style.BRIGHT + """
╔═══════════════════════════════════╗
║   🔍 BASIC PORT SCANNER - v1.0   ║
╚═══════════════════════════════════╝
Author: Akarsh Chaturvedi | Language: Python
---------------------------------------
""")

target = input(Fore.YELLOW + "Enter Target IP (e.g. 192.168.1.1): ")

ports = [21, 22, 23, 25, 53, 80, 110, 443]

print(Fore.MAGENTA + "\n[+] Starting scan...\n")
time.sleep(1)

for port in ports:
    try:
        s = socket.socket()
        s.settimeout(1)
        s.connect((target, port))
        print(Fore.GREEN + f"[+] Port {port} is OPEN")
        s.close()
    except:
        print(Fore.RED + f"[-] Port {port} is closed")
        pass

print(Fore.CYAN + "\n[✓] Scan completed. Stay secure!\n")

