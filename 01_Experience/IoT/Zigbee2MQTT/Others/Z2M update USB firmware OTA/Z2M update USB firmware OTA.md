# 
- Update firmware trực tiếp cho USB Zigbee Sonoff trên Orange Pi/Raspberry Pi
	- Yêu cầu: 
		- Cài đặt Python 3: sudo apt-get install -y python3-pip
		- This script uses the pyserial package to communicate with the serial port and chip (https://pypi.org/project/pyserial/). You can install it by running sudo pip install pyserial.
		- If you want to be able to program your device from an Intel Hex file, you will need to install the IntelHex package: https://pypi.python.org/pypi/IntelHex (e.g. by running sudo pip install intelhex).
		- The script will try to auto-detect whether your firmware is a raw binary or an Intel Hex by using python-magic: (https://pypi.python.org/pypi/python-magic). You can install it by running sudo pip install python-magic. Please bear in mind that installation of python-magic may have additional dependencies, depending on your OS: (https://github.com/ahupp/python-magic#dependencies).
		- If python-magic is not installed, the script will try to auto-detect the firmware type by looking at the filename extension, but this is sub-optimal. If the extension is .hex, .ihx or .ihex, the script will assume that the firmware is an Intel Hex file. In all other cases, the firmware will be treated as raw binary.
	- Tải source code cc2538-bsl (https://github.com/JelmerT/cc2538-bsl): sudo git clone https://github.com/JelmerT/cc2538-bsl.git
	- Câu lệnh update firmware: sudo python3 cc2538-bsl.py -e -v -w --bootloader-sonoff-usb ./CC1352P2_CC2652P_launchpad_coordinator_20211217.hex


- Install pip: sudo apt-get install -y python3-pip
- Install pyserial: sudo pip install pyserial
- Install Intel Hex: 
- sudo pip install python-magic


# 

---
- Status: #done

- Tags: #z2m 

- References:
	- 

- Related:
	- 
