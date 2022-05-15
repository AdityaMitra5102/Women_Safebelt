import smtplib
from flask import *

senderacc=""
senderpass=""
server=''
port=587

app = Flask(__name__)

def sendEmail(id,name,ssid,ip):
        s = smtplib.SMTP(server,port)
        s.starttls()
        s.login(senderacc, senderpass)
        message = "Subject:Emergency\n\nHelp needed, "+name+"\nSSID: "+ssid+"\n IP "+ip
        s.sendmail(senderacc, id, message)
        s.quit()


@app.route('/safebandemail', methods=["GET","POST"])
def sndeml():
        nm = request.args.get('name')
        ssid = request.args.get('ssid')
        eml = request.args.get('email')
        ip = request.remote_addr
        sendEmail(eml,nm,ssid,ip)
        return "Email sent"

# main driver function
if __name__ == '__main__':
        # run() method of Flask class runs the application
        # on the local development server.
        app.run()
