#This python script was written for setting time for network cam which does not have access to WAN. The isolated network made cam to uanble to update time via ntp. This script does work as ntp(kinda) via Raspberry pi.
from time import localtime, strftime
import requests

#get nowtime from computer. Specifing  time format separeted by dot instead of dash.
nowtime = strftime("%Y.%m.%d.%H.%M.%S", localtime())

#Make get request to following URL to make CAM sync with computer time. +nowtime+ is dynamic time getting from computer.
url = requests.get("http://192.168.0.100/web/cgi-bin/hi3510/param.cgi?time=1565240679353&cmd=setntp&-ntpserver=%20&-ntpinterval=24&cmd=setservertime&-time="+nowtime+"&-timezone=Asia/Tokyo&-dstmode=off&-autoupdate=1")

#following print strings for debugging. 
#print(nowtime)
#print(url.status_code)
#print(url.text)
