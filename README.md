**README**

---

### Port Scanner

This Python script is a simple port scanner designed to scan ports within a specified range on a given host. It utilizes the `socket` library for network communication and `time` for performance measurement.

### Usage

1. **Setup**: Ensure you have Python installed on your system.
2. **Execution**: Run the script in a Python environment.
3. **Input**: Enter the host you want to scan when prompted.
4. **Results**: The script will output a list of open ports on the specified host.
5. **Performance**: The execution time of the scan will be displayed upon completion.

### Code Structure

- **Imports**: The script imports necessary modules: `socket` for network communication and `time` for performance measurement.
- **`scan_port` Function**: This function takes a port number as input, attempts to connect to it on the specified host, and prints a message if the port is open.
- **User Input**: The script prompts the user to input the host to be scanned.
- **Scanning Process**: It iterates through a range of ports (1 to 1024) and calls the `scan_port` function for each port.
- **Performance Measurement**: The script records the time taken for the entire scan process.

### Note

- This script provides a basic demonstration of port scanning functionality and may require adjustments or enhancements for specific use cases.
- It's important to use this script responsibly and only on hosts and networks you have permission to scan. Unauthorized port scanning can be illegal and unethical.

---
