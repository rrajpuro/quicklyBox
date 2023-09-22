A folder to store all the dns and dhcp config for running VMs
A sample file structure looks as follows:
```
dnsmasq
|--bridge01
|  |--bridge01-dnsmasq.conf
|  |--bridge01-dnsmasq.leases
|--bridge02
|  |--bridge02-dnsmasq.conf
|  |--bridge02-dnsmasq.leases
```

The `<bridge-name>-dnsmasq.conf` file has the DHCP stsic bindings
For example:
```
# Configuration file for dnsmasq.
server=8.8.8.8
server=8.8.4.4
strict-order
except-interface=lo
bind-dynamic
interface=bridge01
dhcp-range=192.168.131.2,192.168.131.253,255.255.255.0,12h
# set the default route option
dhcp-option=option:router,192.168.131.1
dhcp-no-override
dhcp-authoritative
dhcp-lease-max=150
dhcp-leasefile=/home/eb2-2027/quickly/run/dnsmasq/bridge01/bridge01-dnsmasq.leases

dhcp-host=52:54:05:77:01:02,192.168.131.2
dhcp-host=52:54:05:77:01:03,192.168.131.3
dhcp-host=52:54:05:77:01:04,192.168.131.4
dhcp-host=52:54:05:77:01:05,192.168.131.5
...
```