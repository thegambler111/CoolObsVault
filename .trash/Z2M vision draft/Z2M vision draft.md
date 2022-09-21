# ?
- Device pairing
	- Base message structure (Converter)
	- End device function discovery
- Connection monitoring
	- Dynamic heartbeat management?
- Smart wakeup
- Smart reconnect (Accidental deletion prevention)
- Zigbee USB control
	- Logging USB-> Debug
	- Monitoring
	- Auto repair
- MQTT broker connection control
	- Logging communication-> Debug
	- Monitoring
	- Auto repair
- Security
	- MQTT broker connection
- Device group control
- Auto configuration
- Local linkage? (Running internally inside gateway: Binding)
- Hot swap GW: Migrate hardware without losing connections (PanID)
	- GW synchronization?
- Blacklist/whitelist devices

- OTA update of GW and device firmware
- Logging -> Debug -> Move to platform storage
- Ease to install (even end user can do it)
	- Tuya: Connect through same internet connection
- Multi connection protocol GW (Zigbee + Wifi + Bluetooth + )

- Hardware
	- Permit join LED indicator
	- Physical button to join 

- Can be migrate from platform:
	- Device health monitoring
	- Automation


=> Test number of connections

## Current state
# Tính năng đang có:
- Kết nối end device:
	- Pair thiết bị
		- Thiết lập kết nối
		- Khám phá thuộc tính
	- Giám sát kết nối (sử dụng last seen)
	- Tự động cấu hình mạng Zigbee (Dựa trên default option)
	- Local linkage (binding): Thiết bị A trực tiếp điều khiển thiết bị B, không qua gateway (Tính năng chưa hoàn thiện hoặc em chưa biết dùng)
- Giám sát chung:
	- Thiết lập nhóm
	- Ghi nhớ trạng thái (scene)
	- Danh sách blacklist, whitelist
	- Update firmware thiết bị OTA (chưa kiểm tra)
	- Bảo mật (chưa kiểm tra)
# Tính năng cần phát triển thêm:
- Giám sát chung:
	- Smart wakeup
	- Accidental deletion prevention
	- Gateway hotswap (thay GW giữ nguyên trạng thái mạng)
- Kết nối đến USB Zigbee:
	- Ghi log
	- Giám sát
	- Tự động khôi phục
- Kết nối đến MQTT broker:
	- Ghi log
	- Giám sát
	- Tự động khôi phục


# Tuya
- This is implemented through the linkage of devices connected to a gateway, which serves as an "interpreter" for devices designed with different protocols.
- Accidental deletion prevention
	- Under normal conditions, a sub-device will be reset if it is disconnected by mistake. If the user does not pair the network for this sub-device, it will be automatically connected to the previous gateway in three minutes.
- Dynamic heartbeat management
	- The online and offline status of the connected sub-devices can be dynamically detected based on a dynamic heartbeat algorithm. The whole process takes 10 seconds or longer, depending on the number of the connected sub-devices.



# What is the function of Zigbee gateway?
- The gateway device provides a communication bridge between the Zigbee device and the network router.
- [Source](https://support.tuya.com/en/help/_detail/K9skz0lrv6vjb)

# Does Tuya Zigbee module support the gateways of other brands?
- Currently the Tuya's Zigbee devices can only be connected to the Tuya's Zigbee gateway.
- [Source](https://support.tuya.com/en/help/_detail/K9tndv24itu8u)





# 

---
- Status: #done

- Tags: 

- References:
	- 

- Related:
	- 
