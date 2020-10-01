import requests
from requests.auth import HTTPBasicAuth


def get_auth():
    consumer_key = "BHNZIOyFn2mcxGDufA31jZWVnhiUnGJz"
    consumer_secret = "HM6KGcQvJ5QgmG28"
    api_url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

    r = requests.get(api_url, auth=HTTPBasicAuth(consumer_key, consumer_secret))

    return r.json()


def register_url():
    access_token = get_auth().get('access_token')
    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
    headers = {"Authorization": "Bearer %s" % access_token}
    request = {"ShortCode": "600343",
               "ResponseType": "Complete",
               "ConfirmationURL": "http://pesaenk.enkishaatechnologies.co.ke/confirm.php",
               "ValidationURL": "http://pesaenk.enkishaatechnologies.co.ke/confirm.php"}

    response = requests.post(api_url, json=request, headers=headers)

    return response.json()


def simulator():
    access_token = get_auth().get('access_token')
    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate"
    headers = {"Authorization": "Bearer %s" % access_token}
    request = {"ShortCode": "600343",
               "CommandID": "CustomerPayBillOnline",
               "Amount": "21000",
               "Msisdn": "254708374149",
               "BillRefNumber": "951b1a8b"}

    response = requests.post(api_url, json=request, headers=headers)

    return response.json()


simulator()
