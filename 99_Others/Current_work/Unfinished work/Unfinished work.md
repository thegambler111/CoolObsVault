# Unfinished work
- [ ] Z2M:
	- [ ] Features:
		- [ ] Gateway functionality
			- [ ] Create CTKT
		- [ ] Create new GW flash image
		- [ ] Cannot connect to MQTT server
		- [ ] SRSP - AF - dataRequest after 6000ms -> Failed to open system journal: No space left on device
		- [x] Fix PIR bugs? -> Broadcast binding
		- [x] Auto check device online status
		- [x] Converter for new devices
			- [x] Making changes in new files only
		- [ ] Bigger and controllable log storage: Currently store ~ logs of 3 days
		- [ ] Zigbee2mqtt front end: file npm run build != file npm install
		- [ ] Logging and reset USB from GW
		- [x] Fix error: changing configuration -> have to delete coordinator_backup ??
		- [ ] Get OTA link for devices
		- [ ] Update GW, USB, devices firmware on the fly
		- [ ] Control GW from platform: Create APIs
		- [ ] Migrate GW to GW using PanID: To replace GW
		- [ ] White list for permit joins: Auto permit join when receive request from devices in this list -> Seem impossible
		- [ ] Disable router ability of some device types
		- [ ] Low LQI warning
			- [ ] Individual device routing
		- [ ] Control all devices of the same type (or have the same function like onOff) (Can we use group?)
	- [ ] Dev environments
		- [x] Windows alias
		- [x] Windows auto sync files
		- [x] npm debug -> Save to file
	- [ ] Request
		- [ ] Not connect to MQTT server
		- [ ] Accidental deletion prevention
		- [ ] PIR frozen

- [ ] Current work:
	- [ ] Camera:
		- [x] **Xin mở đường Ethernet mạng ngoài**
		- [ ] Hệ thống hoạt động ko ổn định (11/7/2022)

	- [ ] Gateway
		- [ ] Quick CI/CD
		- [ ] Verify newly added manufactureName from KKoen's repos
		- [ ] backup data GW Z0-10
		- [ ] Check bulb: auto select color_temp range
			- [ ] => Have not found a way yet







- [ ] Pair programming?

- [ ] Bài test GW => Hỏi Team VCar
	- [ ] Tải
		- [ ] Thiết bị
		- [ ] Bản tin
		- [ ] Bản tin MQTT nhận và bắn
	- [ ] Performance
		- [ ] Công cụ Performance NodeJS (Clinic doctor)
	- [ ] => Kế hoạch chi tiết

- [ ] Test `option` in fromZ and toZ





- [ ] Platform
	- [x] Thời gian phản hồi của platform
	- [ ] Thời gian phản hồi của GW -> T10
		- Command execute: zh/endpoint.ts
		- Command response: zh/controller/controller.ts:669
		- Define an object to store command send time (Something that can be accessed by both sender and reaceiver)
			- When receiving response, search that object for send time
				- Compare send time with receive time -> execute time
	- [ ] Thiết kế app base: Hỏi ý kiến: 20-21, hoàn thiện (họp nếu cần) 22-23, 26 ký
		- Văn bản đặt hàng tt cđs trình ký 26/9 -> CTKT cho app do cđs phát triển
		- App mở để tích hợp thêm thiết bị mới -> cho người cung cấp tự cấu hình (như NBox)
		- Deadline version 1
		- Mục tiêu
			- Test thiết bị
			- Demo cho người dùng
			- Cho phép chủ đầu tư phát triển thành ứng dụng riêng
- [ ] Team GW
	- [x] Git ultimate
	- [ ] Add default profile for device for Mr Hungpm8 -> 21/9
	- [ ] New feature plan -> 26-28/9
		- [ ] Vision
		- [ ] Slogan
			- [ ] Ritual
			- [ ] Language
		- [ ] **Định hướng công việc**
	- [ ] Check pull requests -> Q4
	- [ ] CTKT GW -> Q4
	- [ ] Process to auto reset GW -> 21/9
- [x] Camera
	- [x] Check camera performance
- [ ] Khung năng lực
	- [x] E-learning -> 20/9
	- [ ] Khóa học lab -> Q4
- [ ] Personal
	- [ ] MQTT
- [x] GW z5



test










# 

---
- Status: #writing

- Tags: 

- References:
	- 

- Related:
	- 
