from flask import Flask
from datetime import datetime

def timestamp():
    timenow = datetime.now()
   
    time = timenow.strftime("%I:%M:%S %p")  
    return time