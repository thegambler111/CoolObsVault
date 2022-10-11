# Protocols in ThingsBoard
- 6 IoT protocols:
	- Why 6?
	- Is 6 enough?
- 4 protocols in app layers
- 2 protocols in transport layers:
	- UDP
	- TCP
	- App layer in UDP and TCP does not have a concrete form
- Payload of lower layer = header + payload of higher layer

# TCP
- Divide information into segments
- ACK
- TCP sliding window ACK:
- Connection oriented
- 3 way hand shake
- Port:
	- Phiên liên kết (port đích và nguồn)
- Yêu cầu tính toàn vẹn tuyệt đối
- Không phù hợp với ứng dụng yêu cầu realtime -> UDP

# UDP
- Phù hợp với ứng dụng yêu cầu realtime:
	- Voice call
	- Live stream
- Faster
- "Connectionless":
	- No connection setup
	- No data recovery

# HTTP
- Default port = 80
- URL format: _protocol_://_hostname_:_port_/_path-and-file-name_
	- Protocol
	- Hostname
	- Port
	- Path-and-file-name
- REQUEST messages:
	- Method
	- URI
	- HTTP version
	- Content Type/Accept
	- Connection
	- Request message body
- RESPONSE messages:
	- Status code
	- Connection
	- Content Type/Accept
	- Keep alive
	- Response message body
- URL in platform need to be configured
- Web hook?

# CoAP
- Component:
	- Method
	- CoAP request: Confirmable/Non-confirmable/acknowledgement/Reset
	- CoAP URL
	- Query
	- Content Type/Accept
	- Token
	- Security
- CoAP ~ HTTP, with less options
- CoAP in UDP
- HTTP in TCP

# LWM2M
- Similarity LWM2M and Zigbee
| LWM2M | Zigbee |
| --------------------------------- | --------------------- |
| Object | Cluster |
| Instance | Endpoint |
| Resource: mandatory/not mandatory | Attribute and command |
| Location path | Network ID |
| Location | Report |

- Object -> Instance -> Resource
- LWM2M $\in$ CoAP $\in$ HTTP

#
---
- Status: #done
- Tags: #IoT_platform
- References:
	- [Source]()
- Related:
