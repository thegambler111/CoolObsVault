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

Unlocking
09 56 23 28 0f ea a9 a3 bb 62 4f ad eb f7 58 8d e3 8d 53

09 57 02 9e d1 cb a6 9b c7 6c be 87 bb ee 13 40 ba 84 67

09 58 02 9a 21 45 48 3c 24 a5 53 c1 b6 60 0a 54 50 7c c5

11 55 23 2e ad e4 2b 54 9b f3 61 23 b9 e1 bc 9f df e1 d6

unlocked -> lock
09 59 02 2c c4 52 33 96 a0 b2 84 02 d5 c0 a8 22 6a f6 c0

09 5a 02 e3 e0 9d 0b f2 6a bb 6e 3d 8c 71 2e 5f 49 a3 bb

09 5b 02 04 3c de a3 ee e8 52 1b 13 ed f7 42 b2 84 26 e4

---
dynamic pass
27115587
09 2c 02 cb 34 01 6e e8 77 2c 71 55 c7 84 d8 76 41 94 d6

---
One time pass
587850
09 39 02 77 bf 3a cc 4b c5 90 ba bc 40 33 7f d8 17 b6 4b

11 61 00 cd 4d f1 9c 48 76 87 05 34 db 7e 37 4a db 4d b0 28 00 6a 4e 4f 73 8e 5c b7 cc 80 6d 1d 17 fa cc fd 09 10 d3 8f 05 d6 34 86 cd bf 4f 78 19 e0 a2

---
Door bell
09 48 02 59 c8 df 5d 5c 6d a2 a2 68 20 a0 a5 3f de 07 1e
09 49 02 18 68 96 74 8a 9e a2 70 33 88 14 b6 be 7f 45 1a
09 4a 02 21 94 32 ec c5 d9 ca 28 60 5e 1a 13 83 7e 99 d2
09 4e 02 1e bb 22 11 b7 11 72 9d d6 b9 af 9f ae ea b5 44

---

Potential password
0a d0 b9 07 2b 13 76 ba 07 2b 12

0a 42 c9 07 2b 13 6a c9 07 2b 12

0a eb c9 07 2b 13 ff c9 07 2b 12


---
door password

<https://github.com/Koenkk/zigbee2mqtt/issues/4478#issuecomment-806310481>

---

#
---
- Status: #writing
- Tags:
- References:
- Related:
