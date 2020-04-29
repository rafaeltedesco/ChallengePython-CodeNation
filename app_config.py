import requests
import json
from cryptography import Crypto


def access_token(token):
    """Get token from the user and return a dict's token to the application"""
    return {'token': token}


class Cesar:
    """Cesar's encrypt and decrypt for Code Nations Developers Challenge"""

    def __init__(self):
        self.crypto = Crypto()
        self.dc_token = ''

    def request(self, url, token):
        """Make a request for the Code Nation's Api and return a json file"""
        self.dc_token = access_token(token)
        #print(requests.get(url, params=dc_token).text)
        self.crypto.set_json(requests.get(url, params=self.dc_token).text)

    def post_request(self, j_file):
        #with open(j_file, 'b') as f:
        #    answer = json.load(f)
        url = 'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution'
        files = {'answer': open(j_file, 'rb')}
        r = requests.post(url, params=self.dc_token, files=files)
        print(r.text)
