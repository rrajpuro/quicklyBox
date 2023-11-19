# https://stafwag.github.io/blog/blog/2018/06/04/nested-virtualization-in-kvm/

import subprocess
import re
import libvirt
import xml.etree.ElementTree as ET

def replace_cpu_configuration(domain_name):

    # Find the domain
    domain = conn.lookupByName(domain_name)

    # Get the current XML configuration
    current_xml = domain.XMLDesc()

    # Modify the XML to replace the existing <cpu> element
    root = ET.fromstring(current_xml)

    # Find the existing <cpu> element and remove it
    for cpu_elem in root.findall('.//cpu'):
        root.remove(cpu_elem)

    # Add the new <cpu> element
    new_cpu_xml = """
    <cpu mode='host-model' check='partial'>
        <model fallback='forbid'/>
    </cpu>
    """
    new_cpu_elem = ET.fromstring(new_cpu_xml)
    root.append(new_cpu_elem)

    # Convert the modified XML back to a string
    modified_xml = ET.tostring(root, encoding='utf-8').decode('utf-8')

    # Define the updated domain configuration
    domain.undefine()
    domain = conn.defineXML(modified_xml)
    return

if __name__ == "__main__":
    
    allvmlist = [f"vm{x:03}" for x in range(2,157)]

    command = ['virsh', 'list', '--all']
    output = subprocess.check_output(command, universal_newlines=True)

    # Iterate through the lines and extract VM names
    vm_names = re.findall(r'vm\d{3}', output)

    conn = libvirt.open('qemu:///system')  # Use the appropriate URI for your hypervisor

    for vm in vm_names:
        if vm in allvmlist:
            print(f"-----------------------")
            print(f"Replacing VM XML for {vm}")
            replace_cpu_configuration(vm)
    
    conn.close()
