# 
01. Install following python library:
```bash
sudo apt-get install python3-pip -y
pip install paho-mqtt pyyaml
```

02. Copy folder z2m_mon to same folder with folder zigbee2mqtt: `/opt`

03. Change folder path in z2m_monitor.service

04. Copy file z2m_monitor.service to Linux service folder: 
```bash
sudo cp /opt/z2m_mon/z2m_monitor.service /etc/systemd/system 
```

05. Enable service: 
```bash
sudo systemctl start z2m_monitor.service
sudo systemctl enable z2m_monitor.service
```

# 

---
- Status: #done

- Tags: #z2m 

- References:
	- 

- Related:
	- 
