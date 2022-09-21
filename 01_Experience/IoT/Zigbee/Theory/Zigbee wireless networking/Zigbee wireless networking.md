# ZigBee
![[01_Experience/IoT/Zigbee/Theory/Zigbee wireless networking/Wireless Technologies Compared.png]]

- ZigBee features:
	- Highly reliable
	- Cost-effective
	- Able to achieve very low power
	- Highly secure
	- An open global standard 
- Zigbee constraint:
	- Low data rate -> To achieve the low power and low cost criteria
- ZigBee is all about wireless monitoring and control

## ZigBee Is Highly Reliable
- ZigBee achieves high reliability in a number of ways:
	- IEEE 802.15.4 with O-QPSK and DSSS
		- Modern, robust radio technology
		- Provides excellent performance in low signal-to-noise ratio environments
	- CSMA-CA
		- Before transmitting, ZigBee listens to the channel.
		- When the channel is clear, ZigBee begins to transmit
	- 16-bit CRCs
		- This ensures that the data bits are correct
	- Acknowledgments at each hop
		- Each packet is retried up to 3 times (4 transmissions in total)
		- After 4 failed transmissions, ZigBee informs the sending node
	- Mesh networking to find reliable route
		- Mesh
			- Extended range through multi-hop
			- Ad-hoc formation of the network
			- Automatic route discovery and self healing
		- Other than mesh
			- Provides reliable broadcasting to distribute a message to many nodes in the network
			- Provides multicasting, which can send a message to any given group of nodes
			- Provides tree routing to augment ZigBee mesh networking
	- End-to-end acknowledgments to verify data made it to the destination 
		- Your application can know whether a particular packet was received by the other node
		- ZigBee filters out any duplicate received packets

## ZigBee Is Cost-Effective
- Low silicon (chip) costs
- Low MCU and radio costs
- There are module vendors who provide ready-to-go ZigBee boards.
- Its core technology is free of patent infringements.
- It requires only low cost development environments.
- ZigBee experts are available for consulting or custom engineering.
- There are Application Profiles for ready-made vendor interoperability. 





















# 

---
- Status: #done

- Tags: #zigbee 

- References:
	- [Book: Zigbee wireless networking]

- Related:
	- 
