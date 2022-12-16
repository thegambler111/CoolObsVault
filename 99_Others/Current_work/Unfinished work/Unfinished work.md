# Unfinished work
Mission:

Values:

# 2023
- 3 nhiệm vụ chính 2023:
	- Xây dựng IoT Platform để đưa lên Cloud
	- Mở rộng hệ sinh thái IoT, tăng số lượng thiết bị tích hợp
	- Xây dựng các báo cáo gợi ý sản phẩm chiến lược
- Xây dựng CTKT ATTT cho IoT platform
	- [[01_Experience/IoT/Viettel IoT Platform/CTKT/ATTT/ATTT]]
	- Deadline 28/2

---

# Queue
- Thành lập nhóm tìm hiểu các use case iot trên thế giới (theo quý)
- Chặn quyền các anh nhóm thiết bị
- Tìm hiểu các loại kết nối Modbus, EDP
- So sánh MQTT vs LwM2M:
	- OneNet đẩy mạnh LwM2M -> Why
- Hoàn thiện các yêu cầu để đạt -> KNL 13

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
- 3 đối tượng người sử dụng:
	- Sản xuất thiết bị
	- Cung cấp giải pháp (thiết bị + firmware + software)
	- Bán giải pháp (Mang giải pháp đi bán)
- 2 sản phẩm 2023
	- Đồng hồ nước
	- Sensor nông nghiệp
		- Hải sản
		- Chăn nuôi, trồng trọt
- ? Tổ chức hội thảo để phát triển cộng đồng IoT Việt Nam
- **Thống nhất**
	- CTKT ok
	- Lập budget làm hết trừ CMP
		- Nếu VHT ko làm CMP -> Đến giữa 2023 sẽ làm phần thiết yếu của CMP
	- Thống nhất công việc cần làm giữa CĐS và CLML
		- -> Trong tháng, đóng gói kế hoạch chi tiết năm 2023: timeline, người làm
			- Cái nào CLML làm end-to-end
			- Cái nào lead, cái nào CĐS làm
			- Cái nào CĐS làm end-to-end
			- Lộ trình theo quý
			- Performances:
				- Số lượng
					- Người dùng
					- Thiết bị
				- Hiệu năng hệ thống
					- Thời gian phản hồi
					- Khả năng xử lý
				- Check performance với OneNet, Tuya
		- -> Quản lý chi tiêu theo quý

---
- IoT platform -> vẽ giá trị làm lợi -> Thuyết phục
- Phát triển firmware NB-IoT
- Sáng kiến phục vụ giải pháp tòa nhà thông minh
	- IoT Gateway:
		- Thay 1x con Gateway tại tòa nhà Thái Bình (5tr/con)
		- Khi mua sử dụng với 5 thiết bị -> ok
		- thực tế 30 thiết bị -> nok
		- Thay cho việc phải mua Gateway mới
	- Sử dụng HomeAssistance để điều khiển tự động
		- Số lượng menMonth
		- Hệ thống bên ngoài giá ntn

---
Giải pháp điều khiển tự động do hãng Quang Thông cung cấp cho dự án Smart Office tồn tại nhiều hạn chế:
- Mỗi thiết bị chỉ được có 1 kịch bản điều khiển tự động và điều khiển toàn thời gian (24/7). Nhu cầu thực tế cần 1 kịch bản có thể điều khiển cùng lúc nhiều thiết bị, hoặc 1 thiết bị có thể được điều khiển bởi nhiều kịch bản khác nhau, và có thể điều khiển theo các khung giờ khác nhau trong ngày, trong tuần.
- Mỗi thiết bị chỉ có thể được điều khiển tự động từ 1 thiết bị khác. Nhu cầu thực tế cần 1 thiết bị cảm biến có thể điều khiển cho 1 nhóm thiết bị, hoặc 1 nhóm cảm biến có thể điều khiển 1 thiết bị, hoặc 1 nhóm cảm biến điều khiển cho cả 1 nhóm thiết bị.
- Mỗi thiết bị chỉ được có 1 kịch bản điều khiển theo lịch vào đúng 1 thời điểm trong ngày. Nhu cầu thực tế cần 1 kịch bản điều khiển theo lịch có thể điều khiển cùng lúc nhiều thiết bị, hoặc 1 thiết bị có thể được điều khiển bởi nhiều kịch bản điều khiển theo lịch khác nhau, và có thể đặt lịch điều khiển vào nhiều thời điểm khác nhau trong ngày, trong tuần.
- Kịch bản được cấu hình theo giao diện dòng lệnh không thân thiện với người dùng, khó triển khai, điều chỉnh, phân tích, quản lý, thống kê, giám sát, chỉ phù hợp cho các nhu cầu cá nhân với số lượng thiết bị ít, kịch bản điều khiển đơn giản.

Giải pháp của đối tác:
- Tích hợp thiết bị thông qua Command line
- Mỗi loại thiết bị có một chuẩn bản tin khác nhau
- Kênh của mạng Zigbee cố định, không tùy chỉnh được
- Cấu hình của Gateway Zigbee cố định
- Không có tích hợp sẵn với các hệ thống quản lý bên ngoài
- Chỉ kết nối được 20 thiết bị/gateway
- Không có khả năng mở rộng tính năng mới

# Tình trạng
Các giải pháp do hãng Quang Thông cung cấp cho dự án Smart Office tồn tại nhiều hạn chế
- Với thiết bị Gateway:
	- Ứng dụng Gateway được cung cấp sử dụng giao diện dòng lệnh, không thân thiện với người dùng, rất khó để cấu hình, quản lý, phân tích
	- Cấu hình của Gateway Zigbee không thay đổi được. Điều này gây khó khăn cho việc tối ưu hệ thống, nhất là trong công đoạn lựa chọn băng tần hoạt động hợp lý để tránh bị nghẽn với hệ thống mạng Wifi tại tòa nhà Thái Bình.
	- Cấu hình của các mạng Zigbee giống hệt nhau, không thay đổi được. Điều này dẫn đến tình trạng thiết bị không phân biệt được mạng Zigbee của các tầng khác nhau, gây ra tình trạng thiết bị tự động chuyển mạng Zigbee giữa các tầng, không ở cố định 1 mạng. Vấn đề này khiến cho người dùng không thể quản lý được thiết bị và thiết bị thường xuyên mất kết nối
	- Mỗi loại thiết bị trong kết nối đến Gateway có một cấu trúc bản tin khác nhau. Điều này làm cho việc vận hành khai thác hệ thống gặp rất nhiều khó khăn do phải xử lý thông tin của mỗi loại thiết bị một cách khác nhau
	- Mỗi Gateway do Quang Thông cung cấp chỉ kết nối được tối đa 15 thiết bị, không đảm bảo nhu cầu sử dụng là 40 thiết bị/ Gateway
	- Ngoài platform, Gateway được cung cấp không có khả năng kết nối, giao tiếp với hệ thống thứ ba, cản trở việc mở rộng dịch vụ của hệ thống
- Với điều khiển tự động:
	- Mỗi thiết bị chỉ được có 1 kịch bản điều khiển tự động và điều khiển toàn thời gian (24/7). Nhu cầu thực tế cần 1 kịch bản có thể điều khiển cùng lúc nhiều thiết bị, hoặc 1 thiết bị có thể được điều khiển bởi nhiều kịch bản khác nhau, và có thể điều khiển theo các khung giờ khác nhau trong ngày, trong tuần.
	- Mỗi thiết bị chỉ có thể được điều khiển tự động từ 1 thiết bị khác. Nhu cầu thực tế cần 1 thiết bị cảm biến có thể điều khiển cho 1 nhóm thiết bị, hoặc 1 nhóm cảm biến có thể điều khiển 1 thiết bị, hoặc 1 nhóm cảm biến điều khiển cho cả 1 nhóm thiết bị.
	- Mỗi thiết bị chỉ được có 1 kịch bản điều khiển theo lịch vào đúng 1 thời điểm trong ngày. Nhu cầu thực tế cần 1 kịch bản điều khiển theo lịch có thể điều khiển cùng lúc nhiều thiết bị, hoặc 1 thiết bị có thể được điều khiển bởi nhiều kịch bản điều khiển theo lịch khác nhau, và có thể đặt lịch điều khiển vào nhiều thời điểm khác nhau trong ngày, trong tuần.
	- Kịch bản được cấu hình theo giao diện dòng lệnh không thân thiện với người dùng, khó triển khai, điều chỉnh, phân tích, quản lý, thống kê, giám sát, chỉ phù hợp cho các nhu cầu cá nhân với số lượng thiết bị ít, kịch bản điều khiển đơn giản.

# Nội dung
Xây dựng các sản phẩm của Viettel hoặc sử dụng các ứng dụng có sẵn:
- Tự xây dựng sản phẩm Gateway Zigbee xử lý được các hạn chế của giải pháp đối tác cung cấp và cho phép phát triển thêm các tính năng nâng cao:
	- Phát triển giao diện trên web cho phép người dùng cấu hình, quản lý một cách thuận tiện, thân thiện
	- Xây dựng quy chuẩn bản tin cho các loại thiết bị Zigbee, cho phép nhân bản quy trình vận hành, khai thác của một loại thiết bị cho nhiều loại thiết bị khác
	- Cho phép thay đổi cấu hình mạng Zigbee cũng như toàn bộ hệ thống Gateway để phù hợp với tình trạng triển khai cũng như nhu cầu thực tế. Từ đó, khắc phục được tình trạng nghẽn mạng do xung khắc tần số với mạng Wifi và vấn đề tự động chuyển mạng của các thiết bị Zigbee
	- Cho phép tích hợp với các hệ thống thứ ba như HomeAssistant
	- Phát triển thêm các tính năng giám sát, cảnh báo, đánh giá hiệu năng thiết bị, hệ thống, giúp tiết kiệm thời gian và công sức vận hành, khai thác
	- Mở rộng khả năng kết nối đến các chủng loại thiết bị khác trên thị trường, mở ra hướng kinh doanh mới cho ngành IoT
- Cài đặt và triển khai hệ thống Home Assistant để cấu hình, vận hành, quản lý, giám sát các kịch bản điều khiển tự động trong dự án Smart Office
	- Cài đặt hệ thống Home Assistant trên hệ thống server có sẵn của Viettel
	- Kết nối hệ thống với IoT platform để thu thập thông tin và điều khiển thiết bị
	- Xây dựng kịch bản tự động cho toàn bộ hệ thống chiếu sáng tại Trụ sở Tổng Công ty
	- Cấu hình kịch bản tự động cho các thiết bị trong dự án Smart office
	- Vận hành, giám sát các kịch bản tự động
	- Tiếp nhận phản ánh và thay đổi kịch bản theo nhu cầu của người dùng

# Khả năng áp dụng
- Giải pháp phần mềm quản lý Gateway Zigbee có thể áp dụng để quản lý gần như toàn bộ các loại thiết bị Zigbee có trên thị trường, cho phép tùy biến và phát triển thêm các tính năng theo yêu cầu người dùng
- Giả pháp điều khiển tự động có thể điều khiển được toàn bộ các loại thiết bị đã được tích hợp với IoT platform của Viettel và áp dụng được cho toàn bộ các dự án IoT tại Viettel (Smart Home, Smart Office, Smart Urban...).

# Điểm mới
- Giải pháp phần mềm quản lý Gateway Zigbee là giải pháp táo bạo, mang tính đột phá cao do lĩnh vực IoT đặc biệt là mảng ứng dụng Zigbee còn mới mẻ chưa có nhiều hãng sản xuất tại Việt Nam
- Giải pháp điều khiển tự động là giải pháp tự nghiên cứu, tìm hiểu và triển khai. Giải pháp đã thay thế và chứng minh sự ưu việt so với giải pháp sẵn có của nhà cung cấp thiết bị. Giải pháp phù hợp cho triển khai mọi dự án IoT lớn nhỏ.

# Hiệu quả
- Giải pháp phần mềm quản lý Gateway Zigbee vừa xử lý được các vấn đề trong dự án Smart office tại Trụ sở Tổng Công ty, vừa mở ra một hướng đi mới cho ngành IoT.
	- Gateway Zigbee do Viettel tự phát triển khắc phục được các lỗi phát sinh của hệ thống cung cấp bởi đối tác, giúp triển khai thành công các ứng dụng Zigbee trong Tòa nhà Thái Bình
	- Gateway tự phát triển bổ sung các tính năng cần thiết cho việc vận hành, khai thác, giúp tiết kiệm 70% thời gian, công sức so với giải pháp được đối tác cung cấp
	- Mở ra hướng phát triển hoàn toàn mới cho ngành IoT: Phát triển hệ sinh thái các thiết bị Zigbee
	- Tiết kiệm được tiền thuê ngoài để phát triển: 30 men month * 35.000.000 = 1.050.000.000
- Giải pháp điều khiển tự động giải quyết được các nhược điểm của giải pháp đối tác cung cấp và đem lại kinh nghiệm để ứng dụng vào việc xây dựng IoT platform của Viettel
	- Khắc phục hoàn toàn các nhược điểm của giải pháp cung cấp bởi hãng. Người dùng có thể tùy ý cấu hình kịch bản với nhiều tác động từ nhóm gồm tùy ý các cảm biến điều khiển đến nhóm gồm tùy ý các thiết bị vận hành (công tắc, relay...), với các khung thời gian điều khiển trong ngày và các ngày tùy ý.
	- Đã triển khai hơn 200 kịch bản điều khiển tự động cho tòa nhà Thái Bình. Tự động kiểm soát hệ thống chiếu sáng giúp tiết kiệm điện, giảm chi phí và công sức vận hành tòa nhà cũng như gia tăng trải nghiệm làm việc của CBNV VTNet.
	- Học hỏi cấu trúc quản lý, thiết kế của ứng dụng Home Assisttant, làm tiền đề cho việc phát triển giải pháp điều khiển tự động toàn trình trên Platform của Viettel.
	- Tiết kiệm được tiền thuê ngoài để phát triển: 20 men month * 35.000.000 = 700.000.000
- Tổng cộng tiết kiệm 1.750.000.000

---

- Làm firmware cho 1 thiết bị Khởi tạo mạng Zigbee, thu phát tín hiệu Zigbee: 60 mm
	- Khởi tạo mạng Zigbee:
		- Lựa chọn cấu hình mạng
		- Thủ tục khởi tạo mạng
		- Bảo mật
	- Thêm/xóa thiết bị trong mạng
		- Thủ tục
		- Bảo mật
		- Khám phá chức năng thiết bị
	- Giao tiếp trong mạng
		- Routing
		- Thủ tục
		- Cấu trúc bản tin
	- Kiểm soát, khắc phục sự cố
		- Giám sát hoạt động các phần tử
		- Tự động khắc phục các sự cố rounting, lỗi bản tin
		- Đẩy cảnh báo kèm thông tin liên quan của các loại lỗi khác
- Nhận dữ liệu từ phần cứng và giải mã: 30 mm
	- Giao tiếp với phần cứng
	- Giải mã các loại bản tin
	- Tích hợp thiết bị (3 thiết bị trong dự án Smart Office)
	- Tổng hợp, lưu trữ, debug
- Kết nối tới Platform: 20 mm
	- Liên kết với platform
	- Giao tiếp với platform
	- Bảo mật
- Frontend: 10 mm
	- Thiết kế giao diện
	- Liên kết với các thành phần
	- Thiết kế điều khiển cho các loại thiết bị

---


---



---

#
---
- Status: #writing
- Tags:
- References:
- Related:
