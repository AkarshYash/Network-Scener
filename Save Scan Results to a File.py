import socket
import threading
from colorama import Fore, Style, init

init(autoreset=True)

print(Fore.CYAN + Style.BRIGHT + """
╔═══════════════════════════════════════╗
║     🔍 PORT SCANNER WITH LOGGING     ║
╚═══════════════════════════════════════╝
By Akarsh Chaturvedi
""")

target = input(Fore.YELLOW + "[?] Enter Target IP or Hostname: ")
start_port = int(input(Fore.YELLOW + "[?] Start Port: "))
end_port = int(input(Fore.YELLOW + "[?] End Port: "))

# Open file to save results
output_file = open("scan_results.txt", "w")
output_file.write(f"Scan Results for {target} (Ports {start_port}-{end_port})\n\n")

def scan_and_log(port):
    try:
        s = socket.socket()
        s.settimeout(1)
        s.connect((target, port))
        try:
            banner = s.recv(1024).decode().strip()
            message = f"[+] Port {port} OPEN - Banner: {banner}"
        except:
            message = f"[+] Port {port} OPEN - No banner returned."
        print(Fore.GREEN + message)
        output_file.write(message + "\n")
        s.close()
    except:
        pass

# Launch threads
threads = []
for port in range(start_port, end_port + 1):
    t = threading.Thread(target=scan_and_log, args=(port,))
    threads.append(t)
    t.start()

# Wait for threads to complete
for t in threads:
    t.join()

# Close file
output_file.write("\n[OK] Scan complete.\n")
output_file.close()

print(Fore.CYAN + "\n[✓] Scan complete. Results saved to scan_results.txt")
