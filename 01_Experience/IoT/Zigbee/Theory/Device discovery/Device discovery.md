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

# Device Profile

## Device and Service Discovery

### Device Discovery:
- Provides the ability for a device to determine the identity of other devices on the PAN.
- Device Discovery is supported for both
	- The 64-bit IEEE address
	- The 16-bit Network address.
- Device Discovery messages can be used in one of two ways:
	- Broadcast addressed:
		- All devices on the network shall respond
			- ZigBee End Devices shall respond with just their address.
			- ZigBee Coordinators and ZigBee Routers shall respond with their address as the first entry followed by the addresses of their associated devices
	- Unicast addressed:
		- Only the specified device responds.
			- A ZigBee End Device shall respond only with its address.
			- A ZigBee Coordinator or Router shall reply with its own address and the address of each associated child device.

### Service Discovery:
- Provides the ability for a device to determine services offered by other devices on the PAN.
- These service discovery functions belongs to "Profile: ZigBee Device Profile (0x0000)
"
- Service Discovery messages can be used in one of two ways:
	- Broadcast addressed:
		- Only the individual device or the primary discovery cache shall respond
			- Device will only respond their information.
			- If the device is sleeping, their parent node will do it instead (if the parent holds cached discovery information)
	- Unicast addressed:
		- Only the specified device shall respond.
		- In the case of a ZigBee Coordinator or ZigBee Router shall respond instead of their sleeping child node
- Service Discovery is supported with the following query types:
	- Active Endpoint:
		- Command enquires active end-points
		- Unicast addressed.
	- Match Simple Descriptor:
		- This command permits enquiring devices to
			- Supply a Profile ID (and, optionally, lists of input and/or output Cluster IDs)
			- Return the identity of an endpoint which matches the supplied criteria.
		- Unicast addressed or broadcast to all devices which macRxOnWhenIdle = TRUE
	- Simple Descriptor:
		- Command enquires Simple Descriptor from the specified device.
		- Unicast addressed.
	- Node Descriptor:
		- Command enquires Node Descriptor from the specified device.
		- Unicast addressed.
	- Power Descriptor:
		- Command enquires Power Descriptor from the specified device.
		- Unicast addressed.
	- Complex Descriptor:
		- Optional command enquires Complex Descriptor from the specified device.
		- Unicast addressed.
	- User Descriptor:
		- Optional command enquires User Descriptor from the specified device.
		- Unicast addressed.

## End Device Bind

## Bind and Unbind

## Binding Table Management

## Network Management

# Client Services (requests)

## Match_Desc_req
- Local device is the device which send the command
- Remote device is the device which receive the command
- The Match_Desc_req command (ClusterID=0x0006) format

| Name              | Type                     | Valid Range        | Bytes    | Description                                                                                                                   |
| ----------------- | ------------------------ | ------------------ | -------- | ----------------------------------------------------------------------------------------------------------------------------- |
| NWKAddrOfInterest | Device Address           | 16-bit NWK address | 2        | NWK address for the request; 0xfffd if broadcast                                                                              |
| ProfileID         | Integer                  | 0x0000-0xffff      | 2        | Profile ID to be matched at the destination.                                                                                  |
| NumInClusters     | Integer                  | 0x00-0xff          | 1        | The number of Input Clusters in the InClusterList.                                                                            |
| InClusterList     | 2 bytes * NumInClusters  | 0                  | Variable | List of Input ClusterIDs to be used for matching; these clusters are in list of supported output clusters of the Local Device |
| NumOutClusters    | Integer                  | 0x00-0xff          | 1        | The number of Output Clusters in OutClusterList.                                                                              |
| OutClusterList    | 2 bytes * NumOutClusters | 0                  | Variable | List of Output ClusterIDs to be used for matching; these clusters are in list of supported input clusters of the Local Device |

# Server Services (responses)
| Name              | Type            | Valid Range                                                 | Bytes    | Description                                                                   |
| ----------------- | --------------- | ----------------------------------------------------------- | -------- | ----------------------------------------------------------------------------- |
| Status            | Integer         | SUCCESS, DEVICE_NOT_FOUND, INV_REQUESTTYPE or NO_DESCRIPTOR | 1        | The status of the Match_Desc_req command.                                     |
| NWKAddrOfInterest | Device Ad-dress | 16-bit NWK address                                          | 2        | NWK address for the request.                                                  |
| MatchLength       | Integer         | 0x00-0xff                                                   | 1        | The count of endpoints on the Re-mote Device that match the request criteria. |
| MatchList         | 0               | 0                                                           | Variable | List of bytes each of which represents an 8-bit endpoint.                     |





#
---
- Status: #done
- Tags: #zigbee
- References:
	- Source: Zigbee specification
- Related:
