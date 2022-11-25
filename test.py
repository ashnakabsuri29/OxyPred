import requests
TOKEN = "BBFF-Q0rviS1phK0cRzmxaqBHsgOw6RxUEp"  # Assign your Ubidots Token
DEVICE = "pulseoxy"  # Assign the device label to obtain the variable
VARIABLE = "spo2"  # Assign the variable label to obtain the variable value
DELAY = 2  # Delay in seconds


def get_var(device, variable):
   try:
      url = "http://industrial.api.ubidots.com/"
      url = url + \
         "api/v1.6/devices/{0}/{1}/values".format(device, variable)
      headers = {"X-Auth-Token": TOKEN, "Content-Type": "application/json"}
      req = requests.get(url="http://industrial.api.ubidots.com/api/v1.6/devices/pulseoxy/spo2/values", headers=headers)
      return req.json()['results'][0]['value']
        
   except:
      pass

print(get_var(DEVICE, VARIABLE))