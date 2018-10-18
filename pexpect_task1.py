# Bring in 'Expect script' like capabilities
#
import pexpect
#

# Base variables
username = 'ignw'
password = 'ignw'
device_ip = '10.0.0.5'
#
# Seeing what happened prior and positive
def meatbag():
    print('spacer line')
    print(connection.before)
    print(connection.after)
    print ('spacer line')
    return
#
# Merrily we connect with ssh
#
connection = pexpect.spawn(f'ssh {username}@{device_ip}')
#
# Meatbag data
#print (connection)
#print (type(connection))
#
# Now to set 'expectations'...
connection.expect('Password:')
connection.sendline(password)
#
# Checking on outputs
# print(connection.before)
# print(connection.after)
# Now to check on the host prompt
connection.expect('ignw-csr#')
# meatbag()
#
# Set host ID variables
# hostid = connection.after
#print (hostid)
#
print('In the device now!')
#
# Grab an interface (gig1)
#
connection.sendline('sh run int g1')
connection.expect('ignw-csr#')
#
print('Got G1 Data!')
interface_output = connection.before
print (interface_output)
#
print()
split_output = interface_output.decode().split('\r\n')
print(split_output)
#
#
for line in split_output:
    if line.startswith('interface'):
        interface_name = line[10:]
    elif line.startswith(' ip address'):
        interface_ip_address = line[12:]
    elif line.startswith(' description'):
        interface_description = line[12:]
#
print(f'Interface: {interface_name}, Description: {interface_description},'
    f' IP: {interface_ip_address}')
#
