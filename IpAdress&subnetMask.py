
import ipaddress

print("Welcome to Ip address and subnet calculating tool : ")

#Subnet Mask : 
#shows which part of IP address is belong to the host(Company). or which part belongs to user !
# subnet mask is 32 bits same to IP v4!
#subnet have multiple octets : Network octet, and User octet.


def subnet_calculator(ip, subnet_mask):
    # Create an IP network object
    network = ipaddress.IPv4Network(f"{ip}/{subnet_mask}", strict=False)

    # Calculate network address
    network_address = network.network_address

    # Calculate broadcast address
    broadcast_address = network.broadcast_address

    # Calculate number of usable hosts
    num_hosts = network.num_addresses - 2  # Subtract network ID and broadcast ID addresses from the total! since they are resereved!

    # Display All results
    print(f"IP Address: {ip}")
    print(f"Subnet Mask: {subnet_mask}")
    print(f"Network Address: {network_address}")
    print(f"Broadcast Address: {broadcast_address}")
    print(f"Number of Usable Hosts: {num_hosts}")

if __name__ == "__main__":
    ip = input("Please Enter the IP address: ")
    subnet_mask = input("Please Enter subnet mask: ")
    subnet_calculator(ip, subnet_mask)
	
	
	
	
	

	
	
		
