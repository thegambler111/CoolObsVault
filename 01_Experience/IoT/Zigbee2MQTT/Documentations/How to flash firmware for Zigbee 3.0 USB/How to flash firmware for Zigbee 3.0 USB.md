# Z2M guide
- [Source](https://www.zigbee2mqtt.io/guide/adapters/#notes)
## Flashing CC1352/CC2652/CC2538 based adapters

Adapters based on CC1352 or CC2652 chips can be flashed by putting them in the bootloader. See your adapter manual on how to do this. After you have done this one of the following tools can be used to flash it.

-   [ZigStar GW Multi toolopen in new window](https://github.com/xyzroe/ZigStarGW-MT) (multi platform GUI tool)
-   [CC2538-BSLopen in new window](https://github.com/JelmerT/cc2538-bsl) (multi platform Python based command line tool) ([instructions](https://www.zigbee2mqtt.io/guide/adapters/flashing/flashing_via_cc2538-bsl.html))
-   [llama-bslopen in new window](https://github.com/electrolama/llama-bsl) (multi platform Python based command line tool, a fork of cc2538-bsl with added features)
-   Texas Instruments [FLASH PROGRAMMER 2open in new window](https://www.ti.com/tool/FLASH-PROGRAMMER) (Windows only) (can't find your device? read below!)


# Using [FLASH PROGRAMMER 2](https://www.ti.com/tool/FLASH-PROGRAMMER)


## Firmware acquisition

- Download the ZNP firmware of CC2652P USB Dongle from the following link:
	- [https://www.home-assistant.io/integrations/zha](https://www.home-assistant.io/integrations/zha)

![[01_Experience/IoT/Zigbee2MQTT/Documentations/How to flash firmware for Zigbee 3.0 USB/USB firmware 1.png]]
![[01_Experience/IoT/Zigbee2MQTT/Documentations/How to flash firmware for Zigbee 3.0 USB/USB firmware 2.png]]


## Firmware flashing

- CC2652P USB Dongle supports serial port Bootloader to flash firmware.

### Enter the serial port Bootloader

There are two ways for Dongle to enter Bootloader:

#### Manual mode
- Keep pressing the Boot button, restart the device, and release the Boot button after Dongle enters the serial port Bootloader.

#### Automatically enter the serial port Bootloader through a python script
- Step to execute python script:

1. [Download](https://sonoff.synology.me:5001/d/s/mkaJDnFsnqMHQA4kFty9lpMDBKfA764v/rKPut07ljxL6DF3nmYr-LyrBAxjLe4aS-2bHA65meKAk), unzip and execute the file
![[01_Experience/IoT/Zigbee2MQTT/Documentations/How to flash firmware for Zigbee 3.0 USB/python 1.png]]

2. Enter the serial port number inserted into the dongle
![[01_Experience/IoT/Zigbee2MQTT/Documentations/How to flash firmware for Zigbee 3.0 USB/python 2.png]]

3. After executing the file, enter 55 55 in the serial port assistant tool, and receive the returned result 00 CC, which means that the dongle has successfully entered the Bootloader.
![[01_Experience/IoT/Zigbee2MQTT/Documentations/How to flash firmware for Zigbee 3.0 USB/python 3.png]]

_Note: The serial port Bootloader does not enable hardware flow control._

### Using Flash Programmer2 serial port flashing firmware
![[01_Experience/IoT/Zigbee2MQTT/Documentations/How to flash firmware for Zigbee 3.0 USB/flash 1.png]]
![[01_Experience/IoT/Zigbee2MQTT/Documentations/How to flash firmware for Zigbee 3.0 USB/flash 2.png]]
_Note: There is no difference between the coordinator and routing firmware flashing steps._


# Using Python
## Setup environment
- Install python, pip and packages
```bash
sudo apt update && sudo apt install python3-pip
sudo pip3 install pyserial intelhex
```

## Download cc2538-bsl
```bash
mkdir cc2538-bsl
cd cc2538-bsl
curl -sSL https://github.com/JelmerT/cc2538- bsl/archive/refs/heads/master.tar.gz | tar xz --strip 1
```


## Download firmwave
- NOTE: If you already have firmware image, skip this step
```bash
wget https://github.com/Koenkk/Z-Stack-firmware/raw/master/coordinator/Z-Stack_3.x.0/bin/CC1352P2_CC2652P_launchpad_coordinator_20220219.zip
unzip CC1352P2_CC2652P_launchpad_coordinator_20220219.zip
```

## Flash firmware

- First you need to find the USB port
	- In MacOS, you can use `ls /dev/*`
```bash
sudo python3 cc2538-bsl.py -ewv -p "your_usb_port" --bootloader-sonoff-usb "path_to_your_image"
```

## Finish
- If the USB is successfully flashed, you will see similar lines like below being printed out:
```
Write done
Verifying by ...
Verified (match: ...)
```



# 

---
- Status: #done

- Tags: 

- References:
	- 

- Related:
	- 
