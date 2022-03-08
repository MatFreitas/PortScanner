import socket
import ipaddress 

# Validate Address of User input
def IPaddress_validator(address):
    try:
        ip = ipaddress.ip_address(address)
        return True
    except:
        print(f"{address} is not a valid IPv4 Address!\n")

# Resolve IP to Hostname
def resolve_IP(address):
    try:
        hostName = socket.gethostbyaddr(address)
        return hostName[0]
    except:
        print(f"Couldn't Resolve IP {address}")

# Connect to port in host, send random data
# to discover application running,
def scanner(host, port, application):
    try:
        # Specifying an IPv4 type connection with TCP protocol.
        connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Setting timeout to determine whether port is closed.
        connection.settimeout(5)

        connection.connect((host, port))
        connection.send(b'RandomData\r\n')
        results = connection.recv(100).decode()
        print(f"\nApplication {application}")
        print(f"Port {port} open")
        print(results)

        # Close Connection
        connection.close()
    except:
        print(f"Port {port} closed.")



# User input info
host = input("\nPlease enter the IP address to scan: ")
while not IPaddress_validator(host):
    host = input("Please enter the IP address to scan: ")

applicationName = resolve_IP(host)


port_option = input("\nDo you wish to scan:\n  A single port (1)\n  A range of ports (2)\n\nPlease input option '1' or '2': ")
while port_option != "1" and port_option != "2":
    port_option = input("\nInvalid input! Try again: ")

if port_option == "1":
    port = input("\nPlease enter the port to scan: ")
    while not port.isdigit():
        print("Port must be an int.\n")
        port = input("Please enter the port to scan: ")

    port = int(port)
    scanner(host, port, applicationName)

elif port_option == "2":
    ports = input("\nPlease enter the port range to scan (example: '1-50'): ")
    port_range = ports.split('-')

    for port in range(int(port_range[0]), int(port_range[1]) + 1):
        scanner(host, port, applicationName)