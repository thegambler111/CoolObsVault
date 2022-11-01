# Unfinished work
Mission:

Values:

---
- Quý 4:
	- IoT Platform Cần bổ sung gì để kinh doanh được trên cloud -> Lộ trình
		- Tính năng:
			- ATTT
			- API
			- Time
		- Tính cước
		- Mô hình trên thế giới
			- Bài toán đặt ra
				- Cho team
				- Cho CĐS
		- Mục tiêu:
			- Cung cấp cho khách hàng developer
				- Cung cấp cho người dùng
		- CMP tự làm
		- AEP -> CĐS
		- Lên danh sách đầu mục các công việc cần làm để phát triển IoT platform
---

- [ ] Plan Zigbee
	- [ ] Định cỡ
		- [ ] Mở rộng theo chiều rộng (tính năng):
			- Tích hợp với router wifi
			- Kịch bản tự động tại GW
			- Phân chia chức năng giữa GW và platform
			- Tại sao MQTT?
			- Thêm phương thức tích hợp: QR code?
			- Tự động tạo profile thiết bị mới
		- [ ] Mở rộng theo chiều sâu (code + tối ưu):
			- Bổ sung tính năng:
				- Theo Zigbee
				- Theo GW
			- Tính năng:
				- Lựa chọn tần số
				- Group
				- Đánh giá phần cứng
		- [ ] Lộ trình Zigbee:
			- Về tính năng vs GW vendor
			- Chạy song song với việc tối ưu
		- [ ] Kế hoạch dài hạn:
			- Kế hoạch năm, hoàn thành trong quý 4 -> Xin ngân sách
				- Nhân sự
				- Mua thiết bị
				- Tư vấn
				- Outsource
	- [ ] Đánh giá lại công việc của Tú
		- [ ] Giám sát
		- [ ] Quản lý chất lượng
		- [ ] Đánh giá Prometheus có phù hợp với GW ko? (về phần cứng)
- [ ] Platform: Tập trung phần
	- [ ] Transport
	- [ ] Rule engine: -> Tham khảo Home Assistant
		- Message
		- Method
	- [ ] A Công gợi ý: Làm sâu giao thức HTTP (do có nhiều mục đính sử dụng)
- [ ] Tài liệu VTNet
	- Lựa chọn kiến trúc
	- Lựa chọn môi trường
	- Không liên quan code

---
- Việt:
	- Flow tích hợp thiết bị
		- Xác thực
		- Dịch tin
			- Hướng 1: theo Byte -> word -> data
			- Hướng 2: Json
	- UDP:
		- Ko có chuẩn bản tin
		- Chỉ có 2 thông tin src/des port và payload
		- IP định trước
		- Xác thực:
			- Chọn rule chain để xử lý
				- Quy hoạch theo port
				- Phân loại trong rule chain
			- Định danh:
				- Nhận dữ liệu -> xử lý payload -> Rule chain
- HTTP:
	- Quy hoạch
- CTKT GW: -> Assign
	- Phần cứng
	- Tính năng
		- Coordinator: Mạng Zigbee
		- GW: MQTT
	- Hiệu năng:
		- Zigbee:
			- Khả năng quản lý:
		- GW:
			- Wifi/Ethernet
			- Ipv6

---

# Daily:
- Verify writing Duc and Trung
- [x] Count PIR
- Help Tu setup
- Platform breakdown
	- LWM2M
	- HTTP
	- UDP
- CTKT GW
	- How many part
- Vision
- Commit herdsman
- Chuyển hàng anh Thi
- Đặt mua Hue Bridge
- [x] Họp thống nhất lại quy trình sniff thiết bị Zigbee
	- [x] Chuẩn bị nội dung
- Khóa học quý 4
	- MQTT
	- LinkedIn
	- ....
- [ ] Thiết kế app base:
	- Mục tiêu
		- Test thiết bị
		- Demo cho người dùng
		- Cho phép chủ đầu tư phát triển thành ứng dụng riêng
- Công việc quý 4
	- [x] Zigbee
	- [ ] **Platform**
		- [x] Sáng T2 chia việc tích hợp thiết bị
- [x] GW setup Đức
- [x] FTTH
- [x] Update GW HCM
- [x] Chuyển cảm biến Moes -> HCM
- [x] Anh Tân
- [x] ssh tb server

---

# Quý 4

## Platform
- Mục tiêu cụ thể là: Chuẩn hóa giao thức UDP, TCP, HTTP, LWM2M để đơn giản hóa việc tích hợp các thiết bị Cellular nên nền tảng platform
- Hiện trạng cụ thể
	- 1.Giao thức UDP ==> Tích hợp qua một third party module, phải thực hiện case by case ==> Chưa chuẩn hóa, quy hoạch phương thức tích hợp cho nhiều loại thiết bị khác nhau.
	- 2.Giao thức TCP, HTTP: ==> Cũng tương tự như UDP
	- 3.Giao thức LWM2M: Thingsboard đã phát triển một service chuyên biệt cho LWM2M, nhưng làm thực tế với nhiều loại thiết bị thì sinh ra rất nhiều case khù khoằm, không hỗ trợ ==> Cần phát triển thêm
- mục tiêu của mình trong giai đoạn này là làm chủ các giao thức truyền dữ liệu trên nền tảng platform
	- 1.Giao thức MQTT, CoAP, LWM2M ==> Cái này hiện Thingsboard đã phát triển thành các service riêng, tuy nhiên chưa thực sự tiện dụng và adaptive cho tất cả các trường hợp
	- 2.Giao thức HTTP cũng tương tự
	- 3.Giao thức UDP, TCP: Hiện đang nhét hết vào con gateway, không phổ quát được cách tích hợp cho nhiều thiết bị
- nên anh thấy mục tiêu cụ thể của anh em mình là:
	- Với các giao thức đã có service riêng ==> Phát triển nó theo hướng phổ quát cho nhiều thiết bị, dễ dàng cho người dùng tích hợp một loại thiết bị mới (ít nhất có thể làm như kiểu rule chain)
	- Với các giao thức chưa có service riêng ==> Tư duy tạo ra một service mới cho giao thức đó (theo kiểu microservice), cũng hướng tới phổ quát như trên
- cách làm
	- Với mỗi giao thức ==> Bọn em làm rõ khả năng hỗ trợ của Thingsboard hiện tại; các tồn tại, hạn chế; các tính năng mong muốn phát triển
- để làm nhanh thì cần học người đi trước
	- người đi trước ở đây là các nền tảng platform khác đã thương mại ==> Tham khảo nền tảng platform của Huawei, CTWing, Thingsworx
	- ngoài ra cũng có thể tìm thêm một số nền tảng platform mã nguồn mở khác được đánh giá tốt ở phần này
- mình làm tốt phần này thì mới tính tới làm tiếp các bước sau của platform được

### Dũng
- (40%) Tích hợp, xây dựng CTKT, nghiệm thu thiết bị
- (40%) LWM2M
- (10%) Hoàn thành khung năng lực
- (10%) Hoàn thành các khóa học

### Việt
- (40%) Tích hợp, xây dựng CTKT, nghiệm thu thiết bị
- (40%) UDP
- (10%) Hoàn thành khung năng lực
- (10%) Hoàn thành các khóa học

### Kiệt
- (40%) Tích hợp, xây dựng CTKT, nghiệm thu thiết bị
- (20%) Tìm hiểu hướng làm các giao thức HTTP, UDP, LWM2M, MQTT của
	- Các nền tảng platform khác đã thương mại (Huawei, CTWing, Thingsworx)
	- Các nền tảng platform mã nguồn mở khác được đánh giá tốt ở phần này
	- Expected time: 3-5 work day
	- Expected output:tỏn
		- Hướng phát triển các giao thức HTTP, UDP, LWM2M, MQTT trên ThingsBoard
		- Danh sách tổng hợp cách triển khai các giao thức HTTP, UDP, LWM2M, MQTT trên các nền tảng thao khảo
			- Cách tích hợp, bắt tay thiết bị
			- Nội dung bản tin và cách xử lý
			- Bảo mật
			- (Optional) Cách đẩy bản tin lên ứng dụng người dùng
			- ...
			- Nhận xét cách làm đó tại ThingsBoard -> Có nên sử dụng hay ko
- (20%) HTTP
- (10%) Hoàn thành khung năng lực
- (10%) Hoàn thành các khóa học

### Mai Anh
- (60%) Tích hợp, xây dựng CTKT, nghiệm thu thiết bị
- (20%) MQTT
- (20%) Tổng hợp tài liệu hướng dẫn tích hợp thiết bị qua các giao thức HTTP, UDP, LWM2M, MQTT

### Hai
- (20%) MQTT in Platform
- (40%) Tích hợp thiết bị Zigbee
- (20%) Xây dựng hệ thống giám sát chất lượng GW với Tú
- (10%) Xây dựng kế hoạch năm 2023 cho team Zigbee và Platform
- (10%) Hoàn thành các khóa học

---

#
---
- Status: #writing
- Tags:
- References:
- Related:
