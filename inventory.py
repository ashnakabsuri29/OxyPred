import random
import time
from urllib import request
from flask import *
from ioe import RegressorRNN
import requests
import random
import time
import pandas as pd
import threading
import math
app = Flask(__name__)
r = RegressorRNN()
original_cases, predicted_cases = [0],[0]
@app.route('/')
def index():

    inv = 1520
    curr = 0 if original_cases[-1] == 0 else math.trunc((original_cases[-1]-7500)/7531)*7.5
    pred = 0 if predicted_cases[-1] == 0 else math.trunc((predicted_cases[-1][0]-7500)/7531)*7.5
    days = math.trunc(inv / pred) if pred != 0 else 0
    arr = {
        'curr':  str(curr) + ' mt. cu.',
        'pred':  str(pred) + ' mt. cu.',
        'days':  str(days) +' days',
        'inv': inv
    }
    # str(inv / (7.5*(predicted_cases[-1]/7531 -7500 if predicted_cases[-1] > 0 else 0)))+ ' days'
    
    return render_template('index.html', arr=arr)


@app.route('/plot')
def plot():
    return r.plotter(original_cases, predicted_cases)


def getData():
    TOKEN = "BBFF-AC1130pYOifdieEkw6w0BBTvtZ4QpV"  # Assign your Ubidots Token
    DEVICE = "pulseoxy"  # Assign the device label to obtain the variable
    VARIABLE = "hypoxia"  # Assign the variable label to obtain the variable value
    DELAY = 2  # Delay in seconds


    def get_var(device, variable):
        try:
            url = "http://industrial.api.ubidots.com/"
            url = url + \
                "api/v1.6/devices/{0}/{1}/values".format(device, variable)
            headers = {"X-Auth-Token": TOKEN, "Content-Type": "application/json"}
            req = requests.get(url=url, headers=headers)
            return req.json()['results'][0]['value']
        except:
            pass
    count = 0
    val = [] 
    while True:
        val.append(get_var(DEVICE, VARIABLE)+7500)
        if count > 30:
            oc,pc = r.predictor(pd.DataFrame({'newCases': val}))
            global original_cases 
            original_cases = oc
            global predicted_cases
            predicted_cases = pc
            val.pop(0)
        count += 1
        print(count)
        print(val)
        time.sleep(DELAY)

    

# if __name__ == "__main__":
t2 = threading.Thread(target = getData)
t2.start()
    #app.run(debug=True)
    
    
