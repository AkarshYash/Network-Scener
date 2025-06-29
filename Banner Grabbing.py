import socket
import threading
from colorama import Fore, Style, init

init(autoreset=True)

print(Fore.CYAN + Style.BRIGHT + """
╔═══════════════════════════════════════╗
║     🔍 BANNER GRABBING SCANNER       ║
╚═══════════════════════════════════════╝
By Akarsh Chaturvedi
""")

target = input(Fore.YELLOW + "[?] Enter Target IP or Hostname: ")
start_port = int(input(Fore.YELLOW + "[?] Start Port: "))
end_port = int(input(Fore.YELLOW + "[?] End Port: "))

def scan_and_grab(port):
    try:
        s = socket.socket()
        s.settimeout(1)
        s.connect((target, port))
        try:
            banner = s.recv(1024).decode().strip()
            print(Fore.GREEN + f"[+] Port {port} OPEN - Banner: {banner}")
        except:
            print(Fore.GREEN + f"[+] Port {port} OPEN - No banner returned.")
        s.close()
    except:
        pass

# Launch threads
threads = []
for port in range(start_port, end_port + 1):
    t = threading.Thread(target=scan_and_grab, args=(port,))
    threads.append(t)
    t.start()

# Wait for threads
for t in threads:
    t.join()

print(Fore.CYAN + "\n[✓] Banner grabbing complete.")
