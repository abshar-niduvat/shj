import requests
from django.shortcuts import render

# Create your views here.
def SmsSent(msg,no,peid,teid):
    response = requests.get('http://sms.bulksmsind.in/v2/sendSMS?username=skssfkannur&message=' + str(msg) + '&sendername=ISKSSF&smstype=TRANS&numbers=' + str(no) + '&apikey=4094a9df-5337-4f93-812f-3b286ffbbfe1&peid='+ str(peid) +'&templateid='+ str(teid))
    return response

