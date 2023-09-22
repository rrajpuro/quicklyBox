from ansible_runner import run

# Define the path to the playbook file
# Replace with your playbook path
playbook_path = "../southbound/create-vm-ubuntu.yaml"

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

# Define the number of VMs
num_vms =  1 #27

# Create an empty list to store VM data
vms = []

# Generate data for each VM
for i in range(1, num_vms + 1):

    vmdata = {
        "name": f"vm{i:03}",
        "capacity": 128,
        "image_path": "/home/eb2-2027/quickly/run/base/lunar-server-cloudimg-amd64-disk-kvm.img",
        "memory": 8192,
        "vcpu": 2,
        "interfaces": [
            {
                # {:02X} specifies that you want to format the decimal number as a hexadecimal
                # string with two digits, and any empty space will be filled with leading zeros.
                "mac": f"52:54:05:47:01:{i:02X}",
                "name": "eth0",
                "network": "cctbr1"
            }
        ]
    }
    vms.append(vmdata)
    
# Define the variables as a dictionary
variables = [
    {"vms": vms},
    # {"var2": "value2"},
    # Add more variables as needed
]

# Iterate through the variables and create a list of dictionaries
extra_vars = [{"vars": variable} for variable in variables]

# Define the run options
run_options = {
    "playbook": playbook_path,
    "quiet": False,  # Set to True if you want less output
    "extra_vars": extra_vars,
}

try:
    # Run the playbook using Ansible Runner
    result = run(**run_options)
    print("Ansible playbook executed successfully.")
    print(result.stats)
except Exception as e:
    print(f"Error running Ansible playbook: {e}")
