
## 📘 Final `README.md` – Basic Port Scanner v1.0

```markdown
# 🔍 Basic Port Scanner v1.0

A stylish, beginner-friendly Python tool to scan common open ports on a target IP.  
🎯 Great for getting started with cybersecurity, ethical hacking, and tool development.

![banner](https://img.shields.io/badge/Python-3.x-blue?style=flat-square)
![status](https://img.shields.io/badge/status-Working-green?style=flat-square)
![author](https://img.shields.io/badge/Author-Akarsh--Chaturvedi-orange?style=flat-square)

---

## ✨ Features

- ✅ Scans 8 essential ports: FTP, SSH, Telnet, DNS, HTTP, HTTPS, and more
- 🎨 Enhanced terminal UI with colors and ASCII banner
- ⚡ Fast and lightweight
- 🧠 Beginner-friendly Python code
- 💥 Color-coded output using `colorama`

---

## 📦 Requirements

- Python 3.x installed
- `colorama` library

---

## ⚙️ Setup Instructions

### 1. 📥 Download the Script

Save it as:
```

basic\_port\_scanner.py

````

### 2. 🐍 Install `colorama`

Run this once:
```bash
pip install colorama
````

---

## 🌐 How to Find Your IP

### 🖥️ On Windows:

1. Press `Win + R`, type `cmd`, hit **Enter**
2. Type:

```cmd
ipconfig
```

3. Copy the **IPv4 Address** (e.g., `192.168.1.5`)

Use this as your **target IP**.

---

## 🚀 How to Run

### On Windows PowerShell:

```powershell
python "C:\Path\To\basic_port_scanner.py"
```

### On Linux/macOS:

```bash
python3 basic_port_scanner.py
```

---

## 📸 Screenshot Example

```
╔═══════════════════════════════════╗
║   🔍 BASIC PORT SCANNER - v1.0   ║
╚═══════════════════════════════════╝
Author: Akarsh Chaturvedi | Language: Python
---------------------------------------

Enter Target IP (e.g. 192.168.1.1): 192.168.1.1

[+] Starting scan...

[-] Port 21 is closed
[-] Port 22 is closed
[+] Port 80 is OPEN
[+] Port 443 is OPEN

[✓] Scan completed. Stay secure!
```

---

## 🛡️ Ports Scanned

| Port | Service | Description       |
| ---- | ------- | ----------------- |
| 21   | FTP     | File Transfer     |
| 22   | SSH     | Secure shell      |
| 23   | Telnet  | Remote login      |
| 25   | SMTP    | Email sending     |
| 53   | DNS     | Domain resolution |
| 80   | HTTP    | Web (insecure)    |
| 110  | POP3    | Email retrieval   |
| 443  | HTTPS   | Secure web        |

---

## ⚠️ Legal & Ethical Use

This tool is meant for **learning and testing on authorized systems only**.
🚫 Do **NOT** scan devices you don’t own or don’t have permission to test.

---

## 👨‍💻 Author

**Akarsh Chaturvedi**
Cybersecurity | Security Tool Development | Python | Machine Learning | Web Development

---

⭐ If you found this useful, give it a star and keep hacking (ethically)!

```

