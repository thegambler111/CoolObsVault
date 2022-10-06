# Mục tiêu
- Mục tiêu của mình trong giai đoạn này là làm chủ các giao thức truyền dữ liệu trên nền tảng platform
- Hiện trạng:
	1. Giao thức MQTT, CoAP, LWM2M ==> Cái này hiện Thingsboard đã phát triển thành các service riêng, tuy nhiên chưa thực sự tiện dụng và adaptive cho tất cả các trường hợp
	2. Giao thức HTTP cũng tương tự
	3. Giao thức UDP, TCP: Hiện đang nhét hết vào con gateway, không phổ quát được cách tích hợp cho nhiều thiết bị
- Nên anh thấy mục tiêu cụ thể của anh em mình là:
	- Với các giao thức đã có service riêng ==> Phát triển nó theo hướng phổ quát cho nhiều thiết bị, dễ dàng cho người dùng tích hợp một loại thiết bị mới (ít nhất có thể làm như kiểu rule chain)
	- Với các giao thức chưa có service riêng ==> Tư duy tạo ra một service mới cho giao thức đó (theo kiểu microservice), cũng hướng tới phổ quát như trên

- Cách làm
- Với mỗi giao thức ==> Bọn em làm rõ khả năng hỗ trợ của Thingsboard hiện tại; các tồn tại, hạn chế; các tính năng mong muốn phát triển
	- Để làm nhanh thì cần học người đi trước: người đi trước ở đây là các nền tảng platform khác đã thương mại ==> Tham khảo nền tảng platform của Huawei, CTWing, Thingsworx
- Ngoài ra cũng có thể tìm thêm một số nền tảng platform mã nguồn mở khác được đánh giá tốt ở phần này
	- Mình làm tốt phần này thì mới tính tới làm tiếp các bước sau của platform được









# 

---
- Status: #done 

- Tags: #thingsboard

- References:
	- 

- Related:
	- 
