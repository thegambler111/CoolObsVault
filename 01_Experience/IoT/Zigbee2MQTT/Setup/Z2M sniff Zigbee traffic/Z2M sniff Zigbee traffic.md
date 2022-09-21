# Download Wireshark
- [Official page](https://www.wireshark.org/download.html)

# Download Z-boss
- [Official page](http://zboss.dsr-wireless.com/downloads/index/zboss)
- Require login -> Download elsewhere

# Plugin USB Zigbee CC2531 
- USB need to be flashed with sniffer firmware
- Checked plugin port in Device Manager

# Open zboss_sniffer.exe in "gui" folder
![[01_Experience/IoT/Zigbee2MQTT/Setup/Z2M sniff Zigbee traffic/Z-boss.png]]

# Wireshark will start and capture Zigbee traffic
## Add security keys:
- There are 2 types of keys:
	- Default Trust Center link key (usually is): 5A:69:67:42:65:65:41:6C:6C:69:61:6E:63:65:30:39
	- Network encryption key (Transport Key): depends on the coordinator
		- Search in `data/configuration.yaml` file, under the tag "network_key"
		- Convert into Hexadecimal

- Add keys in Wireshark menu: Edit -> Preference -> Protocol -> Zigbee -> Edit
![[01_Experience/IoT/Zigbee2MQTT/Setup/Z2M sniff Zigbee traffic/Add keys.png]]

# Wait for traffic to be capture

# Stop Wireshark and store captured traffic in .pcapng



# 

---
- Status: #done

- Tags: #z2m 

- References:
	- [Official guide](https://www.zigbee2mqtt.io/advanced/zigbee/04_sniff_zigbee_traffic.html)

- Related:
	- 
