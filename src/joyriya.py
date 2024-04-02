import sys
import urllib.request
import json
import time
def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./10)
slowprint("##################")
slowprint("#      ~~~~~~~ JOYRIYA AKHTAR~~~~~")
slowprint("#  ~~~~~~~~~~Ip Tracker~~~~~~~~~	")
slowprint("#~~~~~~Accurate IP tracking Tool~~~~~~~~	")
slowprint("# Author: https://www.facebook.com/profile.php?id=61556758367912")
slowprint("# GitHub: https://github.com/users/Jhaiyaakhtar/projects/6")
slowprint("#   ~~~~~~~~~~~~~~ Version: 1.1~~~~~~~~~~")
slowprint("#   note all ip not supported")
slowprint("####################")

print("\n")

ip1 = input("Enter the targeted ip address: ")
url = "http://ip-api.com/json/" + ip1
try:  
  response = urllib.request.urlopen(url)
  data = response.read()
  values = json.loads(data)
  print("\n")
  slowprint("#################################################################")
  slowprint("#      Query      : " + values['query'])
  slowprint("#      Status     : " + values['status'])
  slowprint("#      Country    : " + values['country'])
  slowprint("#      RegionName : " + values['regionName'])
  slowprint("#      City       : " + values['city'])
  slowprint("#      ZipCode    : " + values['zip'])
  slowprint("#      Isp        : " + values['isp'])
  slowprint("#      Org        : " + values['org'])
  slowprint("#      As         : " + values['as'])
  slowprint("#      Region     : " + values['region'])
  slowprint("#################################################################")
except Exception as e:
    print("An error occurred:", e)
    
    