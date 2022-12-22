# 5G Private network

## Definition
1. Định nghĩa Private Mobile Network (hiểu ở đây là 5G)

### [Redhat](https://www.redhat.com/en/topics/5g-networks/what-is-private-5g)
- Private 5G refers to a 5G mobile network which allows the owner to provide priority access or licensing for its wireless spectrum.
- Model of 5G private network
	- a “full private” 5G network is where the organization owns the spectrum owns both spectrum and infrastructure
		- In full private 5G, it possible to completely isolate network users from public network
	- a “private shared” 5G network or a “hybrid private” 5G network is where a slice of public network is used as private network

### [Cisco](https://www.cisco.com/c/en/us/solutions/private-5g-networks.html)
- Private 5G networks are nonpublic mobile networks that can use licensed, unlicensed, or shared spectrum.
- models of private 5G networks
	- Wholly owned and operated private 5G networks, where an organization owns all the equipment, private clouds, and spectrum, and manages the network in-house
	- Hybrid private-public cloud 5G networks, where a business may own or lease on-premises equipment and use a public or private cloud service to host parts of the network
	- Private 5G delivered via network slicing, which may include an on-site Radio Access Network (RAN) and other equipment, depending on application needs
	- Neutral host networks with a RAN and signal sharing

### Forbes
- private 5G networks are networks that don't share traffic with other cellular networks in the vicinity

---

## Private vs public

### Redhat
- priority access:
	- allow different levels of priority access when certain network activities are deemed more business-critical than others
- isolation
	- allow operators to completely or partially isolate end user devices from MNOs’ public networks

## 5G Vs 4G LTE

### Redhat
- Private 5G providing lower-latency, higher-throughput and more reliable connectivity compare to 4G LTE
	- Example:
		- a large manufacturing site where reliable connectivity is needed inside the shop floor, but also outside
		- autonomous guided vehicles moving parts from one shopfloor to the other.
 - It’s possible to have a private cellular network that uses 4G LTE and 5G technologies because they operate across separate frequency bands

### Cisco
- faster data transmission, lower latency, and the ability to connect to more devices in a defined area

# Ecosystem, services of 5G private network
1. Hệ sinh thái các ứng dụng 5G private network: em list cho anh các dịch vụ kèm mô tả ngắn gọn dịch vụ để người đọc dễ hiểu.

## Redhat
- The Industrial Internet of Things (IIoT) is one of the more prevalent use cases for both private 4G LTE and private 5G networks.
- allowing for deployment in hybrid [multi-access edge computing (MEC)](https://www.redhat.com/en/topics/edge-computing/what-is-multi-access-edge-computing) environments
- 5G is moving more and more to a software defined implementation. That trend is called [network function virtualization](https://www.redhat.com/en/topics/virtualization/what-is-nfv) (NFV).

## Cisco
- Manufacturing
	- Power robotics, autonomous guided vehicles (AGV), scanners, virtual reality (VR) remote devices
	- drive closed-loop manufacturing
- Logistics and warehousing
	- Support autonomous guided vehicles
	- remote expert solutions such as augmented reality (AR), VR
	- real-time asset and inventory tracking, facility modeling, predictive analytics
	- automated logistics control and management
		- support for massive machine-type communications (mMTC)
	- facility and environmental control
- Hospitality and venues
	- Provide a mix of wireless connectivity options (with Wifi)
	- Support interior and exterior security cameras and sensors
- Education and universities
	- Provide security and support research and development in inter-vehicle communication, drones, and related data.
- Fixed wireless access (FWA) providers
	- offer high-bandwidth internet access to underserved areas and places where fiber connection is unavailable
- Industrial
	- enable technologies such as collaborative mobile robots, autonomous machines, swarm intelligence, AR, and predictive maintenance
	- bring new levels of performance and reliability to mines and other remote locales

## [Ericsson](https://www.ericsson.com/494b57/assets/local/5g/documents/ericsson-private-5g-solution-brief.pdf)
- an **ecosystem** of communications service providers, resellers, device makers, system integrators, and software providers
	- Secure
	- Optimizes and simplifies business operations with cloud-based network management.
	- Keeps data on-premises
	- zero downtime upgrades and guarantees high performance
- Ericsson Private 5G supports many use cases
	- dynamic reconfiguration of manufacturing machines on factory floors
	- untethered mobile robots and drones
	- autonomous cranes in ports
	- Providing local voice services for mission critical communication
	- connecting mines above and underground
	- monitoring asset locations

# Market of 5G private network
1. Các số liệu về thị trường: số nhà mạng áp dụng, thị phần toàn cầu,... trong các link em gửi anh thấy chắc đủ, vì phần này cũng phổ biến

---

# Evolving Private Networks: Global trends and deployment
The Global Mobile Suppliers Association (GSA) defines a private mobile network as a 3GPP-based 4G LTE or 5G network intended for the sole use of private entities such as enterprises, industries, and governments.

- The demand for private mobile networks based on 4G long term evolution (LTE) and 5G technologies is being driven by the surge in data, security, digitization, and enterprise mobility requirements of modern business and government entities.

## Adoption trends by vertical
- Manufacturing: 165 identified companies, up from 111 at the end of 2021
- Education: 95 customers, followed by mining companies with 74, power utility companies with 71
- Defense and peacekeeping: 53 and 40
- Automotive: 90 discrete manufacturing customers, 45 process manufacturing customers

## Spectrum bands
- C-band spectrum is the most widely assigned, followed by citizens broadband radio service (CBRS) spectrum.
- Telecom regulators are showing signs of increasing allocations of dedicated spectrum available for private mobile networks, typically small tranches in specified locations
- A large number and wide range of market participants are actively engaged in developing and delivering solutions for private networks

#
---
- Status: #done
- Tags: #product_strategy
- References:
	- From telecommunication services to IT services
		- <https://www.google.com/search?q=telecommunications+service+provider+information+service+site:https://www.gartner.com/en/documents&lr=&safe=images&hl=en&as_qdr=all&tbs=cdr:1,cd_min:12/22/2022,cd_max:12/22/2019&sxsrf=ALiCzsYxkx1Gg5F_1Qqw8Yd4aeryxx4SiA:1671683761928&ei=sd6jY6mOOIGh-QapsZeoDQ&start=0&sa=N&ved=2ahUKEwjpqrmms4z8AhWBUN4KHanYBdU4ChDy0wN6BAgeEAQ&biw=2048&bih=1042&dpr=1.25>
			- <https://www.gartner.com/en/documents/4005826>
			- <https://www.gartner.com/en/documents/4002576>
			- <https://www.gartner.com/en/documents/4000781>
			- <https://www.gartner.com/en/documents/4003571>
			- <https://www.gartner.com/en/documents/4003044>
			- <https://www.gartner.com/en/documents/3997046>
			- <https://www.gartner.com/en/documents/4002617>
		- <https://www.sktelecom.com/en/press/press_detail.do?page.page=1&idx=1546&page.type=all&page.keyword=>
		- <https://www.linkedin.com/pulse/top-10-telecom-trends-2022-ankit-tyagi/>
	- Private network
		- Trends
			- <https://www.gartner.com/en/documents/3993224>
			- <https://www.gartner.com/en/documents/4003470>
			- <https://www.gartner.com/en/documents/4011664>
			- <https://tele.net.in/evolving-private-networks-global-trends-and-deployment/>
			- <https://telecominfraproject.com/tip-5g-private-networks-solution-group-paves-the-way-to-transform-private-network-economics-and-introduces-blueprint/>
			- <https://learn.microsoft.com/en-us/azure/private-multi-access-edge-compute-mec/affirmed-private-network-service-overview>
			- <https://www.affirmednetworks.com/products-solutions/private-network-service/>
			- <https://www.nokia.com/networks/private-wireless/podcasts/six-private-wireless-trends-to-watch-in-2022/>
			- <https://www.businesswire.com/news/home/20220906005944/en/United-States-Private-LTE-5G-Network-Market-Analysis-Report-2022-A-13.6-Billion-by-2030---Focus-on-Upcoming-Trends-in-Various-Spectrums-Numerous-Private-5G-Use-Cases-and-Regulatory-Scenario---ResearchAndMarkets.com>
			- <https://www.agileintelresearch.com/reportdetails/Global-Private-5G-Network-Market/9>
			- <https://www.grandviewresearch.com/industry-analysis/private-5g-network-market>
			- <https://www.verifiedmarketresearch.com/product/private-5g-network-market/>
			- <https://www.vodafone.com/business/news-and-insights/glossary/what-is-mobile-private-network>
	- others:
		- <https://www.gartner.com/en/articles/gartner-top-10-strategic-technology-trends-for-2023>
		- <https://www.gartner.com/en/articles/what-s-new-in-artificial-intelligence-from-the-2022-gartner-hype-cycle>
		- <https://www.gartner.com/en/articles/what-s-new-in-the-2022-gartner-hype-cycle-for-emerging-technologies>
		- <https://www.gartner.com/en/articles/gartner-top-10-strategic-predictions-for-2023-and-beyond>
- Related:
