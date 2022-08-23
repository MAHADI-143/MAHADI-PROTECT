import os, platform
 
try:
 
        import requests
 
except:
 
        os.system('pip2 install requests')
 
 
 
import requests
 
bit = platform.architecture()[0]
 
if bit == "64bit":
 
        from MP64 import ONOFF
 
        ONOFF()
 
 
 
elif bit == "32bit":
 
        from MP32 import ONOFF
 
 
        ONOFF()
 
 
