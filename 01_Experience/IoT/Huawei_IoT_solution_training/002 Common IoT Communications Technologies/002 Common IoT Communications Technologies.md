# TLDR
- 

# Preface
Starting page: 26
- Common communications technologies can be classified into:
	- Wired communications technologies
	- Wireless communications technologies.

# Wired Communications Technologies

## Ethernet

- 2 layers:
	- Physical layer (PHY):
		- Convert digital signals into analog signals
		- Define:
			- Electrical signals
			- Symbols
			- Line status
			- Clock requirements
			- Data coding scheme
			- The connectors.
	- Data link layers:
		- Media access control (MAC):
			- Responsible for:
				- Sending and receiving data
				- Synchronizing data transmission
				- Identifying errors
				- Controlling the data flow direction.
		- Logical link control (LLC):


## RS-232 and RS-485

| Item                   | RS-232                                                    | RS-485                                                |
| ---------------------- | --------------------------------------------------------- | ----------------------------------------------------- |
| Communication distance | Less than 20 m                                            | 1200 m theoretically; 300–500 m in reality            |
| Transmission mode      | Unbalanced transmission mode; single-ended communications | Balanced transmission mode; differential transmission |
| Number of transceivers | One-to-one communications                                 | A maximum of 128 transceivers on the bus              |
| Transmission rate      | 38.4 kbit/s                                               | 10 Mbit/s                                             |


## M-Bus

- M-Bus (Meter Bus) is a data bus designed for
	- Information transmission
	- Remote reading of utility (water, gas or electricity) meters 
	- Remote power supply system or battery power supply system.
- The maximum transmission distance is 1000 m.
- The M-Bus can supply power to onsite devices.
	- The power supply capability is 5 A.
	- The current of each node < 0.65 mA.

## Power Line Communication

- Power Line Communication (PLC) is a technology to transmit data and media in signals on an electrical power cable
- PLC operates by adding high frequency carrier signals containing information to the wiring system

## Comparison of Wired Communications Technologies

| Communications Mode | Characteristic                                                                              | Application Scenario                          |
| ------------------- | ------------------------------------------------------------------------------------------- | --------------------------------------------- |
| ETH                 | Comprehensive protocol, universal, cost-effective                                           | Intelligent terminal, video surveillance      |
| RS-232              | One-to-one communications, cost-effective, short transmission distance                      | Meters, industrial control                    |
| RS-485              | Bus topology, cost-effective, strong anti-interference capability                           | Industrial instruments, meter reading         |
| M-Bus               | Designed for meter reading, common twisted-pair cables, strong anti-interference capability | Industrial energy consumption data collection |
| PLC                 | For power line communication, wide coverage, easy installation                              | Power grid transmission, electricity meter    | 


# Wireless Communications Technologies

## Short-Range Wireless Communications Technologies

### Bluetooth

- Features:
	- Large-capacity
	- Short distance
	- Maximum data transmission rate of 1 Mbit/s
	- Maximum transmission distance of 10 cm to 10 m.
	- The transmission distance can reach 100 m by increasing the transmit power.
- Advantages:
	- High speed
	- Low power consumption
	- High security 
- Disadvantages:
	- Not suitable for multi-point deployment because of few network nodes

### Wi-Fi

- Wi-Fi allows connecting to a wireless local area network (WLAN) using radio frequency band of
	- 2.4 GHz UHF
	- 5 GHz SHF ISM
- Advantages:
	- Wide coverage
	- Fast data transmission rate
- Disadvantages:
	- Low transmission security
	- Low stability
	- Considerable power consumption
	- Poor networking capability

### ZigBee

- Features:
	- Low complexity
	- Self-organization
	- Widely used in industrial and smart home fields


|                       |                                                       |
| --------------------- | ----------------------------------------------------- |
| Low power consumption | Two batteries can support the device for 6–24 months. |
| Cost-effective        | No patent fee is needed and the cost is about US$2    |
| Low speed             | 20–250 kbit/s                                         |
| Short range           | 10–100 m                                              |
| Low latency           | 15–30 ms                                              |
| Large capacity        | The number of theoretical nodes is 254                |
| High security         | Three security levels                                 |
| Grant free            | 915 MHz, 868 MHz, 2.4 GHz                             |
| Easy networking       | Mesh networking, ad hoc networking                    |
| Low compatibility     | The compatibility of different chips is low.          |
| Difficult to maintain | due to high networking flexibility                    | 


### Z-Wave

- Features
	- RF-based
	- Short range
- Advantages:
	- Simple structure
	- Low rate
	- Low power consumption
	- Low cost
	- High reliability 
- Disadvantages:
	- The standard is not open
	- The chip can only be obtained from Sigma Designs.

### Comparison of Short-Range Wireless Communications Technologies

|           | Frequency band                            | Transmission rate                                                        | Typical distance                 | Typical application                                      |
| --------- | ----------------------------------------- | ------------------------------------------------------------------------ | -------------------------------- | -------------------------------------------------------- |
| Bluetooth | 2.4 GHz                                   | 1 Mbit/s to 24 Mbit/s                                                    | 1–100 m                          | Data exchange between adjacent nodes                     |
| Wi-Fi     | 2.4 GHz <br> 5 GHz                        | 11b: 11 Mbit/s<br> 11g: 54 Mbit/s<br> 11n: 600 Mbit/s<br> 11ac: 1 Gbit/s | 50–100 m                         | WLAN, high-speed Internet access at indoor places        |
| ZigBee    | 868 MHz/915 MHz <br> 2.4 GHz              | 868 MHz: 20 kbit/s<br> 915 MHz: 40 kbit/s<br> 2.4 GHz: 250 kbit/s        | 2.4 GHz band: 10–100 m           | Home automation, building automation, and remote control | 
| Z-Wave    | 868.42 MHz (Europe) <br> 908.42 MHz (USA) | 9.6 kbit/s or 40 kbit/s                                                  | 30 m (indoor) to 100 m (outdoor) | Smart home appliance, monitoring and control             |


## Cellular Mobile Network

### 2G

- Global System for Mobile Communications (GSM):
	- Is the second-generation mobile communications technology
	- The data rate in GSM is 9.6 kbit/s.
- General Packet Radio Service (GPRS)
	- Is an extension of GSM
	- Is a data transmission technology
	- Provides data rates of 56–114 kbit/s

### 3G

- 3G integrates wireless communications and multimedia communications such as the Internet. 
- 3G has three standards: CDMA2000, WCDMA, and TD-SCDMA. 
- The latest WCDMA technology HSPA+ supports a downlink rate of 42 Mbit/s.

### 4G

- 4G includes two modes: 
	- LTE TDD
	- LTE FDD.
- The download speed of 4G exceeds 100 Mbit/s

### 5G

- Theoretical maximum transmission rate of 5G can reach 10 Gbit/s
- Three major 5G application scenarios:
	- Enhanced Mobile Broadband (eMBB)
	- Massive Machine-Type Communications (mMTC)
	- Ultra-Reliable and Low-Latency Communications (uRLLC)

### Comparison of Cellular Mobile Network Technologies

|     | Frequency band                                          | Transmission rate                                                                                | Typical application                                           |
| --- | ------------------------------------------------------- | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------- |
| 2G  | Authorized frequency band (Mainly 900 MHz)              | 114 Kbit/s                                                                                       | POS and smart wearable devices                                |
| 3G  | Authorized frequency band (Mainly 900 MHz and 1800 MHz) | TD-SCDMA: 2.8 Mbit/s<br> CDMA2000: 3.1 Mbit/s<br> WCDMA: 14.4 Mbit/s                             | Vending machine, smart home appliances                        |
| 4G  | Authorized frequency band (1800 MHz to 2600 MHz)        | Downlink:<br> Cat.6 and 7: 220 Mbit/s<br> Cat.9 and 10: 330 Mbit/s                               | Intelligent terminal, video surveillance                      |
| 5G  | Authorized frequency band C-band mmWave                 | 10 Gbit/s<br> (Supported by the Baolong 5000 Downlink rate: 4.6 Gbit/s; uplink rate: 2.5 Gbit/s) | AR, VR, assisted driving, automated driving, and telemedicine | 

## LPWA Communications Technologies

### SigFox

- SigFox network:
	- Uses Ultra Narrow Band (UNB) technology
	- Simplified network architecture
	- Low power consumption
	- Stable connection
	- Unlicensed ISM radio frequency band
		- Europe: 868 MHz
		- US: 915 MHz
	- Transmission distance: over 1000km
	- Maximum of 1 mil IoT terminals

### LoRa

- The Long Range (LoRa):
	- Is a physical-layer-based bidirectional data transmission
	- Uses unlicensed spectrum
	- Solution for network implementation is called LoRaWAN


### NB IoT

- NB-IoT:
	- Is a cellular based narrowband IoT
	- Built on a cellular network
	- Requires the bandwidth of only 180 kHz
	- 
	- Can be directly deployed on legacy GSM, UMTS, and LTE networks
	- Enhanced coverage
	- Wide connections
	- Low rate
	- Low cost
	- Low power consumption
	- Optimal architecture
	- Supports mobility scenarios with a speed of less than 80 km/h according to 3GPP Release 14

### eMTC

- eMTC
	- Low rate
	- Deep coverage
	- Low power consumption
	- Considerable connections.
	- Vs NB-IoT
		- Higher rate (1 Mbit/s)
		- Smaller coverage
		- Higher power consumption
		- Smaller capacity
		- Supports voice communications.

### eLTE-IoT

- eLTE-IoT:
	- Based on an unlicensed spectrum below 1 GHz
	- Flexible and easy-to-deploy lightweight devices
	- Has standard protocol stacks
	- Targets at the enterprise private narrowband IoT market

### Comparison of LPWA Technologies

|          | Frequency band                      | Data rate     | Typical distance | Typical application                                                                              |
| -------- | ----------------------------------- | ------------- | ---------------- | ------------------------------------------------------------------------------------------------ |
| SigFox   | SubG unlicensed frequency band      | 100 bit/s     | 1–50 km          | Smart home appliances, smart electricity meter, mobile healthcare, remote monitoring, and retail |
| LoRa     | SubG unlicensed frequency band      | 0.3–50 kbit/s | 1–20 km          | Smart agriculture, intelligent building, and logistics tracking                                  |
| NB-IoT   | Mainly SubG **licensed** frequency band | < 100 kbit/s  | 1–20 km          | Water meter, parking, pet tracking, trash can, smoke alarm, and retail terminal                  |
| eMTC     | SubG **licensed** frequency band    | < 1 Mbit/s    | 2 km             | Shared bicycle, pet collar, POS, and smart elevator                                              |
| eLTE-IoT | SubG unlicensed frequency band      | < 100 kbit/s  | 3–5 km           | Power grid, street lamp, trash can, and smart campus                                             | 


## Comparison of Wireless Communications Technologies

![[01_Experience/IoT/Huawei_IoT_solution_training/002 Common IoT Communications Technologies/Comparison wireless technologies.png]]




# 

---
Status: #done

Tags: #IoT #Huawei 

References:
- 

Related:
- Huawei IoT solution training
