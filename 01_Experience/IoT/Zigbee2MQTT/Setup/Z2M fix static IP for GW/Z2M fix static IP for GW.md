# 
- Create backup of `/etc/network/interfaces`
```bash
sudo cp /etc/network/interfaces /etc/network/interfaces.backup
sudo vi /etc/network/interfaces
%% OR %%
sudo nano /etc/network/interfaces
```

- Change content of file `/etc/network/interfaces`, replace `???` with Gateway IP
	- Gateway IP: 10->20
	- For example, GW at floor G has ip 192.168.68.10
```
source /etc/network/interfaces.d/*
auto eth0
allow-hotplug eth0
#no-auto-down eth0
iface eth0 inet static
address 192.168.68.???
netmask 255.255.255.0
gateway 192.168.68.1
dns-nameservers 8.8.8.8 8.8.8.4
# Network is managed by Network manager
auto lo
iface lo inet loopback
```

- Reboot GW
```bash
sudo reboot
```

> TODO: Find a way to change IP without rebooting GW


# For haint126 only
```bash
scp .\Desktop\interfaces labiot@192.168.68.122:/opt/zigbee2mqtt

ssh labiot@192.168.68.122
cd /etc/network
sudo mv interfaces interfaces.backup
sudo mv /opt/zigbee2mqtt/interfaces ./
sudo reboot

scp -r labiot@192.168.68.87:/opt/zigbee2mqtt/data .\Desktop
```



# 

---
- Status: #done

- Tags: #z2m

- References:
	- 

- Related:
	- 
