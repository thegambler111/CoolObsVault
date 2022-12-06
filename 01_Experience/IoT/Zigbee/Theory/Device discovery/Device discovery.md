# Device discovery

## Device discovery
- Device discovery is:
	- A ZigBee device discover other ZigBee devices.
- There are two forms of device discovery requests:
	- The IEEE address request
		- **Unicast** to a particular device
		- The NWK address of that device is known
	- The NWK address request
		- **Broadcast**
		- Carries the known IEEE address as data payload.

## Service discovery
- Service discovery is:
	- A ZigBee device discover the capabilities of other devices
- Service discovery can be accomplished by:
	- Issuing a query for each endpoint on a given device
	- OR using a match service feature (either broadcast or unicast).
- The service discovery facility defines and utilizes **various descriptors** to outline the capabilities of a device.
- Service discovery information may also be cached in the network

# Zigbee descriptor
- There are 5 descriptors:

| Descriptor Name | Status | Description                                       |
| --------------- | ------ | ------------------------------------------------- |
| Node            | M      | Type and capabilities of the node                 |
| Node power      | M      | Node power characteristics                        |
| Simple          | M      | Device descriptions contained in node             |
| Complex         | O      | Further information about the device descriptions |
| User            | O      | User-definable descriptor                         |

- Descriptor transmission order is from top to bottom of the above table
	- Node -> Node power -> Simple -> User

## Node descriptor
- The node descriptor contains information about the capabilities of the ZigBee node
- Each Zigbee node shall have only one node descriptor
- The fields in node descriptor:

| Field Name                     | Length (Bits) | Description                                                                                                                              |
|--------------------------------|---------------|------------------------------------------------------------------------------------------------------------------------------------------|
| Logical type                   | 3             | Device type of the ZigBee node                                                                                                           |
| Complex descriptor available   | 1             | Whether a complex descriptor is available                                                                                                |
| User descriptor available      | 1             | Whether a user descriptor is available                                                                                                   |
| Reserved                       | 3             |                                                                                                                                          |
| APS flags                      | 3             | This field is currently not supported and shall be set to zero. It specifies the application support sub-layer capabilities of the node. |
| Frequency band                 | 5             | Supported frequency bands                                                                                                                |
| MAC capability flags           | 8             | Specifies the node capabilities                                                                                                          |
| Manufacturer code              | 16            | Manufacturer code allocated by the ZigBee Alliance                                                                                       |
| Maximum buffer size            | 8             | Maximum size of data or commands in bytes passed to or from the application                                                              |
| Maximum incoming transfer size | 16            | Maximum size of data or commands in bytes transferred to this node in one single message transfer                                        |
| Server mask                    | 16            | System server capabilities                                                                                                               |
| Maximum outgoing transfer size | 16            | Maximum size of data or commands in bytes transferred from this node in one single message transfer                                      |
| Descriptor capability field    | 8             | Descriptor capabilities of this node                                                                                                     |

### Logical Type Field
| Type Value | Description        |
| ---------- | ------------------ |
| 00         | ZigBee coordinator |
| 01         | ZigBee router      |
| 10         | ZigBee end device  |
| 011-111    | Reserved           |

### Frequency Band Field
- Each bit corresponds to a frequency band

| Frequency Band Field Bit Number | Supported Frequency Band                                |
| ------------------------------- | ------------------------------------------------------- |
| 0                               | 868 – 868.6 MHz BPSK                                    |
| 1                               | Reserved                                                |
| 2                               | 902 – 928 MHz BPSK                                      |
| 3                               | 2400 – 2483.5 MHz                                       |
| 4                               | European FSK sub-GHz bands: (863-876MHz and 915-921MHz) |

### MAC Capability Flags Field
| Bits | Capability                | Value = 1                                                                           | Value = 0                      |
|------|---------------------------|-------------------------------------------------------------------------------------|--------------------------------|
| 0    | Alternate PAN coordinator | The node is capable of becoming a PAN coordinator                                   | Otherwise                      |
| 1    | Device type               | Fll function device                                                                 | Reduced function device        |
| 2    | Power source              | The current power source is mains power                                             | Otherwise                      |
| 3    | Receiver on when idle     | Not disable the receiver when idle                                                  | Disable the receiver when idle |
| 4-5  | Reserved                  |                                                                                     |                                |
| 6    | Security capability       | Device is capable of sending and re-ceiving frames secured using the security suite | Otherwise                      |
| 7    | Allocate address          |

### Server Mask Field
| Bit Number | Assignment                  |
|------------|-----------------------------|
| 0          | Primary Trust Center        |
| 1          | Backup Trust Center         |
| 2          | Primary Binding Table Cache |
| 3          | Backup Binding Table Cache  |
| 4          | Primary Discovery Cache     |
| 5          | Backup Discovery Cache      |
| 6          | Network Manager             |
| 7 – 8      | Reserved                    |
| 9 – 15     | Stack Compliance Revision   |

- Stack Compliance Revision indicate the revision of the ZigBee Pro Core specification that the running stack is implemented to

### Descriptor Capability Field
| Bit Number | Assignment                                |
|------------|-------------------------------------------|
| 0          | Extended Active Endpoint List Available   |
| 1          | Extended Simple Descriptor List Available |
| 2–7        | Reserved                                  |
## Node Power Descriptor
## Simple Descriptor
## Complex Descriptor
## User Descriptor
# The following capabilities exist for device and service discovery:
- Device Discovery: Provides the ability for a device to determine the identity of other devices on the PAN. Device Discovery is supported for both the 64-bit IEEE address and the 16-bit Network address.
	- Device Discovery messages can be used in one of two ways:
		- Broadcast addressed:
			- All devices on the network shall respond according to the Logical De-vice Type and the matching criteria. ZigBee End Devices shall respond with just their address. ZigBee Coordinators and ZigBee Routers with associated devices shall respond with their ad-dress as the first entry followed by the addresses of their associated devices depending on the type of request. The responding devices shall employ APS acknowledged service on the unicast responses.
		- Unicast addressed:
			- Only the specified device responds. A ZigBee End Device shall respond only with its address. A ZigBee Coordinator or Router shall reply with its own address and the address of each associated child device. Inclusion of the associated child devices allows the requestor to determine the network topology underlying the specified device.
- Service Discovery: Provides the ability for a device to determine services offered by other devices on the PAN.
	- Service Discovery messages can be used in one of two ways:
		- Broadcast addressed:
			- Due to the volume of information that could be returned, only the individual device or the primary discovery cache shall respond with the matching criteria established in the request. The primary discovery cache shall only respond in this case if it holds cached discovery information for the NWKAddrOfInterest from the request. The responding devices shall also employ APS acknowledged service on the unicast responses.
		- Unicast addressed:
			- Only the specified device shall respond. In the case of a ZigBee Coordinator or ZigBee Router, these devices shall cache the Service Discovery information for sleeping associated devices and respond on their behalf.
- Service Discovery is supported with the following query types:
	- Active Endpoint:
		- This command permits an enquiring device to determine the active end-points. An active endpoint is one with an application supporting a single profile, described by a Simple Descriptor. The command shall be unicast addressed.
	- Match Simple Descriptor:
		- This command permits enquiring devices to supply a Profile ID (and, optionally, lists of input and/or output Cluster IDs) and ask for a return of the identity of an endpoint on the destination device which matches the supplied criteria. This command may be broadcast to all devices for which macRxOnWhenIdle = TRUE, or unicast addressed. For broadcast addressed requests, the responding device shall employ APS acknowledged service on the unicast responses.
	- Simple Descriptor:
		- This command permits an enquiring device to return the Simple Descriptor for the supplied endpoint. This command shall be unicast addressed.
	- Node Descriptor:
		- This command permits an enquiring device to return the Node Descriptor from the specified device. This command shall be unicast addressed.
	- Power Descriptor:
		- This command permits an enquiring device to return the Power Descriptor from the specified device. This command shall be unicast addressed.
	- Complex Descriptor:
		- This optional command permits an enquiring device to return the Complex Descriptor from the specified device. This command shall be unicast addressed.
	- User Descriptor:
		- This optional command permits an enquiring device to return the User Descriptor from the specified device. This command shall be unicast addressed.

---

  { modelID: 'TS0601', manufacturerName: '_TZE200_eaac7dkw' },
  { modelID: 'TS0601', manufacturerName: '_TZE200_ntcy3xu1' },
  { modelID: 'TS0601', manufacturerName: '_TZE200_vm1gyrso' },
#
---
- Status: #done
- Tags: #zigbee
- References:
	- Source: Zigbee specification
- Related:
