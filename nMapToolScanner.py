#/usr/bin/nmap
import nmap
scanner = nmap.PortScanner()

print("Welcome to N-MAP port scanner! ")
print("___________________________________")


ip_addr = input("Please enter the IP Address you want to scan : ")
print("The IP Address you entered is : ", ip_addr)
#Type method on Ip Address : return the class
type(ip_addr) 
	
while True :
	#Get the response : #tripple cote to have the multiple lines ! 
	resp = int(input("""\n Please enter the type of scan : 
			1. SYN ACK Scan.
			2. UDB Scan.
			3. Comprehensive Scan.
			4. Quit\n"""))
			
	print("You have selected option: ", resp)

	if resp == 1:  #DONE
	#IF choice 1 means SYN ACK SACN : three-way handshake !
		print("Nmap version : ", scanner.nmap_version()) #print nmap version
		#what the scan does (gives the dictionary! )
		scanner.scan(ip_addr , '1-1024', '-v -sS') #scan 
		print(scanner.scaninfo()) #Gives dictionary
		print("IP status : ", scanner[ip_addr].state()) #to see if ip is up or down ! by state method !
		print(scanner[ip_addr].all_protocols()) #get TCP
		#check for open ports :
		print("Open ports: ", scanner[ip_addr]['tcp'].keys())
		#dict {{123,45, 455 }}
		break
	elif resp == 2: #DONE
	#IF choice 2 means  UDP SACN : fast, not secure, do a traffic to the network!
	#takes more time than SYN ACK Scan, about one minute
		print("Nmap version : ", scanner.nmap_version()) #print nmap version
		#what the scan does (gives the dictionary! )
		scanner.scan(ip_addr , '1-1024', '-v -sU') #UDP scan, command -sU stands for UDP!
		print(scanner.scaninfo()) #Gives dictionary, info's about scan
		print("IP status : ", scanner[ip_addr].state()) #to see if ip is up or down ! by state method !
		print(scanner[ip_addr].all_protocols()) #get TCP
		#check for open ports :
		print("Open ports: ", scanner[ip_addr]['udp'].keys())
		#dict {{123,45, 455 }}
		break
	elif resp == 3:
	#IF choice 3 means Comprehensive SCAN : 
	#take more than one minute !
		print("Nmap version : ", scanner.nmap_version()) #print nmap version
		#what the scan does (gives the dictionary! )
		scanner.scan(ip_addr , '1-1024', '-v -sS -sV -sC -A -O') #use OS detection to do : comprehensive scan
		print(scanner.scaninfo()) #Gives dictionary
		print("IP status : ", scanner[ip_addr].state()) #to see if ip is up or down ! by state method !
		print(scanner[ip_addr].all_protocols()) #get TCP
		#check for open ports :
		print("Open ports: ", scanner[ip_addr]['tcp'].keys())
		#dict {{123,45, 455 }}

		#takes more time than UDP Scan!
		break

	elif resp ==4:
		print("Exiting the program ...")
		break
	else:
		print("Invalid choice! Pleasr enter a valid option from choices below!\n")
	
	

