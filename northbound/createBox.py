from ansible_runner import run
import yaml

# Define the path to the playbook file
# Replace with your playbook path
playbook_path = "/home/eb2-2027/quicklyBox/southbound/create-vm-ubuntu.yaml"

''' ANSIBLE VARS EXAMPLE
  vars:
    vms:
      - name: vm15
        memory: 24576
        vcpu: 4
        capacity: 256
        image_path: /home/eb2-2027/quickly/run/base/lunar-server-cloudimg-amd64-disk-kvm.img
        interfaces:
          - name: eth0
            network: 'snmbr1'
            # mac: 52:54:<coursenumber>:<coursenumber>:<bridgenumber>:<hostnumber>
            # ipaddr: 192.168.<140+bridgenumber>.<hostnumber>
            mac: '52:54:05:47:01:15'
'''

# Create an empty list to store VM data
vms = []

# Define the number of VMs
num_vms =  5 #28

# Generate data for each VM
# for i in range(5, num_vms + 1):
for i in range(1, 28):

    vmdata = {
        "name": f"vm{i:03}",
        "capacity": 128,
        "image_path": "/home/eb2-2027/quicklyBox/run/base/lunar-server-cloudimg-amd64-disk-kvm.img",
        "memory": 8192,
        "vcpu": 2,
        "interfaces": [
            {
                # {:02x} specifies that you want to format the decimal number as a hexadecimal
                # string with two digits, and any empty space will be filled with leading zeros.
                "mac": f"52:54:05:47:01:{i:02x}",   #Device’s MAC address in the form xx:xx:xx:xx:xx:xx. Letters must be lowercase.
                "name": "eth0",
                # If using a custom dnsmasq service use bridge and configure dnsmasq service as defined in ./run/dnsmasq
                "inftype" : "network",
                # "inftype" : "bridge"
                "network": "cctbr11-net"
                
            }
        ]
    }
    vms.append(vmdata)
    
# with open("vars.yaml", 'w') as f:
#     yaml.dump(vms, f)
# exit(0)

# Define the run options
run_options = {
    "playbook": playbook_path,
    "quiet": False,  # Set to True if you want less output
    "extravars": {"vms": vms},
}

try:
    # Run the playbook using Ansible Runner
    result = run(**run_options)
    print("Ansible playbook executed successfully.")
    print(result.stats)
except Exception as e:
    print(f"Error running Ansible playbook: {e}")
