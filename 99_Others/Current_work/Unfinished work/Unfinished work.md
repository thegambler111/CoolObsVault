# Unfinished work
Mission:

Values:

# 2023
- 3 nhiệm vụ chính 2023:
	- Xây dựng IoT Platform để đưa lên Cloud
	- Mở rộng hệ sinh thái IoT, tăng số lượng thiết bị tích hợp
	- Xây dựng các báo cáo gợi ý sản phẩm chiến lược
- Xây dựng CTKT ATTT cho IoT platform
	- Deadline 28/2

---

# Queue
- Thành lập nhóm tìm hiểu các use case iot trên thế giới (theo quý)
- Chặn quyền các anh nhóm thiết bị
- Tìm hiểu các loại kết nối Modbus, EDP
- So sánh MQTT vs LwM2M:
	- OneNet đẩy mạnh LwM2M -> Why
- Hoàn thiện các yêu cầu để đạt -> KNL 13
- Tạo document về phần kịch bản tự động app base cho outsource
- Định cỡ cloud

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
	- [x] LinkedIn
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
- Đầu việc -> Scope -> Nguồn lực
- Check số lượng phần cứng và firmware của các vendor khác
	- => Số lượng firmware cần làm
	- Chứng minh tại sao phải làm
	- Phạm vi, nguồn lực
- Học theo OneNet của Huawei
- Các công việc khác ngoài phần firmware
- CMP:
	- Check ctkt cũ
	- Check nhu cầu vtt
	- Check cmp của vht
		- Nếu vht ok -> yêu cầu hỗ trợ
		- Nếu vtn làm thì ai làm
	- Nếu ko có VHT thì theo OneNet
- DMP
	- Tại sao phải làm
	- Đầu việc không liên quan đến loại thiết bị cụ thể
	- Phụ thuộc hệ sinh thái
		- Đã làm:
			- Smart home
			- Smart community
		- Sẽ làm:
			- Smart home:
				- Sẽ làm phần nào
				- Sẽ làm những thiết bị nào
			- Smart community
				- Theo chiến lược TĐ
			- Các lĩnh vực tiềm năng khác
				- Smart agriculture -> A Tân
					- Xem lại TH TrueMilk chỗ Phòng Di động
				- Smart city -> Kiệt
				- Bố sung thêm 2 lĩnh vực nữa
	- Sở cứ: Tiềm năng, trên thế giới đã làm ntn
	- Framework
	- Công việc -> Nguồn lực
- AEP:
	- Các công việc cần làm
		- Feature
		- Đầu việc
	- Kế hoạch cho bên CĐS -> Đầu mối cụ thể
		- CĐS làm bao nhiêu
		- Outsource ?
- 5G:
	- Manufacture: Inspect
	- Mining:
	- Port
	- Steel
		- Xu thế
		- Ứng dụng sử dụng 5G -> Tích hợp trên Private network ntn
		- Thực tế các nhà mạng
		- => Scope là gì, đầu việc, ai làm
	- ViettelPost
- Học tập
	- -> Xem các điều kiện của khung năng lực bậc trên
	- PMP:
		- <https://www.udemy.com/course/pmp-certification-exam-prep-course-pmbok-6th-edition/>

---

---

# Thay đổi KNL
- Chứng chỉ: -> Hoàn thành được
	- Chuyên môn: 3
	- Kỹ năng: 5
- Kinh nghiệm:
	- 3 năm -> Đạt
	- Chủ trì ứng dụng và triển khai giải pháp ở **quy mô khu vực** -> Chưa đạt
	- Chủ trì hướng dẫn triển khai/CTKT/QHTK/HLD/LLD -> Hiện đã làm 1 bản CTKT sơ bộ của app base và 1 CTKT sơ bộ của platform, liệu có được tính?
	- Có kinh nghiệm giải quyết vấn đề nghiêm trọng -> Gateway Zigbee tòa nhà thái bình có được tính ko ạ?
- Chia sẻ kinh nghiệm:
	- Yêu cầu 3 điểm -> Cần thêm 2 điểm nữa, có thể sử dụng cách tạo seminar để hoàn thành được
- SKYT:
	- Yêu cầu 2 sáng kiến -> Hiện đã có 1 sáng kiến Zigbee Gateway
	- Giá trị làm lợi 0.5 tỷ -> Chưa có

---

# CTKT IoT platform
- Check lại các chỉ tiêu của Thingsboard đã đảm bảo
	- -> Chỉ tiêu cần phát triển thêm
- Check lại các tính năng, xem cái nào cần làm, cái nào Thingsboard đã có sẵn
- Các tính năng người dùng cần từ platform
	- -> Tham khảo onenet

---

# Tính năng người sử dụng platform cần
- Quản lý thiết bị theo
	- Chủng loại -> Template
	- Cá thể -> Device
- Dịch bản tin theo chủng loại thiết bị
- Quản lý thiết bị theo nhóm
- 

---
- Connection module
	- Create procedure to connect to platform through NB-IoT
		- Attach to network
		- Initialize connection through HTTP, MQTT, ....
		- Network monitoring
- Battery monitoring
	- Collect and report battery status
- Logging:
	- Store
- Advance
	- Remote configure
	- Debug mode
	- 
- Security
	- Support TLS
- OTA
	- 

#
---
- Status: #writing
- Tags:
- References:
- Related:
