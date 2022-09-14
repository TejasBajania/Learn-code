"""
For fetching network password from already connected Wifi

"""

import subprocess
import sys

data = subprocess.check_output(['netsh','wlan','show','profiles']).decode('utf-8').split('\n')

profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

print(profiles)


result_file = open("results.txt","w")

# Enter your Network name 
i = "Add-your-network-name-here"
results = subprocess.check_output(['netsh','wlan','show','profile',i,'key=clear']).decode('utf-8').split('\n')

results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]

try:
    print("{},{}\n".format(i, results[0]))
except IndexError:
    print("Index error")
    
result_file.write("{},{}\n".format(i, results[0]))
