
import socket
import time
from colorama import Fore, Style, init

init(autoreset=True)

print(Fore.CYAN + Style.BRIGHT + """
╔════════════════════════════════════╗
║     🔍 ADVANCED PORT SCANNER      ║
╚════════════════════════════════════╝
By Akarsh Chaturvedi
""")

target = input(Fore.YELLOW + "[?] 1.90.87: ")

start_port = int(input(Fore.YELLOW + "[?] Start Port: "))
end_port = int(input(Fore.YELLOW + "[?] End Port: "))

print(Fore.MAGENTA + f"\n[+] Scanning {target} from port {start_port} to {end_port}...\n")
time.sleep(1)

for port in range(start_port, end_port + 1):
    try:
        s = socket.socket()
        s.settimeout(0.5)
        s.connect((target, port))
        print(Fore.GREEN + f"[+] Port {port} is OPEN")
        s.close()
    except:
        pass  


print(Fore.CYAN + "\n[✓] Scan complete.")
