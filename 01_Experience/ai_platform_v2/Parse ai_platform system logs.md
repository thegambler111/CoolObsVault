# Get raw summary

- [Source function](http://10.240.203.2:8180/haint126/tools_ai_project/-/blob/develop/extra_files/production_tools/view_results_in_production/view_api_logs.py#L236-323)
- This return the number of images sent to server and their results, which including deleted images

# Draw all results

- [Source function](http://10.240.203.2:8180/haint126/tools_ai_project/-/blob/develop/extra_files/production_tools/view_results_in_production/view_api_logs.py#L45-150)
-  Add "production_tools" folder into "ai_platform_project", same level as "platform_ai"
- Details:
	- This function only count the images the still exist on the ftp server
	- [Run the function in multi-process and separate the log file accordingly](http://10.240.203.2:8180/haint126/tools_ai_project/-/blob/develop/extra_files/production_tools/view_results_in_production/view_api_logs.py#L203-221)
	- [Content of each log line](http://10.240.203.2:8180/haint126/tools_ai_project/-/blob/develop/extra_files/production_tools/view_results_in_production/view_api_logs.py#L71-74)
	- [Set maximum number of bdnt images to print, default = 500 per process](http://10.240.203.2:8180/haint126/tools_ai_project/-/blob/develop/extra_files/production_tools/view_results_in_production/view_api_logs.py#L60)
	- [Check number of printed bdnt images, if exceeding threshold, skip the log line](http://10.240.203.2:8180/haint126/tools_ai_project/-/blob/develop/extra_files/production_tools/view_results_in_production/view_api_logs.py#L91-93)
	- [Request was not stored in json format so it needs to be changed](http://10.240.203.2:8180/haint126/tools_ai_project/-/blob/develop/extra_files/production_tools/view_results_in_production/view_api_logs.py#L101)
	- [Check if the request was a test request sent with image from "test images" folder](http://10.240.203.2:8180/haint126/tools_ai_project/-/blob/develop/extra_files/production_tools/view_results_in_production/view_api_logs.py#L109-111)
	- [Get the image information including task_id, targeted_object(i.e. ac, dc,...), image_name, image_url, value, result, score and draw it](http://10.240.203.2:8180/haint126/tools_ai_project/-/blob/develop/extra_files/production_tools/view_results_in_production/view_api_logs.py#L117-142)
	- [Draw image code](http://10.240.203.2:8180/haint126/tools_ai_project/-/blob/develop/extra_files/production_tools/view_results_in_production/view_api_logs.py#L153-200)
		- [Load image](http://10.240.203.2:8180/haint126/tools_ai_project/-/blob/develop/extra_files/production_tools/view_results_in_production/view_api_logs.py#L165-175)
		- [Declare plot and draw image](http://10.240.203.2:8180/haint126/tools_ai_project/-/blob/develop/extra_files/production_tools/view_results_in_production/view_api_logs.py#L178-183)
		- [Draw text](http://10.240.203.2:8180/haint126/tools_ai_project/-/blob/develop/extra_files/production_tools/view_results_in_production/view_api_logs.py#L187-197)
			- [Source code for draw text](https://stackoverflow.com/questions/48079364/wrapping-text-not-working-in-matplotlib/56552098#56552098)



# 

---
Status: #done 

Tags: #ai_platform_v2  

References:
-  

Related:
- 
