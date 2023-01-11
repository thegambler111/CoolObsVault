# Resource
- [How to setup](https://ubuntu.tutorials24x7.com/blog/how-to-install-and-configure-monit-on-ubuntu-20-04-lts)
- [Official Document](https://mmonit.com/monit/documentation/monit.html#LOGGING)
- [Viblo guide](https://viblo.asia/p/gioi-thieu-ve-monit-cong-cu-giam-sat-server-manh-me-gAm5ybDXKdb)
- [Total CPU?](https://stackoverflow.com/questions/38638836/monit-configuration-total-cpu-syntax-error)

# Use `Stress` to test monit
- [Use `stress` to test](https://stackoverflow.com/questions/33467918/how-can-i-configure-monit-to-kill-a-high-cpu-process-after-a-few-seconds)
- Add service to be monitored by monit at `/etc/monit/conf.d/`

# Monit command
- Reload and restart monit and restart all services running under monit

```bash
sudo monit -t && sudo service monit restart && sudo monit start all
```

- Read monit log:

```bash
sudo tail -f /var/log/monit.log
```

- Check running services

```bash
sudo minit status
```

# Monit open control frontend
- Monit config file location:
	- `/etc/monit/monitrc` (Ubuntu / Debian / Linux Mint)
	- `/etc/monit.conf` (RedHat / CentOS / Fedora)

```bash
set httpd port 2812 and
    allow localhost
    allow 192.168.68.126 # haint126 laptop
```

# Monit service file example
- Monit service file location:
	- `/etc/monit/conf.d/`

```bash
set daemon 2
check process zigbee2mqtt
    matching "^node index.js" # Using regex to find process
    start program = "/usr/bin/systemctl start zigbee2mqtt.service" with timeout 10 seconds
    stop program = "/usr/bin/systemctl stop zigbee2mqtt.service"
    if total cpu > 95% for 2 cycle then alert
    if total cpu > 95% for 20 cycles then restart

```

#

---
- Status: #done
- Tags: #linux
- References:
- Related:
