
import socket

def scan_ports(ip, start_port, end_port):
    print(f"Scanning {ip} from port {start_port} to {end_port}...")
    open_ports = []
    
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        
        if result == 0:
            open_ports.append(port)
        sock.close()
    
    return open_ports

def main():
    target_ip = input("Enter IP address to scan: ")
    start_port = int(input("Enter starting port: "))
    end_port = int(input("Enter ending port: "))
    
    open_ports = scan_ports(target_ip, start_port, end_port)
    
    if open_ports:
        print(f"Open ports on {target_ip}: {', '.join(map(str, open_ports))}")
    else:
        print(f"No open ports found on {target_ip}.")
        
if __name__ == "__main__":
    main()

