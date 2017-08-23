import requests

URL = 'https://www.calixtaondeand.com/Controller.php/__a/sms.send.remote.ol.sa'
payload = {
    'cte': '',
    'encpwd': '',
    'email': '',
    'msg': 'Mensaje a través de petición HTTP',
    'numtel': '',
    'mtipo': 'SMS'
}

#session = requests.session()
try:
    r = requests.post(URL, data=payload, timeout=40)
    print("Text")
    print(r.text)
    print("code")
    print(r.status_code)
    print("content")
    print(r.content)
except Exception as e:
    print("Exception " + str(e.args))