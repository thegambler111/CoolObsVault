# LWM2M library
<https://github.com/OpenMobileAlliance/lwm2m-registry>

# Change port LWM2M
- In file `thingsboard\application\src\java\org\thingsboard\server\thingsboard.yml`
	- In `lwm2m/server/bind_port`, change port: 5685 -> YOUR_LWM2M_PORT (35685)
- In file `dao/src/main/java/org/thingsboard/server/dao/service/validator/DeviceProfileDataValidator.java`
	- In line 446 and 448, `port = serverConfig.isBootstrapServerIs()`
		- Change NO_SEC port: 5685 -> YOUR_LWM2M_PORT (35685)

# Leshan github
- [Leshan github](<https://github.com/eclipse/leshan)

#
---
- Status: #done
- Tags: #thingsboard
- References:
- Related:
