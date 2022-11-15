# Unfinished work
Mission:

Values:

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

# Daily:
- Verify writing Duc and Trung
- Help Tu setup
- Platform breakdown
	- **HTTP**
	- LWM2M
	- UDP
- CTKT GW
	- How many part
- Vision
- Commit herdsman
- Đặt mua Hue Bridge
- Khóa học quý 4
	- [x] MQTT
	- LinkedIn
	- 3xAI
	- Big data
- [x] Count PIR
- [x] Họp thống nhất lại quy trình sniff thiết bị Zigbee
	- [x] Chuẩn bị nội dung
- [x] Chuyển hàng anh Thi
- [x] Thiết kế app base:
- [x] Công việc quý 4
	- [x] Zigbee
	- [x] **Platform**
		- [x] Sáng T2 chia việc tích hợp thiết bị
- [x] GW setup Đức
- [x] FTTH
- [x] Update GW HCM
- [x] Chuyển cảm biến Moes -> HCM
- [x] Anh Tân
- [x] ssh tb server
---
- K8s:
	- Triển khai xong K8S trên 5 server với sự giúp đỡ của CĐS
		- -> Tự triển khai trên con 227 để làm chủ
	- Chưa có kinh nghiệm về phần kết nối giữa các thành phần của K8S
- HTTP:
	- Mục tiêu: Tích hợp thiết bị HTTP <= 1 ngày
	- Hiện tại:
		- Tích hợp qua Gateway
			- Host HTTP: nhận bản tin từ thiết bị để điều phối về Platform
			- Converter: xử lý dữ liệu từ thiết bị và bắn lên MQTT broker của Thingsboard
		- Thingsboard có khả năng tích hợp trực tiếp HTTPs
			- Tuy nhiên hiện tại địa chỉ của thiết bị chưa custumize được hoàn toàn
			- -> Nếu customize được thì hoàn thành mục tiêu
	- Kế hoạch:
		- Gạt bỏ Gateway, kết nối trực tiếp đến platform, đoạn converter sẽ đẩy lên rulechain
			- Tìm hiểu cách chuyển bản tin về Rule chain để xử lý
				- Bản tin cần điều kiện gì để vào được Rule Chain
			- Tìm cách tạo các node custom trong Rule Chain
				- Trước mắt sẽ là các node mới cho HTTP
				- Sau này sẽ là các node có khả năng custom cao, dành cho mọi giao thức

---
-> Nhờ anh Sáng phòng chiến lược cũ






---
#
---
- Status: #writing
- Tags:
- References:
- Related:
