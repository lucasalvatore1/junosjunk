from netmiko import Netmiko
from getpass import getpass
from sys import argv
from netmiko import ConnectHandler

script, devices, user_name = argv

device_list = open(devices).read()

password = getpass("Enter your password:")

with open(devices) as infile:
    for host in infile:
        try:
            device = {
                "host": host.strip(),
                "username": user_name,
                "password": password,
                "device_type": "juniper_junos"
            }
            #print(f'{host!r}')
            #print(f"device = {host}")
            #print(f"username = {user_name}")

            net_connect = ConnectHandler(**device)
            command = "YOUR COMMANDS HERE"

            print()
            print(net_connect.find_prompt())
            output = net_connect.send_command(command)
            net_connect.disconnect()
            print(output)
            print()
        except Exception as e:
            print("Error:", e)
        continue
