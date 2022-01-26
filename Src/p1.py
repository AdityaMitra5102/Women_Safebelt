from flask import Flask, request
from sql import *
import logging
import os
import sys
import azure.functions as func
from azf_wsgi import AzureFunctionsWsgi

from __app__.project.wsgi import application
app=Flask(__name__)

@app.route("/api/WomenSecurity/", methods=['GET'])
def root():
    
    UID = request.args.get('UID')
    SSID=request.args.get('SSID')
    Name=getNAME_BY_UID(UID)
    eml= getEMAIL_BY_UID(UID)
    sendEmail(eml, Name, SSID)
    

def sendEmail(eml, Name, SSID):
    
    payload={'eml':eml, 'Name': Name, 'loc': SSID}
    r=requests.get('http://20.106.248.18/',params=payload)
    print(r.text)


   
if __name__=='main':
    app.run(debug=True)

