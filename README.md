
```markdown
 🌐 Network-Scener

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green)
![Last Commit](https://img.shields.io/github/last-commit/AkarshYash/Network-Scener)

A suite of network security tools featuring a powerful port scanner with logging capabilities. Perfect for security professionals and network administrators.

```python
╔═══════════════════════════════════════╗
║     🔍 PORT SCANNER WITH LOGGING     ║
╚═══════════════════════════════════════╝
```

✨ Features

- **Multi-threaded port scanning** for blazing fast results
- **Banner grabbing** to identify running services
- **Comprehensive logging** to text files
- **Color-coded terminal output** for better visibility
- **Custom port range scanning**
- **Easy-to-use interactive CLI**

📦 Installation

```bash
git clone https://github.com/AkarshYash/Network-Scener.git
cd Network-Scener
pip install -r requirements.txt
```

🚀 Quick Start

Run the port scanner:
```bash
python port_scanner.py
```

Sample output:
```bash
[?] Enter Target IP or Hostname: scanme.nmap.org
[?] Start Port: 20
[?] End Port: 80

[+] Port 22 OPEN - Banner: SSH-2.0-OpenSSH_7.9
[+] Port 80 OPEN - Banner: HTTP/1.1 200 OK
```

📂 File Structure

```
Network-Scener/
├── port_scanner.py       # Main port scanning utility
├── scan_results.txt      # Sample output file
├── requirements.txt      # Dependencies
└── README.md            # This documentation
```

🛠 Future Roadmap

- [ ] Add vulnerability scanning
- [ ] Implement GUI version
- [ ] Add network mapping features
- [ ] Support for export formats (JSON, CSV)
- [ ] Ping sweep functionality

🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

📜 License

Distributed under the MIT License. See `LICENSE` for more information.

 📧 Contact

Akarsh Chaturvedi - - Chaturvediakarsh51@gmail.com

Project Link: [https://github.com/AkarshYash/Network-Scener](https://github.com/AkarshYash/Network-Scener)

---

Made with ❤️ by [Akarsh Chaturvedi](https://github.com/AkarshYash)
```

Key Improvements:
1. Modern Badges - Added shields.io badges for better visibility
2. ASCII Art - Kept your cool scanner banner
3. Clear Structure - Organized sections with emoji headings
4. Roadmap - Added future plans to attract contributors
5. Professional Tone - Maintained a clean, technical but approachable style
6. Responsive Formatting - Looks great on both desktop and mobile GitHub

To implement this:
1. Create a new `README.md` file in your repository
2. Copy this entire content
3. Update the contact information and any other personal details
4. Commit and push to GitHub

Would you like me to make any specific adjustments to better match your project vision?

🛡️ Ports Scanned

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


