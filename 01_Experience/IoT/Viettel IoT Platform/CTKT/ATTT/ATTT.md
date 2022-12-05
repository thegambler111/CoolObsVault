# Xây dựng CTKT ATTT cho nền tảng IoT Platform. Bao gồm:

## Bảo mật phần cứng:
 - Hệ thống network phải đảm bảo các yêu cầu về bảo mật như:
	 - Firewall: blacklisting/whitelisting, packet-filtering
	 - Web application firewall (WAF)
	 - Intrusion detection system (IDS)
	 - Intrusion prevention system (IPS)
	 - Wireless intrusion prevention and detection system (WIDPS)
	 - Network access control (NAC)
	 - DoS Attack prevention

## Bảo mật phần mềm
 - Sử dụng proxy server để phân tách giao tiếp các service với hệ thống ngoài
 - Sử dụng Internal firewall (OS firewall), chặn tất cả các port không cần thiết.
 - Phần mềm phải có cơ chế Authentication và Authorization giữa các services.
 - Data giao tiếp phải được mã hóa và truyền tải qua kênh SSL (HTTPS, MQTTS, WSS)
 - Có cơ chế xác thực và đánh giá dữ liệu an toàn, chống SQL Injection.
 - Xây dựng phần mềm dựa trên các mô hình bảo mật OWASP, Microsoft SDL,…
 - Đối với các phần mềm có sử dụng password authentication, thì password cho user phải bao gồm trên 8 ký tự và có các ký tự Hoa, thường, ký hiệu, con số và hỗ trợ cơ chế 2FA.
 - Đối với user admin password hệ thống yêu cầu bắt buột đổi password ít nhất sau 3 tháng và bắt buộc cơ chế 2FA.

#
---
- Status: #done
- Tags: #IoT_platform
- References:
- Related:
