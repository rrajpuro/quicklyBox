import pexpect
import sys
import json

vms = [
    'vm02',
    ]

for vm in vms:

    # Connect to the virtual machine console using virsh console
    child = pexpect.spawn(f'virsh console { vm }')
    # child = pexpect.spawn(f'virsh console 1155')
    child.logfile = sys.stdout.buffer

    # Wait for the login prompt and enter the username
    child.expect('Escape')
    child.sendline('')

    # Wait for the login prompt and enter the username
    r = child.expect(['login:','\$'])
    if r == 0:
        child.sendline('vmadm')
        # Wait for the password prompt and enter the password
        child.expect('Password:')
        child.sendline('vmadm')
        s = child.expect(['Login incorrect', '\$'])
        if s == 0:
            continue
    elif r == 1:
        break

    # Wait for the command prompt and enter the command to configure the IP address
    child.sendline('')
    child.expect('\$')
    
    child.sendline(f"sudo dhclient eth0")
    child.expect('\$')
    
    child.sendline('ip addr')
    child.expect('\$')
    
    child.sendline('')
    child.expect('\$')
    
    # # Wait for the command to complete and exit the console
    # child.sendline('exit')
    # child.expect('\$')
    
    child.sendline('\u001d')
    child.expect(pexpect.EOF)
    print(child.before.decode())
    print(str(child))
