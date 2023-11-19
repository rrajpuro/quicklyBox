# (echo "1" && sleep 5) & (echo "2" && sleep 5) & (echo "3" && sleep 5) & (echo "4" && sleep 5) & (echo "5" && sleep 5)
import subprocess
import re

if __name__ == "__main__":
    
    allvmlist = [f"vm{x:03}" for x in range(2,157)]

    command = ['virsh', 'list', '--all']
    output = subprocess.check_output(command, universal_newlines=True)

    # Iterate through the lines and extract VM names
    vm_names = re.findall(r'vm\d{3}', output)

    destroy = [f'echo "Start:{vm}" && sleep 2 && echo "Stop:{vm}"' for vm in vm_names if vm in allvmlist]
    # destroy = [f'virsh destroy {vm}' for vm in vm_names if vm in allvmlist]
    destroy_command = ' & '.join(destroy)
    prompt1 = input(f'\nThe following action will destroy VMs:\n{vm_names}\n\nAre you sure you sure you want to proceed?(Y/n):')
    if prompt1 == 'Y':
        print('\nDestroying VMs...\n')
        subprocess.run(destroy_command, shell=True)
    elif prompt1 == 'n':
        print('\nOperation cancelled. Exiting...\n')
    else:
        print('\nInvalid input. Exiting...\n')

    
    start = [f'echo "Start:{vm}" && sleep 2 && echo "Stop:{vm}"' for vm in vm_names if vm in allvmlist]
    # start = [f'virsh start {vm}' for vm in vm_names if vm in allvmlist]
    start_command = ' & '.join(start)
    prompt2 = input(f'\nThe following action will start VMs:\n{vm_names}\n\nAre you sure you sure you want to proceed?(Y/n):')
    if prompt2 == 'Y':
        print('\nStarting VMs...\n')
        subprocess.run(start_command, shell=True)
    elif prompt2 == 'n':
        print('\nOperation cancelled. Exiting...\n')
    else:
        print('\nInvalid input. Exiting...\n')
