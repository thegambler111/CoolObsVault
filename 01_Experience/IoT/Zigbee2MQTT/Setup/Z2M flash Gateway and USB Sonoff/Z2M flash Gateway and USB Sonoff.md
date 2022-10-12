# 1. Update firmware USB Sonoff

## Firmware acquisition

- Download the ZNP firmware of CC2652P USB Dongle from the following link:
	- [https://www.home-assistant.io/integrations/zha](https://www.home-assistant.io/integrations/zha)

![[01_Experience/IoT/Zigbee2MQTT/Setup/Z2M flash Gateway and USB Sonoff/USB firmware 1.png]]
![[01_Experience/IoT/Zigbee2MQTT/Setup/Z2M flash Gateway and USB Sonoff/USB firmware 2.png]]


## Firmware flashing

- CC2652P USB Dongle supports serial port Bootloader to flash firmware.

### Enter the serial port Bootloader

There are two ways for Dongle to enter Bootloader:

#### Manual mode
- Keep pressing the Boot button, restart the device, and release the Boot button after Dongle enters the serial port Bootloader.

#### Automatically enter the serial port Bootloader through a python script
- Step to execute python script:

1. [Download](https://sonoff.tech/wp-content/uploads/2022/08/uartLog.zip), unzip and execute the file

![](file:///C:/Users/HP/AppData/Local/Temp/msohtmlclip1/01/clip_image007.png)

2. Enter the serial port number inserted into the dongle

![](file:///C:/Users/HP/AppData/Local/Temp/msohtmlclip1/01/clip_image009.png)

3. After executing the file, enter 55 55 in the serial port assistant tool, and receive the returned result 00 CC, which means that the dongle has successfully entered the Bootloader.

![](file:///C:/Users/HP/AppData/Local/Temp/msohtmlclip1/01/clip_image011.png)

_Note: The serial port Bootloader does not enable hardware flow control._

### Using Flash Programmer2 serial port flashing firmware

![](file:///C:/Users/HP/AppData/Local/Temp/msohtmlclip1/01/clip_image013.jpg)

![](file:///C:/Users/HP/AppData/Local/Temp/msohtmlclip1/01/clip_image015.jpg)

_Note: There is no difference between the coordinator and routing firmware flashing steps._

# 2. Flash Gateway Quang Thông

- 2.1. Download firmware: Armbian_Zigbee2MQTT_included.rar: [https://drive.google.com/file/d/1j6y5-EEYClElv7B9PWarXUO89vNdYrhR/view](https://drive.google.com/file/d/1j6y5-EEYClElv7B9PWarXUO89vNdYrhR/view)

- 2.2. Download Flash app: [https://www.balena.io/etcher/](https://www.balena.io/etcher/)

- 2.3. Disassemble the Gateway cover and take the Micro SD

- 2.4. Connect the Micro SD to your computer

- 2.5. Run flash app, choose the .img and the Micro SD card

# 3. Change setting

- zigbee channel = 25
- extend panid: 1x1
- panid: 67x1
- network key: GENERATE
- transmit power = 20
- Basic topic: z2n/TBH/Zx
- External converter: tuya.js
- *Note*: When change config (which will create a new Zigbee network)
	- You need to delete `data/coordinator_backup.json` file contain old Zigbee network configuration

```yaml
homeassistant:
  discovery_topic: homeassistant
  legacy_entity_attributes: true
  legacy_triggers: true
  status_topic: hass/status
permit_join: false
mqtt:
  base_topic: z2m/CIT/Z2 # Change
  server: mqtt://171.244.173.204:1884
  user: admin
  password: admin
  keepalive: 60
  reject_unauthorized: true
  version: 5
serial:
  port: /dev/ttyUSB0
advanced:
  homeassistant_legacy_entity_attributes: false
  legacy_api: false
  network_key: GENERATE
  log_syslog:
    app_name: Zigbee2MQTT
    eol: /n
    host: localhost
    localhost: localhost
    path: /dev/log
    pid: process.pid
    port: 123
    protocol: tcp4
    type: '5424'
  transmit_power: 20
  channel: 25
  ext_pan_id: # Change xx2
    - 222
    - 222
    - 222
    - 222
    - 222
    - 222
    - 222
    - 222
  pan_id: 6821 # Change 6xx1
  legacy_availability_payload: false
  log_level: debug
  last_seen: ISO_8601
device_options:
  legacy: false
frontend:
  port: 8084
  host: 0.0.0.0
```

# 4. Fix IP address
![[01_Experience/IoT/Zigbee2MQTT/Setup/Z2M fix static IP for GW/Z2M fix static IP for GW]]


# 5. Copy ssh key


# 6. Delete coordinator_backup.json

- ssh: labiot/Vtnet@1812 (Raspberry: pi/Vtnet@1812)
```bash
sudo systemctl stop zigbee2mqtt
cd /opt/zigbee2mqtt/data
```
- In here:
	- configuration.yaml: Zigbee network configuration
	- database.db: Information of paired devices
	- log/: Log folder
	- tuya.js: module converter: fingerprint -> for recognizing devices when pairing
	- ../note_module/: contains:
		- zigbee2mqtt
		- zigbee_herdsman
		- zibgee_herdsman_converter

```bash
rm coordinator_backup.json
cd /opt/zigbee2mqtt
npm start    (Optional: Manual test)
sudo reboot
```



# 

---
- Status: #done

- Tags: #z2m

- References:
	- [Source for USB flash](https://sonoff.tech/wp-content/uploads/2021/12/SONOFF-Zigbee-3.0-USB-dongle-plus-firmware-flashing-1-1.pdf)
	- [(Updated 202208) Source](https://sonoff.tech/wp-content/uploads/2022/08/SONOFF-Zigbee-3.0-USB-dongle-plus-firmware-flashing-.pdf)

- Related:
	- 
