from napalm import get_network_driver
import getpass

# Grab credentials
username = input("Enter your username:")
password = getpass.getpass("Enter your password:")
driver = get_network_driver("junos")

# Open a file called swichlist which has a list of devices to modify
with open('switchlist') as infile:
	for host in infile:
		try:
			junos_driver = get_network_driver("junos")
			device = junos_driver(hostname=host.strip(), username=username, password=password)
			device.open()
			#print("Working on:", host, end=" ")
			print(device.get_facts()["hostname"],end=" ")
			print(device.get_facts()["model"],end=" ")
			print(device.get_facts()["serial_number"])
			device.close()
		except Exception as e:
			print("Error:", e)
		continue

# device = driver("bbr1.ewr1.packet.net", username, password)
