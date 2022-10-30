# Device management
- Device management (DM):
	- Provisioning
	- Configurations
	- Update on firmware
	- Status
	- Diagnostic information
- IoT DM characteristics
	- Resource constraint devices
	- Machine-to-machine communication
	- Efficient, autonomous, and secure management operations
	- Support deployment at scale
	- Address the entire life cycle of a device
- Advantages:
	- Support deployment at scale
	- Reduce operational and maintenance costs
	- Mitigate security risks
	- Reduce business risks

# Device classification
 - Hardware capability attributes
	- Compute power
	- Storage
	- Network connectivity options
	- Sensing capability
	- Power
- Communication:
	- Unidirectional: Send or receive data
	- Bidirectional: Send and receive data
- Functions
	- M2M gateway
	- M2M devices
	- Proxy/relay devices

# DM architecture

# DM functionalities
- Pre-deployment
	- Security credentials and policies
	- Initializing device metadata
- Post-deployment
	- Device provisioning or re-provisioning
	- Device onboarding
- Operation/Maintenance
	- Device configuration
	- Change device metadata
	- Securely changing or updating device software/firmware
	- Creating event alerts, diagnostic information, or event logs
- Decommission
	- Decommissioning or removing a device from the DM registry on DM servers

# DM standards for IoT/M2M
- TR-069
	- Version 1.4 - 2014
	- Functions: 
		- Auto-configuration and dynamic service provisioning
		- Firmware image management
		- Software module management
		- Status and performance monitoring and diagnostics
- OMA DM
	- Version 2.0 - 2016
	- Functions:
		- Setting initial configuration information:
			- Provision, installation and updates of persistent information
		- Retrieval of management information
		- Processing, events and alarms 
- OMA LightweightM2M (LwM2M)
- oneM2M

# Message transfer protocols
- HTTP: "heavy-weight"
- MQTT and CoAP: 'light-weight'
- MQTTSN is used when TCP connection is not available

## CoAP
- Constrained Application Protocol
- CoAP endpoints can directly interoperate with each other, or with HTTP and RESTful web services through CoAP proxies
- CoAP runs over connectionless UDP datagrams, and is possible to run over SMS or TCP bears

# LwM2M
## Entities
- LwM2M entities:
	- Server
	- Client
## Resource model
### Resource
- Resource is a piece of information made available by the client
- There are 3 resource actions:
	- Read
	- Write
	- Execute
		- For executable resource
### Object
- Object is an entity which resources are logically organized into
- An object must be instantiated
	- An instantiated object is called Object instance
- Object definition:
	- Name
	- Object ID: 16-bit Uint
	- Instances: Single/Multiple
	- Mandatory: Mandatory/Optional
	- URN:
		- Unique, uniform name of object
- Form of URN:
	- `urn:oma:lwm2m:{oma,ext,x}:{Object ID}[:{version}]`
		- {oma,ext,x}:
			- oma: Object is defined by OMA (Open Mobile Alliance)
			- ext: Object is defined a third party standards development organization
			- x: Object is defined a company or an individual
		- {version}: is optionally used in case an Object has many versions
- Example of URN:
	- Firmware update object defined by OMA:
		- `urn:oma:lwm2m:oma:5
	- Temperature sensor object defined by the IPSO Alliance
		- `urn:oma:lwm2m:ext:3303
	- HostDeviceInfo object Defined by AT&T
		- `urn:oma:lwm2m:x:10241

### Object/Resource identifier:
- Format:
	- /{Object ID}/{Object Instance ID}/{Resource ID}

### Data format
- Plain text:
	- For Read and Write
- Opaque:
	- For Read and Write
	- Resource value is in an opaque sequence of binary octets
- TLV (Type-length-value):
	- For Read and Write
	- An array of values
- JSON
	- For Read and Write
	- Used to transport multiple Object instances, resources

## Interfaces
- 4 interfaces:
	- Bootstrap
	- Client registration
	- Device management and Service enablement
	- Information Reporting
### Bootstrap
- Used for server to provision bootstrap information into client
- 4 modes to initiate bootstrap sequence:
	- Factory Bootstrap:
		- Pre-deployment configuration on client
	- Bootstrap from Smartcard:
		- Client retrieves bootstrap information from the Smartcard
	- Client/server initiated bootstrap:
		- Bootstrap procedure initiated by a client or server
		- Require a LwM2M bootstrap server to help client connect to server
		- The client must be pre-provisioned to have the bootstrap server account
### Client registration
- Used to register client with one or more servers
- There are three operations
	- Register
		- Set registration lifetime
	- Update registration information
	- Deregister
		- Deregister is sent when
			- Client want to close the connection
			- Server is shutting down
###  Device management and Service enablement
- Used by server to access client resources
- Available operations:
	- Create
	- Read
	- Write
	- Delete
	- Execute
	- Discover
### Information Reporting
- Used by client to report resource information to server (when changes happen)

## Security
### Authorization
- Server need to be authorized to access Object instance and resource of client
- Authorization is provided through access control object instances within client
- All communication between client and server or bootstrap server are authorized
### Confidentiality and Data integrity
- All communication between client and server or bootstrap server are encrypted and integrity protected

### DTLS
- DTLS 1.2 is used in LwM2M
- There are 3 types of credentials supported:
	- Pre-shared key
	- Raw public key
	- Certificate

|                        | Pre-shared key          | Raw public key                | Certificate                      |
| ---------------------- | ----------------------- | ----------------------------- | -------------------------------- |
| Security mode          | 0                       | 1                             | 2                                |
| Public key or identity | Pre-shared key identity | Raw public key of DTLS client | x.509 certificate of DTLS client |
| Secret key             | Pre-shared key          | Private key of DTLS client    | Private key of DTLS client       |
| Server public key      |                         | Raw public key of DTLS server | Certificate of DTLS server       | 

## Leshan example






#
---
- Status: #done
- Tags: #IoT
- References:
	- [Source](https://www.linkedin.com/learning/iot-foundations-device-management)
- Related:
