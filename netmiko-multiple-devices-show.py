from netmiko import Netmiko
from getpass import getpass
from sys import argv
from netmiko import ConnectHandler

script, devices, commands, user_name = argv

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
            net_connect = ConnectHandler(**device)
            with open(commands) as c:
                for line in c:
                    try:
                        #print(line)
                        command = line.strip()
                        print()
                        print(net_connect.find_prompt())
                        output = net_connect.send_command(command)
                        #net_connect.disconnect()
                        print(output)
                        print()
                    except Exception as e:
                        print("Error:", e)
                    continue
            net_connect.disconnect()
        except Exception as e:
            print("Error:", e)
        continue