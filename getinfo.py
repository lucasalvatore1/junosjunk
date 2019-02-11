from napalm import get_network_driver
import getpass

# Grab credentials
username = input("Enter your username:")
password = getpass.getpass("Enter your password:")
driver = get_network_driver("junos")

# Open a file called "switchlist" which has a list of devices to modify
with open('switchlist') as infile:
	for host in infile:
		try:
			junos_driver = get_network_driver("junos")
			device = junos_driver(hostname=host.strip(), username=username, password=password)
			device.open()
			print(device.get_facts()["hostname"],end=" ")
			print(device.get_facts()["model"],end=" ")
			print(device.get_facts()["serial_number"])
			device.close()
		except Exception as e:
			print("Error:", e)
		continue

