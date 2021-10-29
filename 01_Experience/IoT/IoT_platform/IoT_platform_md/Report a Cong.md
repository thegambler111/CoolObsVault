# What is an IoT platform
## Definition

- IoT platform from Gartner:
	- Full:
		- Enterprises are increasingly connecting a broad variety and number of IoT endpoints to access data from and better manage physical assets that are relevant to their business. Typical IoT-enabled business objectives include traditional benefits, such as improved asset optimization, as well as new business opportunities and revenue models, such as subscribed-to services (versus owned assets). An IoT platform is an on-premises software suite or a cloud service (IoT platform as a service [PaaS]) that monitors and may manage and control various types of endpoints, often via applications business units deploy on the platform. The IoT platform usually provides (or provisions) Web-scale infrastructure capabilities to support basic and advanced IoT solutions and digital business operations.
	-  Main:
		- An IoT platform is an on-premises software suite or a cloud service (IoT platform as a service [PaaS]) that monitors and may manage and control various types of endpoints, often via applications business units deploy on the platform. The IoT platform usually provides (or provisions) Web-scale infrastructure capabilities to support basic and advanced IoT solutions and digital business operations.
	- Short:
		-  An IoT platform is a software or a cloud service that
			- Monitor, manage and control various types of endpoints
			- Provide and provision Web-scale infrastructure to support IoT solutions and digital business operations.
	- TLDR:
		- Monitor and manage endpoints
		- Enable digital solutions and operations

- Industrial IoT platform from Gartner:
	- Full:
		- Gartner defines the market for industrial Internet of Things (IIoT) platforms as a set of integrated software capabilities. These capabilities span efforts to improve asset management decision making, as well as operational visibility and control for plants, depots, infrastructure and equipment within asset-intensive industries. These efforts also occur within related operating environments of those industries. The IIoT platform may be consumed as a technology suite or as an open and general-purpose application platform, or both in combination. The platform is engineered to support the requirements of safety, security and mission criticality associated with industrial assets and their operating environments. The IIoT platform software that resides on devices — such as, controllers, routers, access points, gateways and edge computing systems — is considered part of a distributed IIoT platform.
	- Main:
		- These capabilities span efforts to improve asset management decision making, as well as operational visibility and control for plants, depots, infrastructure and equipment within asset-intensive industries.
		- The platform is engineered to support the requirements of safety, security and mission criticality associated with industrial assets and their operating environments.
	- TLDR:
		- Improve asset control and management
		- Improve safety, security and mission criticality of specific industries
- IIoT platform vs IoT platform:
	- They cover a similar array of capabilities
	- But IIoT platform
		- Has bigger scope
		- Focuses on specific industries
		- Satisfies industry-level security standards
			

## IoT platform structure

- [Intel end-to-end IoT reference architecture](http://d885pvmm0z6oe.cloudfront.net/hubs/intel_80616/assets/downloads/general/Architecture_Specification_Of_An_IOT_Platform.pdf)
	- ![[Images/IoT_platform/IoT_platform_Intel_layers.png]]
		- White blocks are user layers
		- Dark blue blocks are major runtime layers!
		- Light blue blocks are layers for developers

- 6 layers:
	- Connectivity management layer:
		- Provides:
			- Communications protocols
			- APIs
			- Application adapters 
		- To minimally address the integration requirements of:
			- Data
			- Process
			- Enterprise application
			- IIoT ecosystem
		- Between:
			- Devices
			- Gateways
			- Edge
			- Platforms.
	- Data management layer:
		- Ingests (collect and normalize) IoT endpoint and edge device data
		- Stores data from edge to enterprise platforms
		- Provides data accessibility (by devices, IT and OT systems, and external parties, when required)
		- Tracks lineage and flow of data
		- Enforces data and analytics governance policies to ensure the quality, security, privacy and currency of data
	- Analytics layer:
		- Processes:
			- Data streams
			- Contextual data
		- To provide insights into asset state by:
			- Monitoring use
			- Providing indicators
			- Tracking patterns
			- Optimizing asset use.
		- May apply a variety of techniques:
			- Rule engines
			- Event stream processing
			- Data visualization
			- Machine learning
	- Device management (+ control) layer:
		- Creates, provisions, configures, troubleshoots and manages fleets of IoT devices and gateways remotely, in bulk or individually, and securely.
	-  Application enablement and development layer:
		- Enables business applications to analyze data and accomplish IoT-related business functions.
		- Includes:
			- Application enabling infrastructure components
			- Application development
			- Runtime management
			- Digital twins.
	- Security:
		- Software, tools and practices facilitated to
			- Audit and ensure compliance
			- Establish and execute preventive, detective and corrective controls and actions
				- To ensure the privacy and security of data across the IIoT solution.


## Types of IoT platforms

- Connectivity management platform:
	- This is one of the most basic yet highly specialized and widespread types
	- Capabilities:
		- Connection management
		- Invoicing/billing management
		- Connectivity between sensors and servers
		- Management of data rates

- Device management platform
	- This is one of the most common concerns in the world of IoT
	- Capabilities:
		- Device provisioning, 
		- Device authentication, 
		- Logging, 
		- Remote device monitoring and control, 
		- Administration over the air, 
		- Software updates,
		- Security patching, 
		- Troubleshooting, and more. 

- Analytics platform
	- Collecting, storing and making sense of IoT data
	- Capabilities:
		- IoT data collection via compatible communication protocols,
		- Data processing, including transformation, modeling, and the creation of long-term data histories,
		- Scalable data storage clusters to accommodate both structured and unstructured data,
		- Advanced data analytics / Big Data analytics capabilities to identify patterns and relations within the IoT data,
		- Flexible reporting and data visualization tools that can be easily customized.

- Orchestration hub
	- Orchestration hub = CMP + DMP + Analytics platform
	-  Capabilities:
		- Communication management,
		- Forwarding capabilities, 
		- IoT device management,
		- Integration with analytics services.

- Application enablement platform
	- It focuses on data processing and insight generation
	- Capabilities:
		- Rule engines,
		- Highly customizable data visualization tools,
		- The abstraction of the underlying infrastructure.

- Application development platform:
	- It strives to improve the developer experience, community-building and IoT collaboration.
	-  Capabilities:
		- OTA application development in a cloud IDE,
		- Live development and deployment of IoT apps,
		- Integrations with external repositories such as GitHub & GitLab,
		- A marketplace for IoT apps and app templates,
		- Collaborative & community features.

- End-to-end IoT platform:
	- End-to-end IoT platform = CMP + DMP + Analytics platform + AEP + Development platform
	- Ideally, the end-to-end IoT platform is suitable for a variety of use cases and transcends industry borders.
	- Capabilities:
		- Connectivity, 
		- Security by design,
		- Protocol and data structure interoperability, 
		- IoT device management, 
		- Configuration & update management, 
		- Data storage clusters & scalability,
		- Advanced data analytics and ML, 
		- Reports with data visualization and dashboard customization options, 
		- User management with a highly granular authorization structure to enable IoT collaboration, 
		- A cloud app development studio, 
		- Ideally, an IoT app store with ready-made IoT apps and app templates, 
		- Services that allow for IoT app reuse and duplication, 
		- Open APIs to allow for further integrations. 


# IoT platform comparison
## In the world

### Industrial IoT platform

- Based on Gartner's Magic Quadrants and Critical Capabilities published on July 2020, the top IIoT platform vendors are:
	- Hitachi
		- Device management is the weakest point
		- Strengths lies in analytics and edge deployment
	- Microsoft
		- Device management and ease of implementation and use are its weak points
		- Strengths lies in security, analytics and integration
- Other notable vendors:
	- PTC and AWS with high user base
		- PTC has excellent service and support but their Thingworx is expensive and the analytics layer does not meet user's expectation
		- AWS has board range of capabilities but no guide to choose from those capabilities and also bad customer support
	- Software AG and Altizone with good capabilities but lower userbase
		- Software AG has strong integration and master data management capabilities but bad overall ease of implementation and use.
		- Altizone has strong device management capabilities but bad analytics, application enablement and security capabilities.



## In Viettel

### Thingworx

Thingworx provides a good end-to-end IIoT platforms which are very popular worldwide.

Its biggest problems are weak analytics layer and high cost.

### Mainflux vs Thingsboard

- There is no trustworthy source for comparing open-source IoT platform
- One source used in many sites are PAC-RADAR report: ![[Images/IoT_platform/IoT_platform_pac_radar_2021_open_source.png]]
	- From this report, we can see that they value Thingsboard higher than Mainflux
- From many other sources:
	- Mainflux:
		- Its full stack capabilities are developed as microservices containerized by Docker and orchestrated with Kubernetes.
		- It also provides SDK in many programming languages: C/C++, JavaScript, Go and Python
		- => Its more suitable for developing a horizontal platform that different developers can use with ease
	- Thingsboard:
		- It has better data analytics and visualization capabilities
		- It also uses Kafka and Apache Spark to handle complex data processing
		- => Its more suitable for developing a vertical platform that require heavy data processing


# Proposal

- Continue to use Thingsboard as base technology stack
	- Build Viettel's Connectivity management platform
	- Improve the currently used Thingsboard platform
		- Add more connectivity protocols to satisfy more device types
		- Develop extensions suitable for hardware vendors in Vietnam
		- Provide more development tools
		- Improve security of the platform
- Create a base end-to-end IoT platform for people from all kinds of industry to use
- Focus on developing a few vertical solutions served as Viettel products and also promotions to the base platform


# Additional information

## Huawei IoT platform structure
![[01_Experience/IoT/IoT_platform/IoT_platform_md/Huawei IoT platform structure.png]]


# 

---
Status: #writing

Tags: #IoT_platform 

References:
- [Types of IoT platforms](https://www.record-evolution.de/en/what-types-of-iot-platforms-are-there-and-how-to-choose-the-right-one/)
- [# An IIoT Platform, an IoT Platform, or MES: What’s the Difference and How to Pick One?](https://www.record-evolution.de/en/industrial-iot-platform-vs-iot-platform-mes-whats-the-difference/)
- [Intel end-to-end IoT reference architecture](http://d885pvmm0z6oe.cloudfront.net/hubs/intel_80616/assets/downloads/general/Architecture_Specification_Of_An_IOT_Platform.pdf)
- [Comparison of some open-source IoT platform](https://cookmyproject.com/blog/mainflux-is-an-innovative-scalable-reliable-open/)

Related:
- 
