# Install
``` bash
sudo apt update && sudo apt install tcpdump
```

# Daemon file
- File location: `/usr/lib/systemd/system/`
``` bash
:x[Unit]
After=network.target
 
[Service]
Restart=always
RestartSec=30
Environment="TCPDUMP_FORMAT=%%Y-%%m-%%d__%%H-%%M"
ExecStart=sudo /usr/bin/tcpdump -i eth0 port 1884 -C 50 -s 65535 -w '/opt/FL08.pcap' -Z root
ExecStop=/bin/kill -s QUIT $MAINPID
 
[Install]
WantedBy=multi-user.target

```


# 

---
- Status: #done

- Tags: 

- References:
	- 

- Related:
	- 
