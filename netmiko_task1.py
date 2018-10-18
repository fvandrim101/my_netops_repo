# Working with NetMiko tool
#
from netmiko import ConnectHandler
cisco_cloud_router = {'device_type' : 'cisco_ios',
                        'ip' : '10.0.0.5',
                        'username' : 'ignw',
                        'password' : 'ignw'}
#
connection = ConnectHandler(**cisco_cloud_router)
#
print(connection)
print(type(connection))
print()
hostname = connection.find_prompt()
print(hostname[:-1])
#
interface_name = connection.send_command('show run int g1 | i ^interface')
#
print(interface_name)
#
description = connection.send_command('show run int g1 | i des')
#
print(description)
#
ip_address = connection.send_command('show run int g1 | i ip add')
#
print(ip_address)
#
