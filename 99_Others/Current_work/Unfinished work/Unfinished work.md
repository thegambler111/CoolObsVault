# Unfinished work
Mission:

Values:

# 2023
- 3 nhiệm vụ chính 2023:
	- ~~Xây dựng IoT Platform để đưa lên Cloud (Cancel)~~
	- Quản lý quá trình đưa IoT platform của VHT lên Cloud
		- -> Bám sát lộ trình. Yêu cầu VHT cung cấp đầy đủ tài liệu hướng dẫn
	- Mở rộng hệ sinh thái IoT, tích hợp thêm ứng dụng và mang ra thương mại
		- Xác định niche: Nên lựa chọn những lĩnh vực yêu cầu vùng phủ rộng, số lượng thiết bị nhiều như Smart city, smart air port, smart port
		- Digital twins
	- Nghiên cứu chiến lược lựa chọn công nghệ kết nối cho các ứng dụng Short range và Cellular IoT
		- -> Đưa ra các tiêu chuẩn của Viettel về các loại công nghệ trên
		- So sánh MQTT vs LwM2M:
			- OneNet đẩy mạnh LwM2M -> Why
	- Ứng dụng cho Private Network
		- --> Hướng tới IoT
	- Xây dựng các báo cáo gợi ý sản phẩm chiến lược
		- -> Đưa ra được các sản phẩm nên làm của các lĩnh vực khác
		- Lựa chọn 1-2 lĩnh vực để thực hiện tại phòng

## Quý 1

### Important, big
- **Xác định công nghệ mới để theo**
- Báo cáo công nghệ quý 1
- Hoàn thành khung năng lực KNL13
- Tìm hiểu Matter + Thread

### Important, small
- Theo dõi quá trình đưa IoT Platform lên Cloud kinh doanh
- Tạo tài khoản IoT platform trên cloud và làm quen cách tích hợp, quản lý thiết bị
- Hướng làm, phát triển SDK
	- Chuẩn bị
- Tìm hiểu các giao thức mới:
	- Cũ: HTTP, MQTT, CoAP, LwM2M, TCP/UDP
	- NovaLand: Modbus, EPD, FTP, KNX, BACNET, NATS
	- Ngoài: OPC-UA, SNMP, CAN
	- So sánh MQTT vs LwM2M:
		- OneNet đẩy mạnh LwM2M -> Why

### Unimportant, big
- Đưa sản phẩm 2022 ra kinh doanh
- Private network???
- Đóng gói giải pháp GW
	- Đóng gói code
	- Hoàn thiện tài liệu

### Unimportant, small
- [x] (Đức) Cập nhật phiên bản mới cho GW tại tòa nhà Thái Bình

---

# Queue
- Small task
	- Đặt kìm tách dây và đồng hồ đo điện
	- Tổng hợp yêu cầu của VTNet cho IoT Platform
	- Đóng gói GW
	- Check lỗi GW gửi 3 bản tin MQTT sau khi điều khiển trên frontend
- Thành lập nhóm tìm hiểu các use case iot trên thế giới (theo quý)
- Chặn quyền các anh nhóm thiết bị trên github
- Tìm hiểu loại kết nối, giao thức:
	- Modbus, EPD
	- So sánh MQTT vs LwM2M:
		- OneNet đẩy mạnh LwM2M -> Why
- Hoàn thiện các yêu cầu để đạt -> KNL 13
- PMP:
	- <https://www.udemy.com/course/pmp-certification-exam-prep-course-pmbok-6th-edition/>
- [Building your own AI-powered generative search engine](https://twitter.com/kazuki_sf_/status/1609093988484804610)
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

# Báo cáo công nghệ
- Mục tiêu: Tình kiếm thị trường có sự tương đồng cao với thì trường Việt Nam và đã có những bước tiến trước
	- Sự tương đồng đánh giá qua
		- Chính sách của chính phủ
		- Mức độ phổ cập công nghệ
		- Thói quen tiêu dùng của người dân
		- Thu nhập người dân
	- Các nước tiềm năng
		- Trung Quốc
		- Các nước ĐNÁ khác
		- Ấn Độ
		- Các nước nam Mỹ
		- Một vài nước thuộc top Châu Phi
		- Nhật, Hàn
		- Mỹ
		- Các nước ở Châu Âu
	- Cách đánh giá
		- Kiểm tra lại các công nghệ mới được áp dụng rộng rãi ở các khu vực trên từ 2012 hoặc 2015 hoặc 2018 đến nay (càng về trước thì càng nhiều dữ liệu để đánh giá, nhất là với các nước đã phát triển trước nhiều)
		- Matching các công nghệ đó với Việt Nam
		- Sau đó tìm các nước có độ tương đồng cao
		- Đánh giá lại thông qua các chỉ tiêu đã nêu trên để loại bỏ trùng hợp ngẫu nhiên
		- Kết quả mong muốn: Các nước có thị trường tương đồng nhưng phát triển trước không quá 5 năm
	- Nghiên cứu các công ty lớn trong các nước tương đồng ở trên
		- Chiến lược từ 2012 hoặc 2015 hoặc 2018 đến nay
		- Tại sao lại chọn chiến lược như vậy
		- Chiến lược có thành công không
		- -> Viettel có thể học hỏi được gì?
- Mục tiêu: Tìm kiếm các trending công nghệ mới
	- Gartner
		- Thu thập các Hype cycle từ 2012 đến nay
		- Nhìn lại toàn bộ các Hype cycle để đánh giá khả năng dự đoán của chúng dựa trên các dữ liệu thực tế
		- -> Kinh nghiệm khi tham khảo Hype Cycle của Gartner
- Mục tiêu: Metaverse
- Mục tiêu: Build Matter certification lab
	- [With the launch of the Matter certification program for both hardware and software products, there are now eight authorized test labs in 16 locations across nine countries, making it easy to bring Matter products to life.](https://iotbusinessnews.com/2022/11/04/06665-smart-home-innovation-set-to-accelerate-with-matter/)

---

---

# SKYT
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

## Tình trạng
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

## Nội dung
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

## Khả năng áp dụng
- Giải pháp phần mềm quản lý Gateway Zigbee có thể áp dụng để quản lý gần như toàn bộ các loại thiết bị Zigbee có trên thị trường, cho phép tùy biến và phát triển thêm các tính năng theo yêu cầu người dùng
- Giả pháp điều khiển tự động có thể điều khiển được toàn bộ các loại thiết bị đã được tích hợp với IoT platform của Viettel và áp dụng được cho toàn bộ các dự án IoT tại Viettel (Smart Home, Smart Office, Smart Urban...).

## Điểm mới
- Giải pháp phần mềm quản lý Gateway Zigbee là giải pháp táo bạo, mang tính đột phá cao do lĩnh vực IoT đặc biệt là mảng ứng dụng Zigbee còn mới mẻ chưa có nhiều hãng sản xuất tại Việt Nam
- Giải pháp điều khiển tự động là giải pháp tự nghiên cứu, tìm hiểu và triển khai. Giải pháp đã thay thế và chứng minh sự ưu việt so với giải pháp sẵn có của nhà cung cấp thiết bị. Giải pháp phù hợp cho triển khai mọi dự án IoT lớn nhỏ.

## Hiệu quả
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

## Related
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

# Reread
![[03_Life_experience/Conversation/50 Ways to Fuel a Conversation/50 Ways to Fuel a Conversation#50 Ways to Fuel a Conversation]]
![[03_Life_experience/Conversation/10 Tips to become a better listener/10 Tips to become a better listener#10 Tips to become a better listener]]

---

# IoT platform
- Tích hợp thử 1 vài thiết bị lên cloud
- Mở 1 gateway để custom kết nối
- Kế hoạch tích hợp thiết bị lên platform
	- Với VHT
		- Kế hoạch hỗ trợ các giao thức phổ biến
		- VHT có hỗ trợ các giao thức đặc biệt ko
	- Với nội bộ
		- Duy trì đội phát triển platform để tích hợp nhanh thiết bị, trước khi VHT hỗ trợ
		- Nếu VHT ko hỗ trợ thì bố trí nguồn lực phát triển ntn

---

# Câu hỏi làm rõ chương trình trọng điểm
- SDK, firmware, module là gì?
	- Module:
		- Là mạch thu phát sóng NB-IoT (user equipment)
			- Sensor -> MCU -> Module -> platform
		- Thành phần chính:
			- Chíp xử lý tín hiệu số
			- GPIO: General purpose input/output (physical interface)
			- API giao tiếp bằng câu lệnh AT commands (Tập lệnh điều khiển module)
	- MCU
		- Là 1 vi điều khiển (máy tính mini) dùng để tiếp nhận và xử lý dữ liệu từ sensor. Sau đó gửi dữ liệu lên platform thông qua module
		- Thành phần chính (như 1 máy tính)
			- CPU
			- Memory
			- GPIO
	- Firmware
		- Là một chương trình (program) điều khiển MCU hoạt động theo yêu cầu, mong muốn của người sử dụng
	- SDK
		- Thư viện tập lệnh có sẵn để xây dựng lên firmware một cách dễ dàng, nhanh chóng
- Tại sao phải phát triển firmware
- 5G PMN:
	- Tại sao lại có các lĩnh vực tiềm năng như vậy
	- MOU?
	- Triển khai thực tế?
		- Bán dịch vụ
		- Thử nghiệm trả phí
		- Thử nghiệm miễn phí
- Bổ sung slide
	- Định nghĩa dịch vụ
		- Là gì
		- đặc điểm
	- Business model
		- Vtnet vai trò gì
		- ai kinh doanh
		- khách hàng?
	- Mục tiêu dự án
	- Kế hoạch triển khai
---

---

#
---
- Status: #writing
- Tags:
- References:
- Related:
