# quicklyBox
A virtual machine manager based on libvirt

# Setup
- Clone the Git repo
- Install 'qemu-utils', 'cloud-init', 'cloud-image-utils'
    - sudo apt install qemu-utils
    - sudo apt install cloud-init
    - sudo apt install cloud-image-utils

- Installing ansible on ubuntu
    - sudo apt install software-properties-common
    - sudo add-apt-repository --yes --update ppa:ansible/ansible
    - sudo apt install ansible

### Create Bridge device
sudo brctl addbr cctbr1
sudo ip addr add 192.168.141.1/24 dev cctbr1

### Create a dummy nic to ensure a MAC for virtual bridge
https://listman.redhat.com/archives/libvirt-users/2012-September/msg00038.html
sudo ip link add cctbr1-nic type dummy
sudo ip link set cctbr1-nic address 52:54:05:47:00:01

sudo ip link set cctbr1-nic master cctbr1

sudo ip link set cctbr1-nic up
sudo ip link set cctbr1 up

### Start DHCP services for the bridge - CHANGE VALUES
- sudo dnsmasq --conf-file=/home/eb2-2027/quicklyBox/run/dnsmasq/<bridge>/<bridge>-dnsmasq.conf

### Add a NAT iptable rule for traffic from the bridge - CHANGE VALUES
- sudo iptables -t nat -A POSTROUTING -s 192.168.xxx.0/24 ! -d 192.168.xxx.0/24 -j MASQUERADE


ansible-galaxy collection install community.libvirt

sudo apt install pkg-config
sudo apt install libvirt-dev
python3 -m pip install libvirt-python


sudo -E python3 createBox.py
"sudo" may not inherit your user's environment variables. 
You may need to set environment variables explicitly in your script or 
when using "sudo -E" to preserve your environment.

use "sudo -E" to run playbooks instead of using become as the python packages are installed in `ansible python module location = /home/eb2-2027/.local/lib/python3.8/site-packages/ansible` instead of `ansible python module location = /usr/lib/python3/dist-packages/ansible` in newer versions of ansible (or Python, possibly as pip defaults to user installation because normal site-packages is not writeable. Possible reason: Ubuntu 20.04 notice default to user installation because normal site-packages not writeable - default config is /usr/lib not writeable for other users except root)(PEP reference https://peps.python.org/pep-0370/)


### Destroy and undefine all VMs
virsh list | awk 'NR > 2 {print $2}' | xargs -n 1 -P 10 virsh destroy
virsh list --all | awk 'NR > 2 {print $2}' | xargs -n 1 -P 10 virsh undefine
