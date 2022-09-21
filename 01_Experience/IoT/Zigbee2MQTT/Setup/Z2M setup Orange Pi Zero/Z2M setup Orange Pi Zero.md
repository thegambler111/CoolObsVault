# Flash new Armbian OS

## Download Armbian for Orange Pi Zero
- [Website](https://www.armbian.com/orange-pi-zero/)
- Download **stable** version
- Currently using Bullseye version

## Flash the SD card using BalenaEtcher app

## Update the newly installed OS
- Connect through Ethernet
- SSH into the machine with default user: root/1234
	- Remove old hostkey if needed:
 ```bash
 ssh-keygen -R hostname
 ```
- Select terminal type: zsh, instead of ~~bash~~
- Set new account: labiot/Vtnet@1812
- Update OS:
 ```bash
 sudo apt update
 sudo apt upgrade
 ```

## [Disable USB autosuspend](https://www.zigbee2mqtt.io/guide/faq/#zigbee2mqtt-crashes-after-some-time)
- if `cat /sys/module/usbcore/parameters/autosuspend` returns `1` or `2`, USB autosuspend is enabled
- To disable it, run
```bash
sed -i 's/GRUB_CMDLINE_LINUX_DEFAULT="/&usbcore.autosuspend=-1 /' /etc/default/grub
update-grub
systemctl reboot
```


## 
- NOTE: Disable wifi ?????


# Setup Zigbee2MQTT

## Installation with docker:
- Armbian OS Bullseye version for Orange Pi Zero is 32-bit OS -> Cannot install docker which needs 64-bit OS
- => Cannot setup using docker

## Installation in Linux OS

### Determine location of the adapter and checking user permissions
#### For Linux
- Use this command to get the information:

```bash
ls -l /dev/serial/by-id
```
- => Example output:
```
total 0 
lrwxrwxrwx 1 root root 13 Mar  3 11:03 usb-ITead_Sonoff_Zigbee_3.0_USB_Dongle_Plus_cc121a1f3939ec11ae6de0680aac08d5-if00-port0 -> ../../ttyUSB0 
```

- [Check if current user has permission to connect to the adapter](https://www.zigbee2mqtt.io/guide/installation/20_zigbee2mqtt-fails-to-start.html#verify-that-the-user-you-run-zigbee2mqtt-as-has-write-access-to-the-port)
- Location of mounted device to fill in `configuration.yaml` file:
	- **(Recommended)** Using `/dev/tty*` path: Use the part after `->`
		- In the example, it is `../../ttyUSB0` -> The path is `/dev/ttyUSB0`
	- Using the `/dev/serial/by-id/` path: Use the part after hour, before `->`
		- In the example, it is `usb-ITead_Sonoff_Zigbee_3.0_USB_Dongle_Plus_cc121a1f3939ec11ae6de0680aac08d5-if00-port0` -> The path is `/dev/serial/by-id/usb-ITead_Sonoff_Zigbee_3.0_USB_Dongle_Plus_cc121a1f3939ec11ae6de0680aac08d5-if00-port0

- You can check the `/dev/serial/by-id/` path using `/dev/tty*` path:
```bash
find -L /dev/serial/by-id/ -samefile /dev/ttyUSB0
```
- => Example output:
```bash
/dev/serial/by-id/usb-ITead_Sonoff_Zigbee_3.0_USB_Dongle_Plus_cc121a1f3939ec11ae6de0680aac08d5-if00-port0
```

> Note:
> - `/dev/tty*` path can change - for example `/dev/ttyACM0` may become `/dev/ttyACM1`
> - `/dev/serial/by-id/` path depends on adapter devices

- Another way of finding adapter is using `sudo dmesg`: [read more](https://www.zigbee2mqtt.io/guide/getting-started/#_1-find-the-zigbee-adapter)
#### For Windows
- Find port in 'Device manager'

#### For Mac
 - Open terminal and type: `ls /dev/*`.
 - Note the port number listed for `/dev/tty.usbmodem*` or `/dev/tty.usbserial*`. The port number is represented with `*` here.
- [Source](https://www.mathworks.com/help/supportpkg/arduinoio/ug/find-arduino-port-on-windows-mac-and-linux.html)

### Installing

```bash
# Install Node.js and required dependencies
# In Debian/Raspbian bullseye and up (11 and up), NodeJS v12.X is packaged, this is the safest method of installing NodeJS (from official repositories) for Zigbee2MQTT. Older i386 hardware can work with [unofficial-builds.nodejs.org](https://unofficial-builds.nodejs.org/download/release/v12.16.3/ e.g. Version 12.16.3 should work.
# Check https://github.com/nodesource/distributions/blob/master/README.md if you want to install a specific version from NodeJS repositories instead.
sudo apt-get install -y nodejs npm git make g++ gcc

# Verify that the correct nodejs and npm (automatically installed with nodejs)
# version has been installed
node --version  # Should output v10.X, v12.X, v14.X, v15.X or V16.X
npm --version  # Should output 6.X or 7.X

# Clone Zigbee2MQTT repository
git clone https://github.com/Koenkk/zigbee2mqtt.git
sudo mv zigbee2mqtt /opt/zigbee2mqtt

# Install dependencies (as user "pi")
sudo chmod -R 777 /opt
cd /opt/zigbee2mqtt
npm ci
```

### Add environmental variable
- Fix error: JavaScript heap out of memory
- Add this line (not include comments) to `~/.zshrc` file (for zsh) or `~/.bashrc` (for bash):
```bash
# Increase Javascript heap memory (https://github.com/Koenkk/zigbee2mqtt/issues/12081)
# Limit memory of OrangePiZero is 500MB
# If you asign more memory than the system has, it will fail silently :p
#
# In Linux, run command`free -m` and add both 'free' and 'buff/cache' memory
# The sum is the upper limit of memory for npm
# https://stackoverflow.com/a/63495296
# For example: On a machine with 2GB of memory, consider setting this to 1536 (1.5GB)
# For OrangePiZero running Armbian, the upper limit is ~ 350MB
export NODE_OPTIONS=--max_old_space_size=300
```

- Reload `~/.zshrc` for Debian OR `~/.bashrc` for Ubuntu
```bash
source ~/.zshrc
# OR
source ~/.bashrc
```


### Configuring
- Detailed configuration can be found here: https://www.zigbee2mqtt.io/guide/configuration/


- Create `/opt/zigbee2mqtt/data/secret.yaml` file to store MQTT server authentication:
```bash
user: admin
password: admin
# Automatically generate a network key
network_key: GENERATE
```

- Open config file in `/opt/zigbee2mqtt/data/configuration.yaml`
- Change config for MQTT broker under the MQTT part:
	- base_topic: MQTT base topic for Zigbee2MQTT MQTT messages
	- server: MQTT server URL
	- user/password: MQTT server authentication
```yaml
mqtt:
base_topic: z2m/TBH/Z2
  server: mqtt://171.244.173.204:1884
  user: '!secret user' // admin
  password: '!secret password' // admin
```
- Add:
```yaml
# Disable join when starting Zigbee2MQTT. If enable here, joining will not automatically disable
permit_join: false
advanced:
  # Automatically generate a network key
  network_key: '!secret network_key' // GENERATE
  log_level: info
# Enable front-end
frontend:
  port: 8084
  host: 0.0.0.0
external_converters:
  - tuya.js
```

- Example configuration:
```yaml
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
  ext_pan_id: # Change
    - 222
    - 222
    - 222
    - 222
    - 222
    - 222
    - 222
    - 222
  pan_id: 6821 # Change
  legacy_availability_payload: false
  log_level: debug
  last_seen: ISO_8601
device_options:
  legacy: false
frontend:
  port: 8084
  host: 0.0.0.0
```
```


### Starting Zigbee2MQTT
```bash
cd /opt/zigbee2mqtt
npm start
```


## Running as a daemon with systemctl

### Setup
- Purpose: To run Zigbee2MQTT as daemon (in background) and start it automatically on boot

- Create a systemctl configuration file for Zigbee2MQTT
```bash
sudo vi /etc/systemd/system/zigbee2mqtt.service
```

- Paste the below into systemctl file:
```
[Unit]
Description=zigbee2mqtt
After=network.target

[Service]
ExecStart=/usr/bin/npm start
WorkingDirectory=/opt/zigbee2mqtt
StandardOutput=null
# Or use StandardOutput=inherit if you want to log Zigbee2MQTT messages in syslog, for more options see systemd.exec(5)
StandardError=inherit
Restart=always
RestartSec=10s
User=pi

[Install]
WantedBy=multi-user.target
```

- Check directory of command `npm` and compare with field: ExecStart
```bash
whereis npm
```
- Compare username of Armbian with field: User
- Change field StandardOutput if storage is limited: [Read here for more information](https://www.zigbee2mqtt.io/guide/installation/01_linux.html#optional-running-as-a-daemon-with-systemctl)

### Test
``` bash
# Start Zigbee2MQTT
sudo systemctl start zigbee2mqtt

# Show status
systemctl status zigbee2mqtt.service
```

### Run

- Enable systemctl to start Zigbee2MQTT automatically on boot
```bash
sudo systemctl enable zigbee2mqtt.service
```

### Check Zigbee2MQTT service status

```bash
# Stopping Zigbee2MQTT
sudo systemctl stop zigbee2mqtt

# Starting Zigbee2MQTT
sudo systemctl start zigbee2mqtt

# View the log of Zigbee2MQTT
sudo journalctl -u zigbee2mqtt.service -f
```

### Deamon with nvm
```
[Unit]
Description=zigbee2mqtt
After=network.target

[Service]
ExecStart=/home/labiot/.nvm/nvm-exec npm start
Environment=NODE_VERSION=16
WorkingDirectory=/opt/zigbee2mqtt
StandardOutput=inherit
StandardError=inherit
Restart=always
RestartSec=10s
User=labiot

[Install]
WantedBy=multi-user.target
```
- Source:
	- https://gist.github.com/patoi/f725a9a39d0145bcda4c3796b6419db7
	- https://gist.github.com/joepie91/73ce30dd258296bd24af23e9c5f761aa


## Tuya.js


# Update Zigbee2MQTT to the latest version

```bash
# Stop Zigbee2MQTT and go to directory
sudo systemctl stop zigbee2mqtt
cd /opt/zigbee2mqtt

# Backup configuration
cp -R data data-backup

# Update
git checkout HEAD -- npm-shrinkwrap.json
git pull
npm ci

# Restore configuration
cp -R data-backup/* data
rm -rf data-backup

# Start Zigbee2MQTT
sudo systemctl start zigbee2mqtt
```


# Configuration
## Adapter settings

```yaml
serial:
  # Required: location of the adapter
  port: /dev/ttyUSB0

advanced:
  # Optional: Transmit power setting in dBm (20dBm for CC2652P/CC1352P-2)
  transmit_power: 20
```

### Connect Adapters over TCP
- It's also possible to connect Adapters over TCP. See how to connect a [remote adapter](https://www.zigbee2mqtt.io/advanced/remote-adapter/connect_to_a_remote_adapter.html).

## MQTT

```yaml
mqtt:
  # MQTT base topic for Zigbee2MQTT MQTT messages
  base_topic: z2m/TBH/Z2
  # MQTT server URL
  server: mqtt://171.244.173.204:1884
  # MQTT server authentication
  user: my_user
  password: my_password
```
```yaml
advanced:
  # Disables the legacy api
  # ???????????
  legacy_api: false
```

## Network config
```yaml
advanced:
  # ZigBee channel, changing requires re-pairing of all devices
  # 25 is default channel at TBH building
  channel: 25
  # network encryption key, will improve security
  network_key: [ 1, 3, 5, 7, 9, 11, 13, 15, 0, 2, 4, 6, 8, 10, 12, 13 ]
```

## Frontend

```yaml
frontend:
  # Optional, default 8080
  port: 8084
  # Optional, default 0.0.0.0
  host: 0.0.0.0
```

## Devices and Groups
```yaml
advanced:
  # Optional: Logging level, options: debug, info, warn, error (default: info)
  log_level: info
```

## Device blocklist / passlist
```yaml
# Optional: Block devices from the network (by ieeeAddr) (default: empty)
blocklist:
  - '0x000b57fffec6a5b2'

# Optional: Allow only certain devices to join the network (by ieeeAddr)
# Note that all devices not on the passlist will be removed from the network!
# (default: empty)
passlist:
  - '0x000b57fffec6a5b3'
```

## OTA device firmware update
- Allows to update your Zigbee devices over-the-air.
- Only for devices which have OTA updates via Zigbee2MQTT => Not current switch -> Need to check all devices

## Device-Availability
```yaml
availability:
  active:
    # Time after which an active device will be marked as offline in
    # minutes (default = 10 minutes)
    timeout: 10
  passive:
    # Time after which a passive device will be marked as offline in
    # minutes (default = 1500 minutes aka 25 hours)
    timeout: 1500
```

## Network map
- Config appearance of network map => Skip


## External converters
- You can define external converters to e.g. add support for a DiY device
```yaml
external_converters:
  - tuya.js
```


# Error handling

## Configuration is not consistent with adapter state/backup!

- Behavior:
	- Happened when start the app
- Cause:
	- Changing `data/configuration.yaml`
- Solution:
	- Delete `data/coordinator_backup.`

## Full storage because of big log file:
- Cause:
	- Output of Zigbee2MQTT is currently written in 2 locations:
		- In `journalctl` through the systemd unit
		- Default logging to files under `data/log`
- Solution:
	- Change in file `/etc/systemd/system/zigbee2mqtt.service`, field StandardOutput
	- Read here for more information: https://www.zigbee2mqtt.io/guide/installation/01_linux.html#optional-running-as-a-daemon-with-systemctl

## Limited log files:
- There are only 10 log folders
- Every time the server starts, it will create a new log folder
	- The oldest log folder will be deleted
- Need confirmation:
	- In each log folder there are at most 3 files
	- When a file reach 10MB, the app make a new log file
	- What happen when all 3 files are full (10MB)?

## Error: AREQ - SYS - resetInd after 30000ms
- Happened when running for the first time
- How to fix: Changing `configuration.yaml` file
- => Problem might be in the default configuration file


## Error: JavaScript heap out of memory
- Happened when build and allocated JavaScript memory is too low
- How to fix: Add environmental variables (view in setup steps)


##  Error: Could not locate the bindings file
- Happened when update nodejs and npm
- How to fix:
	- Remove `sudo apt-get remove nodejs npm git make g++ gcc`
	- Reinstall `sudo apt-get install nodejs npm git make g++ gcc`

## Error: Permission denied on USB port
- [Check if current user has permission to connect to the adapter](https://www.zigbee2mqtt.io/guide/installation/20_zigbee2mqtt-fails-to-start.html#verify-that-the-user-you-run-zigbee2mqtt-as-has-write-access-to-the-port)





# 

---
- Status: #writing

- Tags: #z2m #IoT 

- References:
	- [Source](https://www.zigbee2mqtt.io/guide/installation/01_linux.html#determine-location-of-the-adapter-and-checking-user-permissions)

- Related:
	- 
