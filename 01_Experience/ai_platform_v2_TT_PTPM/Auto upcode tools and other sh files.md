# Auto restart docker when GPU memory is full
## Add to cronjob: 
- Type "crontab -e"
- Add this line to the file to check GPU every minute:
	- \* * * * * /home/vt_admin/tunm10/auto_check_gpu.sh >> /home/vt_admin/tunm10/auto_check_gpu.log
- Save the file

## How "auto_check_gpu.sh" file work:
- [Set reset threshold, default = 85](http://10.240.203.2:8180/haint126/tools_ai_project/-/blob/develop/sh_files/auto_check_gpu.sh#L4)
- [Set which docker to restart if memory is full](http://10.240.203.2:8180/haint126/tools_ai_project/-/blob/develop/sh_files/auto_check_gpu.sh#L6)
-  [For all GPUs, get used_memory, free_memory, total_memory info](http://10.240.203.2:8180/haint126/tools_ai_project/-/blob/develop/sh_files/auto_check_gpu.sh#L8-10)
-  [Process the info to take only number](http://10.240.203.2:8180/haint126/tools_ai_project/-/blob/develop/sh_files/auto_check_gpu.sh#L18-37)
-  [Check each GPU, if any GPU memory is > threshold, restart all dockers](http://10.240.203.2:8180/haint126/tools_ai_project/-/blob/develop/sh_files/auto_check_gpu.sh#L39-60)

# [Upcode from scratch](http://10.240.203.2:8180/haint126/tools_ai_project/-/blob/develop/sh_files/upcode_from_scrach.txt)

# [Tu's legacy 🤣- How to build dockers to run AI project](http://10.240.203.2:8180/haint126/tools_ai_project/-/blob/develop/sh_files/H%C6%B0%E1%BB%9Bng%20d%E1%BA%ABn%20build%20server.txt)


# 

---
Status: #done 

Tags: #ai_platform_v2

References:
-  

Related:
- 
